const { test, expect } = require('@playwright/test');
class TestGroupingAndTaggingSystem {
  constructor(browser) {
    this.browser = browser;
  }

  async launchBrowser() {
    const context = await this.browser.newContext();
    const page = await context.newPage();
    return page;
  }

  async closeBrowser(page) {
    await page.close();
  }
}
// Example usage:
const browser = await chromium.launch({ headless: false });
const testGroupingAndTaggingSystem = new TestGroupingAndTaggingSystem(browser);
const page = await testGroupingAndTaggingSystem.launchBrowser();
// Perform tests using page object
await testGroupingAndTaggingSystem.closeBrowser(page);
await browser.close();
