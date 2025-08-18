API Root
========

The API root provides access to all resources available in BioSamples via hypermedia links (HAL).

Request
-------

.. code-block:: http

   GET /biosamples HTTP/1.1
   Accept: application/hal+json
   Host: www.ebi.ac.uk

Response
--------

.. code-block:: http

   HTTP/1.1 200 OK
   Vary: Origin
   Vary: Access-Control-Request-Method
   Vary: Access-Control-Request-Headers
   Cache-Control: max-age=3600, public
   Content-Type: application/hal+json
   Content-Length: 364

.. code-block:: json

   {
     "_links": {
       "samples": {
         "href": "https://www.ebi.ac.uk/biosamples/samples"
       },
       "curations": {
         "href": "https://www.ebi.ac.uk/biosamples/curations"
       },
       "privacyNotice": {
         "href": "/biosamples/privacy/privacy_notice.pdf"
       },
       "termsOfUse": {
         "href": "https://www.ebi.ac.uk/about/terms-of-use"
       }
     }
   }

Links Reference
---------------

You can find a full list of BioSamples links in the `Links <links.html>`_ Reference documentation section.
