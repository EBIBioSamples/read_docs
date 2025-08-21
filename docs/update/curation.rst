Sample Curation Guide
=====================

BioSamples applies both automatic and manual curation to enhance the findability and standardization of sample metadata. Curation is applied as layered records, preserving original data while providing cleaned, enriched views.

Sample curation
---------------

BioSamples performs automatic curation and supports manual curation to improve sample data findability. It removes missing values, performs ontology annotation and text curation through automatic curation. BioSamples also imports curation from other services. The curation rules are described below and updated periodically.
The curation records are stored separately along with the original data; BioSamples applies curation as layered overlays on the original dataset.

Automatic curation, remove missing values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Missing values—such as `"N/A"` or `"none"`—are automatically removed upon submission.

For example, Field ``disease state`` contains ``N/A`` in the original data.

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
