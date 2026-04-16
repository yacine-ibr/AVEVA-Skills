# AVEVA System Platform Developer Skill

A practical GitHub-ready guide for writing, reviewing, and generating **AVEVA System Platform 2023 / 2023 R2 / 2023 R2 SP1** code and configuration with a strong focus on **Application Server scripting**, **QuickScript .NET**, **Industrial Graphics**, **OMI**, and **template-based engineering**.

> This repository is designed as a "skill" or operating guide for engineers and AI assistants that must produce **valid, maintainable, production-oriented AVEVA System Platform content**.

---

## 1) What this skill is for

Use this skill when you need help with:

- **Application Server** object scripting
- **QuickScript .NET** syntax and patterns
- attribute-driven logic in templates and instances
- script reviews and refactoring
- OMI / System Platform engineering conventions
- Industrial Graphics integration with object models
- maintainable object templates, alarms, states, commands, and navigation logic
- code examples that must look like real **AVEVA System Platform** code rather than generic pseudo-code or Python/C#

This skill is **not** for:

- Ignition Jython
- generic Python 3 code
- full .NET modern C# features inside AppServer scripts
- Vision/Perspective concepts from Ignition
- AVEVA Plant SCADA Cicode unless explicitly requested

---

## 2) Target platform and version rules

### Primary target
- **AVEVA System Platform 2023 family**
- Prefer compatibility with **System Platform 2023 R2 SP1** when writing examples

### Scripting language to use
For **Application Server / object scripts**, the language is:
- **QuickScript .NET**

AVEVA documentation explicitly states that scripts in Application Server are written using **QuickScript .NET**, and the Application Server Scripting Guide covers the language, syntax, commands, and .NET usage. AVEVA also documents sample Application Server scripts specifically as **QuickScript .NET** scripts. citeturn988841search6turn988841search13turn988841search0

### Critical compatibility note
Do **not** treat AppServer scripting like modern C#.

AVEVA documents that QuickScript supports imported libraries built with **.NET CLR version 2.0.50727**, but **does not support newer language features** introduced later. At the same time, **System Platform 2023 requires .NET Framework 4.8** for installation/runtime prerequisites. These are different layers:

- **Platform prerequisite**: .NET Framework **4.8**
- **Script compatibility model**: QuickScript .NET behavior aligned with older **CLR 2.0.50727** constraints

That means your scripts must be written in a **conservative QuickScript .NET style**, not in a modern C# style. citeturn546390search0turn546390search8turn546390search1

### Practical conclusion
For **SP 2023**, the correct answer to “which version should I use?” is:

- Use **QuickScript .NET** for Application Server scripting
- Write code in a style compatible with the **older QuickScript/.NET CLR 2.0.50727 scripting model**
- Do **not** assume support for recent C#/.NET language features just because the platform installs on **.NET Framework 4.8** citeturn546390search0turn546390search8

---

## 3) Core coding principles

When generating or reviewing AVEVA System Platform code, always follow these rules.

### 3.1 Write for templates first
Prefer script logic at the **template level** whenever the behavior is generic and reusable. AVEVA recommends template-level scripting for reusable object behavior. citeturn988841search6

### 3.2 Keep scripts deterministic
Scripts should:
- read clear input attributes
- evaluate conditions explicitly
- write to output/status attributes deliberately
- avoid hidden side effects
- avoid complex multi-purpose scripts when smaller scripts are clearer

### 3.3 Prefer attributes over hard-coded constants
Model behavior through attributes such as:
- `CmdStart`
- `CmdStop`
- `PermissiveOK`
- `State`
- `Mode`
- `Faulted`
- `InterlockActive`
- `RuntimeSec`
- `AlarmInhibit`

### 3.4 Separate state evaluation from command handling
Do not mix all logic into one monolithic script when avoidable.
A maintainable pattern is:
- command input script
- permissive/interlock evaluation script
- state derivation script
- alarm/status propagation script

### 3.5 Be explicit about execution mode
AVEVA documents that Application Server scripts run in **two execution modes**. Always specify or document whether the script is intended to be:
- **On True / condition-based**
- **While True / periodic or continuously active logic**

Use the least aggressive mode needed. citeturn988841search8

### 3.6 Respect attribute and script best practices
AVEVA documents specific best-practice guidance for **attributes and scripting**. Follow an attribute-centered design and avoid unnecessary write churn. citeturn988841search9

---

## 4) QuickScript .NET syntax baseline

The following style is the baseline syntax this skill should generate.

## Variable declaration
QuickScript .NET variables must be declared before use. AVEVA documents variable declaration rules for QuickScript .NET. citeturn988841search12

