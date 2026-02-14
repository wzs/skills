# Index

## Core Documents[​](#core-documents "Direct link to Core Documents")

[]()

For the full table of contents (TOC), see [below](#reference-toc). The following list is a subset of the full TOC that detail core Fastify APIs and concepts in order of most likely importance to the reader:

* [Server](reference-Server.md): Documents the core Fastify API. Includes documentation for the factory function and the object returned by the factory function.
* [Lifecycle](reference-Lifecycle.md): Explains the Fastify request lifecycle and illustrates where [Hooks](reference-Hooks.md) are available for integrating with it.
* [Routes](reference-Routes.md): Details how to register routes with Fastify and how Fastify builds and evaluates the routing trie.
* [Request](reference-Request.md): Details Fastify's request object that is passed into each request handler.
* [Reply](reference-Reply.md): Details Fastify's response object available to each request handler.
* [Validation and Serialization](reference-Validation-and-Serialization.md): Details Fastify's support for validating incoming data and how Fastify serializes data for responses.
* [Plugins](reference-Plugins.md): Explains Fastify's plugin architecture and API.
* [Encapsulation](reference-Encapsulation.md): Explains a core concept upon which all Fastify plugins are built.
* [Decorators](reference-Decorators.md): Explains the server, request, and response decorator APIs.
* [Hooks](reference-Hooks.md): Details the API by which Fastify plugins can inject themselves into Fastify's handling of the request lifecycle.

## Reference Documentation Table Of Contents[​](#reference-documentation-table-of-contents "Direct link to Reference Documentation Table Of Contents")

[]()

This table of contents is in alphabetical order.

* [Content Type Parser](reference-ContentTypeParser.md): Documents Fastify's default content type parser and how to add support for new content types.
* [Decorators](reference-Decorators.md): Explains the server, request, and response decorator APIs.
* [Encapsulation](reference-Encapsulation.md): Explains a core concept upon which all Fastify plugins are built.
* [Errors](reference-Errors.md): Details how Fastify handles errors and lists the standard set of errors Fastify generates.
* [Hooks](reference-Hooks.md): Details the API by which Fastify plugins can inject themselves into Fastify's handling of the request lifecycle.
* [HTTP2](reference-HTTP2.md): Details Fastify's HTTP2 support.
* [Lifecycle](reference-Lifecycle.md): Explains the Fastify request lifecycle and illustrates where [Hooks](reference-Hooks.md) are available for integrating with it.
* [Logging](reference-Logging.md): Details Fastify's included logging and how to customize it.
* [Long Term Support](reference-LTS.md): Explains Fastify's long term support (LTS) guarantee and the exceptions possible to the [semver](https://semver.org) contract.
* [Middleware](reference-Middleware.md): Details Fastify's support for Express.js style middleware.
* [Plugins](reference-Plugins.md): Explains Fastify's plugin architecture and API.
* [Reply](reference-Reply.md): Details Fastify's response object available to each request handler.
* [Request](reference-Request.md): Details Fastify's request object that is passed into each request handler.
* [Routes](reference-Routes.md): Details how to register routes with Fastify and how Fastify builds and evaluates the routing trie.
* [Server](reference-Server.md): Documents the core Fastify API. Includes documentation for the factory function and the object returned by the factory function.
* [TypeScript](reference-TypeScript.md): Documents Fastify's TypeScript support and provides recommendations for writing applications in TypeScript that utilize Fastify.
* [Validation and Serialization](reference-Validation-and-Serialization.md): Details Fastify's support for validating incoming data and how Fastify serializes data for responses.
* [Warnings](reference-Warnings.md): Details the warnings Fastify emits and how to solve them.


# Index

## Guides Table Of Contents[​](#guides-table-of-contents "Direct link to Guides Table Of Contents")

[]()

This table of contents is in alphabetical order.

* [Benchmarking](guides-Benchmarking.md): This guide introduces how to benchmark applications based on Fastify.
* [Contributing](guides-Contributing.md): Details how to participate in the development of Fastify, and shows how to setup an environment compatible with the project's code style.
* [Delay Accepting Requests](guides-Delay-Accepting-Requests.md): A practical guide on how to delay serving requests to specific routes until some condition is met in your application. This guide focuses on solving the problem using [`Hooks`](reference-Hooks.md), [`Decorators`](reference-Decorators.md), and [`Plugins`](reference-Plugins.md).
* [Detecting When Clients Abort](guides-Detecting-When-Clients-Abort.md): A practical guide on detecting if and when a client aborts a request.
* [Ecosystem](guides-Ecosystem.md): Lists all core plugins and many known community plugins.
* [Fluent Schema](guides-Fluent-Schema.md): Shows how JSON Schema can be written with a fluent API and used in Fastify.
* [Getting Started](guides-Getting-Started.md): Introduction tutorial for Fastify. This is where beginners should start.
* [Migration Guide (v4)](guides-Migration-Guide-V4.md): Details how to migrate to Fastify v4 from earlier versions.
* [Migration Guide (v3)](guides-Migration-Guide-V3.md): Details how to migrate to Fastify v3 from earlier versions.
* [Plugins Guide](guides-Plugins-Guide.md): An informal introduction to writing Fastify plugins.
* [Prototype Poisoning](guides-Prototype-Poisoning.md): A description of how the prototype poisoning attack works and is mitigated.
* [Recommendations](guides-Recommendations.md): Recommendations for how to deploy Fastify into production environments.
* [Serverless](guides-Serverless.md): Details on how to deploy Fastify applications in various Function as a Service (FaaS) environments.
* [Style Guide](guides-Style-Guide.md): Explains the writing style we use for the Fastify documentation for those who want to contribute documentation.
* [Testing](guides-Testing.md): Explains how to write unit tests for Fastify applications.
* [Write Plugin](guides-Write-Plugin.md): A set of guidelines for what the Fastify team considers good practices for writing a Fastify plugin.


Creation note: This file was created by concatenating `reference.md` and `guides.md` from the same Fastify v5.7.x snapshot to provide one entrypoint.
