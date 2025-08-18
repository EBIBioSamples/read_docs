API Overview
============

Contents
--------

- **Accessing the service**
  - `Hypermedia <#hypermedia>`__
  - `Content negotiation for data representation <#content-negotiation-for-data-representation>`__
- **HTTP conventions**
  - `Authentication <#authentication>`__
  - `Supported HTTP verbs <#supported-http-verbs>`__
  - `HTTP Status codes <#http-status-codes>`__
  - `HTTPS vs HTTP <#https-vs-http>`__

Accessing the service
---------------------

The BioSamples API is organized around REST. It provides predictable, resource-oriented URLs and uses HTTP response codes to indicate API errors. It leverages HTTP features such as authentication, verbs, and content negotiation.

### Hypermedia

This API uses hypermedia—the responses include links to other resources. Responses follow the HAL format and contain `_links`, which clients should use to navigate between resources. Links may be **templated** (RFC 6570) and require expansion before use.

Link naming conventions:

- Each resource includes a `self` link (the canonical URL).
- Individual resources: named with singular type name (e.g., `sample`).
- Collections: named with camelCased plurals (e.g., `samples`, `curations`, `curationLinks`).

Refer to the **Links** section for a list of all available API links.

### Content negotiation for data representation

BioSamples supports multiple serialization formats via HTTP content negotiation. Although JSON is recommended for API interactions, other supported formats include:

+------------------+-------------------------------------------+-----------------------------------+
| **Type**         | **Accept Header**                         | **Comments**                      |
+==================+===========================================+===================================+
| HTML             | `text/html`                               |                                   |
+------------------+-------------------------------------------+-----------------------------------+
| JSON             | `application/hal+json` / `application/json` | Recommended                      |
+------------------+-------------------------------------------+-----------------------------------+
| JSON-LD          | `application/ld+json`                     | For BioSchemas content            |
+------------------+-------------------------------------------+-----------------------------------+
| XML              | `text/xml` / `application/xml`            | Soon deprecated                   |
+------------------+-------------------------------------------+-----------------------------------+

HTTP conventions
----------------

### Authentication

Authentication is managed via a JWT token in the HTTP request header. In examples requiring authorization, use `$TOKEN` as a placeholder.

### Supported HTTP verbs

BioSamples API follows HTTP method conventions:

+--------+----------------------------------------------+
| **Verb** | **Description**                              |
+========+==============================================+
| `GET`   | Retrieve resources                            |
+--------+----------------------------------------------+
| `POST`  | Create new resources                          |
+--------+----------------------------------------------+
| `PUT`   | Fully replace existing resources              |
+--------+----------------------------------------------+
| `OPTIONS` | Get allowed verbs for a resource             |
+--------+----------------------------------------------+
| `HEAD`  | Check resource availability (no body)         |
+--------+----------------------------------------------+
| `PATCH` | Partially update resources (e.g., add antibiogram data) |
+--------+----------------------------------------------+

### HTTP Status codes

The API uses standard HTTP status codes to indicate request outcomes. For a full reference, see MDN Web Docs.

+------------------+------------------------------------------------+
| **Status Code**  | **Description**                                |
+==================+================================================+
| `200 OK`         | Request succeeded                              |
+------------------+------------------------------------------------+
| `201 Created`    | Resource successfully created with `POST`      |
+------------------+------------------------------------------------+
| `400 Bad Request`| Malformed request; response includes error info|
+------------------+------------------------------------------------+
| `401 Unauthorized` | Missing or invalid `Authorization` header     |
+------------------+------------------------------------------------+
| `403 Forbidden`  | No permission to access this resource          |
+------------------+------------------------------------------------+
| `405 Method Not Allowed` | HTTP method not allowed on this resource |
+------------------+------------------------------------------------+

### HTTPS vs HTTP

BioSamples is served exclusively over HTTPS in line with EMBL-EBI’s security guidelines. Refer to the linked Technical Services Cluster blog post for full details.

