import { z } from "zod";

const envSchema = z.object({
  DATABASE_URL: z.string().min(1),
  JWT_SECRET: z.string().min(1),
  ownerOpenId: z.string().min(1),
});

export const ENV = {
  DATABASE_URL: process.env.DATABASE_URL || "",
  JWT_SECRET: process.env.JWT_SECRET || "fallback_secret",
  ownerOpenId: process.env.OWNER_OPEN_ID || "U8m5kNZUJGA6baMxYxLncP",
};
