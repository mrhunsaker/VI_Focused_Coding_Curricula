# Accessibility verification protocol and evidence register

Scope: Python Unit 11 Personal Data Manager (PYTHON/capstone/app.py) and its NiceGUI browser interface.

Status as of 2026-11-12: Automated Python page tests are included in .github/workflows/pull-request-validation.yml. They verify page-level interactions in NiceGUI's test harness. They are not a substitute for browser + assistive-technology testing. The project owner subsequently reported that every item in the manual audit checklist passed; see [ACCESSIBILITY_MANUAL_AUDIT_2026-11-12.md](ACCESSIBILITY_MANUAL_AUDIT_2026-11-12.md). The report records this user-reported outcome and its evidence limitations. It does not claim independent inspection of the completed workbook or infer unreported environment details.

## Automated evidence

| Evidence | Current result | What it establishes | What it does not establish |
|---|---|---|---|
| test_records.py | Run in Unit 11 capstone runtime workflow | Validation, CRUD, timestamps, search, JSON schema, malformed/missing file handling, storage failures | Browser semantics or assistive-technology behavior |
| test_app_ui.py | Run in PR validation workflow | Add, reject blank title, complete, delete, empty-state/status text | Real browser keyboard/focus behavior |
| test_app_v1_ui.py | Run in PR validation workflow | Add and search interactions | Real browser keyboard/focus behavior |
| test_hello_ui.py | Run in PR validation workflow | Initial page and greeting feedback | Real browser keyboard/focus behavior |
| Main-branch PR validation | Run 43208932201 — success at commit 08dda9a715a368bf549c8938db43311124d7286b | Repository validation, Python page tests, merge-marker scan, JSON checks, and mdBook build | Manual accessibility conformance |

## Manual test procedure

Perform these tests in a real supported browser with the named screen reader enabled. Record exact product versions and date. Use a fresh temporary data file for each run.

1. Keyboard-only operation
   - Reload the page and use Tab / Shift+Tab only.
   - Confirm every input, select, and button is reachable in a logical order.
   - Confirm focus is visible at every stop and never becomes trapped.
   - Operate add, search, select, update, complete, and delete without a pointer.
   - Confirm Enter/Space activation works as expected for each control.
2. Labels and control semantics
   - Navigate by form controls and confirm each field has a meaningful accessible name.
   - Confirm the record selector announces the selected record and its state.
   - Confirm headings and page title provide a useful document outline.
3. Dynamic status and errors
   - Submit a valid record and confirm the success message is announced once.
   - Submit a blank title/category and confirm the error is announced.
   - Search for a match and for no matches; confirm result changes are discoverable.
   - Complete and delete a record; confirm the resulting status is announced.
   - Load malformed JSON and confirm the load warning is announced without losing the ability to use the page.
4. Screen-reader browse/forms modes
   - Repeat the workflow using the screen reader's normal browse/reading mode and forms/focus mode.
   - Confirm labels, buttons, selected values, record details, empty states, and status changes are understandable without visual context.
5. Braille display (when in the supported test environment)
   - Confirm labels, current focus, selected option, status/error text, and record summaries are readable and not truncated in a misleading way.
   - Record display model, connection mode, and relevant screen-reader settings.

## Evidence record template

Create one completed record per tested environment. Do not mark a row Pass without the tester's observation.

| Field | Value |
|---|---|
| Date / tester | Pending |
| Commit SHA | Pending |
| OS and version | Pending |
| Browser and version | Pending |
| Screen reader and version | Pending |
| Screen reader settings / verbosity | Pending |
| Braille display and firmware (or N/A) | Pending |
| Keyboard-only checks | Not tested |
| Labels / semantics | Not tested |
| Dynamic status / errors | Not tested |
| Browse and forms modes | Not tested |
| Braille checks | Not tested / N/A |
| Defects and reproduction steps | Pending |
| Overall result | Not yet verified |

## Defect severity

- Blocker: a core action cannot be completed without a pointer, visual-only cue, or inaccessible custom control.
- Major: a core action is possible but its name, state, result, or error is not announced or discoverable.
- Moderate: navigation or feedback is unnecessarily difficult but a reliable workaround exists.
- Minor: wording or verbosity issue that does not block task completion.

A completed evidence record should be committed with the environment details and defect references. Re-test fixes on the same environment and, where possible, a second supported browser/screen-reader combination.


## Latest manual audit outcome

See [ACCESSIBILITY_MANUAL_AUDIT_2026-11-12.md](ACCESSIBILITY_MANUAL_AUDIT_2026-11-12.md) for the reported checklist result, audit baseline, and outstanding evidence metadata. The protocol remains available for future regression audits.
