Links in the BioSamples API
============================

In BioSamples API links are used to connect resources. Use the links to move reliably through the API.
For more details about links, check out the `standard docs <https://tools.ietf.org/html/rfc5988>`_ and the
`link relation types <https://www.iana.org/assignments/link-relations/link-relations.xhtml>`_


Pagination Links
----------------

.. list-table:: Pagination links (for navigating collections)
   :header-rows: 1
   :widths: 15 65

   * - **Type**
     - **Description**
   * - ``self``
     - Current page of a collection
   * - ``first``
     - First page of a collection
   * - ``last``
     - Last page of a collection (the ``page`` parameter is deprecated—use the ``cursor`` instead)
   * - ``next``
     - Next page of a collection (``page`` parameter deprecated—use the ``cursor``)
   * - ``prev``
     - Previous page of a collection
   * - ``cursor``
     - Pointer for the next page of a collection (cursor-based pagination)


Relation-Type Links
-------------------

.. list-table:: BioSamples API relation-type links
   :header-rows: 1
   :widths: 20 60

   * - **Type**
     - **Description**
   * - ``autocomplete``
     - Collection of autocompletion terms related to the current query
   * - ``curation``
     - A single curation resource
   * - ``curationLinks``
     - Collection of curation resources associated with a sample
   * - ``curations``
     - Collection of curation resources
   * - ``cursor``
     - Navigation cursor for sample resource collections
   * - ``domainCuration``
     - Filter or limit curations to a specific domain
   * - ``facets``
     - Collection of facets associated with current search results
   * - ``sample``
     - A single sample resource
   * - ``samples``
     - Collection of sample resources
   * - ``self``
     - The canonical link to the current resource
