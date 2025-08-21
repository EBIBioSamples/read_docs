BioSamples — Release Notes
===========================

Last updated: 29 July 2025

Contents
--------
- v5.3.11 Release notes
- v5.3.10 Release notes
- v5.3.8 Release notes
- v5.3.7 Release notes
- v5.3.6 Release notes
- v5.2.20 Release notes
- v5.2.19 Release notes
- v5.2.18 Release notes
- What’s Changed
- v5.2.16 Release notes
- v5.2.15 Release notes
- v5.2.14 Release notes
- v5.2.13 Release notes
- v5.2.12 Release notes
- v5.2.11 Release notes
- v5.2.10 Release notes
- v5.2.9 Release notes
- v5.2.8 Release notes
- v5.2.7 Release notes
- v5.2.6 Release notes
- v5.2.5 Release notes
- v5.2.4 Release notes
- v5.2.3 Release notes
- v5.2.2 Release notes
- v5.2.1 Release notes (v5.1.15 & v5.2.0 included)
- v5.1.14 Release notes
- v5.1.13 Release notes
- v5.1.12 Release notes
- v5.1.11 Release notes
- v5.1.10 Release notes
- v5.1.6 Release notes (v5.1.5 included)
- v5.1.4 Release notes
- v5.1.3 Release notes
- v5.1.2 Release notes
- v5.1.1 Release notes (v5.1.0 included)
- v5.0.7 Release notes
- v5.0.6 Release notes
- v5.0.5 Release notes
- v5.0.4 Release notes
- v5.0.3 Release notes
- v5.0.2 Release notes
- v5.0.1 Release notes
- v5.0.0 Release notes
- v4.2.7 Release notes
- v4.2.6 Release notes
- v4.2.5 Release notes
- v4.2.3 Release notes
- v4.2.2 Release notes
- v4.2.1 Release notes
- v4.2.0 Release notes
- v4.1.15
- v4.1.14
- v4.1.13
- v4.1.12
- v4.1.11
- v4.1.10
- v4.1.9
- v4.1.8
- v4.1.7
- v4.1.6
- v4.1.5
- v4.1.4
- v4.1.3
- v4.1.2
- v4.1.1
- v4.1.0
- v4.0.7
- v4.0.6
- v4.0.5
- v4.0.4
- v4.0.3
- v4.0.2
- v4.0.1
- v4.0.0 Release notes

v5.3.11 Release notes
----------------------
- Fixed ASCII docs.
- Fixed file upload submissions: attributes no longer transformed to lower case.

v5.3.10 Release notes
----------------------
- JSON schema validation for ENA samples instead of XML checklist validation.

v5.3.8 Release notes
---------------------
- Deprecated AAP authentication in BioSamples.
- Bug fixes.

v5.3.7 Release notes
---------------------
- Added MICROBE logo to front page.
- Fixed NCBI and ENA sample mirroring.
- Added option to perform JSON schema validation on all WEBIN submissions.

v5.3.6 Release notes
---------------------
- Fixed documentation template issues.
- Fixed NCBI sample mirroring handling.

v5.2.20 Release notes
----------------------
- Introduced ERS accessioning in BioSamples.
- Upgraded to Java 17 and Spring Boot 2.5.

v5.2.19 Release notes
----------------------
- Fixed BioSamples client multithreading issue.

v5.2.18 Release notes
----------------------
*(No content specified.)*

What’s Changed
--------------
- Added public filter for INSDC status ≠ suppressed.
- CI/CD enhancements including sample post-release actions.
- Added Stackdriver monitoring and other CI/CD improvements.

v5.2.16 Release notes
----------------------
*(No content specified.)*

v5.2.15 Release notes
----------------------
*(No content specified.)*

v5.2.14 Release notes
----------------------
**Improvements**
1. Upgraded Elixir biovalidator for better performance and error handling.
2. Added EVA logo to external links for EVA sample mapping.

**Note**
- Holiday message: BioSamples team out of office 19 Dec 2022 – 02 Jan 2023; delays in Helpdesk responses expected.

v5.2.13 Release notes
----------------------
- Internal improvements and critical bug fixes.

v5.2.12 Release notes
----------------------
- Internal improvements only.

v5.2.11 Release notes
----------------------
- Internal improvements only.

v5.2.10 Release notes
----------------------
- Internal improvements only.

v5.2.9 Release notes
----------------------
- Internal improvements only.

v5.2.8 Release notes
---------------------
- Internal improvements only.

