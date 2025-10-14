How to Search BioSamples Interactively
======================================

This guide explains how to search the BioSamples database using the web interface and the REST API.

Searching BioSamples
--------------------

You can search `BioSamples <https://www.ebi.ac.uk/biosamples/samples>`_ by providing free text or structured queries. The search bar at the top of the BioSamples page accepts:

- **Free text** (e.g. ``liver``) to return all samples with this word in their metadata.
- **Attribute:value pairs** (e.g. ``organism:Homo sapiens``) to refine results.
- **Boolean operators** (``AND``, ``OR``, ``NOT``) to combine search terms.
- **Wildcards** (``*``) for partial matches.

Examples:

.. code-block:: text

   liver AND disease
   organism:"Homo sapiens" AND tissue:lung
   cell* AND NOT cancer


Search
---------------

You can also search on **specific attributes** and filter by accession, dates, or metadata values.
Results can be narrowed down further using **filters** (e.g. by organism, project, or date).
Facets are shown on the left side of the BioSamples web interface and can also be used via the REST API.

Tips
----

- Use quotes for exact phrases: ``"lung cancer"``
- Use wildcards for partial words: ``hepat*`` (matches ``hepatocyte``, ``hepatitis``)
- Combine terms for precision.

