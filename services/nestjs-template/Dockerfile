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

COPY package.json pnpm-workspace.yaml ./
RUN pnpm install --prod --no-frozen-lockfile

COPY --from=build /app/dist ./dist

EXPOSE 3000

CMD ["node", "dist/main.js"]
