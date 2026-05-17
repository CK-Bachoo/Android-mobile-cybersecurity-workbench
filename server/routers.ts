import { z } from "zod";
import { systemRouter } from "./_core/systemRouter";
import { publicProcedure, router } from "./_core/trpc";
import { getRecentTelemetryLogs, insertTelemetryLog, getAIAgents } from "./db";

export const appRouter = router({
  system: systemRouter,
  telemetry: router({
    getLogs: publicProcedure.query(async () => {
      return await getRecentTelemetryLogs(40);
    }),
    ingest: publicProcedure
      .input(
        z.object({
          event: z.string().min(1),
          message: z.string().min(1),
        })
      )
      .mutation(async ({ input }) => {
        const result = await insertTelemetryLog(input.event, input.message);
        return { success: !!result };
      }),
  }),
  agents: router({
    list: publicProcedure.query(async () => {
      return await getAIAgents();
    }),
  }),
});

export type AppRouter = typeof appRouter;
