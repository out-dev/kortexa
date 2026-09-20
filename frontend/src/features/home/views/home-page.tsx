import { HealthStatusCard } from "../../health/components/health-status";
import { useHealthChecks } from "../../health/api/queries";
import { Button } from "../../../components/ui/button";
import { useTheme } from "../../../core/providers/theme-provider";

export function HomePage() {
  const health = useHealthChecks();
  const { theme, toggleTheme } = useTheme();

  return (
    <main className="mx-auto min-h-screen max-w-5xl px-6 py-10 sm:py-16">
      <header className="max-w-2xl">
        <div className="flex items-center justify-between gap-4">
          <p className="text-sm font-semibold uppercase tracking-[0.2em] text-sky-600 dark:text-sky-400">Kortexa</p>
          <Button type="button" onClick={toggleTheme} aria-label="Toggle color theme">
            {theme === "dark" ? "Light mode" : "Dark mode"}
          </Button>
        </div>
        <h1 className="mt-4 text-4xl font-semibold tracking-tight text-slate-950 dark:text-white sm:text-6xl">
          A clear starting point for thoughtful work.
        </h1>
        <p className="mt-5 text-lg leading-8 text-slate-600 dark:text-slate-300">
          The application shell is ready. Your backend connection is checked below.
        </p>
      </header>
      <section aria-label="API health" className="mt-12 grid gap-4 sm:grid-cols-2">
        <HealthStatusCard label="Liveness" query={health.live} />
        <HealthStatusCard label="Readiness" query={health.ready} />
      </section>
    </main>
  );
}
