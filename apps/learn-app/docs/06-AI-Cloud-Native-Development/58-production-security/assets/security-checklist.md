# Production Security Checklist for Kubernetes

**Purpose**: Use this checklist to verify security controls for any Kubernetes deployment.
**Source**: Chapter 58 - Production Security & Compliance

## 10-Point Security Audit Checklist

Run each command and verify the expected output before marking complete.

| # | Check | Command | Expected | Status |
|---|-------|---------|----------|--------|
| 1 | **Dedicated ServiceAccount** | `kubectl get pod <pod> -o jsonpath='{.spec.serviceAccountName}'` | Not `default` | [ ] |
| 2 | **Minimal RBAC permissions** | `kubectl auth can-i --list --as=system:serviceaccount:<ns>:<sa>` | Only required permissions | [ ] |
| 3 | **Default-deny NetworkPolicy** | `kubectl get networkpolicy -n <ns> -o name \| grep deny` | Policy exists | [ ] |
| 4 | **DNS egress allowed** | `kubectl exec <pod> -- nslookup kubernetes.default` | Resolves successfully | [ ] |
| 5 | **Secrets via volume mount** | `kubectl get pod <pod> -o jsonpath='{.spec.volumes[*].secret}'` | Secrets mounted as volumes | [ ] |
| 6 | **PSS Restricted compliance** | `kubectl label ns <ns> pod-security.kubernetes.io/enforce=restricted --dry-run=server` | No errors | [ ] |
| 7 | **No CRITICAL vulnerabilities** | `trivy image <image> --severity CRITICAL --exit-code 1` | Exit code 0 | [ ] |
| 8 | **Dapr mTLS enabled** | `dapr status -k \| grep sentry` | Sentry running | [ ] |
| 9 | **Component scopes configured** | `kubectl get component <name> -o jsonpath='{.scopes}'` | App IDs listed | [ ] |
| 10 | **Audit logging enabled** | `kubectl logs -n kube-system -l component=kube-apiserver \| head` | Audit entries present | [ ] |

## Quick Verification Script

```bash
#!/bin/bash
# security-audit.sh - Run all checks for a deployment

NAMESPACE=${1:-production}
APP=${2:-task-api}
IMAGE=${3:-task-api:latest}

echo "=== Security Audit for $APP in $NAMESPACE ==="
echo ""

# Check 1: ServiceAccount
SA=$(kubectl get pod -n $NAMESPACE -l app=$APP -o jsonpath='{.items[0].spec.serviceAccountName}')
if [ "$SA" != "default" ]; then
  echo "[PASS] 1. Dedicated ServiceAccount: $SA"
else
  echo "[FAIL] 1. Using default ServiceAccount"
fi

# Check 2: RBAC permissions
echo ""
echo "2. RBAC Permissions for $SA:"
kubectl auth can-i --list --as=system:serviceaccount:$NAMESPACE:$SA | head -10

# Check 3: NetworkPolicy
NP=$(kubectl get networkpolicy -n $NAMESPACE -o name 2>/dev/null | wc -l)
if [ "$NP" -gt 0 ]; then
  echo ""
  echo "[PASS] 3. NetworkPolicies present: $NP policies"
else
  echo ""
  echo "[FAIL] 3. No NetworkPolicies in namespace"
fi

# Check 4: DNS resolution
POD=$(kubectl get pod -n $NAMESPACE -l app=$APP -o jsonpath='{.items[0].metadata.name}')
if kubectl exec -n $NAMESPACE $POD -- nslookup kubernetes.default > /dev/null 2>&1; then
  echo "[PASS] 4. DNS resolution working"
else
  echo "[FAIL] 4. DNS resolution blocked"
fi

# Check 5: Secrets as volumes
SECRETS=$(kubectl get pod -n $NAMESPACE $POD -o jsonpath='{.spec.volumes[*].secret.secretName}')
if [ -n "$SECRETS" ]; then
  echo "[PASS] 5. Secrets mounted: $SECRETS"
else
  echo "[WARN] 5. No secrets mounted (or using env vars)"
fi

# Check 6: PSS compliance
if kubectl label ns $NAMESPACE pod-security.kubernetes.io/enforce=restricted --dry-run=server -o name > /dev/null 2>&1; then
  echo "[PASS] 6. PSS Restricted compatible"
else
  echo "[FAIL] 6. PSS Restricted violations"
fi

# Check 7: Image vulnerabilities
echo ""
echo "7. Image vulnerability scan:"
trivy image $IMAGE --severity CRITICAL,HIGH --quiet || echo "[FAIL] Vulnerabilities found"

# Check 8: Dapr mTLS
if dapr status -k 2>/dev/null | grep -q sentry; then
  echo ""
  echo "[PASS] 8. Dapr Sentry (mTLS) running"
else
  echo ""
  echo "[SKIP] 8. Dapr not installed or Sentry not running"
fi

# Check 9: Component scopes
SCOPES=$(kubectl get component -n $NAMESPACE -o jsonpath='{.items[*].scopes}' 2>/dev/null)
if [ -n "$SCOPES" ]; then
  echo "[PASS] 9. Component scopes configured"
else
  echo "[SKIP] 9. No Dapr components or scopes"
fi

# Check 10: Audit logging
echo "[INFO] 10. Check audit logs manually in your cluster"

echo ""
echo "=== Audit Complete ==="
```

## Usage

1. Save the script as `security-audit.sh`
2. Make executable: `chmod +x security-audit.sh`
3. Run: `./security-audit.sh <namespace> <app-label> <image>`

Example:
```bash
./security-audit.sh production task-api task-api:v1.0.0
```

## When to Use This Checklist

- **Before production deployment**: All 10 checks must pass
- **After security incidents**: Verify controls weren't bypassed
- **During compliance audits**: Document evidence for each check
- **Quarterly reviews**: Catch configuration drift

## Related Resources

- L01: Cloud Native Security Model (4C framework)
- L02: RBAC Deep Dive (checks 1-2)
- L03: NetworkPolicies (checks 3-4)
- L04: Secrets Management (check 5)
- L05: Pod Security Standards (check 6)
- L06: Image Scanning (check 7)
- L07: Dapr Security (checks 8-9)
- L08: Compliance Fundamentals (check 10)
