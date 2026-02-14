---
name: fastify-docs
description: Fastify documentation skill. Use when implementing or debugging Fastify services, verifying API behavior (routes, hooks, plugins, validation, request/reply lifecycle), planning migrations, or answering Fastify questions with source-grounded documentation.
---

# Fastify Docs

Use the local references as the primary source of truth for Fastify behavior.

## Quick Start
1. Start from `## Embedded Reference Guide (v5.7.x)` below.
2. Search first, do not open files blindly:
```bash
rg -n "server|route|plugin|hook|schema|validation|serialization" references/
```
3. Read only the files needed for the active question.
4. Prefer `reference-*.md` files for API semantics and exact behavior.
5. Use `guides-*.md` files for patterns, architecture, and operational advice.
6. For plugin/package discovery, use [ecosystem.md](references/ecosystem.md).

## Answering Rules
1. Ground claims in retrieved Fastify reference files.
2. Cite exact local file paths in responses when explaining non-trivial behavior.
3. State uncertainty explicitly when the mirrored docs do not cover an edge case.
4. Avoid inventing Fastify options, hooks, lifecycle order, or plugin behavior.

## Scope Discipline
1. Keep context small: load only relevant documents from `references/`.
2. Treat `v5.7.x` references as the canonical version for this snapshot.
3. If a needed topic is missing from `v5.7.x`, state the gap and request a refresh from a newer snapshot.
4. Use `## Embedded Reference Guide (v5.7.x)` as the single navigation entrypoint in this file.


## Embedded Reference Guide (v5.7.x)

# Index

## Core Documents[​](#core-documents "Direct link to Core Documents")

[]()

