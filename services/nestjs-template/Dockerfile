FROM node:24-alpine AS base
WORKDIR /app
RUN corepack enable

FROM base AS deps
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY services/nestjs-template/package.json services/nestjs-template/package.json
RUN pnpm install --filter @toolshare/service-template --frozen-lockfile

FROM deps AS build
COPY services/nestjs-template/nest-cli.json services/nestjs-template/tsconfig*.json services/nestjs-template/
COPY services/nestjs-template/src services/nestjs-template/src
RUN pnpm --filter @toolshare/service-template build

FROM base AS runtime
ENV NODE_ENV=production

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY services/nestjs-template/package.json services/nestjs-template/package.json
RUN pnpm install --filter @toolshare/service-template --prod --frozen-lockfile

WORKDIR /app/services/nestjs-template
COPY --from=build /app/services/nestjs-template/dist ./dist

EXPOSE 3000

CMD ["node", "dist/main.js"]