v5.2.7 Release notes
---------------------
*(No content specified.)*

v5.2.6 Release notes
---------------------
- Internal improvements only.

v5.2.5 Release notes
---------------------
**Bug Fixes**
1. Fixed issue of accession duplication.

v5.2.4 Release notes
---------------------
**New Features**
1. Added ability to bulk fetch multiple accessions.

v5.2.3 Release notes
---------------------
**Improvements**
1. Uploader now accepts case-insensitive column names.
2. Enhanced error reporting for submission failures.
3. Improved accessioning performance (e.g., ~9,985 accessions generated in ~81 seconds in a single call).

**New Features**
1. Referencing private BioSamples during ENA WEBIN submissions. Automatically makes those private samples public when related ENA runs are public.
2. Introduced generic structured data model (allow any structured data submission, e.g., AMR).

**Bug Fixes**
- Fixed filtered search inconsistencies mixing private and public samples.
- Resolved Solr out-of-memory issues.

**New Endpoints**
1. Structured data:
- `PUT structureddata/<accession>` to add structured data.
- `GET structureddata/<accession>` to fetch structured data.

v5.2.2 Release notes
---------------------
**Internal improvements**
1. Removed sample name uniqueness constraint for file uploader submissions.

v5.2.1 Release notes (v5.1.15 & v5.2.0 included)
------------------------------------------------
**Internal improvements**
- Improved uploader error messages.
- Allowed case-insensitive column names.
- Enhanced structured data handling.
- Speed improvements in accessioning and ENA import pipeline.
- Added pipeline to handle sample release when ENA runs/analyses refer to them.

v5.1.14 Release notes
----------------------
**Bug Fixes**
1. Fixed search indexing issue.

v5.1.13 Release notes
----------------------
**Internal improvements**
1. Updated release process, phased out SPOT infrastructure.

**Note**
- Holiday message: Out of office 20 Dec 2021 – 03 Jan 2022; delayed Helpdesk responses.

v5.1.12 Release notes
----------------------
**New Features**
1. Private sample search via WEBIN Authentication:
- GET single private sample.
- Filtered search for private-only or mixed sample lists.
- Example API usage with `authProvider=WEBIN` and JWT tokens.

2. Added support for publications, contacts, and organizations in drag-and-drop uploader.

3. Refactored structured data API to support generic data, with dedicated ownership of structured blocks.

**Bug Fixes**
- Fixed BioSamples API docs to include complete request/response examples.

**New V2 endpoints**
- Deployed improved submission and accession endpoints for bulk operations. GA planned for Dec 10, 2021 (99.5% target availability).

v5.1.11 Release notes
----------------------
**Bug Fixes**
- Fixed private sample GET via WEBIN authentication.

v5.1.10 Release notes
----------------------
**Bug Fixes**
- Fixed missing `curationdomain` parameter handling in HAL sample API responses when using “no-curations” flag.

v5.1.6 Release notes (v5.1.5 included)
--------------------------------------
**New Features**
- Improved file uploader: large submissions queued & tracked via submission ID with status: ACTIVE, COMPLETED, FAILED.

- Integrated JSON schema-store with dedicated checklist IDs (e.g., BSDC00001); ENA checklists imported with maintained IDs.

**Internal improvements**
- Enhanced submission API performance and improved pipeline resilience.

v5.1.4 Release notes
---------------------
**Bug Fixes**
- Fixed ENA import pipeline to preserve authority samples’ submitter ID linkage.

v5.1.3 Release notes
---------------------
**Bug Fixes**
- Resolved Elixir biovalidator response format errors by standardizing validator versions.

v5.1.2 Release notes
---------------------
**Internal improvements**
- General performance optimizations.

v5.1.1 Release notes (v5.1.0 included)
---------------------------------------
**New Features**
1. Integrated JSON Schema store: checklist management.
2. Released drag-and-drop uploader (supports Webin and AAP).
3. ENA taxonomy service validation on organism attribute.
4. BioSamples client updated to support Webin authentication.
5. Enhanced DUO code tooltips in UI.

**Bug Fixes**
- Fixed Phenopacket export errors on disease-related attributes.

v5.0.7 Release notes
---------------------
**Bug Fixes**
- Reintroduced `samples/validate` endpoint (deprecated but retained).
- Added support for `hal+json` Accept header.
- Enabled ENA pre-accessioning via WEBIN superuser.

