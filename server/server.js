// importar a lib express 
const express = require('express');
const path = require('path')
const pages = require('./pages.js')
// iniciando o express 
const server = express()
server
    .use(express.urlencoded({extended: true}))
    .use(express.static(path.join(__dirname , 'views')))
    // configurar template engine 
    .set ('views', path.join(__dirname , 'views'))
    .set ('view engine', 'hbs')
    // criar uma rota 
    .get('/', pages.index )



// ligar o servidor
server.listen(5500)