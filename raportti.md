# Xyndril-kit: Agent Execution Report

## Summary of ohjeet.txt instructions

1. **Start from Key Files**: Always read `PROJECT_INTRO.md`, `agent-guidelines.md`, `tasks.json`, and `tasks.template.json` before handling any tasks.
2. **Task Handling**: Only process files listed in the task's `input_files` and `output_files`. Update task status from `todo` → `in_progress` → `done`. Skip `blocked` tasks. Repeat until all tasks are processed.
3. **File Handling Rules**: Do not modify files or directories not specified in the task. All changes must be documented in `CHANGELOG.md`. Never modify `README.md`, `PROJECT_INTRO.md`, or `agent-guidelines.md` unless instructed by a task.
4. **SonarLint Integration**: Automatically detect and fix issues flagged by SonarLint, such as unused imports or incorrect type definitions, before saving or committing code.
5. **Language Policy**: All code, variable names, error messages, logs, and comments must be in English. Communication with the user is in English unless the user explicitly requests otherwise (e.g., “puhu suomeksi”).
6. **Version Control**: Always perform `git pull` before edits, and commit & push after changes to keep both Windsurf and VS Code environments synchronized.
7. **Other Notes**: Files like `README-agent.txt`, `ohjeet.txt`, `raportti.md`, and `tasks.json` are in `.gitignore` and can be handled freely by the agent.

## Implementation Status
- The instructions in `ohjeet.txt` have been read and understood.
- No tasks have been executed yet; this report summarizes the operational guide.
- The agent will follow the above rules for all future actions in this project.

---

## Correction and Explanation

The previous version of this report was incomplete and did not follow the full instructions of `ohjeet.txt`. According to the guide, the agent should:
- Read `tasks.json` and find the first task with status `"todo"`.
- Analyze and execute that task using only the specified files.
- Update the task status and document all changes.

In the previous step, I only summarized the instructions and did not process any actual tasks. This was a mistake and not in line with the workflow described in `ohjeet.txt`.

**Next steps:**
- I will now proceed to read `tasks.json`, find the first `todo` task, and execute it according to the instructions.
- After executing the task, I will update this report to reflect the actions taken.

*This correction was added to comply with the project guidelines and to transparently document the mistake and the plan to fix it.*
