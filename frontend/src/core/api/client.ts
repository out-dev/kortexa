import { env } from "../config/env";

export type HealthStatus = { status: string };

export async function getHealth(path: "live" | "ready"): Promise<HealthStatus> {
  const response = await fetch(`${env.apiBaseUrl}/health/${path}`);

  if (!response.ok) {
    throw new Error(`Health check failed with status ${response.status}`);
  }

  return response.json() as Promise<HealthStatus>;
}
