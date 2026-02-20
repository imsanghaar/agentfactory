"use client";

import { useEffect, useState } from "react";
import { formatDistanceToNow } from "date-fns";
import { Button } from "@/components/ui/button";
import { OrgBadge } from "@/components/organizations/OrgBadge";

interface OrgDetails {
  id: string;
  name: string;
  slug: string;
  logo: string | null;
  createdAt: string;
  members: Array<{
    userId: string;
    email: string;
    name: string | null;
    role: string;
    joinedAt: string;
  }>;
  invitations: Array<{
    id: string;
    email: string;
    role: string;
    expiresAt: string;
    status: string;
  }>;
  metadata: Record<string, any> | null;
}

interface OrgDetailsModalProps {
  orgId: string;
  currentUserId: string;
  onClose: () => void;
}

export function OrgDetailsModal({
  orgId,
  currentUserId,
  onClose,
}: OrgDetailsModalProps) {
  const [details, setDetails] = useState<OrgDetails | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchDetails() {
      try {
        setLoading(true);
        const response = await fetch(`/api/admin/organizations/${orgId}`);
        if (!response.ok) {
          throw new Error("Failed to fetch organization details");
        }
        const data = await response.json();
        setDetails(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      } finally {
        setLoading(false);
      }
    }

    fetchDetails();
  }, [orgId]);

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden flex flex-col">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between">
          <h2 className="text-2xl font-bold text-slate-900">
            Organization Details
          </h2>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-slate-600 transition-colors"
          >
            <svg
              className="w-6 h-6"
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
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6">
          {loading && (
            <div className="flex items-center justify-center py-12">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-pana-500"></div>
            </div>
          )}

          {error && (
            <div className="bg-red-50 text-red-600 rounded-lg p-4">{error}</div>
          )}

          {details && (
            <div className="space-y-6">
              {/* Basic Info */}
              <div>
                <h3 className="text-lg font-semibold text-slate-900 mb-4">
                  Basic Information
                </h3>
                <div className="bg-slate-50 rounded-lg p-4 space-y-3">
                  <div className="flex items-center gap-4">
                    {details.logo ? (
                      <img
                        src={details.logo}
                        alt={details.name}
                        className="w-16 h-16 rounded-lg object-cover"
                      />
                    ) : (
                      <div className="w-16 h-16 bg-gradient-to-br from-pana-500 to-pana-600 rounded-lg flex items-center justify-center text-white font-semibold text-2xl">
                        {details.name.charAt(0).toUpperCase()}
                      </div>
                    )}
                    <div>
                      <div className="font-semibold text-lg text-slate-900">
                        {details.name}
                      </div>
                      <code className="text-sm text-slate-600 bg-white px-2 py-1 rounded">
                        @{details.slug}
                      </code>
                    </div>
                  </div>
                  <div className="grid grid-cols-2 gap-4 pt-3 border-t border-slate-200">
                    <div>
                      <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">
                        Created
                      </div>
                      <div className="text-sm text-slate-900">
                        {formatDistanceToNow(new Date(details.createdAt), {
                          addSuffix: true,
                        })}
                      </div>
                    </div>
                    <div>
                      <div className="text-xs text-slate-500 uppercase tracking-wider mb-1">
                        Organization ID
                      </div>
                      <code className="text-xs text-slate-600">
                        {details.id}
                      </code>
                    </div>
                  </div>
                </div>
              </div>

              {/* Members */}
              <div>
                <h3 className="text-lg font-semibold text-slate-900 mb-4">
                  Members ({details.members.length})
                </h3>
                <div className="border border-slate-200 rounded-lg overflow-hidden">
                  <table className="w-full">
                    <thead className="bg-slate-50 border-b border-slate-200">
                      <tr>
                        <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                          User
                        </th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                          Role
                        </th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                          Joined
                        </th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-200">
                      {details.members.map((member) => (
                        <tr key={member.userId} className="hover:bg-slate-50">
                          <td className="px-4 py-3">
                            <div>
                              <div className="font-medium text-slate-900">
                                {member.name || "Unknown"}
                              </div>
                              <div className="text-sm text-slate-600">
                                {member.email}
                              </div>
                            </div>
                          </td>
                          <td className="px-4 py-3">
                            <OrgBadge role={member.role as any} />
                          </td>
                          <td className="px-4 py-3">
                            <div className="text-sm text-slate-600">
                              {formatDistanceToNow(new Date(member.joinedAt), {
                                addSuffix: true,
                              })}
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* Invitations */}
              {details.invitations.length > 0 && (
                <div>
                  <h3 className="text-lg font-semibold text-slate-900 mb-4">
                    Pending Invitations ({details.invitations.length})
                  </h3>
                  <div className="border border-slate-200 rounded-lg overflow-hidden">
                    <table className="w-full">
                      <thead className="bg-slate-50 border-b border-slate-200">
                        <tr>
                          <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                            Email
                          </th>
                          <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                            Role
                          </th>
                          <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                            Expires
                          </th>
                          <th className="px-4 py-3 text-left text-xs font-medium text-slate-600 uppercase tracking-wider">
                            Status
                          </th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-200">
                        {details.invitations.map((inv) => (
                          <tr key={inv.id} className="hover:bg-slate-50">
                            <td className="px-4 py-3 text-sm text-slate-900">
                              {inv.email}
                            </td>
                            <td className="px-4 py-3">
                              <OrgBadge role={inv.role as any} />
                            </td>
                            <td className="px-4 py-3">
                              <div className="text-sm text-slate-600">
                                {formatDistanceToNow(new Date(inv.expiresAt), {
                                  addSuffix: true,
                                })}
                              </div>
                            </td>
                            <td className="px-4 py-3">
                              <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                                {inv.status}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              )}

              {/* Metadata */}
              {details.metadata && Object.keys(details.metadata).length > 0 && (
                <div>
                  <h3 className="text-lg font-semibold text-slate-900 mb-4">
                    Metadata
                  </h3>
                  <div className="bg-slate-50 rounded-lg p-4">
                    <pre className="text-xs text-slate-600 overflow-x-auto">
                      {JSON.stringify(details.metadata, null, 2)}
                    </pre>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-4 border-t border-slate-200 flex items-center justify-between">
          <div>
            {details &&
              (() => {
                const myMembership = details.members.find(
                  (m) => m.userId === currentUserId,
                );
                if (
                  myMembership &&
                  (myMembership.role === "owner" ||
                    myMembership.role === "admin")
                ) {
                  return (
                    <a
                      href={`/account/organizations/${orgId}/settings/members`}
                      className="inline-flex items-center gap-2 text-sm font-medium text-pana-600 hover:text-pana-700 transition-colors"
                    >
                      <svg
                        className="w-4 h-4"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                        />
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                        />
                      </svg>
                      Manage Roles
                    </a>
                  );
                }
                return null;
              })()}
          </div>
          <Button variant="outline" onClick={onClose}>
            Close
          </Button>
        </div>
      </div>
    </div>
  );
}
