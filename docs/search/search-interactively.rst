How to Search BioSamples Interactively
======================================

This guide explains how to search the BioSamples database using the web interface and the REST API.

Searching BioSamples
--------------------

You can search BioSamples by providing free text or structured queries. The search bar at the top of the BioSamples page accepts:

- **Free text** (e.g. ``liver``) to return all samples with this word in their metadata.
- **Attribute:value pairs** (e.g. ``organism:Homo sapiens``) to refine results.
- **Boolean operators** (``AND``, ``OR``, ``NOT``) to combine search terms.
- **Wildcards** (``*``) for partial matches.

Examples:

.. code-block:: text

   liver AND disease
   organism:"Homo sapiens" AND tissue:lung
   cell* AND NOT cancer

Advanced search
---------------

You can also search on **specific attributes** and filter by accession, dates, or metadata values.
Queries follow the EBISearch syntax: https://www.ebi.ac.uk/ebisearch/documentation

REST API Search
---------------

The same search functionality is available programmatically through the REST API.

**Endpoint:**

.. code-block:: text

   https://www.ebi.ac.uk/biosamples/samples

**Example request:**

.. code-block:: bash

   curl "https://www.ebi.ac.uk/biosamples/samples?text=lung"

**Example response:**

.. code-block:: json

   {
     "content": [
       {
         "accession": "SAMEA1234567",
         "name": "Human lung tissue",
         "characteristics": {
           "organism": [ { "text": "Homo sapiens" } ],
           "tissue": [ { "text": "lung" } ]
         }
       }
     ],
     "page": {
       "size": 25,
       "totalElements": 1,
       "totalPages": 1,
       "number": 0
     }
   }

Faceted search
--------------

Results can be filtered further using **facets** (e.g. by organism, project, or date).
Facets are shown on the left side of the BioSamples web interface and can also be used via the REST API.

.. code-block:: bash

   curl "https://www.ebi.ac.uk/biosamples/samples?text=liver&filter=organism:Homo sapiens"

Tips
----

- Use quotes for exact phrases: ``"lung cancer"``
- Use wildcards for partial words: ``hepat*`` (matches ``hepatocyte``, ``hepatitis``)
- Combine terms for precision.

