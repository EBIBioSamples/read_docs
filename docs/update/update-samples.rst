How to Interactively Update Existing Samples
--------------------------------------------
After `registering your samples <../submit/interactively/step-by-step.html>`_, the uploader will send back a file for download. This file will depend on the size of your sample registration.

- If your tsv file of samples is less than 20 KBytes and the file has less than 200 samples, the result file will have the sample metadata and the accessions. See here for how to update.
- If your tsv file of samples is greater than 20 KBytes or the file has more than 200 samples the result file will have a unique submission ID for the upload. The unique submission ID can be used to get the result of the upload using the View Submissions tab. In this case, on the 'View Submissions' tab, you will be able to download a JSON file which shows the mapping between sampleName and sampleAccession. See here for how to update.

In order to update samples interactively:

1. Take the original tsv submission file and make metadata changes within that file.
2. Add the ``Sample Identifier`` column to the tsv submission file, filling it in with the appropriate sample accessions. You can find these sample accessions in the JSON file in the 'View Submissions' tab.
3. Submit this update tsv submission file to the drag'n'drop uploader.

OR

1. Take the tsv file that you have received with the sample metadata and the ``Sample Identifier`` column already present
2. Remove the receipt in this file, the resulting bottom few rows.
3. Make any metadata changes to this file and submit

The uploader sends back a file for download with the submission result, in case of same time uploads where the file size is less than 20 KBytes and
If you are looking to update existing samples that have been uploaded, you can use the file returned to you after your submission. Please remember to remove the receipt section.




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
