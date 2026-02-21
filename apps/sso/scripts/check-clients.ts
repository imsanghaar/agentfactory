import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

async function checkClients() {
  const sql = neon(process.env.DATABASE_URL!);
  
  const clients = await sql(`
    SELECT client_id, name, redirect_urls, type 
    FROM "oauth_application"
  `);
  
  console.log('Registered OAuth Clients:\n');
  clients.forEach((client: any) => {
    console.log(`\n${client.name || 'Unnamed'}`);
    console.log(`  Client ID: ${client.client_id}`);
    console.log(`  Type: ${client.type}`);
    console.log(`  Redirect URIs:`);
    const urls = (client.redirect_urls || '').split(',');
    urls.forEach((url: string) => {
      if (url.trim()) console.log(`    - ${url.trim()}`);
    });
  });
}

checkClients();
