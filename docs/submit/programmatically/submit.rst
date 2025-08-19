Register Samples via API
========================

Using the BioSamples API you can submit new samples to our resource, as well as update or curate samples.

This website requires the limited processing of your personal data in order to function. By using the site you are agreeing to this as outlined in our `Submission Privacy Notice <https://www.ebi.ac.uk/biosamples/privacy/privacy_notice.pdf>`_.

Contents
--------

- `Submission minimal fields`_
- `Submit a sample`_
- `Update sample`_
- `Submit structured data`_
- `Submit curation object`_
- :ref:`accessioning a sample`.
- :ref:`validating sample fields`.
- `POST sample with external references`_
- `PUT sample with relationships`_



Submission minimal fields
--------------------------
**Sample**

.. list-table:: Sample submission fields
   :header-rows: 1
   :widths: 15 40 20 25

   * - **Field**
     - **Description**
     - **Type**
     - **Cardinality**
   * - name
     - The short name of the sample.
     - `String`
     - Required
   * - release
     - The date at which the sample was first made public.
     - `Date ISO 8601`
     - Required
   * - update
     - The date at which the sample was last updated.
     - `Date ISO 8601`
     - System Generated
   * - accession
     - The sample unique identifier in the BioSamples database; assigned automatically if omitted.
     - `String`
     - Required for `PUT` requests
   * - characteristics
     - The key-value pairs representing the attributes of the sample.
     - `Object`
     - Optional
   * - externalReferences
     - A list of links to external references (e.g., datasets in other archives).
     - `Array`
     - Optional
   * - relationships
     - A list of relationships this sample has to other, existing, samples.
     - `Array`
     - Optional
   * - data
     - A structured format (e.g., antibiogram) alongside key-value pairs.
     - `Array`
     - Optional (required only for structured-data submission)

.. list-table:: Structure of `characteristics` elements
   :header-rows: 1
   :widths: 20 40 20

   * - **Field**
     - **Type**
     - **Cardinality**
   * - text
     - `String`
     - Recommended
   * - ontologyTerms
     - `Array`
     - Optional
   * - unit
     - `String`
     - Optional

**Curation Link**

.. list-table:: Curation link fields
   :header-rows: 1
   :widths: 25 25 25

   * - **Field**
     - **Type**
     - **Cardinality**
   * - sample
     - `String`
     - Required
   * - curation
     - `Object`
     - Required
   * - curation.attributesPre
     - `Array`
     - Required (could be empty)
   * - curation.attributesPost
     - `Array`
     - Required (could be empty)
   * - curation.externalReferencesPre
     - `Array`
     - Required (could be empty)
   * - curation.externalReferencesPost
     - `Array`
     - Required (could be empty)

Submit a sample
----------------

`POST` a sample to BioSamples.

**Request**

.. code-block:: http

   POST /biosamples/samples HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 121
   Host: www.ebi.ac.uk

   {
     "name" : "FakeSample",
     "release" : "2025-07-30T08:54:07.592313138Z",
     "webinSubmissionAccountId" : "Webin-12345"
   }

**Response**

.. code-block:: http

   HTTP/1.1 201 Created
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Location: https://www.ebi.ac.uk/biosamples/samples
   Content-Type: application/hal+json
   Content-Length: 1001

.. code-block:: json

   {
     "name": "FakeSample",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:07.592313138Z",
     "update": "2025-07-30T08:54:07.592313231Z",
     "submitted": "2025-07-30T08:54:07.592313316Z",
     "characteristics": {},
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:07.592313275Z",
     "_links": {
       "self": {"href": "https://www.ebi.ac.uk/biosamples/samples"},
       "applyCurations": {
         "href": "https://www.ebi.ac.uk/biosamples/samples{?applyCurations}",
         "templated": true
       },
       "curationLinks": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/{accession}/curationlinks",
         "templated": true
       },
       "curationLink": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/{accession}/curationlinks/{hash}",
         "templated": true
       },
       "structuredData": {
         "href": "https://www.ebi.ac.uk/biosamples/structureddata/{accession}",
         "templated": true
       }
     }
   }

For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_

Update sample
-------------

`PUT` a sample to BioSamples. The submitted sample must include an accession matching the URL. Updating a sample overwrites its existing content. To preserve existing attributes, download the current sample, augment it, and resubmit.

**Request**

.. code-block:: http

   PUT /biosamples/samples/SAMEA12345 HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 376
   Host: www.ebi.ac.uk

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:04.025031918Z",
     "update": "2025-07-30T08:54:04.025032058Z",
     "submitted": "2025-07-30T08:54:04.025032140Z",
     "characteristics": {},
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:04.025032099Z"
   }

**Response**

