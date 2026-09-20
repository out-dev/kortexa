import type { UseQueryResult } from "@tanstack/react-query";
import type { HealthStatus } from "../../../core/api/client";

export function HealthStatusCard({
  label,
  query,
}: {
  label: string;
  query: UseQueryResult<HealthStatus, Error>;
}) {
  const state = query.isPending ? "Checking" : query.isError ? "Unavailable" : "Operational";
  const tone = query.isError ? "text-rose-600 dark:text-rose-400" : "text-emerald-600 dark:text-emerald-400";

  return (
    <article className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      <div className="flex items-center justify-between gap-4">
        <h2 className="font-medium text-slate-900 dark:text-white">{label}</h2>
        <span className={`text-sm font-semibold ${tone}`}>{state}</span>
      </div>
      <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">
        {query.isError ? query.error.message : "Connected to the Kortexa API."}
      </p>
    </article>
  );
}
