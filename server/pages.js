const Database = require('../src/module/data/db');

module.exports = {

    async index(req, res) {
        const db = await Database;
        const results = await db.all(`SELECT * FROM storage`);
        const storage = results
        return res.render("index", {storage})
    },
}