.. code-block:: http

   HTTP/1.1 200 OK
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Content-Type: application/hal+json
   Content-Length: 998

.. code-block:: json

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:04.025031918Z",
     "update": "2025-07-30T08:54:04.025032058Z",
     "submitted": "2025-07-30T08:54:04.025032140Z",
     "characteristics": {},
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:04.025032099Z",
     "_links": {
       "self": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345"},
       "applyCurations": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345{?applyCurations}",
         "templated": true
       },
       "curationLinks": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks"},
       "curationLink": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/{hash}",
         "templated": true
       },
       "structuredData": {"href": "https://www.ebi.ac.uk/biosamples/structureddata/SAMEA12345"}
     }
   }

Links

For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_

Submit structured data
----------------------

`PUT` structured data associated with a sample (e.g., antibiogram data).

**Request**

.. code-block:: http

   PUT /biosamples/structureddata/SAMFAKE123456 HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 1825
   Host: www.ebi.ac.uk

   {
     "accession": "SAMFAKE123456",
     "create": "2025-07-30T08:54:07.421677129Z",
     "update": "2025-07-30T08:54:07.421717217Z",
     "data": [
       {
         "domain": "self.ExampleDomain",
         "webinSubmissionAccountId": null,
         "type": "AMR",
         "schema": null,
         "content": [
           {
             "resistancePhenotype": {"value": "intermediate", "iri": null},
             "astStandard": {"value": "CLSI", "iri": null},
             "laboratoryTypingMethod": {"value": "disk diffusion", "iri": null},
             "laboratoryTypingMethodVersionOrReagent": {"value": "missing", "iri": null},
             "vendor": {"value": "Becton Dickinson", "iri": null},
             "measurementSign ": {"value": "==", "iri": null},
             "antibioticName": {"value": "nalidixic acid", "iri": "http://purl.obolibrary.org/obo/value_1"},
             "measurementUnits": {"value": "mm", "iri": null},
             "measurement": {"value": "17", "iri": null},
             "platform": {"value": "missing", "iri": null}
           }
         ]
       },
       {
         "domain": "self.ExampleDomain",
         "webinSubmissionAccountId": null,
         "type": "CHICKEN_DATA",
         "schema": null,
         "content": [
           {
             "Measurement": {"value": "value_1", "iri": null},
             "Marker": {"value": "value_1", "iri": "http://purl.obolibrary.org/obo/value_1"},
             "Method": {"value": "value_1", "iri": null},
             "Measurement Units": {"value": "value_1", "iri": null},
             "Partner": {"value": "value_1", "iri": null}
           }
         ]
       }
     ]
   }

**Response**

.. code-block:: http

   HTTP/1.1 200 OK
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Content-Type: application/hal+json
   Content-Length: 1825

.. code-block:: json

   {
     "accession": "SAMFAKE123456",
     "create": "2025-07-30T08:54:07.421677129Z",
     "update": "2025-07-30T08:54:07.421717217Z",
     "data": [
       {
         "domain": "self.ExampleDomain",
         "webinSubmissionAccountId": null,
         "type": "AMR",
         "schema": null,
         "content": [
           {
             "resistancePhenotype": {"value": "intermediate", "iri": null},
             "astStandard": {"value": "CLSI", "iri": null},
             "laboratoryTypingMethod": {"value": "disk diffusion", "iri": null},
             "laboratoryTypingMethodVersionOrReagent": {"value": "missing", "iri": null},
             "vendor": {"value": "Becton Dickinson", "iri": null},
             "measurementSign ": {"value": "==", "iri": null},
             "antibioticName": {"value": "nalidixic acid", "iri": "http://purl.obolibrary.org/obo/value_1"},
             "measurementUnits": {"value": "mm", "iri": null},
             "measurement": {"value": "17", "iri": null},
             "platform": {"value": "missing", "iri": null}
           }
         ]
       },
       {
         "domain": "self.ExampleDomain",
         "webinSubmissionAccountId": null,
         "type": "CHICKEN_DATA",
         "schema": null,
         "content": [
           {
             "Measurement": {"value": "value_1", "iri": null},
             "Marker": {"value": "value_1", "iri": "http://purl.obolibrary.org/obo/value_1"},
             "Method": {"value": "value_1", "iri": null},
             "Measurement Units": {"value": "value_1", "iri": null},
             "Partner": {"value": "value_1", "iri": null}
           }
         ]
       }
     ]
   }

Links
For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_

Submit curation object
----------------------

`POST` a curation object to BioSamples.

**Request**

