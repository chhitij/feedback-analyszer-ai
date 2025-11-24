# Dependency Management with pip-tools

This project uses `pip-tools` to manage dependencies with pinned versions.

## Files

- **`requirements.in`** - High-level dependencies (what you edit)
- **`requirements.txt`** - Pinned dependencies (auto-generated, don't edit manually)

## Workflow

### 1. Install pip-tools (one time)
```bash
pip install pip-tools
```

### 2. Edit requirements.in
Add or modify high-level dependencies in `requirements.in`:
```
crewai
streamlit
pandas
numpy<2.0  # with version constraints if needed
```

### 3. Compile to requirements.txt
```bash
pip-compile requirements.in
```

This generates `requirements.txt` with all dependencies pinned to specific versions.

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Update dependencies
To upgrade packages to latest compatible versions:
```bash
pip-compile --upgrade requirements.in
```

To upgrade a specific package:
```bash
pip-compile --upgrade-package crewai requirements.in
```

## Why pip-tools?

✅ **Reproducible builds** - Exact versions locked  
✅ **Easy updates** - Simple upgrade workflow  
✅ **Clear separation** - High-level vs pinned deps  
✅ **Dependency resolution** - Handles conflicts automatically  

## Current Dependencies

See `requirements.in` for the high-level dependencies we use.
