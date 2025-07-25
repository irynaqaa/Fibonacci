const { chromium } = require('playwright');
const browser = await chromium.launch({ headless: false });

async function run() {
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.click('text="Login"');
  await page.fill('input[name="username"]', 'username');
  await page.fill('input[name="password"]', 'password');
  await page.click('text="Submit"');
  await browser.close();
}

run();
