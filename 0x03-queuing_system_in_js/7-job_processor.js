import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate progress steps (for demonstration)
  job.progress(0, 100);

  // You can simulate delay or work using setTimeout if needed
  if (phoneNumber && message) {
    job.progress(50, 100);
    done(); // Finish successfully
  } else {
    done(new Error('Missing phoneNumber or message'));
  }
}

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
