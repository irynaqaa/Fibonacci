function get_file_content(file_path) {
    const fs = require('fs');
    return fs.readFileSync(file_path, 'utf8');
}

function write_file_content(file_path, content) {
    const fs = require('fs');
    fs.writeFileSync(file_path, content);
}

class Utility {
    constructor(page) {
        this.page = page;
    }

    async login(username, password) {
        await this.page.fillOutForm('#username', username);
        await this.page.fillOutForm('#password', password);
        await this.page.clickElement('#login-button');
    }

    async navigateTo(url) {
        await this.page.navigate(url);
    }
}

class LoginUtility extends Utility {
    constructor(page) {
        super(page);
    }

    async login(username, password) {
        await super.login(username, password);
    }
}
