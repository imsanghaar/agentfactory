"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { toast } from "@/lib/utils/toast";
import { authClient } from "@/lib/auth-client";
import { useRouter } from "next/navigation";
import { getDaysUntilExpiry, isInvitationExpired } from "@/lib/utils/organization";

interface Invitation {
  id: string;
  email: string;
  role: string | null;
  status: string;
  expiresAt: Date;
  createdAt: Date;
}

interface PendingInvitationsProps {
  invitations: Invitation[];
  organizationId: string;
}

export function PendingInvitations({ invitations, organizationId }: PendingInvitationsProps) {
  const router = useRouter();
  const [cancelingId, setCancelingId] = useState<string | null>(null);

  const handleCancel = async (invitationId: string) => {
    setCancelingId(invitationId);

    try {
      await authClient.organization.cancelInvitation({
        invitationId,
      });

      toast.success("Invitation cancelled");
      router.refresh();
    } catch (error) {
      console.error("Failed to cancel invitation:", error);
      toast.error("Failed to cancel invitation");
    } finally {
      setCancelingId(null);
    }
  };

  if (invitations.length === 0) {
    return null;
  }

  return (
    <div className="bg-card border border-border rounded-lg shadow-sm p-6">
      <h3 className="text-lg font-semibold text-foreground mb-4">
        Pending Invitations ({invitations.length})
      </h3>

      <div className="space-y-3">
        {invitations.map((inv) => {
          const expired = isInvitationExpired(inv.expiresAt);
          const daysLeft = getDaysUntilExpiry(inv.expiresAt);

          return (
            <div
              key={inv.id}
              className={`flex items-center justify-between p-4 rounded-lg border ${
                expired ? "bg-red-50 border-red-200" : "bg-muted/50 border-border"
              }`}
            >
              <div className="flex items-center gap-4">
                <div className="h-10 w-10 rounded-full bg-primary/10 flex items-center justify-center">
                  <svg
                    className="h-5 w-5 text-primary"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                    />
                  </svg>
                </div>
                <div>
                  <p className="font-medium text-foreground">{inv.email}</p>
                  <div className="flex items-center gap-2 mt-1">
                    <Badge variant="outline" className="capitalize">
                      {inv.role || "member"}
                    </Badge>
                    {expired ? (
                      <span className="text-xs text-red-600">Expired</span>
                    ) : (
                      <span className="text-xs text-muted-foreground">
                        Expires in {daysLeft} day{daysLeft !== 1 ? "s" : ""}
                      </span>
                    )}
                  </div>
                </div>
              </div>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleCancel(inv.id)}
                disabled={cancelingId === inv.id}
                className="text-muted-foreground hover:text-red-600"
              >
                {cancelingId === inv.id ? (
                  <svg
                    className="animate-spin h-4 w-4"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    />
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    />
                  </svg>
                ) : (
                  <svg
                    className="h-4 w-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                )}
              </Button>
            </div>
          );
        })}
      </div>
    </div>
  );
}
