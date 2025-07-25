const { test, expect } = require('@playwright/test');
test.describe.parallel('Test 1', () => {
  test('Test 1.1', async ({ page }) => {
    // Test code
  });

  test('Test 1.2', async ({ page }) => {
    // Test code
  });
});
