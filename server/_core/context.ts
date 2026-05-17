import type { Request, Response } from "express";

export interface TrpcContext {
  req: Request;
  res: Response;
  user: {
    id: number;
    openId: string;
    email: string | null;
    name: string | null;
    loginMethod: string;
    role: "user" | "admin";
    createdAt: Date;
    updatedAt: Date;
    lastSignedIn: Date;
  } | null;
}

export function createContext({ req, res }: { req: Request; res: Response }): TrpcContext {
  return { req, res, user: null };
}
