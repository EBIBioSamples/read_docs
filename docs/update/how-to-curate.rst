How to Submit a Curation Request
================================

How to curate a sample in BioSamples
-----------------------------------

User requirements
~~~~~~~~~~~~~~~~~

I want to improve the quality of metadata for a sample in BioSamples, but I’m not the owner of the sample.

Requirements
~~~~~~~~~~~~

You need a Webin submission account to proceed with this recipe. Please refer to our Authentication Guide for more information.

Steps
~~~~~

1. **Get the JSON Web Token from the Webin Authentication Service**

   Start by obtaining your Webin authentication JWT to use in your application. Please refer to our Authentication Guide for details.

2. **Produce a BioSamples curation object in JSON format**

   To update a field in a sample without being the sample owner, create a BioSamples curation object. Populate the `attributesPre` field with the current value and the `attributesPost` field with the new value.

   To see a comprehensive example, see here: - :ref:`Submit curation object`
   Below is an example sample (simplified):

   .. code-block:: json

      {
        "name": "OAR_USU_Benz2616_LNG",
        "accession": "SAMN08432304",
        "domain": "self.BiosampleImportNCBI",
        "release": "2018-01-29T00:00:00Z",
        "update": "2018-06-08T16:22:08.220Z",
        "characteristics": {
          "breed": [
            {
              "text": "Rambouillet"
            }
          ],
          "development stage": [
            {
              "text": "adult"
            }
          ]
          ...
        }
      }

   Suppose we want to add an ontology code to the `development stage` attribute:

   **Before:**

   .. code-block:: json

      {
        "type": "development stage",
        "value": "adult"
      }

   **After:**

   .. code-block:: json

      {
        "type": "development stage",
        "value": "adult",
        "iri": [
          "http://www.ebi.ac.uk/efo/EFO_0001272"
        ]
      }

   To apply this curation to sample `SAMN08432304`, create a curation object like:

   .. code-block:: json

      {
        "sample": "SAMN08432304",
        "curation": {
          "attributesPre": [
            {
              "type": "development stage",
              "value": "adult"
            }
          ],
          "attributesPost": [
            {
              "type": "development stage",
              "value": "adult",
              "iri": [
                "http://www.ebi.ac.uk/efo/EFO_0001272"
              ]
            }
          ],
          "externalReferencesPre": [],
          "externalReferencesPost": []
        }
      }

3. **Submit the curation object to BioSamples using a POST request**

   You can now submit the curation object using your preferred HTTP client. Here’s how to do it with `curl`:

   .. code-block:: bash

      curl 'https://www.ebi.ac.uk/biosamples/samples/SAMN08432304/curationlinks' \
           -i -X POST \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer $TOKEN' \
           -d '{
             "sample": "SAMN08432304",
             "curation": {
               "attributesPre": [
                 {
                   "type": "development stage",
                   "value": "adult"
                 }
               ],
               "attributesPost": [
                 {
                   "type": "development stage",
                   "value": "adult",
                   "iri": [
                     "http://www.ebi.ac.uk/efo/EFO_0001272"
                   ]
                 }
               ],
               "externalReferencesPre": [],
               "externalReferencesPost": []
             }
           }'

Templates
~~~~~~~~~

### Attribute and external reference curation template

.. code-block:: json

   {
     "sample": "<accession-of-the-interest-sample>",
     "curation": {
       "attributesPre": [
         {
           "type": "<attribute-name>",
           "value": "<attribute-value>",
           "iri": [ "<existing-iris-if-any>", "..." ]
         },
         ...
       ],
       "attributesPost": [
         {
           "type": "<new-attribute-name>",
           "value": "<new-attribute-value>",
           "iri": [ "<new-iris-if-any>", "..." ]
         },
         ...
       ],
       "externalReferencesPre": [
         {
           "url": "<URL-of-external-reference-to-replace>"
         },
         ...
       ],
       "externalReferencesPost": [
         {
           "url": "<new-URL-of-external-reference>"
         },
         ...
       ]
     }
   }



How to add an external reference to a sample using the JSON API
----------------------------------------------------------------

User requirements
~~~~~~~~~~~~~~~~~

I want to link a BioSamples accession with an external repository or resource even if I’m not the owner of the sample.

Requirements
~~~~~~~~~~~~

You need a Webin submission account to proceed with this recipe. Please refer to our Authentication Guide for more information.

Steps
~~~~~

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
~~~~~~~~~

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






How to retrieve sample without any curations or only specified curations
------------------------------------------------------------------------

User requirements
~~~~~~~~~~~~~~~~~

I want to retrieve samples without any curations or apply only selected curations.

Limitations
~~~~~~~~~~~

* The BioSamples JSON API is the only method available for retrieving samples with different curation domains applied.

Use Cases
~~~~~~~~~

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