```qsnet
Dim i as Integer;
Dim speed as Float;
Dim isReady as Boolean;
Dim msg as String;
```

## Assignment
```qsnet
speed = Me.SpeedSP;
isReady = Me.PermissiveOK;
msg = "Pump ready";
```

## If / ElseIf / Else
```qsnet
If Me.PermissiveOK == True Then
    Me.Ready = True;
ElseIf Me.InterlockActive == True Then
    Me.Ready = False;
    Me.StatusText = "Interlock active";
Else
    Me.Ready = False;
EndIf;
```

## For loop
```qsnet
Dim i as Integer;

For i = 1 To 10;
    Me.Counter = i;
Next;
```

## While loop
```qsnet
Dim retryCount as Integer;
retryCount = 0;

While retryCount < 3;
    retryCount = retryCount + 1;
EndWhile;
```

## Logical operators
```qsnet
If Me.AutoMode == True AND Me.PermissiveOK == True Then
    Me.ReadyToRun = True;
EndIf;
```

## Comparison operators
```qsnet
If Me.ProcessValue >= Me.HighLimit Then
    Me.HighAlarm = True;
EndIf;
```

AVEVA provides QuickScript .NET references for functions, variables, operators, and control structures in the Application Server scripting reference. citeturn988841search1turn988841search15turn988841search12

---

## 5) Exact coding style to enforce

This section is the most important part of the skill. Any generated code should follow these rules.

### Always do
- Declare local variables explicitly with `Dim`
- Use **simple, readable control flow**
- Use `Me.AttributeName` for object attributes
- Terminate statements consistently with semicolons in examples
- Keep one script focused on one responsibility
- Use descriptive attribute names
- Use status text attributes for diagnostics when useful
- Prefer template-driven reuse over copied instance logic
- Comment only where the intent is not obvious

### Never do
- Do not generate **Python**, **Jython**, or pseudo-code when the request is for AppServer scripts
- Do not generate modern **C# syntax sugar** or assume full modern .NET support
- Do not invent unsupported namespaces or libraries
- Do not hide object writes inside overly complex nested logic
- Do not hard-code galaxy paths or object names unless the request explicitly needs them
- Do not write giant scripts when a template + attributes design is cleaner
- Do not assume OMI UI scripts and AppServer object scripts are interchangeable

### Preferred comment style
```qsnet
' Evaluate permissives before accepting a start command.
```

### Preferred naming conventions
Use engineering-style names, for example:
- `CmdStart`
- `CmdStop`
- `StsRunning`
- `StsStopped`
- `StsFaulted`
- `PermissiveOK`
- `InterlockActive`
- `MotorFeedback`
- `RunRequest`
- `AlarmHH`
- `AlarmH`
- `AlarmL`
- `AlarmLL`

---

## 6) Canonical script patterns

## 6.1 Command acceptance pattern
```qsnet
Dim canStart as Boolean;
canStart = False;

If Me.AutoMode == True AND Me.PermissiveOK == True AND Me.InterlockActive == False Then
    canStart = True;
EndIf;

If Me.CmdStart == True Then
    If canStart == True Then
        Me.RunRequest = True;
        Me.StatusText = "Start accepted";
    Else
        Me.RunRequest = False;
        Me.StatusText = "Start rejected: permissive/interlock condition not met";
    EndIf;
EndIf;
```

## 6.2 Start/stop arbitration
```qsnet
If Me.CmdStop == True Then
    Me.RunRequest = False;
    Me.StatusText = "Stop command accepted";
ElseIf Me.CmdStart == True AND Me.PermissiveOK == True AND Me.InterlockActive == False Then
    Me.RunRequest = True;
    Me.StatusText = "Start command accepted";
EndIf;
```

## 6.3 State derivation from feedback
```qsnet
If Me.Faulted == True Then
    Me.State = 3;
    Me.StateText = "Faulted";
ElseIf Me.MotorFeedback == True Then
    Me.State = 2;
    Me.StateText = "Running";
Else
    Me.State = 1;
    Me.StateText = "Stopped";
EndIf;
```

## 6.4 Analog alarm evaluation
```qsnet
If Me.PV >= Me.HHLimit Then
    Me.AlarmHH = True;
    Me.AlarmH = False;
ElseIf Me.PV >= Me.HLimit Then
    Me.AlarmHH = False;
    Me.AlarmH = True;
Else
    Me.AlarmHH = False;
    Me.AlarmH = False;
EndIf;
```

## 6.5 Runtime accumulation trigger
```qsnet
If Me.StsRunning == True Then
    Me.RuntimeEnable = True;
Else
    Me.RuntimeEnable = False;
EndIf;
```

