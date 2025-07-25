const { chromium } = require('playwright');
// Base class for page object model
class PageObject {
    constructor(page) {
        this.page = page;
    }

    async navigateTo(url) {
        await this.page.goto(url);
    }

    async clickElement(selector) {
        await this.page.click(selector);
    }

    async fillInput(selector, value) {
        await this.page.fill(selector, value);
    }

    async getText(selector) {
        return await this.page.textContent(selector);
    }
}

// Concrete class for login page
class LoginPage extends PageObject {
    constructor(page) {
        super(page);
    }

    async login(username, password) {
        await this.fillInput('#username', username);
        await this.fillInput('#password', password);
        await this.clickElement('#login-button');
    }
}

// Concrete class for home page
class HomePage extends PageObject {
    constructor(page) {
        super(page);
    }

    async getWelcomeMessage() {
        return await this.getText('#welcome-message');
    }
}

// Example usage
(async () => {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();
    const loginPage = new LoginPage(page);
    const homePage = new HomePage(page);

    await loginPage.navigateTo('https://example.com/login');
    await loginPage.login('username', 'password');
    await homePage.navigateTo('https://example.com/home');
    const welcomeMessage = await homePage.getWelcomeMessage();
    console.log(welcomeMessage);

    await browser.close();
})();
