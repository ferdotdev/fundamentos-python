# AGENTS.md - Python Fundamentals Repository

## Project Overview
Educational Python repository with Jupyter notebooks and example scripts teaching Python fundamentals. Content and documentation in Spanish.

## Build/Test/Lint Commands

### No Formal Test Framework
This is an educational repository without formal test infrastructure.

### Running Code
```bash
# Run a Python script
python "22 - Listas.py"

# Run with the virtual environment
.venv/bin/python "22 - Listas.py"

# Run Jupyter notebook
jupyter notebook "10 - Manipulacion y conversion de tipos.ipynb"
```

### Manual Testing
- Execute scripts directly to verify output
- Use print statements for debugging (preferred in this codebase)
- Run notebooks cell by cell to validate examples

## Code Style Guidelines

### Language & Naming
- **Language**: Spanish for comments, docstrings, and variable names
- **Variable names**: snake_case (e.g., `tesla_models`, `lista_frutas`)
- **File names**: Descriptive with number prefixes for ordering (e.g., `22 - Listas.py`)
- **Constants**: UPPER_SNAKE_CASE for true constants

### Code Structure
- Use descriptive variable names in Spanish
- Single quotes for strings: `'hola'` (preferred over double quotes)
- No type hints (this is a fundamentals repo)
- No complex error handling (keep it beginner-friendly)
- Use docstrings with `"""` for module/file documentation

### Formatting
- Indentation: 4 spaces
- Maximum line length: ~100 characters (flexible)
- One blank line between logical sections
- No trailing spaces

### Imports
- Prefer no imports for basic examples
- When needed, use standard library only (no third-party deps)
- Group imports: stdlib first, then local (though rare in this repo)
- No wildcard imports (`from module import *`)

### Comments
- Use `#` for inline comments
- Explain the "why" not just the "what"
- Comments should be in Spanish
- Example:
  ```python
  # Para acceder a un elemento se utiliza el indice
  print(tesla_models[4])
  ```

### Documentation Style
- Module-level docstrings explain the concept being taught
- Use triple double quotes: `"""`
- Include brief explanations of Python concepts

## Error Handling
- Keep error handling minimal for educational clarity
- Use simple conditionals instead of try/except where possible
- Example:
  ```python
  if 'elemento' in mi_lista:
      print('Encontrado')
  ```

## Jupyter Notebooks
- Clear output before committing: Kernel > Restart & Clear Output
- Keep cells focused on single concepts
- Use markdown cells for explanations in Spanish

## Git Workflow
```bash
# Check what's excluded
cat .gitignore

# Current exclusions: .env, .venv/, node_modules/, *.log, *.tmp, .DS_Store, /Other, test.py, test.ipynb
```

## Virtual Environment
Located at `.venv/`. Use it when testing code:
```bash
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

## Key Patterns from Existing Code
- Lists: `mi_lista = ['a', 'b', 'c']`
- Tuples: `mi_tupla = ('a', 'b', 'c')`
- Sets: `mi_set = {'a', 'b', 'c'}`
- Dictionaries: `mi_dict = {'clave': 'valor'}`
- Loops: `for item in coleccion:`
- Conditionals: `if 'x' in lista:`

## When Adding New Content
1. Number prefix for ordering: `XX - Nombre Descriptivo.py`
2. Focus on one concept per file
3. Include practical examples
4. Use print statements to show output
5. Keep examples runnable independently