For the full table of contents (TOC), see [below](#reference-toc). The following list is a subset of the full TOC that detail core Fastify APIs and concepts in order of most likely importance to the reader:

* [Server](references/reference-Server.md): Documents the core Fastify API. Includes documentation for the factory function and the object returned by the factory function.
* [Lifecycle](references/reference-Lifecycle.md): Explains the Fastify request lifecycle and illustrates where [Hooks](references/reference-Hooks.md) are available for integrating with it.
* [Routes](references/reference-Routes.md): Details how to register routes with Fastify and how Fastify builds and evaluates the routing trie.
* [Request](references/reference-Request.md): Details Fastify's request object that is passed into each request handler.
* [Reply](references/reference-Reply.md): Details Fastify's response object available to each request handler.
* [Validation and Serialization](references/reference-Validation-and-Serialization.md): Details Fastify's support for validating incoming data and how Fastify serializes data for responses.
* [Plugins](references/reference-Plugins.md): Explains Fastify's plugin architecture and API.
* [Encapsulation](references/reference-Encapsulation.md): Explains a core concept upon which all Fastify plugins are built.
* [Decorators](references/reference-Decorators.md): Explains the server, request, and response decorator APIs.
* [Hooks](references/reference-Hooks.md): Details the API by which Fastify plugins can inject themselves into Fastify's handling of the request lifecycle.

## Reference Documentation Table Of Contents[​](#reference-documentation-table-of-contents "Direct link to Reference Documentation Table Of Contents")

[]()

This table of contents is in alphabetical order.

* [Content Type Parser](references/reference-ContentTypeParser.md): Documents Fastify's default content type parser and how to add support for new content types.
* [Decorators](references/reference-Decorators.md): Explains the server, request, and response decorator APIs.
* [Encapsulation](references/reference-Encapsulation.md): Explains a core concept upon which all Fastify plugins are built.
* [Errors](references/reference-Errors.md): Details how Fastify handles errors and lists the standard set of errors Fastify generates.
* [Hooks](references/reference-Hooks.md): Details the API by which Fastify plugins can inject themselves into Fastify's handling of the request lifecycle.
* [HTTP2](references/reference-HTTP2.md): Details Fastify's HTTP2 support.
* [Lifecycle](references/reference-Lifecycle.md): Explains the Fastify request lifecycle and illustrates where [Hooks](references/reference-Hooks.md) are available for integrating with it.
* [Logging](references/reference-Logging.md): Details Fastify's included logging and how to customize it.
* [Long Term Support](references/reference-LTS.md): Explains Fastify's long term support (LTS) guarantee and the exceptions possible to the [semver](https://semver.org) contract.
* [Middleware](references/reference-Middleware.md): Details Fastify's support for Express.js style middleware.
* [Plugins](references/reference-Plugins.md): Explains Fastify's plugin architecture and API.
* [Reply](references/reference-Reply.md): Details Fastify's response object available to each request handler.
* [Request](references/reference-Request.md): Details Fastify's request object that is passed into each request handler.
* [Routes](references/reference-Routes.md): Details how to register routes with Fastify and how Fastify builds and evaluates the routing trie.
* [Server](references/reference-Server.md): Documents the core Fastify API. Includes documentation for the factory function and the object returned by the factory function.
* [TypeScript](references/reference-TypeScript.md): Documents Fastify's TypeScript support and provides recommendations for writing applications in TypeScript that utilize Fastify.
* [Validation and Serialization](references/reference-Validation-and-Serialization.md): Details Fastify's support for validating incoming data and how Fastify serializes data for responses.
* [Warnings](references/reference-Warnings.md): Details the warnings Fastify emits and how to solve them.


# Index

## Guides Table Of Contents[​](#guides-table-of-contents "Direct link to Guides Table Of Contents")

[]()

This table of contents is in alphabetical order.

* [Benchmarking](references/guides-Benchmarking.md): This guide introduces how to benchmark applications based on Fastify.
* [Contributing](references/guides-Contributing.md): Details how to participate in the development of Fastify, and shows how to setup an environment compatible with the project's code style.
* [Delay Accepting Requests](references/guides-Delay-Accepting-Requests.md): A practical guide on how to delay serving requests to specific routes until some condition is met in your application. This guide focuses on solving the problem using [`Hooks`](references/reference-Hooks.md), [`Decorators`](references/reference-Decorators.md), and [`Plugins`](references/reference-Plugins.md).
* [Detecting When Clients Abort](references/guides-Detecting-When-Clients-Abort.md): A practical guide on detecting if and when a client aborts a request.
* [Ecosystem](references/guides-Ecosystem.md): Lists all core plugins and many known community plugins.
* [Fluent Schema](references/guides-Fluent-Schema.md): Shows how JSON Schema can be written with a fluent API and used in Fastify.
* [Getting Started](references/guides-Getting-Started.md): Introduction tutorial for Fastify. This is where beginners should start.
* [Migration Guide (v4)](references/guides-Migration-Guide-V4.md): Details how to migrate to Fastify v4 from earlier versions.
* [Migration Guide (v3)](references/guides-Migration-Guide-V3.md): Details how to migrate to Fastify v3 from earlier versions.
* [Plugins Guide](references/guides-Plugins-Guide.md): An informal introduction to writing Fastify plugins.
* [Prototype Poisoning](references/guides-Prototype-Poisoning.md): A description of how the prototype poisoning attack works and is mitigated.
* [Recommendations](references/guides-Recommendations.md): Recommendations for how to deploy Fastify into production environments.
* [Serverless](references/guides-Serverless.md): Details on how to deploy Fastify applications in various Function as a Service (FaaS) environments.
* [Style Guide](references/guides-Style-Guide.md): Explains the writing style we use for the Fastify documentation for those who want to contribute documentation.
* [Testing](references/guides-Testing.md): Explains how to write unit tests for Fastify applications.
* [Write Plugin](references/guides-Write-Plugin.md): A set of guidelines for what the Fastify team considers good practices for writing a Fastify plugin.


Creation note: This file was created by concatenating `reference.md` and `guides.md` from the same Fastify v5.7.x snapshot to provide one entrypoint.
