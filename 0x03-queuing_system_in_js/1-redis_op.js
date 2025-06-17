// 1-redis_op.js

import { createClient, print } from 'redis';

// Create Redis client
const client = createClient();

// Handle connection events
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Set a new school with a given value
 * @param {string} schoolName
 * @param {string} value
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);  // uses redis.print for confirmation
}

/**
 * Display the value of a given school
 * @param {string} schoolName
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}:`, err);
      return;
    }
    console.log(reply);
  });
}

// Call the functions as required
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
