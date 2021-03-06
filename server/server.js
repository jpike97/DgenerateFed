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



const uri = "mongodb+srv://" + loginData.username + ":" + loginData.password + "@cluster0.7s8dh.mongodb.net/dGenerate?retryWrites=true&w=majority";
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

var bizPicSnap = mongoose.model('bizPicSnap', new Schema({
  greenTotal: Number,
  redTotal: Number,
  imageTotal: Number,
  HSVavg: Array,
  dateTimeStamp: Date,
  expire_at: {type: Date, default: Date.now, expires: 120} 
}, { collection: 'bizPicSnaps'})
);

var bizWordsCard = mongoose.model('bizWordsCard', new Schema({
  id: String,
  ticker: String,
  currentPrice: Number,
  comments: Array,
  numMentions: Number,
  previousNumMentions: Number,
  dateTimeStamp: Date,
  news: Array
}, { collection: 'bizWordsCards'})
);

var news = mongoose.model('news', new Schema({
  id: String,
  ticker: String,
  currentPrice: Number,
  news: Array,
  dateTimeStamp: Date
}, { collection: 'news'}
));


app.get('/cards', (req, res) => {
  bizWordsCard.find({}, function (error, cards) {
    if (error) { console.error(error); }
    res.send({
      cards: cards
    })
  }).sort({numMentions:-1, currentPrice: -1}).limit(12)
});

app.get('/cards/:id', (req, res) => {
  const id = req.params.id;
  var event = "";
  bizWordsCard.find({ticker: id}, function(err, card) {
    res.send({
      card: card
    })
  }).sort({_id:-1}).limit(1);
});

app.get('/news/:id', (req, res) => {
  const id = req.params.id;
  var event = "";
  news.find({ticker: id}, function(err, card) {
    console.log("hmm");
    console.log(card);
    if (card.length == 0) { 
      console.log("empty");
      res.send({
        news: "no news"
      })
    }
    else { 
      res.send({
        news: card[0].news
      })
    }
  }).sort({_id:-1}).limit(1);
});


//test code end

app.get('/', (req, res) => {
  res.send(`Hi! Server is listening on port ${port}`)
});

app.get('/bizpic', (req, res) => {
  bizPicSnap.find({}, function (error, snap) {
    if (error) { console.error(error); }
    res.send({
      snap: snap
    })
  }).sort({_id:-1}).limit(1)
});

     

// listen on the port
app.listen(port);