## 6.6 One-shot reset pattern
```qsnet
If Me.CmdReset == True Then
    Me.FaultAck = True;
    Me.CmdReset = False;
EndIf;
```

---

## 7) Architecture guidance for System Platform

### Object model first
Model the process in templates and instances instead of pushing logic into graphics.

### Graphics should visualize, not own process logic
Industrial Graphics and OMI should primarily:
- display object state
- expose commands
- navigate between contexts
- present alarms, trends, and diagnostics

Core process behavior should remain in the object model where possible.

### Reuse through templates
A good template should package:
- attributes
- scripts
- alarms
- symbol references
- naming conventions
- state model

### Avoid script duplication across instances
If multiple objects need the same logic, fix the template.

### Be careful with write frequency
Repeated writes in continuously executing scripts can create unnecessary load and noisy behavior.

---

## 8) OMI / Industrial Graphics guidance

When the request touches OMI or graphics:

- treat OMI as the **presentation layer**
- bind symbols to object attributes cleanly
- keep navigation/context logic explicit
- avoid embedding business logic in too many disconnected graphic actions
- maintain consistent states, colors, text, and command exposure across reusable symbols

For OMI-centric projects, standardize:
- state color mapping
- alarm indicators
- command button visibility/enabling
- faceplate layout rules
- navigation path conventions
- diagnostic text and operator feedback

---

## 9) What to say when asked “which language is used in AVEVA System Platform?”

Use this exact answer:

> In **AVEVA System Platform 2023**, Application Server object scripts are written in **QuickScript .NET**. Even though the platform requires **.NET Framework 4.8** as a prerequisite, QuickScript .NET scripting remains constrained by an older compatibility model and supports imported libraries built with **.NET CLR 2.0.50727**. So code should be written in a conservative **QuickScript .NET** style, not as modern C#. 

This is grounded in AVEVA documentation covering Application Server scripting, sample QuickScript .NET scripts, QuickScript function support, and System Platform 2023 .NET prerequisites. citeturn988841search0turn988841search13turn546390search0turn546390search8

---

## 10) Prompting rules for AI assistants

If this repository is used as an AI skill, the assistant should follow these rules.

### When generating scripts
- Output **QuickScript .NET**, not Python or generic pseudo-code
- Prefer template-level examples unless the user asks for instance-specific logic
- Use conservative syntax and straightforward control structures
- Explain execution assumptions: trigger condition, target object, and written attributes

### When reviewing scripts
Check for:
- unsupported modern syntax
- missing variable declarations
- uncontrolled write loops
- poor separation between command/state logic
- duplicated template logic at instance level
- unclear or dangerous attribute writes
- hidden coupling to object names or galaxy structure

### When transforming user logic into AppServer code
Always convert user intent into:
1. input attributes
2. evaluation conditions
3. output/status attributes
4. script trigger mode
5. expected runtime behavior

---

## 11) Bad vs good examples

## Bad
```text
Use Python code to poll tags every 100 ms and update the UI directly.
```

Why bad:
- wrong language
- wrong abstraction level
- too UI-centric
- not aligned with AppServer object scripting

## Better
```text
Create a QuickScript .NET template-level script for a motor object.
The script shall accept CmdStart only when AutoMode is true, PermissiveOK is true, and InterlockActive is false.
If accepted, set RunRequest to true and write StatusText = "Start accepted".
If rejected, keep RunRequest false and write a rejection reason to StatusText.
```

---

## 12) Recommended repository structure

```text
aveva-system-platform-skill/
├── README.md
├── examples/
│   ├── motor-start-stop.qsnet
│   ├── alarm-evaluation.qsnet
│   └── state-derivation.qsnet
└── prompts/
    └── assistant-system-prompt.md
```

---

## 13) References

This repository is based on AVEVA documentation indicating that:

- Application Server scripting uses **QuickScript .NET** and AVEVA provides a dedicated scripting guide and examples. citeturn988841search13turn988841search0turn988841search1
- Template-level scripting is the preferred reusable engineering model. citeturn988841search6
- Script execution modes and attribute/scripting best practices are documented by AVEVA. citeturn988841search8turn988841search9
- QuickScript supports imported libraries built with **.NET CLR 2.0.50727** but does not support newer language features. citeturn546390search0
- System Platform 2023 requires **.NET Framework 4.8** as a product prerequisite. citeturn546390search8turn546390search1

---

## 14) Final operating rule

When in doubt, generate the **simplest valid QuickScript .NET** that clearly expresses the process logic, is reusable at the **template level**, and fits **AVEVA System Platform 2023** constraints.
