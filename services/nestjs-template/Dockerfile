FROM node:24-alpine AS base
WORKDIR /app
RUN corepack enable && corepack prepare pnpm@11.1.2 --activate

FROM base AS deps
COPY package.json pnpm-workspace.yaml ./
RUN pnpm install --no-frozen-lockfile

FROM deps AS build
COPY nest-cli.json tsconfig*.json ./
COPY src ./src
RUN pnpm build

FROM base AS runtime
ENV NODE_ENV=production
ENV PORT=3000
ENV LOG_LEVEL=info

COPY --chown=node:node package.json pnpm-workspace.yaml ./
RUN pnpm install --prod --no-frozen-lockfile

COPY --chown=node:node --from=build /app/dist ./dist

USER node

EXPOSE 3000

CMD ["node", "dist/main.js"]
