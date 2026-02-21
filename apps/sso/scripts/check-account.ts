import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function checkAccount() {
  const sql = neon(process.env.DATABASE_URL!);
  
  // Check user table
  const users = await sql(`SELECT id, email, name FROM "user" WHERE email = 'imamsanghaar@gmail.com'`);
  console.log('User record:', users);
  
  // Check account table
  const accounts = await sql(`SELECT id, user_id, account_id, provider_id, password FROM "account"`);
  console.log('All accounts:', accounts);
}

checkAccount();
