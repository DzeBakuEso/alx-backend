// Import Redis and Promisify tools
import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = createClient();

// Handle Redis connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Promisify the GET function
const getAsync = promisify(client.get).bind(client);

// Function to set new key/value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // `print` logs result
}

// Function to display value using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error('Error fetching value:', err);
  }
}

// Call functions as required
(async () => {
  await displaySchoolValue('ALX');
  setNewSchool('ALXSanFrancisco', '100');
  await displaySchoolValue('ALXSanFrancisco');
})();
