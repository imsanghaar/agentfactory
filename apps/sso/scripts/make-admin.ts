import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function makeAdmin() {
  const sql = neon(process.env.DATABASE_URL!);
  await sql(`UPDATE "user" SET role = 'admin' WHERE email = 'admin@robolearn.io'`);
  console.log('✅ Admin role granted to admin@robolearn.io!');
}

makeAdmin();
