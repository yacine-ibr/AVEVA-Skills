# Official sources and evidence policy

**Purpose:** a checklist of where to verify AVEVA-specific statements. These links are entry points, not automatically verified answers for all versions. Reviewed for the repository on 2026-11-13.

## Prioritize by evidence

1. **Official product/version guide** on [AVEVA Documentation](https://docs.aveva.com/). Find the relevant Application Server scripting guide, System Platform release notes, administration/installation guide, API reference or compatibility matrix. Record **product, release, service pack, patch and publication date**.
2. **AVEVA official support and product advisories**, when a document is not public: [AVEVA Knowledge and Support](https://softwaresupport.aveva.com/).
3. [AVEVA Community](https://community.aveva.com/) for troubleshooting **only as supplemental experience**, not as equivalent to a supported vendor guarantee.
4. **Official component-vendor guides** for Windows/SQL/certificates/OPC UA where relevant. Check actual deployed versions and vendor ownership.

## A concrete verified distinction

The official [Application Server SignedWrite documentation](https://docs.aveva.com/bundle/sp-appserver/page/18792.html) for **Application Server 2023 R2 SP1 P04** distinguishes client/Industrial Graphics scripts from Application Object scripts for `SignedWrite()`. Do not apply a function or sample to another execution surface merely because both are branded System Platform.

## Always check before asserting

- **Script environment:** Application Server object script or Industrial Graphic / OMI action?
- **Product:** AVEVA System Platform versus InTouch HMI standalone, Plant SCADA or MES.
- **Version and patch:** syntax and behavior may change; this skill targets the 2023 family as a reference scope, not a global compatibility guarantee.
- **.NET terminology:** installation prerequisites, supported imported libraries and QuickScript syntax are distinct. Older third-party notes about CLR compatibility must **not** be treated as current compatibility matrices without matching the official product manual.
- **Support:** note whether the official documentation is accessible, requires a customer login or cannot be checked.

## Record evidence in responses

| Claim | Product / version | Official document and URL | Checked on | Status |
|---|---|---|---|---|
| [statement] | [version] | [direct source] | [date] | Verified / Not verified / Conflicting |

If the official documentation is missing or unavailable, write **"Official vendor verification not performed"**, give the suspected information only as an **unverified hypothesis**, and ask for a version-matched manual where necessary.

Never cite old placeholder markers such as `turn988841search6` from an AI session. They are **not reusable references**.
