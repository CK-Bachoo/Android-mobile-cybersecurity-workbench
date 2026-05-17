import express from "express";
import * as trpcExpress from "@trpc/server/adapters/express";
import { appRouter } from "../routers";
import { createContext } from "./context";
import path from "path";

const app = express();
app.use(express.json());

app.use("/api/trpc", trpcExpress.createExpressMiddleware({
  router: appRouter,
  createContext,
}));

if (process.env.NODE_ENV === "production") {
  app.use(express.static(path.join(process.cwd(), "dist/public")));
  app.get("*", (req, res) => {
    res.sendFile(path.join(process.cwd(), "dist/public/index.html"));
  });
}

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`[SYSTEM] Engine online on port ${port}`));
