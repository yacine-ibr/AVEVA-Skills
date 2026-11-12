# AVEVA script review and validation worksheet

Use this for code reviews, script proposals and user acceptance tests.

## 1. Context and evidence
- [ ] Product: [System Platform / Application Server / OMI / Industrial Graphics / other]
- [ ] Exact version, service pack and patch: [to confirm]
- [ ] Script location and execution trigger: [to confirm]
- [ ] Official, version-matched documentation located: [direct URL and version]
- [ ] Whether the example was compiled/tested in the real AVEVA editor: [yes/no, environment]

## 2. Inputs and side effects
- [ ] All input attributes and types are known.
- [ ] Every written attribute is declared and permitted.
- [ ] No private site values, PLC addresses, credentials or IPs were invented or copied.
- [ ] Loss of communications, bad data quality and restart conditions are addressed.
- [ ] Time bases, write rates and scan/trigger behavior are understood.
- [ ] Commands, stop priority, permissives, interlocks and feedback are not confused.

## 3. Script validity
- [ ] Syntax checked against the proper Application Server or graphics manual.
- [ ] Imported functions and libraries are documented for the targeted version.
- [ ] No unsupported modern C#, Python, Jython or cross-product API was silently introduced.
- [ ] Comments and variable names reflect engineering intent.
- [ ] There is no uncontrolled cyclic write or repeated action.
- [ ] Security-sensitive writes and permissions follow vendor guidance.

## 4. Test and deployment gate
- [ ] Simulate normal and faulted conditions in an approved test environment.
- [ ] Validate stop/start arbitration and failure handling.
- [ ] Review logs, exceptions and performance impacts.
- [ ] Engineer, control-system owner and site authority approve changes.
- [ ] Backup, rollback and production change control are documented.

## 5. Response discipline

Distinguish **site-specific requirement**, **illustrative example**, **officially verified product behavior**, **engineering proposal** and **open question**.

A successful static review does **not** prove operational safety or AVEVA runtime compatibility.
