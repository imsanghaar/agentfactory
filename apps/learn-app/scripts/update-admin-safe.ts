/**
 * Admin Password Update Script - SECURE VERSION
 * 
 * Usage: 
 *   npx tsx scripts/update-admin-safe.ts
 * 
 * NEVER commit .env.local to git!
 */

import { neon } from '@neondatabase/serverless';
import bcrypt from 'bcryptjs';
import * as dotenv from 'dotenv';

// Load from .env.local (gitignored)
dotenv.config({ path: '.env.local' });

async function updateAdmin() {
  if (!process.env.DATABASE_URL) {
    console.error('❌ DATABASE_URL not found in .env.local');
    process.exit(1);
  }

  if (!process.env.ADMIN_PASSWORD) {
    console.error('❌ ADMIN_PASSWORD not found in .env.local');
    process.exit(1);
  }

  const sql = neon(process.env.DATABASE_URL);
  
  // Hash password using bcrypt
  const hashedPassword = await bcrypt.hash(process.env.ADMIN_PASSWORD, 10);
  
  console.log('✓ Generated bcrypt hash');
  
  // Update password in account table
  await sql`
    UPDATE "account"
    SET password = ${hashedPassword}
    WHERE user_id = ${process.env.ADMIN_USER_ID || '7vLaM4vTsd3AZzGaASjEJ1ekqjha7mwS'}
  `;
  
  console.log('✅ Admin password updated!');
  console.log(`   Email: ${process.env.ADMIN_EMAIL || 'admin@example.com'}`);
  console.log('   ✓ Check .env.local for credentials (never commit this file!)');
}

updateAdmin().catch(console.error);
