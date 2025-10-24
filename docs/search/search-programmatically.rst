How to Search BioSamples Programmatically
=========================================

You can use BioSamples filters to restrict the search based on the sample characteristics. Filters are generally composed of a `type`, a `field`, and a `value` combined as `<type>:<field>:<value>`. If the `value` is omitted, the filter checks for the existence of the provided field. Filters work with both sample and accession search endpoints.

Type of Filter
--------------
Attribute
~~~~~~~~~

Filter based on sample attributes and their values.

.. list-table:: `attr` (Attribute) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `attr`
     - Fixed indicator
   * - `field`
     - Attribute name
     - Case-sensitive, URL-encoded
   * - `value`
     - Attribute value
     - Case-sensitive, URL-encoded

**Examples**

- filter=attr:Organism:Homo+Sapiens
- filter=attr:organism+part:liver

---

Date range
~~~~~~~~~~

Filter based on the sample's creation or release date over a time range.

.. list-table:: `dt` (Date range) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `dt`
     - Fixed indicator
   * - `field`
     - `release` or `update`
     - Case-sensitive
   * - `value`
     - `from=<date>until=<date>`
     - ISO 8601 format; timezone is UTC by default; both `from=` and `until=` are optional

**Examples**

- filter=dt:release:from=2014-01-01until=2015-01-01
- filter=dt:update:from=2018-01-01
- filter=dt:update:until=2016-12-31T20:30:00

---

Accession
~~~~~~~~~

Filter by BioSamples accession.

.. list-table:: `acc` (Accession) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `acc`
     - Fixed indicator
   * - `field`
     - `NA`
     - Pre-defined (not applicable)
   * - `value`
     - Sample accession
     - Supports wildcards

**Examples**

- `filter=acc:SAMEA341514
- `filter=acc:SAMN.* *(Only NCBI samples)*
- `filter=acc:SAMD.* *(Only DDBJ accessions)*

---

Relationship
~~~~~~~~~~~~

Filter based on a sample’s outgoing relationships.

.. list-table:: `rel` (Relationship) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `rel`
     - Fixed indicator
   * - `field`
     - Relation type (e.g., `derived from`, `child of`)
     - Case-sensitive, URL-encoded
   * - `value`
     - Relation target accession
     - Accession ID of related sample

**Examples**

- `filter=rel:child+of:SAME1596745`
- `filter=rel:derived+from:SAMEA7992418`

---

Reverse Relationship
~~~~~~~~~~~~~~~~~~~~

Filter based on incoming relationships (i.e., who points to this sample).

.. list-table:: `rrel` (Reverse Relationship) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `rrel`
     - Fixed
   * - `field`
     - Relation type
     - Case-sensitive, URL-encoded
   * - `value`
     - Relation target (sample accession)
     - Accession ID

**Examples**

- `filter=rrel:child+of`
- `filter=rrel:has+member:SAMEG316651`

---

Domain
~~~~~~

Filter samples based on their submission domain.

.. list-table:: `dom` (Domain) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `dom`
     - Fixed
   * - `field`
     - `NA`
     - Pre-defined
   * - `value`
     - Domain string (must start with `self.`)
     - Identifies submission domain

**Example**

- `filter=dom:self.70e89c7993c5cbdaea7cc9ceb710e7640d0840a60a1747fa8c9cfdcd94997d1b`

---

Name
~~~~

Filter by sample name.

.. list-table:: `name` (Name) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `name`
     - Fixed
   * - `field`
     - `NA`
     - Pre-defined
   * - `value`
     - Sample name (case-sensitive, URL-encoded)
     - Matches name field

**Examples**

- `filter=name:A5F`
- `filter=name:Generic+sample+from+Glycine+max`

---

External Reference Data
~~~~~~~~~~~~~~~~~~~~~~~
Filter samples that reference external archives.

.. list-table:: `extd` (External Reference Data) filter structure
   :header-rows: 1
   :widths: 15 30 40

   * - **Component**
     - **Value**
     - **Notes**
   * - `type`
     - `extd`
     - Fixed
   * - `field`
     - External reference name (e.g., `ENA`, `ArrayExpress`)
     - Archive identifier
   * - `value`
     - External data ID
     - ID within the external archive

**Examples**

- `filter=extd:ArrayExpress:E-MTAB-3732`
- `filter=extd:ENA:SRS359918`

---

Summary Table of Filter Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Summary of BioSamples filter types
   :header-rows: 1
   :widths: 20 30 50

   * - **Filter Type**
     - **Syntax**
     - **Description**
   * - Attribute
     - `attr:<field>:<value>`
     - Filters by attribute name and value.
   * - Date range
     - `dt:<release|update>:from=<date>until=<date>`
     - Filters by date range (ISO 8601, UTC).
   * - Accession
     - `acc:<accession>`
     - Filters by sample accession (supports wildcards).
   * - Relationship
     - `rel:<relation_type>:<accession>`
     - Filters based on outgoing relationships.
   * - Reverse Relationship
     - `rrel:<relation_type>:<accession>`
     - Filters based on incoming relationships.
   * - Domain
     - `dom:<domain>`
     - Filters by submission domain (must use `self.` prefix).
   * - Name
     - `name:<sample name>`
     - Filters by exact sample name.
   * - External Reference Data
     - `extd:<archive>:<external ID>`
     - Filters samples linked to external repositories.

