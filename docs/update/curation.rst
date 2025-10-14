BioSamples Curation Guide
==========================

Sample curation
---------------

BioSamples performs automatic curation and supports manual curation to improve sample data findability and standardization of sample metadata. Curation is applied as layers on top of records, preserving original data while providing cleaned, enriched views.
It removes missing values, performs ontology annotation and text curation through automatic curation. BioSamples also imports curation from other services. The curation rules are described below and updated periodically. The curation records are stored separately along with the original data;


Automatic curation, remove missing values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Missing values—such as ``"N/A"`` or ``"none"``—are automatically removed upon submission.

**Example — original data:**

.. code-block:: json

   "characteristics": {
     "disease state": [
       { "text": "N/A" }
     ],
     "organism": [
       { "text": "Homo sapiens" }
     ]
   }

**After automatic removal:**

.. code-block:: json

   "characteristics": {
     "organism": [
       { "text": "Homo sapiens" }
     ]
   }

Automatic curation, ontology annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatic ontology annotation uses `ZOOMA <https://www.ebi.ac.uk/spot/zooma/>`_ to map sample attribute texts to ontology term URIs - only high-confidence mappings are accepted. If the user already provided ontology terms, those fields are skipped.

**Example — submitted data:**

.. code-block:: json

   "characteristics": {
     "disease state": [
       { "text": "hepatocellular carcinoma" }
     ],
     "organism": [
       { "text": "Homo sapiens" }
     ]
   }

**After ontology annotation:**

.. code-block:: json

   "characteristics": {
     "disease state": [
       {
         "text": "hepatocellular carcinoma",
         "ontologyTerms": ["http://www.ebi.ac.uk/efo/EFO_0000182"]
       }
     ],
     "organism": [
       {
         "text": "Homo sapiens",
         "ontologyTerms": ["http://purl.obolibrary.org/obo/NCBITaxon_9606"]
       }
     ]
   }

Automatic curation, text curation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Text curation standardizes attribute names (for example, removes underscores, corrects case, fixes minor typos), but does not modify attribute values. This process typically completes within 24 hours.

**Example — submitted with inconsistencies:**

.. code-block:: json

   "characteristics": {
     "disease_state": [
       {
         "text": "hepatocellular_carcinoma",
         "ontologyTerms": ["http://www.ebi.ac.uk/efo/EFO_0000182"]
       }
     ],
     "Organism": [
       {
         "text": "Homo sapiens",
         "ontologyTerms": ["http://purl.obolibrary.org/obo/NCBITaxon_9606"]
       }
     ],
     "tissu": [
       {
         "text": "liver"
       }
     ]
   }

**After automatic text curation:**

.. code-block:: json

   "characteristics": {
     "disease state": [
       {
         "text": "hepatocellular_carcinoma",
         "ontologyTerms": ["http://www.ebi.ac.uk/efo/EFO_0000182"]
       }
     ],
     "organism": [
       {
         "text": "Homo sapiens",
         "ontologyTerms": ["http://purl.obolibrary.org/obo/NCBITaxon_9606"]
       }
     ],
     "tissue": [
       {
         "text": "liver"
       }
     ]
   }

.. note::

   Only the attribute names are cleaned; the values remain exactly as submitted.

User supplied curation
----------------------

Users who are not the original submitter may submit an additional curation layer to correct or enhance attributes in existing samples. These are stored and applied alongside automatic curation layers.

How to find all curation records?
---------------------------------

You can retrieve all curation layers associated with a sample using the ``/curationlinks`` endpoint.

**Example URL:**

::

   https://www.ebi.ac.uk/biosamples/samples/SAMEA1607017/curationlinks

This returns all curation records linked to the sample with accession ``SAMEA1607017``.

How to get uncurated data
-------------------------

By default, API responses are curated. To fetch the original, uncurated data, append ``.json?curationdomain=`` to the sample’s API URL.

**Example URL:**

::

   https://www.ebi.ac.uk/biosamples/samples/SAMEA1607017.json?curationdomain=

This returns the raw version of the sample without any curation applied.
