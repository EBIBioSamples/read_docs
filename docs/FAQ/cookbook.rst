BioSamples Cookbook
===================

If you cannot find the answer to your question in this FAQ or the help pages, please email us at ``biosamples@ebi.ac.uk``.



Contents
--------
- `How to check if a sample has been updated using ETAG functionality`_
- `How to bulk upload samples to BioSamples using the drag’n’drop uploader <../submit/interactively/step-by-step.html>`_


How to check if a sample has been updated using ETAG functionality
-------------------------------------------------------------------


If you would like to monitor a batch of samples in BioSamples, it is possible to do so via the ETAG functionality. This feature provides a unique "fingerprint" of the sample that changes as soon as the sample itself changes or a curation to the sample is applied. Basically the ETAG is like a hash of the sample.

With the ETAG you can submit a conditional request to BioSamples using an ``If-None-Match`` header (see `MDN reference <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match>`_ for details).

If the provided ETAG matches the one in BioSamples for the sample, this means the sample has not changed since last update and a ``304 - Not Modified`` status is returned. Otherwise the new content is provided alongside a new ETAG.

Going back to the original scenario, if the ETAGs for all samples you are interested in are stored locally, now you can use that to quickly scan BioSamples and download the content of the samples that have actually been updated.

For this demo we will use ``curl`` for simplicity, but you can use any HTTP client. Also, we’re going to use a real sample, but be aware that the ETAG value may differ from the value at the time of writing.

1. Fetch the Sample and the corresponding ETAG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the request for the sample ``SAMEA2614688``:

.. code-block:: bash

   curl -H "Accept: application/json" -i https://www.ebi.ac.uk/biosamples/samples/SAMEA2614688

Here are the response headers (we don’t really care about the body here):

.. code-block:: text

   HTTP/2 200
   cache-control: max-age=60, public
   content-type: application/json;charset=UTF-8
   strict-transport-security: max-age=0
   date: Tue, 16 Oct 2018 16:12:55 GMT
   x-application-context: application:8081
   x-xss-protection: 1; mode=block
   x-content-type-options: nosniff
   etag: "06b2bf5fb11041e36ad4c29a77ff3be55"
   x-frame-options: DENY
   content-length: 1488

2. Submit a new GET request including the ETAG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submit a new request with the ``If-None-Match`` header and the ETAG:

.. code-block:: bash

   curl -H "Accept: application/json" \
        -H 'If-None-Match: "06b2bf5fb11041e36ad4c29a77ff3be55"' \
        -i https://www.ebi.ac.uk/biosamples/samples/SAMEA2614688

Here are the response headers:

.. code-block:: text

   HTTP/2 304
   cache-control: max-age=60, public
   strict-transport-security: max-age=0
   date: Tue, 16 Oct 2018 16:14:57 GMT
   x-application-context: application:8081
   x-xss-protection: 1; mode=block
   x-content-type-options: nosniff
   etag: "06b2bf5fb11041e36ad4c29a77ff3be55"
   x-frame-options: DENY

3. Submit a GET request with an older ETAG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let’s pretend that your locally stored ETAG is different, like ``"07b2dc735675d4f54f0dc3df82c34daa1"``.

If you use that in the conditional request, you will get a ``200 - OK`` response with the original sample content:

.. code-block:: bash

   curl -H "Accept: application/json" \
        -H 'If-None-Match: "07b2dc735675d4f54f0dc3df82c34daa1"' \
        -i https://www.ebi.ac.uk/biosamples/samples/SAMEA2614688

And here are the response headers:

.. code-block:: text

   HTTP/2 200
   cache-control: max-age=60, public
   content-type: application/json;charset=UTF-8
   strict-transport-security: max-age=0
   date: Thu, 18 Oct 2018 15:40:54 GMT
   x-application-context: application:8081
   x-xss-protection: 1; mode=block
   x-content-type-options: nosniff
   etag: "06b2bf5fb11041e36ad4c29a77ff3be55"
   x-frame-options: DENY
   content-length: 1488

Template
~~~~~~~~

Here is a template ``curl`` request you can use to try the ETAG functionality:

.. code-block:: bash

   curl -H "Accept: application/json" \
        -H 'If-None-Match: <sample-etag-with-quotes>' \
        -i https://www.ebi.ac.uk/biosamples/samples/<sample-accession>
