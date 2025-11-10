Bulk-submit
===========
How to programmatically submit samples in bulk
----------------------------------------------

The bulk-submit/get-receipt capability allows submitters to send multiple sample metadata records together
(in one bulk operation) and then retrieve a “receipt” that reports the outcome (success/failure) and any
assigned accessions.
In the context of BioSamples this supports high-volume submissions rather than individual sample POSTs.


Important details & caveats (especially for microbiome/metagenome use)
----------------------------------------------------------------------

- **Validation & checklists:** For bulk uploads via files, you’re asked to select a “checklist” for validation (e.g., biosamples-minimal). The system checks required fields such as Characteristics[Organism].

- **Chunking and submission size:** The bulk route may impose limits (e.g., number of samples per submission, file size). In the cookbook: >200 samples or >20 kB often triggers queue rather than instant processing.

- **Queued vs immediate:** For queued submissions you don’t immediately get the accessions; you receive a submission ID and later you get the mapping. This means your pipeline must poll/wait for completion.

- **Relationships between samples:** If your microbiome context involves derivation (e.g., same donor, multiple timepoints, replicates, derived_from relationships), you may need to include relationship attributes (e.g., derived_from, same_as). The API reference shows sample metadata supports relationships.

- **Release date / privacy:** In the sample metadata you must specify a release date. If you need samples to remain private until associated data (e.g., sequence reads) are published, pick appropriate dates.

- **Receipt format:** The receipt is the key item: it shows the mapping from your internal sample names to the assigned BioSamples accessions, and whether each sample succeeded or failed. Keep this mapping because you’ll need to refer to those accessions when linking to datasets.

- **Error handling:** If you receive “COMPLETED WITH ERRORS” or “FAILED”, you should parse the error messages in the receipt (or returned file) to find which samples failed and why (e.g., missing required field, invalid organism, invalid date). Then resubmit only the failed samples if needed.

- **Metadata consistency for search/discovery:** The bulk-submit receipt only ensures technical submission succeeds; you should still review your metadata for FAIR discoverability.
