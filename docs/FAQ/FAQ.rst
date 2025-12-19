BioSamples — Frequently Asked Questions (FAQ)
=============================================

If you cannot find the answer to your question in this FAQ or the help pages, please email us at ``biosamples@ebi.ac.uk``.

Contents
--------

- `How to cite BioSamples?`_
- `How frequent are updates to BioSamples' data?`_
- `What pattern do BioSamples accessions follow?`_
- `Why are some BioSamples linked to RRIDs?`_
- `What is the Bioschemas export?`_
- `How can I stay informed about BioSamples?`_
- `Why do some of my search results not contain my query?`_
- `How will my personal data be used?`_
- `I think some of the data is wrong. Can you fix it?`_
- `Where is the BioSamples source code?`_
- `How do I send my SampleTab files to BioSamples?`_
- `My sample doesn’t have a Submitted on date?`_
- `Why was the ID created on field removed?`_


How to cite BioSamples?
-----------------------

Please cite:

Mélanie Courtot, Luca Cherubin, Adam Faulconbridge, Daniel Vaughan, Matthew Green, David Richardson, Peter Harrison, Patricia L Whetzel, Helen Parkinson, Tony Burdett; *BioSamples database: an updated sample metadata hub*, **Nucleic Acids Research**, Volume 47, Issue D1, 8 January 2019, Pages D1172–D1178, `https://doi.org/10.1093/nar/gky1061 <https://doi.org/10.1093/nar/gky1061>`_.

Courtot M, Gupta D, Liyanage I, Xu F, Burdett T. *BioSamples database: FAIRer samples metadata to accelerate research data management.* Nucleic Acids Res. 2022 Jan 7;50(D1):D1500-D1507. `doi: 10.1093/nar/gkab1046 <https://doi.org/10.1093/nar/gkab1046>`_. PMID: 34747489; PMCID: PMC8728232.

How frequent are updates to BioSamples' data?
---------------------------------------------

BioSamples content is updated daily. Information directly submitted or updated in a source should be reflected within 48 hours. Occasionally, daily updates may be missed due to unexpected circumstances.

What pattern do BioSamples accessions follow?
---------------------------------------------

BioSample accessions always begin with ``SAM``.
The next letter is either ``E`` (EMBL-EBI), ``N`` (NCBI), or ``D`` (DDBJ).
After that, there may be an ``A`` (Assay sample).
Finally there is a numeric component that may or may not be zero-padded.

Why are some BioSamples linked to RRIDs?
----------------------------------------

The Resource Identification (RRID) Initiative collaborates with BioSamples to identify pancreatic islets used by researchers in the `Integrated Islet Distribution Program (IIDP) <https://iidp.coh.org/>`_. BioSamples participates in a limited capacity so IIDP samples can be identified as RRIDs. See the `RRID website <https://rrid.site/>`_ for details.

What is the Bioschemas export?
------------------------------

Bioschemas is an extension of schema.org for consistently structured information on websites and services. The BioSamples team leads the Bioschemas samples specification and adds Bioschemas export (JSON-LD) to all sample pages—see an example `here <https://www.ebi.ac.uk/biosamples/samples/SAMEA1243676>`_.
BioSamples also embeds other Bioschemas entities in the HTML source—for example, the `DataCatalog entity <https://bioschemas.org/profiles/DataCatalog/0.3-RELEASE-2019_07_01>`_ and the `DataSet entity <https://bioschemas.org/profiles/Dataset/1.0-RELEASE>`_.

How can I stay informed about BioSamples?
-----------------------------------------

Subscribe to the low-traffic `announcement mailing list <https://listserver.ebi.ac.uk/mailman/listinfo/biosamples-announce>`_.

Why do some of my search results not contain my query?
------------------------------------------------------

Ontologies are used to refine queries. Your query may match a synonym or a more specific term (e.g. searching for "human" matches "Homo sapiens"). Direct matches are ranked higher in results.

How will my personal data be used?
----------------------------------

This website requires cookies and limited processing of personal data as outlined in the EMBL-EBI `Terms of Use <https://www.ebi.ac.uk/about/terms-of-use>`_.
If you submit information to BioSamples, it will be handled in accordance with the Terms of Use.

I think some of the data is wrong. Can you fix it?
--------------------------------------------------

Most data is submitted by third parties, often via other services, so BioSamples cannot always contact submitters for corrections or clarifications. BioSamples works to extract the highest quality information (e.g. mapping to ontologies and using ontology expansion for queries).

Where is the BioSamples source code?
------------------------------------

BioSamples is open source. The code is published on `GitHub <https://github.com/EBIBioSamples/biosamples-v4>`_ (see project organization there). Licensing information is available on the `licensing page <https://github.com/EBIBioSamples/biosamples-v4/blob/dev/LICENSE>`_. For issues building a local instance, please open a pull request or email ``biosamples@ebi.ac.uk``.

How do I send my SampleTab files to BioSamples?
-----------------------------------------------

SampleTab services were deprecated and retired on **1 July 2020**. Please use the `JSON API <https://www.ebi.ac.uk/biosamples/docs/references/api/submit>`_ to submit and update samples.

My sample doesn’t have a ``Submitted on`` date?
-----------------------------------------------

The ``Submitted on`` field was added in the November 2020 release. All samples submitted after **17 November 2020** include this information. Older samples may not have it; it will be added progressively via curation pipelines, or upon request (``biosamples@ebi.ac.uk``).

Why was the ``ID created on`` field removed?
--------------------------------------------

To avoid confusion, the UI field was removed. The value remains in the JSON as ``create`` for advanced users familiar with processing pipelines and documentation; it reflects when the sample accession was created (generated by BioSamples).
IDs can be created well in advance of collection or submission to support cross-archive data exchange and provenance. They may also be generated internally as placeholders pending user submission.


