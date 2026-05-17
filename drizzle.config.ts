import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './drizzle/schema.ts',
  dialect: 'mysql',
  dbCredentials: {
    url: process.env.DATABASE_URL || 'mysql://GEJb62NVFwAdmwh.root:fF1yfw0xkOe6O23RKk5o@gateway06.us-east-1.prod.aws.tidbcloud.com:4000/WmoNFLzxJwGzQoSVnp5NGL?ssl={"rejectUnauthorized":true}',
  },
});
