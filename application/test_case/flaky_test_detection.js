const { chromium } = require('playwright');
const retry = require('async-retry');

async function retryFlakyTest(testFunction, retries = 3) {
  try {
    await testFunction();
  } catch (error) {
    if (retries > 0) {
      await retry(testFunction, {
        retries: retries - 1,
      });
    } else {
      throw error;
    }
  }
}

module.exports = retryFlakyTest;
