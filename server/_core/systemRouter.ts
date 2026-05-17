import { router, publicProcedure } from "./trpc";
import { z } from "zod";

export const systemRouter = router({
  health: publicProcedure.query(() => ({ status: "ONLINE", timestamp: new Date() })),
});
