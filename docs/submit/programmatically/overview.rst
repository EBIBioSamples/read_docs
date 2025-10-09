Overview
========

Accessing the service
---------------------

The BioSamples API is organized around REST. It provides predictable, resource-oriented URLs and uses HTTP response codes to indicate API errors. It leverages HTTP features such as authentication, verbs, and content negotiation.

Hypermedia
**********

This API uses hypermedia—the responses include links to other resources. Responses follow the HAL format and contain `_links`, which clients should use to navigate between resources. Links may be **templated** (RFC 6570) and require expansion before use.

Link naming conventions:

- Each resource includes a `self` link (the canonical URL).
- Individual resources: named with singular type name (e.g., `sample`).
- Collections: named with camelCased plurals (e.g., `samples`, `curations`, `curationLinks`).

Refer to the `Links <links.html>`_ section for a list of all available API links.

Content negotiation for data representation
*******************************************

BioSamples supports multiple serialization formats via HTTP content negotiation. Although JSON is recommended for API interactions, other supported formats include:

.. list-table:: BioSamples’s supported serializations
   :header-rows: 1
   :widths: 15 30 40

   * - **Type**
     - **Header**
     - **Comments**
   * - HTML
     - ``Accept: text/html``
     - —
   * - JSON
     - ``Accept: application/hal+json`` or ``Accept: application/json``
     - Recommended
   * - JSON-LD
     - ``Accept: application/ld+json``
     - Use to serve BioSchemas content
   * - XML
     - ``Accept: text/xml`` or ``Accept: application/xml``
     - Soon to be deprecated


HTTP conventions
----------------

Authentication
**************

Authentication is managed via a `JWT <https://www.jwt.io/>`_ token in the HTTP request header. For more details see the `authentication guide <authentication.html>`_ In examples requiring authorization, use `$TOKEN` as a placeholder.

Supported HTTP verbs
********************

BioSamples API follows HTTP method conventions with `HTTP verbs <https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>`_ for each action. See below for the list of verbs available in the BioSamples API.

.. list-table:: BioSamples’s API supported verbs
   :header-rows: 1
   :widths: 15 70

   * - **Verb**
     - **Description**
   * - ``GET``
     - Used for retrieving resources
   * - ``POST``
     - Used for creating resources
   * - ``PUT``
     - Used to entirely replace resources
   * - ``OPTIONS``
     - Can be used to determine which verbs can be used for a resource
   * - ``HEAD``
     - Returns whether a resource is available
   * - ``PATCH``
     - Used to add structured data (e.g. antibiogram data) to existing samples


HTTP Status codes
*****************

The API uses standard HTTP status codes to indicate request outcomes. For a full reference, see `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>`_.

.. list-table:: BioSamples’s API HTTP status codes
   :header-rows: 1
   :widths: 15 65

   * - **Code**
     - **Description**
   * - ``200 OK``
     - The request completed successfully.
   * - ``201 Created``
     - Returned after a successful ``POST`` creating a new resource.
   * - ``400 Bad Request``
     - The request was malformed. The response body will include details about the issue.
   * - ``401 Unauthorized``
     - The request did not include an ``Authorization`` header or the credentials were invalid.
   * - ``403 Forbidden``
     - The client is not permitted to access this resource.
   * - ``405 Method Not Allowed``
     - The HTTP method is not allowed on this resource.


HTTPS vs HTTP
*************

BioSamples is served exclusively over HTTPS in line with EMBL-EBI’s security guidelines. Refer to the linked `Technical Services Cluster blog post <https://www.ebi.ac.uk/about/technology/2017/09/https-by-default/>`_ for full details.

