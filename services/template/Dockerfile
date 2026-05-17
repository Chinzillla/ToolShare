FROM node:24-alpine AS base
WORKDIR /app
RUN corepack enable

FROM base AS deps
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY services/template/package.json services/template/package.json
RUN pnpm install --filter template --frozen-lockfile

FROM deps AS build
COPY services/template/nest-cli.json services/template/tsconfig*.json services/template/
COPY services/template/src services/template/src
RUN pnpm --filter template build

FROM base AS runtime
ENV NODE_ENV=production

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY services/template/package.json services/template/package.json
RUN pnpm install --filter template --prod --frozen-lockfile

WORKDIR /app/services/template
COPY --from=build /app/services/template/dist ./dist

EXPOSE 3000

CMD ["node", "dist/main.js"]
