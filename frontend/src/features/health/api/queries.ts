import { useQuery } from "@tanstack/react-query";
import { getHealth } from "../../../core/api/client";

export function useHealthChecks() {
  const live = useQuery({
    queryKey: ["health", "live"],
    queryFn: () => getHealth("live"),
  });
  const ready = useQuery({
    queryKey: ["health", "ready"],
    queryFn: () => getHealth("ready"),
  });

  return { live, ready };
}
