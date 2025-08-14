How to Register Samples Interactively
=====================================

This guide details how to register samples interactively in BioSamples through an ordinary web browser without having to go through the technical challenges of using an API.
If you want to create a process for syncing samples programmatically, refer to the `BioSamples JSON API <programatically.html>`_.

Requirements
------------

You will need a WEBIN submission account to proceed with this route. Please refer to `'Registering a WEBIN Submission Account' <general-guide/registration.html`_ for more information.


Overview
--------

There are two BioSamples portals: one for test registrations and another for production (real) registrations. The test service allows you to trial the interface in a consequence-free manner.

- **Test service URL**: https://wwwdev.ebi.ac.uk/biosamples/submit
- **Production service URL**: https://www.ebi.ac.uk/biosamples/submit

We advise and encourage that you trial your registration using the BioSamples test service before using the production service.

Broadly, interactive sample registration involves completing a csv template spreadsheet with the necessary metadata, validating, and submitting the spreadsheet to the BioSamples online web browser.
In the next section we break this down into individual steps.


Metadata Standards
------------------

BioSamples uses `Sample Checklists <general-guide/metadata-model.html`_ to ensure that each sample is registered with at least a minimum amount of metadata. For more information, see the `BioSamples Metadata Model <general-guide/metadata-model.html>`_ page.
**Please note that registering a BioSample with an ENA checklist is a requirement for submitting data using this sample to ENA.**

See here for the collection of ENA GSC-based `Sample Checklists <https://www.ebi.ac.uk/ena/browser/checklists>`_.


Completing the template spreadsheet
-----------------------------------
The file format for uploading sample metadata to BioSamples is `ISA-Tab<https://isa-specs.readthedocs.io/en/latest/isatab.html>`_, a tab delimited file format (TSV).
Although ISA-Tab is specifically for Investigation, Study and Assay data, we have tried to use the sample table format specified in the ISA-Tab specification.

ISA-Tab requires columns to be in specific orders in order to be successfully validated and processed. See the table below.

.. list-table:: Table 1. TSV file columns (BioSamples drag’n’drop uploader)
   :header-rows: 1
   :widths: 22 46 16 16

   * - **Column**
     - **Description**
     - **Mandatory? (Column)**
     - **Mandatory? (Value)**
   * - ``Source Name``
     - Name/ID of investigation, study, assay, project, donor, or sample. Required by ISA-Tab; BioSamples ignores its value.
     - Mandatory
     - Optional
   * - ``Sample Name``
     - Unique name of the sample within the uploaded TSV.
     - Mandatory
     - Mandatory
   * - ``Release Date``
     - The public release date of the sample.
     - Mandatory
     - Mandatory
   * - ``Characteristics[<name>]``
     - Sample attributes. You may include multiple characteristics. **Each Characteristics column must be followed by matching ``Term Source REF`` and ``Term Accession Number`` columns.** ``Characteristics[Organism]`` is mandatory, and its value must be valid.
     - Optional (repeating); **``Characteristics[Organism]`` is Mandatory**
     - Optional; **for ``Characteristics[Organism]`` the value is Mandatory**
   * - ``Term Source REF``
     - Controlled vocabulary/ontology providing the term (e.g. NCBITAXON, BTO). Must follow each Characteristics column.
     - Mandatory
     - Optional
   * - ``Term Accession Number``
     - Accession/ID from the Term Source (e.g. ``NCBITaxon_9606`` for *Homo sapiens*).
     - Mandatory
     - Optional
   * - ``Comment[bsd_relationship:<relationship_type>]``
     - Relationship to another sample (by sample name if within the same file, or by accession if already in BioSamples).
     - Optional
     - Optional
   * - ``Comment[external DB REF]``
     - Reference to this sample in another database.
     - Optional
     - Optional
   * - ``Comment[submission_contact:name]``
     - Submitter’s name(s).
     - Optional
     - Optional
   * - ``Comment[submission_contact:email]``
     - Submitter’s email address.
     - Optional
     - Optional* (if providing contact info, the email is required)
   * - ``Comment[submission_contact:affiliation]``
     - Submitter’s affiliation.
     - Optional
     - Optional
   * - ``Comment[submission_contact:role]``
     - Submitter’s role.
     - Optional
     - Optional
   * - ``Comment[submission_contact:url]``
     - Submitter’s URL.
     - Optional
     - Optional
   * - ``Comment[publication:doi]``
     - Publication DOI.
     - Optional
     - Optional
   * - ``Comment[publication:pubmed_id]``
     - PubMed ID.
     - Optional
     - Optional
   * - ``Comment[submission_organization:email]``
     - Email address of the submitting organization.
     - Optional
     - Optional* (if providing organization info, the organization name is required)
   * - ``Comment[submission_organization:name]``
     - Name of the submitting organization.
     - Optional
     - Optional
   * - ``Comment[submission_organization:address]``
     - Address of the submitting organization.
     - Optional
     - Optional
   * - ``Comment[submission_organization:role]``
     - Role of the submitting organization.
     - Optional
     - Optional
   * - ``Comment[submission_organization:url]``
     - URL of the submitting organization.
     - Optional
     - Optional
   * - ``Sample Identifier``
     - Sample ID/accession. Optional for new submissions; **mandatory when updating existing samples**.
     - Optional (new) / Mandatory (updates)
     - Optional (new) / Mandatory (updates)

Example tsv template spreadsheets for interactive submission can be found here.


