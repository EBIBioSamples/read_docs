How to Interactively Update Existing Samples
--------------------------------------------
Not... sure....





How to Programmatically Update a Sample
---------------------------------------
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
