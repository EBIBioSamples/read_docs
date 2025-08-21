How to curate a sample in BioSamples
====================================

User requirements
-----------------

I want to improve the quality of metadata for a sample in BioSamples, but I’m not the owner of the sample.

Requirements
------------

You need a Webin submission account to proceed with this recipe. Please refer to our Authentication Guide for more information.

Steps
-----

1. **Get the JSON Web Token from the Webin Authentication Service**

   Start by obtaining your Webin authentication JWT to use in your application. Please refer to our Authentication Guide for details.

2. **Produce a BioSamples curation object in JSON format**

   To update a field in a sample without being the sample owner, create a BioSamples curation object. Populate the `attributesPre` field with the current value and the `attributesPost` field with the new value.   See :ref:`Submit curation object` for an example POST request.


Example sample (simplified):

    .. code-block:: json

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
---------

### Attribute and external reference curation template

  .. code-block:: json

   {
     "sample": "<accession-of-the-interest-sample>",
     "curation": {
       "attributesPre": [
         {
           "type": "<attribute-name>",
           "value": "<attribute-value>",
           "iri": ["<existing-iri-if-any>"]
         }
       ],
       "attributesPost": [
         {
           "type": "<new-attribute-name>",
           "value": "<new-attribute-value>",
           "iri": ["<new-iri-if-any>"]
         }
       ],
       "externalReferencesPre": [
         {
           "url": "<URL-of-external-reference-to-replace>"
         }
       ],