v5.0.6 Release notes
---------------------
**New Features**
1. Introduced ENA WEBIN authentication (in addition to AAP).
2. Bulk download API for up to 100,000 samples (JSON, XML, accession list).
3. Validation checklist via submission body; improved validation and certification workflows.

**Bug Fixes**
- Fixed outdated ENA browser links (old → new URLs).

v5.0.5 Release notes
---------------------
**New Features**
- Private samples now searchable by authenticated owner via API with JWT.

**Bug Fixes**
- Updated documentation to remove deprecated AAP references and improve environment clarity.

v5.0.4 Release notes
---------------------
**New Features**
1. Added Plant-MIAPPE checklist support for certified submissions.
2. Removed holiday banner from site.

v5.0.3 Release notes
---------------------
**New Features**
1. Changed date representations: UI “ID created date” removed; added sample history dates (“Submitted on”, “Released on”, “Last reviewed”).
2. Changed host attribute naming in exports.

**Notifications**
- Holiday message added (21 Dec 2020 – 03 Jan 2021).

v5.0.2 Release notes
---------------------
**New Features**
- Refined date labels: "ID created on", "Submitted on", "Released on", "Updated on".

v5.0.1 Release notes
---------------------
**New Features**
1. Mandatory organism/species attribute enforced.
2. Introduced certification service based on JSON schema.
3. Extended structured data types (e.g., CHICKEN_DATA, HISTOLOGY_MARKERS).
4. Added sample recommendations endpoint for validation.
5. Enabled relationship curation; KILLED samples handling in ENA pipeline.
6. Enabled CORS for all origins; embedded AMR in XML view.

**Bug Fixes**
- Fixed EBI search export, NCBI organism-less sample issues, pipeline error handling, attribute export limits.

v5.0.0 Release notes
---------------------
*(Major architecture overhaul)*
- Retired SampleTab, legacy JSON/XM L APIs.
- Re-architecture using Spring Boot, MongoDB, Solr, AAP authentication, separate curation model, improved faceting, hypermedia API design, containerization, enhanced JSON/XML output formats.

v4.2.7 Release notes
---------------------
**New Features**
1. Sample groups API added in JSON API.
2. Experimental sample graph search via Neo4j.
3. Domain transition from SampleTab to AAP domain.
4. Relationship source validation added.
5. Clearinghouse curation import and improved “not collected/provided” handling.
6. Enhanced EBI Search export and external reference support.

**Bug Fixes**
1. Removed alt text from H1 causing indexing issues.
2. Added missing domain validation.
3. Improved retaining of “not provided/collected” attributes.
4. Enhanced NCBI exchange handling for missing SRA accessions.
5. Fixed private sample update failures via import.

v4.2.6 Release notes
---------------------
**New Features**
1. Optimized Solr weekend replication process.
2. Pipeline usage metrics stored in MongoDB.
3. AMR structured data support with retained access rights.
4. Improved listings of live, suppressed, killed samples.
5. Improved EBI search export.
6. ENA SRA accession updates via pipeline.
7. Added prominent COVID-19 query link on homepage.

**Bug Fixes**
- Handled blank attribute values and AMR import naming issues.

**Notifications**
- SampleTab removal slated 1 May; migration advised.

v4.2.5 Release notes
---------------------
**New Features**
1. Pipeline to remove duplicate BioSamples accessions.
2. Enhanced `/accessions` endpoint with pagination and wildcard search.
3. Added ontology annotations to AMR via Zooma.
4. UI improvements: broken links fixed; timestamp repositioning; faster facet load; maintenance notifications.
5. Standardized ENA attribute usage for external references.

**Notifications**
- SampleTab deprecated from May 2020; users advised to migrate.

**Bug Fixes**
- Fixed retention of attribute tags and pipeline failure alerts.

v4.2.3 Release notes
---------------------
**New Features**
1. AMR structured data with ENA-AMR import pipeline.
2. Case handling for core vs. user-provided attributes in JSON representations.

**Bug Fixes**
- Improved handling of blank values and tags in curami pipeline.

v4.2.2 Release notes
---------------------
**New Features**
1. Improved `/accessions` POST for pre-accessioning.
2. Enhanced filters, pagination in `/accessions` GET.
3. Introduced continuous RDF release pipeline.
4. Refined ENA/NCBI sample attribute tagging and retention logic.

**Bug Fixes**
- Fixed null date imports and upgraded to Java 11.