.. code-block:: http

   POST /biosamples/samples/SAMEA12345/curationlinks HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 1144
   Host: www.ebi.ac.uk

   {
     "sample": "SAMEA12345",
     "curation": {
       "attributesPre": [
         {"type": "Organism", "value": "Human", "iri": ["9606"]}
       ],
       "attributesPost": [
         {"type": "Organism", "value": "Homo sapiens", "iri": ["http://purl.obolibrary.org/obo/NCBITaxon_9606"]}
       ],
       "externalReferencesPre": [
         {"url": "www.google.com", "duo": []}
       ],
       "externalReferencesPost": [
         {"url": "www.ebi.ac.uk/ena/ERA123456", "duo": []}
       ],
       "relationshipsPre": [],
       "relationshipsPost": [
         {"source": "SAMFAKE123456", "type": "DERIVED_FROM", "target": "SAMFAKE7654321"}
       ],
       "externalPre": [
         {"url": "www.google.com", "duo": []}
       ],
       "externalPost": [
         {"url": "www.ebi.ac.uk/ena/ERA123456", "duo": []}
       ],
       "hash": "09a5a9cddbea9f5bb6302b86b922c408abc92b8b10c78f0662ac7e41fd44e91f"
     },
     "domain": null,
     "webinSubmissionAccountId": "Webin-12345",
     "created": "2025-07-30T08:54:05.338606736Z",
     "hash": "d1f611ec2c8caf3d9f58fa40227ea60ebb5fc00eda06338fb81db7d987a6fa63"
   }

**Response**

.. code-block:: http

   HTTP/1.1 201 Created
   Location: https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/d1f611ec2c8caf3d9f58fa40227ea60ebb5fc00eda06338fb81db7d987a6fa63
   Content-Type: application/hal+json
   Content-Length: 1397

.. code-block:: json

   {
     "sample": "SAMEA12345",
     "curation": {
       "attributesPre": [{"type": "Organism", "value": "Human", "iri": ["9606"]}],
       "attributesPost": [{"type": "Organism", "value": "Homo sapiens", "iri": ["http://purl.obolibrary.org/obo/NCBITaxon_9606"]}],
       "externalReferencesPre": [{"url": "www.google.com", "duo": []}],
       "externalReferencesPost": [{"url": "www.ebi.ac.uk/ena/ERA123456", "duo": []}],
       "relationshipsPre": [],
       "relationshipsPost": [{"source": "SAMFAKE123456", "type": "DERIVED_FROM", "target": "SAMFAKE7654321"}],
       "hash": "09a5a9cddbea9f5bb6302b86b922c408abc92b8b10c78f0662ac7e41fd44e91f"]
     },
     "domain": null,
     "webinSubmissionAccountId": "Webin-12345",
     "created": "2025-07-30T08:54:05.338606736Z",
     "hash": "d1f611ec2c8caf3d9f58fa40227ea60ebb5fc00eda06338fb81db7d987a6fa63",
     "_links": {
       "self": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/d1f611ec2c8caf3d9f58fa40227ea60ebb5fc00eda06338f0662ac7e41fd44e91f"
       },
       "sample": {
         "href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345"
       },
       "curation": {
         "href": "https://www.ebi.ac.uk/biosamples/curations/09a5a9cddbea9f5bb6302b86b922c408abc92b8b10c78f0662ac7e41fd44e91f"
       }
     }
   }

Links

For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_

.. _Accessioning a sample:

Accession a sample
------------------

`POST` a sample for accessioning. Accessioned sample is saved as a private sample.

**Request**

.. code-block:: http

   POST /biosamples/samples/accession HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 74
   Host: www.ebi.ac.uk

   {
     "name": "FakeSample",
     "update": "2025-07-30T08:54:06.535179734Z"
   }

**Response**

.. code-block:: http

   HTTP/1.1 201 Created
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Location: https://www.ebi.ac.uk/biosamples/samples/SAMEA12345
   Content-Type: application/json
   Content-Length: 988

.. code-block:: json

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2125-07-30T08:54:06Z",
     "update": "2025-07-30T08:54:06.535179734Z",
     "submitted": "2025-07-30T08:54:06.535179818Z",
     "characteristics": {},
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:06.535179780Z",
     "_links": {
       "self": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345"},
       "applyCurations": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345{?applyCurations}", "templated": true},
       "curationLinks": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks"},
       "curationLink": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/{hash}", "templated": true},
       "structuredData": {"href": "https://www.ebi.ac.uk/biosamples/structureddata/SAMEA12345"}
     }
   }

**Links**

For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_

.. _Validating sample fields:

Validate sample fields
----------------------

`POST` a sample to validate its basic fields before submission.

**Request**

