import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function fixRedirectURIs() {
  const sql = neon(process.env.DATABASE_URL!);
  
  // Update RoboLearn Book Interface with additional redirect URIs
  await sql(`
    UPDATE "oauth_application"
    SET redirect_urls = 'http://localhost:3000/auth/callback,http://localhost:3000/callback,https://mjunaidca.github.io/robolearn/auth/callback,https://mjunaidca.github.io/robolearn/callback'
    WHERE client_id = 'robolearn-public-client'
  `);
  
  console.log('✅ Updated RoboLearn Book Interface redirect URIs');
  console.log('   Added: http://localhost:3000/callback');
  console.log('   Added: https://mjunaidca.github.io/robolearn/callback');
}

fixRedirectURIs();
