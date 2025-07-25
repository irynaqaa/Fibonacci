const { test, expect } = require('@playwright/test');
const allure = require('allure-reporter');
test('test user registration', async ({ page }) => {
  await page.goto('https://example.com/register');
  await page.fill('input[name="username"]', 'username');
  await page.fill('input[name="password"]', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toContainText('Registration successful');

  // Generate test report
  allure.reporter.addTest('test user registration');
  allure.reporter.addStep('fill username');
  allure.reporter.addStep('fill password');
  allure.reporter.addStep('click submit');
});
