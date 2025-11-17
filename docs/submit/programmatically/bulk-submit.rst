Bulk sample registration
========================
How to programmatically submit samples in bulk
----------------------------------------------

The bulk-submit-get-receipt API endpoint allows submitters to send multiple sample metadata records together
(in one bulk operation) and then retrieve a “receipt” that reports the outcome (success/failure) and any
assigned accessions.
In the context of BioSamples this supports high-volume submissions rather than individual sample POSTs.


Example curl commands
---------------------
This is an example of a curl command request and reponse to the bulk-submit-get-receipt API endpoint.

.. code-block:: bash

    curl 'https://wwwdev.ebi.ac.uk/biosamples/v2/samples/bulk-submit-get-receipt' \
        -i -X POST
        -H "Content-Type: application/json;charset=UTF-8"
        -H "Accept: application/hal+json"
        -H "Authorization: Bearer $TOKEN"
        -d '[{
            "name" : "FakeSample1",
            "update" : "2012-03-19T13:56:40.720567Z",
            "release" : "2020-03-10T13:56:40.720559Z",
            "webinSubmissionAccountId" : "Webin-59287",
            "characteristics" : {
            "description" : [ {
                "text" : "fake sample"
            } ],
            "organism" : [ {
                "text" : "Homo sapiens",
                "ontologyTerms" : [ "http://purl.obolibrary.org/obo/NCBITaxon_9606" ]
            } ]
          }
        }]


.. code-block:: json

    {
        "samples": [
            {
                "name": "FakeSample1",
                "accession": "SAMEA131847325",
                "sraAccession": "ERS32039383",
                "webinSubmissionAccountId": "Webin-59287",
                "taxId": 9606,
                "status": "PUBLIC",
                "release": "2020-03-10T13:56:40.720559Z",
                "update": "2025-11-14T12:12:30.396351204Z",
                "submitted": "2025-11-14T12:12:30.396350160Z",
                "characteristics": {
                    "SRA accession": [
                        {
                            "text": "ERS32039383"
                        }
                    ],
                    "description": [
                        {
                            "text": "fake sample"
                        }
                    ],
                    "organism": [
                        {
                            "text": "Homo sapiens",
                            "ontologyTerms": [
                                "http://purl.obolibrary.org/obo/NCBITaxon_9606"
                            ]
                        }
                    ]
                },
                "submittedVia": "JSON_API",
                "create": "2025-11-14T12:12:30.396348732Z"
            }
        ],
        "errors": []
    }





Important details & caveats (especially for microbiome/metagenome use)
----------------------------------------------------------------------

- **Validation & checklists:** For bulk uploads via files, you’re asked to select a “checklist” for validation. The system checks required fields such as Characteristics[Organism].

- **Chunking and submission size:** The bulk route may impose limits (e.g., number of samples per submission, file size). In the cookbook: >200 samples or >20 kB often triggers queue rather than instant processing.

- **Queued vs immediate:** For queued submissions you don’t immediately get the accessions; you receive a submission ID and later you get the mapping. This means your pipeline must poll/wait for completion.

- **Relationships between samples:** If your microbiome context involves derivation (e.g., same donor, multiple timepoints, replicates, derived_from relationships), you may need to include relationship attributes (e.g., derived_from, same_as). The API reference shows sample metadata supports relationships.

- **Release date / privacy:** In the sample metadata you must specify a release date. If you need samples to remain private until associated data (e.g., sequence reads) are published, pick appropriate dates.

- **Receipt format:** The receipt is the key item: it shows the mapping from your internal sample names to the assigned BioSamples accessions, and whether each sample succeeded or failed. Keep this mapping because you’ll need to refer to those accessions when linking to datasets.

- **Error handling:** If you receive “COMPLETED WITH ERRORS” or “FAILED”, you should parse the error messages in the receipt (or returned file) to find which samples failed and why (e.g., missing required field, invalid organism, invalid date). Then resubmit only the failed samples if needed.

- **Metadata consistency for search/discovery:** The bulk-submit receipt only ensures technical submission succeeds; you should still review your metadata for FAIR discoverability.
