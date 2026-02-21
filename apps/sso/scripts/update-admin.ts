import { neon } from '@neondatabase/serverless';
import bcrypt from 'bcryptjs';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function updateAdmin() {
  const sql = neon(process.env.DATABASE_URL!);
  
  // Hash password using bcrypt (same as legacy NextAuth format)
  const hashedPassword = await bcrypt.hash('imsanghaar', 10);
  
  console.log('Generated bcrypt hash:', hashedPassword);
  
  // Update password in account table
  await sql(`
    UPDATE "account"
    SET password = '${hashedPassword}'
    WHERE user_id = '7vLaM4vTsd3AZzGaASjEJ1ekqjha7mwS'
  `);
  
  console.log('✅ Admin password updated with bcrypt hash!');
  console.log('   Email: imamsanghaar@gmail.com');
  console.log('   Password: imsanghaar');
}

updateAdmin();
