import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { AppProvider } from "../../../core/providers/app-provider";
import { HomePage } from "./home-page";

describe("HomePage", () => {
  beforeEach(() => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({ status: "ok" }),
      }),
    );
  });

  it("renders the application shell and health cards", async () => {
    render(
      <AppProvider>
        <HomePage />
      </AppProvider>,
    );

    expect(screen.getByText("Kortexa")).toBeInTheDocument();
    expect(screen.getByText("A clear starting point for thoughtful work.")).toBeInTheDocument();
    expect(await screen.findAllByText("Operational")).toHaveLength(2);
  });
});
