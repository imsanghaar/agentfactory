"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/navigation";
import { toast } from "@/lib/utils/toast";

interface BulkActionsBarProps {
  selectedCount: number;
  selectedOrgIds: string[];
  onClearSelection: () => void;
}

export function BulkActionsBar({
  selectedCount,
  selectedOrgIds,
  onClearSelection,
}: BulkActionsBarProps) {
  const router = useRouter();
  const [processing, setProcessing] = useState(false);
  const [showConfirmDialog, setShowConfirmDialog] = useState<
    "disable" | "enable" | "delete" | null
  >(null);

  const handleBulkAction = async (action: "disable" | "enable" | "delete") => {
    setProcessing(true);
    try {
      const response = await fetch("/api/admin/organizations/bulk", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action,
          organizationIds: selectedOrgIds,
        }),
      });

      if (!response.ok) {
        throw new Error(`Failed to ${action} organizations`);
      }

      toast.success(`${selectedCount} organizations ${action}d successfully`);
      onClearSelection();
      router.refresh();
    } catch (error) {
      console.error(`Bulk ${action} failed:`, error);
      toast.error(`Failed to ${action} organizations`);
    } finally {
      setProcessing(false);
      setShowConfirmDialog(null);
    }
  };

  return (
    <>
      <div className="bg-pana-50 border-b border-pana-200 px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="text-sm font-medium text-pana-900">
              {selectedCount} organization{selectedCount !== 1 ? "s" : ""} selected
            </div>
            <button
              onClick={onClearSelection}
              className="text-sm text-pana-600 hover:text-pana-700 underline"
            >
              Clear selection
            </button>
          </div>

          <div className="flex items-center gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowConfirmDialog("enable")}
              disabled={processing}
            >
              Enable
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowConfirmDialog("disable")}
              disabled={processing}
            >
              Disable
            </Button>
            <Button
              variant="destructive"
              size="sm"
              onClick={() => setShowConfirmDialog("delete")}
              disabled={processing}
            >
              {processing ? "Processing..." : "Delete"}
            </Button>
          </div>
        </div>
      </div>

      {/* Confirmation Dialog */}
      {showConfirmDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6">
            <h3 className="text-xl font-bold text-slate-900 mb-4">
              Confirm Bulk {showConfirmDialog.charAt(0).toUpperCase() + showConfirmDialog.slice(1)}
            </h3>
            <p className="text-slate-600 mb-6">
              {showConfirmDialog === "delete" ? (
                <>
                  Are you sure you want to <strong>permanently delete</strong>{" "}
                  {selectedCount} organization{selectedCount !== 1 ? "s" : ""}?
                  This action cannot be undone and will remove all associated data,
                  members, and OAuth sessions.
                </>
              ) : (
                <>
                  Are you sure you want to {showConfirmDialog} {selectedCount}{" "}
                  organization{selectedCount !== 1 ? "s" : ""}?
                </>
              )}
            </p>

            {showConfirmDialog === "delete" && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
                <div className="flex items-start gap-3">
                  <svg
                    className="w-5 h-5 text-red-600 mt-0.5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                    />
                  </svg>
                  <div className="flex-1">
                    <div className="font-semibold text-red-900 mb-1">
                      Warning: Irreversible Action
                    </div>
                    <div className="text-sm text-red-700">
                      This will permanently delete all organization data and cannot
                      be recovered.
                    </div>
                  </div>
                </div>
              </div>
            )}

            <div className="flex items-center gap-3 justify-end">
              <Button
                variant="outline"
                onClick={() => setShowConfirmDialog(null)}
                disabled={processing}
              >
                Cancel
              </Button>
              <Button
                variant={showConfirmDialog === "delete" ? "destructive" : "default"}
                onClick={() => handleBulkAction(showConfirmDialog)}
                disabled={processing}
              >
                {processing
                  ? "Processing..."
                  : `Confirm ${showConfirmDialog.charAt(0).toUpperCase() + showConfirmDialog.slice(1)}`}
              </Button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
