const express = require('express')
const restful = require('node-restful')
const server = express()
const mongoose = restful.mongoose
const bodyParse = require('body-parser')
const cors = require('cors')

// DataBases
mongoose.Promise = global.Promise
mongoose.connect('mongodb://db/mydb')

// Middlewares
server.use(bodyParse.urlencoded({extended:true}))
server.use(bodyParse.json())
server.use(cors())

// ODM
const Client = restful.model('Client', {
    name: { type: String, require: true }
})

// Rest API 
Client.methods(['get', 'post', 'put', 'delete'])
Client.updateOptions({new: true, runValidators: true})

// Routes
Client.register(server, '/clients')

//Start Server
server.listen(3000)