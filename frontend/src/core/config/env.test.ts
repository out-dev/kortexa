import { describe, expect, it } from "vitest";
import { env } from "./env";

describe("environment configuration", () => {
  it("uses the versioned local API by default", () => {
    expect(env.apiBaseUrl).toBe("http://localhost:8000/api/v1");
  });
});
