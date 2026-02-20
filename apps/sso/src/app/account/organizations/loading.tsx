export default function OrganizationsLoading() {
  return (
    <div className="py-8 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Header Skeleton */}
        <div className="mb-8">
          <div className="relative">
            <div className="absolute -left-3 top-0 bottom-0 w-1 bg-gradient-to-b from-primary/50 to-primary/30 rounded-full animate-pulse" />
            <div className="pl-6 flex items-center justify-between">
              <div>
                <div className="h-10 w-48 bg-muted rounded animate-pulse mb-3" />
                <div className="h-5 w-64 bg-muted rounded animate-pulse" />
              </div>
              <div className="h-10 w-40 bg-muted rounded animate-pulse" />
            </div>
          </div>
        </div>

        {/* Grid Skeleton */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((i) => (
            <div key={i} className="bg-card border border-border rounded-lg p-6 animate-pulse">
              <div className="flex items-center gap-4 mb-4">
                <div className="h-16 w-16 bg-muted rounded-full" />
                <div className="flex-1">
                  <div className="h-6 w-32 bg-muted rounded mb-2" />
                  <div className="h-4 w-24 bg-muted rounded" />
                </div>
              </div>
              <div className="py-4 border-t border-b border-border">
                <div className="flex justify-between">
                  <div className="h-6 w-16 bg-muted rounded" />
                  <div className="h-5 w-20 bg-muted rounded" />
                </div>
              </div>
              <div className="mt-4 flex gap-2">
                <div className="h-10 flex-1 bg-muted rounded" />
                <div className="h-10 flex-1 bg-muted rounded" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
