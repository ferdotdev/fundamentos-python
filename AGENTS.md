# AGENTS

This repo is a collection of small Python scripts and lessons.
Most files are standalone examples executed directly with Python.
There is no build system or test runner configured.

## Repo overview
- Primary language: Python
- Structure: flat list of lesson scripts in repo root plus `Other/`
- Execution style: top-level script statements with print output
- Docs: minimal; only `README.md`
- Notebook: `7 - Variables en Python.ipynb` exists; avoid editing unless asked

## Commands
- Build: none (no build step configured)
- Lint: none (no formatter or linter configured)
- Tests: none (no pytest/unittest config found)
- Install deps: none required for standard library scripts
- If you add tooling, document it here

## Running a single test or script
- Run any example script: `python "15 - Operadores aritmeticos.py"`
- Run the only test-like file: `python test.py`
- Use `python3` if `python` is not available: `python3 test.py`
- There is no test discovery; each file is executed directly
- If you add tests, keep them runnable via `python <file>`

## Command examples
```bash
python "10 - Manipulacion y conversion de tipos.py"
python "Other/main.py"
python test.py
```

## Adding a new lesson script
- Follow the existing numeric prefix naming pattern
- Keep the filename readable, even with spaces
- Start with a short module docstring explaining the concept
- Use simple variables and print output
- Keep the lesson self contained (no imports unless required)
- Add Spanish comments if other lessons nearby use them

## Code style guidelines
- Keep scripts short and didactic; avoid heavy abstractions
- Use clear sequential examples; prints are part of the lesson
- Preserve existing comments and docstrings; keep explanations in place
- Prefer Spanish for new instructional text to match current content
- Avoid adding new dependencies unless the lesson requires them
- Avoid changing output text unless the lesson intent changes

## Imports
- Use standard library imports only unless the lesson requires otherwise
- Put all imports at the top of the file
- Prefer explicit imports: `import random` or `from datetime import datetime`
- Group imports in a single block; do not interleave with code
- Do not leave unused imports
- Keep import count minimal for learning focus

## Formatting
- Indent with 4 spaces
- Keep blank lines between logical sections
- Keep lines reasonably short (around 88-100 chars) when practical
- Use f-strings for formatted output
- Use single or double quotes consistently within a file
- Do not reformat existing examples unless necessary for the change
- Avoid trailing whitespace

## Docstrings and comments
- Many lessons start with a module docstring; keep it if present
- Use docstrings for lesson context, comments for inline explanations
- Keep comments short, clear, and aligned with the code they explain
- Avoid redundant comments that repeat the code
- If adding a new lesson, include a short module docstring
- Keep comment language consistent with the file
- Avoid large comment blocks that read like essays

## Naming
- Variables: `snake_case`, descriptive (e.g., `decimal_negativo`)
- Functions: `snake_case` verbs (e.g., `is_even`, `handle_command`)
- Constants: `UPPER_CASE` only if you introduce them
- Short names are OK for math examples (`a`, `b`, `x`, `y`)
- Avoid shadowing builtins (`sum`, `list`, `dict`) in new code
- Avoid single-letter names outside math examples
- Keep Spanish variable names consistent within a file

## Types
- Type hints are not used in the current code; avoid adding them by default
- If a lesson explicitly teaches typing, keep hints simple and minimal
- Use built-in types in comments or print output when needed
- Avoid introducing typing-only imports
- Prefer straightforward values over complex type tricks
- Do not add runtime type checking unless the lesson is about it

## Control flow and functions
- Keep control flow explicit (`if`/`elif`/`else` over clever expressions)
- Prefer simple loops that show the concept
- Functions are small and focused; keep them easy to read
- Avoid lambda-heavy or functional patterns unless teaching them
- When showing dictionaries of callables, keep keys simple strings
- Avoid deeply nested blocks unless the lesson requires it

## Error handling
- Only add try/except when the lesson needs it
- Catch specific exceptions (e.g., `ZeroDivisionError`)
- Explain errors with a short print message
- Avoid bare `except` and avoid swallowing errors silently
- `pass` is acceptable only when teaching control flow
- Do not introduce logging frameworks
- Do not use custom exception types unless teaching them

## Data and I/O
- Use in-memory examples; avoid file I/O unless required by lesson
- Use `print()` to show results and reinforce the concept
- Keep input prompts simple and explicit when used
- Do not add network calls or external services
- Keep randomness deterministic only if the lesson needs repeatability
- Avoid writing files during examples

## File organization
- Lessons live in the repo root and are named with numeric prefixes
- Additional examples live under `Other/`
- Keep new lesson files consistent with existing naming style
- Do not rename existing lesson files unless explicitly requested
- Keep related examples grouped in the same file when possible
- Avoid moving files between folders without a reason

## Editing guidance
- Make minimal changes needed to satisfy the request
- Do not refactor unrelated examples
- Preserve output semantics; changing print output is a breaking change
- Keep top-level code at module scope (no main guard unless requested)
- Do not reorder statements unless it improves the teaching flow
- Avoid introducing global state changes across files
- Keep edits in the smallest number of files possible

## Cursor and Copilot rules
- No `.cursor/rules/` directory found
- No `.cursorrules` file found
- No `.github/copilot-instructions.md` found

## When unsure
- Follow the existing teaching style in the nearest related file
- Prefer clarity over cleverness
- Ask only if a change would alter lesson intent or output
- If output changes, explain why in the PR or response

## Suggested workflow for agents
- Read the target script before editing
- Keep edits localized to the relevant example
- Run the edited script with `python <file>` to validate output
- If adding a new lesson, include a short module docstring
- Update `README.md` only if the user explicitly asks
- Summarize changes with file paths for quick review
- Mention any commands you ran and their result