v4.2.1 Release notes
---------------------
**New Features**
1. Handled suppressed samples from ENA/NCBI.
2. Saved full contact details with configurable display.
3. Improved ENA integration: alias mapping, tag handling, attribute remapping, performance, create date retention.

**Bug Fixes**
- Fixed contact role display and curation-view pagination issues.

v4.2.0 Release notes
---------------------
- Deprecated SampleTab submission.
- Added static collections for samples/curations.
- Improved curation application ordering.
- Added links to sample accessions.

v4.1.15 Release notes
---------------------
- Updated Phenopacket version.
- Added `curami` pipeline for attribute curation.

v4.1.14 Release notes
---------------------
- Added DUO attribute support to external references.
- Script added for EGA data import.
- Added Presto connector in client.

v4.1.13 Release notes
---------------------
- Enabled JWT token support in client API.
- Fixed ENA pipeline failure on missing FIRST_PUBLIC.

v4.1.12 Release notes
---------------------
- ENA XML dump replication added.
- Annotated USI-submitted samples.
- Support for suppressed samples.
- JSON schema docs added.
- Improved retry logic and indexing validation.

v4.1.11 Release notes
---------------------
- Suppressed sample support for dbGaP import.
- Livelist flush fix.
- Added validation/accession service.
- Fixed SampleTab template link.

v4.1.10 Release notes
---------------------
- Removed holiday message.
- Fixed submission tab link in error pages.

v4.1.9 Release notes
---------------------
- Added “Curation Undo” pipeline.
- Fixed UI issues with long attributes.

v4.1.8 Release notes
---------------------
- Fixed curation pipeline issue removing characteristics.
- Added holiday message.

v4.1.7 Release notes
---------------------
- Added Graylog logging libraries.
- Switched to AAP explore environment and updated client URL.
- Included SampleTab template and cookbook entries.
- Removed name/API key lookup.

v4.1.6 Release notes
---------------------
- Added AMR structured data support.
- Relationship validation on submissions.
- Fixed Phenopacket export bug.
- Updated UI framework and improved documentation navigation.

v4.1.5 Release notes
---------------------
- Fixed search failure with colons.
- Added BioSamples cookbook.
- Fixed duplicate organism attributes.
- Improved UI error messaging for timeout.

v4.1.4 Release notes
---------------------
- Removed “not_applicable” attributes.
- Renamed date titles to "Releases on"/"Updated on".
- Added initial accession endpoint.
- Introduced multi-stage Docker build.
- Fixed Zooma pipeline bug.

v4.1.3 Release notes
---------------------
- Added top-level numeric taxId attribute.
- Fixed download export pop-ups.
- Enhanced search UI per ENA user feedback.

v4.1.2 Release notes
---------------------
- Added numeric taxId, improved IRI resolution, ETag header support, better private sample messaging, and clear-filter button.

v4.1.1 Release notes
---------------------
- Improved Bioschemas markup.
- Rewrote SampleTab pipeline.
- Linked sample name/accession in results.
- Fixed broken links in UI.

v4.1.0 Release notes
---------------------
**New Features**
- Added GDPR notices and enforcement.
- Strengthened SampleTab relationship validation.
- Embedded Bioschema.org entities (UI & API).

**Bug Fixes**
- Fixed header/link issues and SampleTab submission mapping.

v4.0.7 Release notes
---------------------
- Bug fixes: GDPR notices and updated Sitemap format.

v4.0.6 Release notes
---------------------
- Fixed UI search special character handling, curation links, JSON+LD profiles, and documentation links; added export and copy-down pipelines.

v4.0.5 Release notes
---------------------
- Improved search pagination, JSON+LD format, sample group handling, autocomplete links, indexing reliability; reduced Zooma/OLS load.

v4.0.4 Release notes
---------------------
- Preserved search/filter state, fixed legacy JSON/API endpoint behavior, improved titles, and added Elixir banner.

v4.0.3 Release notes
---------------------
- Redirected legacy group/sample URLs, fixed group XML handling, and deprecated reliance on malformed submissions.

v4.0.2 Release notes
---------------------
- Fixes for SampleTab JS, load-balanced accession handling, and relationship source logic.

v4.0.1 Release notes
---------------------
- Fixed submission for unaccessioned relationships, curation IRI formatting, CORS, and updated homepage links.

v4.0.0 Release notes
---------------------
- Major re-architecture: Spring-Boot, MongoDB, Solr, AAP, separate curation model, advanced faceting, hypermedia APIs, Docker support, enhanced data formats and serialization.

