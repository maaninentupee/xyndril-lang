## Documentation Update Checklist

Whenever a change is made to the parser, interpreter, or tests, ensure the following steps are completed to keep documentation in sync:

- [ ] **Parser Update**: If `parser/parser.py` or `parser/xyndril.g4` is modified, update `docs/parser_spec.md` to reflect the new logic.
- [ ] **Interpreter Update**: If `src/interpreter.py` is modified, update `docs/language-spec.md` to reflect the new semantics.
- [ ] **AST Update**: If `src/ast.py` is modified, update both `docs/parser_spec.md` and `docs/language-spec.md` to reflect the new node types or attributes.
- [ ] **Tests Update**: If new test cases are added to `test/parser/` or `test/interpreter/`, document any new behavior in `docs/language-spec.md`.
- [ ] **Validation**: Verify that all documented features match the implementation by running the unit tests (`python3 -m unittest discover test`).

## Test Results Reporting Template

Use the following template to report test results in `dev_report.md`. If tests fail, include the traceback or error details.

### Test Results – YYYY-MM-DD
- **Status**: [Success/Failure]
- **Details**: [Summary of the test run, e.g., "All 18 tests passed successfully" or "2 tests failed due to..."]
- **Command Used**: `python3 -m unittest discover test`
- **Output**:

 [Paste the test output here, including any errors or tracebacks]

- **Next Steps**: [Describe the next actions, e.g., "Fix failing tests" or "Proceed to task-008"]
