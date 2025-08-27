Step-by-Step Guide
=======================================================

Step 1: Select a Sample Checklist
---------------------------------
BioSamples uses Sample Checklists to ensure that each sample is registered with at least a minimum amount of metadata. For more information, see the `BioSamples Metadata Model <../metadata-model.html>`_ page.

.. note:: Please note that registering a BioSample with an ENA checklist is a requirement for submitting data using this sample to ENA.

Select a Sample Checklist from the `collection of ENA GSC-based Sample Checklists <https://www.ebi.ac.uk/ena/browser/checklists>`_ and make a note of the mandatory, recommended, and optional fields.


Step 2: Download a Template Spreadsheet
---------------------------------------
BioSamples provides a number of template spreadsheets corresponding to the most commonly used Sample Checklists. Please find the `tsv template spreadsheets here. <https://github.com/EBIBioSamples/read_docs/tree/main/docs/submit/templates>`_
If your selected Sample Checklist from Step 1 is not present, you will have to create your own template for your checklist.


Step 3: Complete the Template Spreadsheet
-----------------------------------------
The file format for uploading sample metadata to BioSamples is `ISA-Tab <https://isa-specs.readthedocs.io/en/latest/isatab.html>`_, a tab delimited file format (TSV).
Although ISA-Tab is specifically for Investigation, Study and Assay data, we have tried to use the sample table format specified in the ISA-Tab specification.

1. ISA-TAB requires columns to be in a specific order to be successfully validated and processed.
2. Every ``Characteristics`` you select as a column header in the TSV file must have ``Term Source Ref`` and ``Term Accession Number`` column headers following it. While filling up the data (rows) in the file, you may choose to provide blank values if you don’t have the information for it. In the below example, you can always opt to not provide the Term Source Ref and Term Accession Number but the column headers must be present as in the example below.
3. Be aware that if you are not specifying any values for Term Source Ref or Term Accession Number, the tab delimiter must still be provided. This allows for proper parsing of the files.
4. We expect all sample names to be unique in the file.

.. list-table:: Example Characteristic
   :header-rows: 1
   :widths: 23 23 23 9

   * - **Characteristics[Organism]**
     - **Term Source REF**
     - **Term Accession Number**
     - **unit**
   * - Marine metagenome
     - NCBITAXON
     - http://purl.obolibrary.org/obo/NCBITaxon_408172
     -

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
     - Sample attributes. You may include multiple characteristics. **Each Characteristics column must be followed by matching** ``Term Source REF`` and ``Term Accession Number`` columns. ``Characteristics[Organism]`` is mandatory, and its value must be valid.
     - Optional (repeating); ``Characteristics[Organism]`` is Mandatory
     - Optional; for ``Characteristics[Organism]`` the value is Mandatory
   * - ``Term Source REF``
     - Controlled vocabulary/ontology providing the term (e.g. NCBITAXON, BTO). Must follow each Characteristics column.
     - Mandatory
     - Optional
   * - ``Term Accession Number``
     - Accession/ID from the Term Source (e.g. ``NCBITaxon_9606`` for *Homo sapiens*).
     - Mandatory
     - Optional
   * - ``Comment[bsd_relationship:<relationship_type>]``
     - :ref:`Relationship to another sample <../metadata-model:Sample Relationships>`_ (by sample name if within the same file, or by accession if already in BioSamples).
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



Step 4: Submit the Completed Spreadsheet
-----------------------------------------

1. After completing the template spreadsheet with the appropriate metadata, login to BioSamples at the `drag'n'drop interface <https://www.ebi.ac.uk/biosamples/uploadLogin>`_ with your Webin credentials. See `Registering a WEBIN Submission Account <..\general-guide\registration.html>`_ for more details.
2. Select the appropriate checklist for validation from the dropdown list, and then upload your completed spreadsheet.
3. The uploader sends back a file for download with the submission result, in case of same time uploads where the file size is less than 20 KBytes and the file has less than 200 samples, the result file will have the sample metadata and the accessions. In case of queued uploads where the file size is greater than 20 KBytes or the file has more than 200 samples the result file will have a unique submission ID for the upload. The unique submission ID can be used to get the result of the upload using the View Submissions tab.
4. If you are looking to update existing samples that have been uploaded, you can use the file returned to you after your submission. Please remember to remove the receipt section.