# Illustrative QuickScript .NET snippets

The `.qsnet` files in this folder are **examples written for explanation and discussion**. They have **not been compiled, exercised in an AVEVA editor or validated against live equipment in this repository**.

| File | Illustrates | Requires project-specific review |
|---|---|---|
| `motor-start-stop.qsnet` | Command arbitration | Stop priority, interlocks, permissives, output attributes, trigger |
| `alarm-evaluation.qsnet` | Analog threshold pattern | Alarm acknowledgement, hysteresis, deadbands, latching, quality |
| `state-derivation.qsnet` | State mapping | State enumeration, transitions, sensor quality and safety |

Never treat any values, command paths, attributes, behavior or syntax in these files as a production-ready recipe. Confirm the AVEVA product/version and the script surface with the [official-source guide](../references/official-sources.md), then test in an authorized environment.

Do not copy these examples into another customer's system without its requirements and engineering validation.
