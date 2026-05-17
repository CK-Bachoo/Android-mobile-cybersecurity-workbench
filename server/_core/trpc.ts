import { initTRPC, TRPCError } from "@trpc/server";
import type { TrpcContext } from "./context";
import superjson from "superjson";

const t = initTRPC.context<TrpcContext>().create({
  transformer: superjson,
});

export const router = t.router;
export const publicProcedure = t.procedure;
export const protectedProcedure = t.procedure.use(({ ctx, next }) => {
  if (!ctx.user) {
    throw new TRPCError({ code: "UNAUTHORIZED", message: "UNAUTHORIZED_ACCESS_DENIED" });
  }
  return next({ ctx });
});
