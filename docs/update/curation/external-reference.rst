How to add an external reference to a sample using the JSON API
================================================================

User requirements
-----------------

I want to link a BioSamples accession with an external repository or resource even if I’m not the owner of the sample.

Requirements
------------

You need a Webin submission account to proceed with this recipe. Please refer to our Authentication Guide for more information.

Steps
-----

1. **Get the JSON Web Token from the Webin Authentication Service**

   Start by obtaining your Webin authentication JWT for use in your application. Refer to the Authentication Guide for details.

2. **Produce a BioSamples curation object in JSON format**

   To add an external reference to a sample without being its owner, create a BioSamples curation object. Since you’re only adding link(s), you can leave the `attributesPre`, `attributesPost`, and `externalReferencesPre` fields empty, and add your new link(s) in the `externalReferencesPost` field.

   For example, suppose you have a MGnify sample `ERS645361` that you want to link to the BioSamples entry `SAMEA3219512`:

   .. code-block:: json

      {
        "sample" : "SAMEA3219152",
        "curation" : {
          "attributesPre" : [],
          "attributesPost" : [],
          "externalReferencesPre" : [],
          "externalReferencesPost" : [
            {
              "url" : "https://www.ebi.ac.uk/metagenomics/api/v1/samples/ERS645361"
            }
          ]
        }
      }

3. **Submit the curation object using a POST request**

   You’re now ready to submit the curation object using your preferred HTTP client. Here’s how to do it with `curl`:

   .. code-block:: bash

      curl 'https://www.ebi.ac.uk/biosamples/samples/SAMEA3219152/curationlinks' \
           -i -X POST \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer $TOKEN' \
           -d '{
             "sample" : "SAMEA3219152",
             "curation" : {
               "attributesPre" : [],
               "attributesPost" : [],
               "externalReferencesPre" : [],
               "externalReferencesPost" : [
                 {
                   "url" : "https://www.ebi.ac.uk/metagenomics/api/v1/samples/ERS645361"
                 }
               ]
             }
           }'

   If the response returns a successful status (2xx), you will see the new link available on the sample’s page (e.g. at https://www.ebi.ac.uk/biosamples/samples/SAMEA3219152).

Templates
---------

### New external reference curation template

.. code-block:: json

   {
     "sample" : "<accession-of-the-interested-sample>",
     "curation" : {
       "attributesPre" : [],
       "attributesPost" : [],
       "externalReferencesPre" : [],
       "externalReferencesPost" : [
         {
           "url" : "<the-url-to-the-external-reference-you-want-to-add>"
         }
       ]
     }
   }
