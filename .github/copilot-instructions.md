# copilot-instructions for codefield

- Purpose: help AI code assistants produce changes consistent with repository patterns and conventions.

- Project layout: solutions are organized by week directories (e.g. `week1/`, `week2/`, `week6/`). Each file contains a standalone Python function (commonly named `solution`) that implements a small coding problem.

- File examples:
  - `week1/week1_1.py` — defines `def solution(n):` and returns an integer.
  - `week6/week6_1.py` — defines `def solution(A,B):` and returns an integer; uses in-place list sorting.

- Coding conventions & patterns to follow:
  - Keep changes minimal and focused: these are small exercise files. Avoid introducing project-level dependencies or heavy scaffolding.
  - Maintain the `solution` function signature and return type unless the user's request explicitly asks to change the API.
  - Prefer in-place operations when the original code uses them (e.g., `list.sort()`), unless immutability is specifically requested.
  - Print statements are occasionally present for quick local checks (see `week1/week1_2.py`) — preserve or remove only if asked.

- Tests / build / run:
  - There is no centralized test or build system in this repo. To run a file locally, run `python path/to/file.py`.
  - When adding tests, use standard `unittest` or `pytest`, and add them under a `tests/` directory.

- Commits & edits:
  - Make small, single-purpose commits. Each change should clearly reference which weekly exercise it updates.
  - When refactoring multiple files, explain why (e.g., unify naming conventions) in the commit message.

- Common pitfalls and how to fix them:
  - Avoid changing top-level script behavior (such as converting a module into a package) unless requested.
  - If modifying `solution` signatures, update any local ad-hoc invocations (e.g., `print(solution(...))`) in the same file.

- When to ask the user for clarification:
  - If a requested change would alter the public API (function name or signature) or expected return type.
  - If adding tests or CI, confirm preferred test runner and target Python versions.

- Useful quick examples to follow when editing:
  - Small bug fix preserving signature:
    - Input: `week6/week6_1.py` uses `B.sort(reverse = True)` — keep spacing and style consistent with surrounding files.
  - Adding a simple unit test:
    - Create `tests/test_week6_1.py` with one Happy Path assertion calling `solution([1,2],[3,4])`.

- Files to reference when making changes:
  - `README.md` — repo title only; no build instructions.
  - `week*/` — canonical examples of function signatures and small scripts.

If anything in this guidance is unclear or you'd like more detail (e.g., preferred test runner, Python version, or commit guidelines), tell me which area to expand and I will update this file.