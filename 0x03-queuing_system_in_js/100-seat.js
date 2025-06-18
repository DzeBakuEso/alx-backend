// 100-seat.js

import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const queue = kue.createQueue();
const client = redis.createClient();

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const seats = await getAsync('available_seats');
  return parseInt(seats || '0', 10);
};

let reservationEnabled = true;

// Set available seats to 50 at startup
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();
    if (seats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    reserveSeat(seats - 1);
    if (seats - 1 === 0) reservationEnabled = false;
    done();
  });
});

app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
