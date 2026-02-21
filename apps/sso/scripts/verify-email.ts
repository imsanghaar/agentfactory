import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function verifyEmail() {
  const sql = neon(process.env.DATABASE_URL!);
  
  // Update email verified status (snake_case column name)
  await sql(`
    UPDATE "user"
    SET email_verified = true
    WHERE email = 'imamsanghaar@gmail.com'
  `);
  
  console.log('✅ Email verified!');
  console.log('   Email: imamsanghaar@gmail.com');
  console.log('   You can now sign in!');
}

verifyEmail();
