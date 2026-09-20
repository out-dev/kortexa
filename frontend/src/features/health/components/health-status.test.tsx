import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { HealthStatusCard } from "./health-status";

describe("HealthStatusCard", () => {
  it("renders a successful health result", () => {
    render(<HealthStatusCard label="Liveness" query={{ isPending: false, isError: false } as never} />);

    expect(screen.getByText("Operational")).toBeInTheDocument();
    expect(screen.getByText("Connected to the Kortexa API.")).toBeInTheDocument();
  });

  it("renders a failed health result", () => {
    render(
      <HealthStatusCard
        label="Readiness"
        query={{ isPending: false, isError: true, error: new Error("API unavailable") } as never}
      />,
    );

    expect(screen.getByText("Unavailable")).toBeInTheDocument();
    expect(screen.getByText("API unavailable")).toBeInTheDocument();
  });
});
