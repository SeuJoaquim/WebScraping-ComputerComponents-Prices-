const Database = require('sqlite-async');



function execute(db){
    return db.exec(`
        CREATE TABLE IF NOT EXISTS storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            actual_price FLOAT,
            lower_price FLOAT,
            ideal_price FLOAT,
            URL TEXT
        );
    `)
}

module.exports = Database.open(__dirname + '/storage.db').then(execute);