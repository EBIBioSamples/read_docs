User accounts and authentication
================================

This page describes how to create a user account and log in to use the API.

Overview
--------

We support ENA Webin authentication for access and authorization, via EMBL-EBI’s European Nucleotide Archive (ENA) **Webin authentication** service.
For more information please refer to ENA Webin authentication **API documentation**.

Webin authentication is token based—once you have an account, you can log in with your username and password to receive a **token** (see [jwt.io](https://jwt.io) for more info). This token contains all the information needed to identify who you are and what data you're allowed to access. You present this token to the API every time you make a request.

The Webin authentication token is valid for **3 hours** by default. If you need a token with longer validity—for example, for long-running processes—you can request it using the `ttl` (time-to-live) parameter.

> **Note**: This guide describes authentication against our **production system**. If you are testing on our development server, replace the production URL with the corresponding dev URL:

.. list-table:: Webin authentication URLs
   :header-rows: 1
   :widths: 20 40 40

   * - **Context**
     - **URL (Production)**
     - **URL (Development)**
   * - Webin Auth API
     - ``https://www.ebi.ac.uk/ena/submit/webin/auth``
     - ``https://wwwdev.ebi.ac.uk/ena/submit/webin/auth``


Creating your account
---------------------

You can create an account through the **ENA WEBIN AUTHENTICATION SWAGGER UI**.

How to get a token
------------------

You can obtain a Webin authentication token by running the following `curl` command:

.. code-block:: bash

   TOKEN=$(curl -X POST "https://www.ebi.ac.uk/ena/submit/webin/auth/token" \
     -H "accept: */*" \
     -H "Content-Type: application/json" \
     -d "{\"authRealms\":[\"ENA\"],\"password\":\"your_webin_password\",\"username\":\"your_webin_username\"}")

This command returns the Webin authentication token.

Example response

.. code-block:: text

   eyJhbGciOi...your.jwt.token...FC2Rdig

> **Note**: The token is valid for **3 hours** by default.

How to use the obtained token
-----------------------------

You must add this token as an `Authorization` header in all your API requests, using the following format:

.. code-block:: bash

   curl -i -X POST \
     -H "Accept: application/hal+json" \
     -H "Content-Type: application/hal+json" \
     -H "Authorization: Bearer $TOKEN" \
     https://www.ebi.ac.uk/biosamples/samples \
     -d "{ /* sample content */ }"

Don’t copy and paste your token
-------------------------------

You don’t need to manually copy and paste the token. Instead, set it as an environment variable like so:

.. code-block:: bash

   TOKEN=$(curl -X POST "https://www.ebi.ac.uk/ena/submit/webin/auth/token" \
     -H "accept: */*" \
     -H "Content-Type: application/json" \
     -d "{\"authRealms\":[\"ENA\"],\"password\":\"your_webin_password\",\"username\":\"your_webin_username\"}")

Then refer to this variable in your scripts:

.. code-block:: bash

   curl -i -X POST \
     -H "Accept: application/hal+json" \
     -H "Content-Type: application/hal+json" \
     -H "Authorization: Bearer $TOKEN" \
     https://www.ebi.ac.uk/biosamples/samples \
     -d "{ /* sample content */ }"

Be careful with your token—anyone who has it can act as if they are you.

