const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const app = express();
const port = 8000;
var options = require('./options');

var loginData = {
        username: options.storageConfig.username,
        password: options.storageConfig.password
};


app.use(bodyParser.json());
app.use(cors());
app.use(express.urlencoded({ extended: true }));

const uri = "mongodb+srv://" + loginData.username + ":" + loginData.password + "@cluster0.tgu4c.mongodb.net/sampledatabase?retryWrites=true&w=majority";
mongoose.connect(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => {
  console.log("MongoDB Connected…")
})
.catch(err => console.log(err))

var db = mongoose.connection;
db.once('open', function() {
  console.log("Connection Successful!");
});

var Schema = mongoose.Schema;


var users = mongoose.model('users', new Schema({
  id: String,
  units: Number,
  positions: Array
}, { collection: 'users'}
));

var positions = mongoose.model('positions', new Schema({
  id: String,
  units: Number,
  positions: Array
}, { collection: 'positions'}
));


app.get('/users', (req, res) => {
  users.find({}, function (error, users) {
    if (error) { console.error(error); }
    res.send({
      users: users
    })
  }).sort({numMentions:-1, currentPrice: -1}).limit(12)
});

app.get('/users/:id', (req, res) => {
  const id = req.params.id;
  var event = "";
  users.find({id: id}, function(err, user) {
    res.send({
      user: user
    })
  }).sort({id:-1}).limit(1);
});


//test code end
app.get('/', (req, res) => {
  res.send(`Hi! Server is listening on port ${port}`)
});


// listen on the port
app.listen(port);