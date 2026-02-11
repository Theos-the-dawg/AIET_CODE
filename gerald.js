const express = require('express')// importing express
const app = express() // initialization of express 
const port = 3000 // port 

// CRUD Functions are important 
//GET 
app.get('/', (req, res) => {
  res.send('Hello World!')
})
// creation of server on localhost 
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
