"use client";

import { useState } from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { OrgBadge } from "@/components/organizations/OrgBadge";
import { RemoveMemberDialog } from "./RemoveMemberDialog";
import { RoleChangeDialog } from "./RoleChangeDialog";
import type { OrgRole } from "@/types/organization";

interface MemberData {
  id: string;
  role: string;
  userId: string;
  userName: string;
  userEmail: string;
  userImage?: string | null;
  createdAt: Date;
}

interface MemberListProps {
  members: MemberData[];
  organizationId: string;
  currentUserId: string;
  currentUserRole: string;
  isOwnerOrAdmin: boolean;
}

export function MemberList({
  members,
  organizationId,
  currentUserId,
  currentUserRole,
  isOwnerOrAdmin,
}: MemberListProps) {
  const [removeMember, setRemoveMember] = useState<MemberData | null>(null);
  const [changeRoleMember, setChangeRoleMember] = useState<MemberData | null>(null);

  // Count owners to prevent removing last owner
  const ownerCount = members.filter((m) => m.role === "owner").length;

  // Check if current user can manage a specific member
  const canManageMember = (memberRole: string, memberId: string): boolean => {
    if (!isOwnerOrAdmin) return false;
    if (memberId === currentUserId) return false; // Can't manage yourself

    // Role hierarchy: owner > admin > manager > proctor > editor > member
    const roleHierarchy: Record<string, number> = {
      owner: 6,
      admin: 5,
      manager: 4,
      proctor: 3,
      editor: 2,
      member: 1,
    };

    const currentLevel = roleHierarchy[currentUserRole] || 0;
    const memberLevel = roleHierarchy[memberRole] || 0;

    // Can only manage members at lower levels
    return currentLevel > memberLevel;
  };

  const getInitials = (name: string, email: string): string => {
    if (name) {
      return name
        .split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase()
        .slice(0, 2);
    }
    return email.slice(0, 2).toUpperCase();
  };

  if (members.length === 0) {
    return (
      <div className="text-center py-12">
        <svg
          className="mx-auto h-12 w-12 text-muted-foreground/50"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
          />
        </svg>
        <p className="mt-4 text-muted-foreground">No members yet</p>
      </div>
    );
  }

  return (
    <>
      <div className="divide-y divide-border">
        {members.map((m) => {
          const isCurrentUser = m.userId === currentUserId;
          const canManage = canManageMember(m.role, m.userId);
          const isLastOwner = m.role === "owner" && ownerCount === 1;

          return (
            <div
              key={m.id}
              className="flex items-center justify-between py-4 px-2 hover:bg-muted/50 rounded-lg transition-colors"
            >
              <div className="flex items-center gap-4">
                <Avatar className="h-10 w-10">
                  <AvatarImage src={m.userImage || undefined} alt={m.userName} />
                  <AvatarFallback className="bg-primary/10 text-primary font-medium">
                    {getInitials(m.userName, m.userEmail)}
                  </AvatarFallback>
                </Avatar>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-medium text-foreground">
                      {m.userName || m.userEmail}
                    </span>
                    {isCurrentUser && (
                      <span className="text-xs text-muted-foreground">(you)</span>
                    )}
                  </div>
                  <span className="text-sm text-muted-foreground">{m.userEmail}</span>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <OrgBadge role={m.role as OrgRole} />

                {canManage && (
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="icon" className="h-8 w-8">
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
                            d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
                          />
                        </svg>
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuItem onClick={() => setChangeRoleMember(m)}>
                        <svg
                          className="w-4 h-4 mr-2"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                          />
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                          />
                        </svg>
                        Change Role
                      </DropdownMenuItem>
                      <DropdownMenuSeparator />
                      <DropdownMenuItem
                        onClick={() => setRemoveMember(m)}
                        className="text-red-600 focus:text-red-600"
                        disabled={isLastOwner}
                      >
                        <svg
                          className="w-4 h-4 mr-2"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                          />
                        </svg>
                        Remove Member
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Remove Member Dialog */}
      {removeMember && (
        <RemoveMemberDialog
          open={!!removeMember}
          onOpenChange={(open) => !open && setRemoveMember(null)}
          member={removeMember}
          organizationId={organizationId}
          isLastOwner={removeMember.role === "owner" && ownerCount === 1}
        />
      )}

      {/* Change Role Dialog */}
      {changeRoleMember && (
        <RoleChangeDialog
          open={!!changeRoleMember}
          onOpenChange={(open) => !open && setChangeRoleMember(null)}
          member={changeRoleMember}
          organizationId={organizationId}
          currentUserRole={currentUserRole as OrgRole}
        />
      )}
    </>
  );
}
