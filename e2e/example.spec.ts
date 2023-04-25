import { test, expect } from "@playwright/test";

test("should navigate to the id page", async ({ page }) => {
  await page.goto("http://localhost:3000/id");
  await expect(page).toHaveURL("http://localhost:3000/about");
  await expect(page).toContain("text=id");
});
