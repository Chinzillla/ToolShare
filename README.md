# ToolShare
Tool sharing marketplace

# Toolshare

This project is an open source tool rental platform that helps people rent out tools they already own and helps others access tools without needing to buy them.

## Architecture

![architecture](backend_architecture.png)

## Vision

Many tools are purchased, used once, and then stored away for months or years. The goal is to turn those tools into assets and make them useful again

The vision is to create a simple, community-driven platform where unused tools can become shared resources. Instead of every person or company buying the same expensive tool for a one-time job, we make it easy to rent, borrow, and reuse tools that are already available.

Its simple: list a tool, rent a tool, return a tool.

Over time, the platform can grow into a larger ecosystem for managing tool availability, ownership, rental history, and shared access.

## The Problem

Many tools are underused.

A person might buy a tool for one project and then never use it again. A small business might buy expensive equipment for a specific job, only for that tool to sit on a shelf afterward. In other cases, tools are sold in packs or kits, even when only one is needed.

This creates waste:

- Money is spent on tools that are rarely used
- Useful tools sit idle
- Other people still need those same tools
- Tools sometimes are niche and users cant find them through third parties or have to purchase them used from Ebay
- Buyers are forced to purchase tools for short-term use
- Storage space gets filled with equipment that could be helping someone else

The cycle goes on and on

For many tools, ownership is less important than access.

## The Solution

We want to make it easier to turn unused tools into useful shared resources.

Instead of letting tools sit unused, owners can list them for rent. People who need a tool can find one nearby or available through the platform, rent it, use it, and return it.

This creates value for both sides:

### Tool Owners

Tool owners can earn money from tools they already have.

A tool that was previously sitting unused can become a small source of income.

### Tool Renters

Tool renters can access tools without paying full price to buy them.

This is useful for one-time jobs, short projects, or testing whether a tool is worth buying.

### The Community

We encourage users to reuse, reduce waste, and help people get more value out of existing resources.

## Example Use Case

A user buys a specialty tool for $400.

They only need it for one project.

Instead of storing it away forever, they list it on the marketplace for $25 per rental.

Other users who need that same tool can rent it instead of buying it new.

The original owner earns money back over time, and renters save money by only paying for temporary access.

## Core Features

### User Accounts

Users can sign up, log in, and manage their own listings.

### Tool Listings

Users can create tool listings with basic information such as:

- Tool name
- Description
- Category
- Image
- Rental price
- Availability
- Location

### Browse Tools

Users can view available tools and search or filter by category.

### Tool Details

Each tool has a detail page showing its description, price, owner, and availability.

### Rental Requests

A renter can request to rent a tool.

The tool owner can approve or reject the request.

### Rental Return

Once the renter is ready to return the tool
- They can issue a shipping label
- Return it in person
- Rate the tool owner

### Basic Dashboard

Users can view:

- Tools they listed
- Rental requests they made
- Rental requests they received
- Their reputation rating

## Development Commands

### TypeScript services

Run lint checks:

```shell
corepack pnpm --filter @toolshare/nestjs-template lint:check
```

Run formatting checks:

```shell
corepack pnpm --filter @toolshare/nestjs-template format:check
```

Apply formatting:

```shell
corepack pnpm --filter @toolshare/nestjs-template format
```

### Python services

Install development dependencies:

```powershell
cd services/fastapi-template
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Run lint checks:

```powershell
.venv\Scripts\python.exe -m ruff check .
```

Run formatting checks:

```powershell
.venv\Scripts\python.exe -m ruff format --check .
```

Apply formatting:

```powershell
.venv\Scripts\python.exe -m ruff format .
```

### Database Services

Reset Local Databases:
```shell
pnpm db:reset --yes
```

Run Database Integration Test:
```shell
pnpm db:test
```

## Contributing

This is an open source project.

Contributors are welcome to help with development, design, documentation, testing, and ideas for improving the platform.

Please read [Contributing Rules](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) before you get started.

## AI Use Disclaimer

Toolshare is not an AI-generated “vibe-coded” project.

This project may use AI-assisted tools for brainstorming, documentation, code suggestions, debugging ideas, or improving developer workflow. However, AI is not treated as the author, architect, or final authority for this codebase.

All production code is written, reviewed, and approved by human engineer(s) or project maintainer(s) before being accepted into the project.

AI-generated suggestions are only used when they are understood, verified, and intentionally implemented. Code is not copied blindly from AI tools, and no feature is considered complete simply because an AI system produced an output.

AI may assist the workflow, but it does not replace engineering judgment.
