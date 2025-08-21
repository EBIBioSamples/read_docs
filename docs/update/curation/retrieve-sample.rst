How to retrieve sample without any curations or only specified curations
==========================================================================

User requirements
-----------------

I want to retrieve samples without any curations or apply only selected curations.

Limitations
-----------

* The BioSamples JSON API is the only method available for retrieving samples with different curation domains applied.

Use Cases
---------

1. **Retrieve a sample without any curations**

   Include the `applyCurations=false` query parameter to instruct BioSamples to return the original sample without any curations applied.

   .. code-block:: bash

      curl 'https://www.ebi.ac.uk/biosamples/samples/SAMEA9948714?applyCurations=false' \
           -i -X GET \
           -H "Accept: application/json"

2. **View all curations applied to a sample**

   Use the `curationlinks` endpoint to retrieve all curations that have been applied to a specific sample.

   .. code-block:: bash

      curl 'https://www.ebi.ac.uk/biosamples/samples/SAMEA9948714/curationlinks' \
           -i -X GET \
           -H "Accept: application/json"

   In this example, sample `SAMEA9948714` currently has five curations applied — these are all automatic curations performed by BioSamples curation pipelines.
