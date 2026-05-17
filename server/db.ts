import { eq, desc } from "drizzle-orm";
import { drizzle } from "drizzle-orm/mysql2";
import { users, aiAgents, telemetryLogs, InsertUser } from "../drizzle/schema";

let _db: ReturnType<typeof drizzle> | null = null;

export async function getDb() {
  if (!_db && process.env.DATABASE_URL) {
    try {
      _db = drizzle(process.env.DATABASE_URL);
    } catch (error) {
      console.warn("[Database] Connection exception:", error);
      _db = null;
    }
  }
  return _db;
}

export async function getRecentTelemetryLogs(limit: number) {
  const db = await getDb();
  if (!db) return [];
  try {
    return await db.select().from(telemetryLogs).orderBy(desc(telemetryLogs.timestamp)).limit(limit);
  } catch (error) {
    console.error("[Database] Query error:", error);
    return [];
  }
}

export async function insertTelemetryLog(event: string, message: string) {
  const db = await getDb();
  if (!db) return null;
  try {
    return await db.insert(telemetryLogs).values({ event, message, timestamp: new Date() });
  } catch (error) {
    console.error("[Database] Write error:", error);
    return null;
  }
}

export async function getAIAgents() {
  const db = await getDb();
  if (!db) return [];
  try {
    return await db.select().from(aiAgents);
  } catch (error) {
    console.error("[Database] Agent fetch error:", error);
    return [];
  }
}
