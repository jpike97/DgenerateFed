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
  dateTimeStamp: Date
}, { collection: 'bizPicSnaps'})
);

//test code start
let cards = 
[
  {
    id: 'TSLA',
    ticker: 'TSLA',
    currentPrice: '3,000',
    icon: '',
    numMentions: '36',
    comments: [
      'Contrary to popular belief, Lorem Ipsum is not simext. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney Colleg etur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat in, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical',
      'It is a long established fact that a reader will be distracted by the readable content of a  Virginia page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using ,ish.',
      'Lorem ipsum dolor sit amet, consect. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ply random t officia deserunt mollit  making it look like readable Engl anim id est laborum.',
    ],
  },
  {
    id: 'NIO',
    ticker: 'NIO',
    currentPrice: '26.83',
    icon: '',
    numMentions: '36',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  },
  {
    id: 'ALPHA',
    ticker: 'ALPHA',
    currentPrice: '26.83',
    icon: '',
    numMentions: '10',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  },
  {
    id: 'AMZN',
    ticker: 'AMZN',
    currentPrice: '3,002',
    icon: '',
    numMentions: '1',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  },
  {
    id: 'FB',
    ticker: 'FB',
    currentPrice: '26.12',
    icon: '',
    numMentions: '1',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  },
  {
    id: 'GM',
    ticker: 'GM',
    currentPrice: '12.45',
    icon: '',
    numMentions: '5',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  },
  {
    id: 'UBI',
    ticker: 'UBI',
    currentPrice: '11.78',
    icon: '',
    numMentions: '89',
    comments: [
      'Contrary to a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock',
      'It is a long established fact that a reader will be distracted  . Duis aute irur by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English.',
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequate dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    ],
  }
];

app.get('/cards', (req, res) => {
  res.send(cards);
});

app.get('/cards/:id', (req, res) => {
  const id = Number(req.params.id);
  const event = cards.find(event => event.id === id);
  res.send(event);
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