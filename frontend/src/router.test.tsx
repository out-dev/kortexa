import { describe, expect, it } from "vitest";
import { router } from "./router";

describe("application router", () => {
  it("initializes with the home route", () => {
    expect(router.state.location.pathname).toBe("/");
    expect(router.options.routeTree).toBeDefined();
  });
});
