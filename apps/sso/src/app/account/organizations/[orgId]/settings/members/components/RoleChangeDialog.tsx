"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { toast } from "@/lib/utils/toast";
import { authClient } from "@/lib/auth-client";
import { useRouter } from "next/navigation";
import type { OrgRole } from "@/types/organization";
import { OrgBadge } from "@/components/organizations/OrgBadge";

// Available roles for role change with hierarchy levels
const ALL_ROLES: {
  value: OrgRole;
  label: string;
  description: string;
  level: number;
}[] = [
  {
    value: "owner",
    label: "Owner",
    description: "Full control, can delete org",
    level: 7,
  },
  {
    value: "admin",
    label: "Admin",
    description: "Full admin minus delete org",
    level: 6,
  },
  {
    value: "manager",
    label: "Manager",
    description: "Org management, member CRUD",
    level: 5,
  },
  {
    value: "teacher",
    label: "Teacher",
    description: "Content read, assessment read",
    level: 4,
  },
  {
    value: "proctor",
    label: "Proctor",
    description: "Assessment CRUD + grade",
    level: 4,
  },
  {
    value: "editor",
    label: "Editor",
    description: "Content CRUD, assessment read",
    level: 3,
  },
  {
    value: "member",
    label: "Member",
    description: "Read-only access",
    level: 2,
  },
];

interface RoleChangeDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  member: {
    id: string;
    role: string;
    userId: string;
    userName: string;
    userEmail: string;
  };
  organizationId: string;
  currentUserRole: string;
}

export function RoleChangeDialog({
  open,
  onOpenChange,
  member,
  organizationId,
  currentUserRole,
}: RoleChangeDialogProps) {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(false);
  const [selectedRole, setSelectedRole] = useState<OrgRole>(
    (member.role as OrgRole) || "member",
  );

  // Get current user's level (map any custom role to member level for permission check)
  const currentUserLevel =
    ALL_ROLES.find((r) => r.value === currentUserRole)?.level || 1;

  // Filter roles that the current user can assign (levels below their own)
  const assignableRoles = ALL_ROLES.filter(
    (role) => role.level < currentUserLevel,
  );

  const handleSubmit = async () => {
    if (selectedRole === member.role) {
      onOpenChange(false);
      return;
    }

    setIsLoading(true);

    try {
      await authClient.organization.updateMemberRole({
        organizationId,
        memberId: member.id,
        role: selectedRole,
      });

      toast.success(`Role updated to ${selectedRole}`);
      onOpenChange(false);
      router.refresh();
    } catch (error) {
      console.error("Failed to update role:", error);
      toast.error("Failed to update role");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Change Role</DialogTitle>
          <DialogDescription>
            Update the role for {member.userName || member.userEmail}
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Current Role:{" "}
              <span className="font-semibold capitalize">{member.role}</span>
            </label>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              New Role
            </label>
            <Select
              value={selectedRole}
              onValueChange={(v) => setSelectedRole(v as OrgRole)}
            >
              <SelectTrigger>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {assignableRoles.map((role) => (
                  <SelectItem key={role.value} value={role.value}>
                    <span className="flex items-center gap-2">
                      <OrgBadge role={role.value} />
                      <span className="text-slate-500">{role.description}</span>
                    </span>
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          {selectedRole === "owner" && (
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <p className="text-sm text-amber-800">
                <strong>Warning:</strong> Transferring ownership will make this
                user the owner and demote you to admin.
              </p>
            </div>
          )}
        </div>

        <DialogFooter>
          <Button
            variant="outline"
            onClick={() => onOpenChange(false)}
            disabled={isLoading}
          >
            Cancel
          </Button>
          <Button
            onClick={handleSubmit}
            disabled={isLoading || selectedRole === member.role}
          >
            {isLoading ? "Updating..." : "Update Role"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
