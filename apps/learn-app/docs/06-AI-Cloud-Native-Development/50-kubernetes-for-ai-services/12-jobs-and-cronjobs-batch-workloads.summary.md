# Jobs and CronJobs: Batch Workloads - Summary

## Core Mental Models

### Jobs vs Deployments

```
Deployment: Run forever, restart on exit
Job: Run once, complete and stop
CronJob: Run Job on schedule
```

**Key distinction**: `restartPolicy: Never` (Jobs) vs `restartPolicy: Always` (Deployments)

### The Job → Pod Hierarchy

```
Job: embedding-refresh
    ↓ creates
Pod: embedding-refresh-7x9kq (status: Completed)
```

Unlike Deployments (which use ReplicaSets), Jobs directly manage Pods.

### CronJob → Job → Pod Chain

```
CronJob (schedule: "0 2 * * *")
    ↓ creates at 2 AM
Job: cleanup-28473049
    ↓ creates
Pod: cleanup-28473049-abc12 (Completed)
```

## Essential Commands

```bash
# Create and monitor a Job
kubectl apply -f job.yaml
kubectl get jobs -w
kubectl get pods
kubectl logs <pod-name>

# Create and monitor a CronJob
kubectl apply -f cronjob.yaml
kubectl get cronjobs
kubectl get jobs          # See Jobs created by CronJob

# Delete (Job deletion also deletes its Pods)
kubectl delete job <name>
kubectl delete cronjob <name>
```

## Key YAML Patterns

### Basic Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: myapp:v1
        command: ["python", "migrate.py"]
      restartPolicy: Never
  backoffLimit: 4
```

### Parallel Job

```yaml
spec:
  completions: 10     # Total successful completions needed
  parallelism: 3      # Max concurrent Pods
```

### CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-cleanup
spec:
  schedule: "0 2 * * *"          # Cron expression
  concurrencyPolicy: Forbid       # Don't overlap runs
  successfulJobsHistoryLimit: 3   # Keep last 3 successful
  failedJobsHistoryLimit: 1       # Keep last 1 failed
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cleanup
            image: cleanup:v1
          restartPolicy: OnFailure
```

## Cron Expression Quick Reference

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6)
* * * * *
```

| Expression | Meaning |
|------------|---------|
| `0 2 * * *` | Daily at 2 AM |
| `*/15 * * * *` | Every 15 minutes |
| `0 0 * * 0` | Weekly on Sunday midnight |

## Key Parameters

| Parameter | Purpose | Default |
|-----------|---------|---------|
| `completions` | Successful completions needed | 1 |
| `parallelism` | Max concurrent Pods | 1 |
| `backoffLimit` | Retries before failure | 6 |
| `restartPolicy` | Pod restart behavior | Must be Never or OnFailure |
| `ttlSecondsAfterFinished` | Auto-delete after completion | unset |
| `concurrencyPolicy` | Overlapping execution handling | Allow |

## CronJob Concurrency Policies

| Policy | Behavior |
|--------|----------|
| `Allow` | Create new Job even if previous running |
| `Forbid` | Skip new Job if previous still running |
| `Replace` | Cancel running Job, start new one |

## AI Agent Use Cases

1. **Nightly embedding refresh**: CronJob at 2 AM with `concurrencyPolicy: Forbid`
2. **One-time model migration**: Job with `ttlSecondsAfterFinished: 3600`
3. **Parallel document processing**: Job with high `completions` and moderate `parallelism`
4. **Weekly log cleanup**: CronJob with `0 0 * * 0` schedule

## Common Mistakes

1. **Using `restartPolicy: Always`** - Jobs require `Never` or `OnFailure`
2. **Forgetting `backoffLimit`** - Default 6 retries may not be appropriate
3. **No `concurrencyPolicy`** on long-running CronJobs - Can cause overlapping runs
4. **Not setting history limits** - Old Jobs/Pods accumulate indefinitely

## When to Use Each

| Workload Type | Use |
|---------------|-----|
| Always-on service | Deployment |
| One-time task | Job |
| Scheduled task | CronJob |
| Batch processing | Job with parallelism |