.. code-block:: http

   POST /biosamples/validate HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 440
   Host: www.ebi.ac.uk

   {
     "name": "fake_sample",
     "update": "2025-07-30T08:54:06.361023322Z",
     "release": "2025-07-30T08:54:06.361023223Z",
     "domain": "self.ExampleDomain",
     "characteristics": {
       "material": [{
         "text": "cell line",
         "ontologyTerms": ["EFO_0000322"]
       }],
       "Organism": [{
         "text": "Homo sapiens",
         "ontologyTerms": ["9606"]
       }],
       "checklist": [{
         "text": "BSDC00001"
       }]
     }
   }

**Response**

.. code-block:: http

   HTTP/1.1 200 OK
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Content-Type: application/hal+json
   Content-Length: 559

.. code-block:: json

   {
     "name": "fake_sample",
     "domain": "self.ExampleDomain",
     "taxId": 9606,
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:06.361023223Z",
     "update": "2025-07-30T08:54:06.361023322Z",
     "characteristics": {
       "Organism": [{
         "text": "Homo sapiens",
         "ontologyTerms": ["9606"]
       }],
       "checklist": [{
         "text": "BSDC00001"
       }],
       "material": [{
         "text": "cell line",
         "ontologyTerms": ["EFO_0000322"]
       }]
     },
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:06.361023322Z"
   }

POST sample with external references
------------------------------------

`POST` a sample with external references.

**Request**

.. code-block:: http

   POST /biosamples/samples HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 218
   Host: www.ebi.ac.uk

   {
     "name": "FakeSample",
     "release": "2025-07-30T08:54:06.198269289Z",
     "webinSubmissionAccountId": "Webin-12345",
     "externalReferences": [{
       "url": "https://www.ebi.ac.uk/ena/data/view/SAMEA00001"
     }]
   }

**Response**

.. code-block:: http

   HTTP/1.1 201 Created
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Location: https://www.ebi.ac.uk/biosamples/samples
   Content-Type: application/hal+json
   Content-Length: 1090

.. code-block:: json

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:06.198269289Z",
     "update": "2025-07-30T08:54:06.198269371Z",
     "submitted": "2025-07-30T08:54:06.198269453Z",
     "characteristics": {},
     "externalReferences": [{
       "url": "https://www.ebi.ac.uk/ena/data/view/SAMEA00001",
       "duo": []
     }],
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:06.198269412Z",
     "_links": {
       "self": {"href": "https://www.ebi.ac.uk/biosamples/samples"},
       "applyCurations": {"href": "https://www.ebi.ac.uk/biosamples/samples{?applyCurations}", "templated": true},
       "curationLinks": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks"},
       "curationLink": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/{hash}", "templated": true},
       "structuredData": {"href": "https://www.ebi.ac.uk/biosamples/structureddata/SAMEA12345"}
     }
   }

PUT sample with relationships
-----------------------------

`PUT` a sample with relationships.

**Request**

.. code-block:: http

   PUT /biosamples/samples/SAMEA12345 HTTP/1.1
   Content-Type: application/json
   Authorization: Bearer $TOKEN
   Content-Length: 499
   Host: www.ebi.ac.uk

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:06.713767735Z",
     "update": "2025-07-30T08:54:06.713767809Z",
     "submitted": "2025-07-30T08:54:06.713767894Z",
     "characteristics": {},
     "relationships": [
       {
         "source": "SAMFAKE123456",
         "type": "derived from",
         "target": "SAMFAKE654321"
       }
     ],
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:06.713767854Z"
   }

**Response**

.. code-block:: http

   HTTP/1.1 200 OK
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Content-Type: application/hal+json
   Content-Length: 1121

.. code-block:: json

   {
     "name": "FakeSample",
     "accession": "SAMEA12345",
     "webinSubmissionAccountId": "Webin-12345",
     "status": "PUBLIC",
     "release": "2025-07-30T08:54:06.713767735Z",
     "update": "2025-07-30T08:54:06.713767809Z",
     "submitted": "2025-07-30T08:54:06.713767894Z",
     "characteristics": {},
     "relationships": [
       {
         "source": "SAMFAKE123456",
         "type": "derived from",
         "target": "SAMFAKE654321"
       }
     ],
     "submittedVia": "JSON_API",
     "create": "2025-07-30T08:54:06.713767854Z",
     "_links": {
       "self": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345"},
       "applyCurations": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345{?applyCurations}", "templated": true},
       "curationLinks": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks"},
       "curationLink": {"href": "https://www.ebi.ac.uk/biosamples/samples/SAMEA12345/curationlinks/{hash}", "templated": true},
       "structuredData": {"href": "https://www.ebi.ac.uk/biosamples/structureddata/SAMEA12345"}
     }
   }

Links

For all the links available in BioSamples responses, refer to the `**Links Reference**. <links.html>`_
