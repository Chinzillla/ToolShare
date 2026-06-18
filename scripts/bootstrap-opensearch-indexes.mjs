import https from "node:https";

const opensearchUrl = process.env.OPENSEARCH_URL ?? "https://localhost:9200";
const username = process.env.OPENSEARCH_USERNAME ?? "admin";
const password = process.env.OPENSEARCH_PASSWORD ?? "ToolshareLocal123!";

const indexName = "equipment-listings";

const agent = new https.Agent({
  rejectUnauthorized: false,
});

const authHeader = `Basic ${Buffer.from(`${username}:${password}`).toString("base64")}`;

const indexMapping = {
  mappings: {
    properties: {
      id: { type: "keyword" },
      title: { type: "text" },
      description: { type: "text" },
      category: { type: "keyword" },
      condition: { type: "keyword" },
      location: { type: "text" },
      available: { type: "boolean" },
      createdAt: { type: "date" },
      updatedAt: { type: "date" },
    },
  },
};

async function request(path, options = {}) {
  const url = new URL(path, opensearchUrl);
  const body = options.body;

  return new Promise((resolve, reject) => {
    const requestOptions = {
      method: options.method ?? "GET",
      agent,
      headers: {
        Authorization: authHeader,
        "Content-Type": "application/json",
        ...options.headers,
      },
    };

    const request = https.request(url, requestOptions, (response) => {
      const chunks = [];

      response.on("data", (chunk) => {
        chunks.push(chunk);
      });

      response.on("end", () => {
        const responseBody = Buffer.concat(chunks).toString("utf8");

        resolve({
          ok: response.statusCode >= 200 && response.statusCode < 300,
          status: response.statusCode,
          text: async () => responseBody,
        });
      });
    });

    request.on("error", reject);

    if (body) {
      request.write(body);
    }

    request.end();
  });
}

async function main() {
  const existsResponse = await request(`/${indexName}`, {
    method: "HEAD",
  });

  if (existsResponse.status === 200) {
    console.log(`OpenSearch index already exists: ${indexName}`);
    return;
  }

  if (existsResponse.status !== 404) {
    const body = await existsResponse.text();
    throw new Error(`Failed to check index ${indexName}: ${existsResponse.status} ${body}`);
  }

  const createResponse = await request(`/${indexName}`, {
    method: "PUT",
    body: JSON.stringify(indexMapping),
  });

  if (!createResponse.ok) {
    const body = await createResponse.text();
    throw new Error(`Failed to create index ${indexName}: ${createResponse.status} ${body}`);
  }

  console.log(`Created OpenSearch index: ${indexName}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
