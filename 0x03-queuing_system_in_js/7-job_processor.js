import kue from 'kue';

const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklisted = ['4153518780', '4153518781'];

/**
 * Sends notification and tracks job progress
 * @param {string} phoneNumber
 * @param {string} message
 * @param {Object} job
 * @param {Function} done
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Start progress

  if (blacklisted.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Halfway progress

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process queue with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
