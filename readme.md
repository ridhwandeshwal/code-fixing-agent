# Code Fixing Agent

An autonomous agent that fixes buggy Python code using LLMs by calling modular tools for understanding, patching, and validating source code until it passes all test cases.

## Key Features

- **Autonomous Tool Use**: Uses tools like `extract_context`, `generate_fix`, `extract_code`, `write_patch`, and `validate_patch` via LLM-generated tool calls.
- **Error-Driven Fixing**: Generates new code based on actual test errors.
- **Retries on Failures**: Automatically retries generation with error context if a patch fails.
- **Seamless Integration**: Built on top of the QuixBugs dataset for consistent bug benchmarks.

## Tools

| Tool Name        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `extract_context` | Given a program name, returns the original code and the full test error log |
| `generate_fix`   | Uses the LLM to propose a code fix based on the buggy code and error context |
| `extract_code`   | Extracts only the code block from the LLM's full textual response            |
| `write_patch`    | Writes the fixed code to a temporary file for testing                        |
| `validate_patch` | Runs test cases using `pytest` to check if the patched code is correct       |

These tools are invoked dynamically by the LLM itself based on its reasoning at each step.

## Folder Structure
```
code-fixing-agent/
├── README.md
├── The_Agent/
│ ├── main.py
│ ├──tmp/
│ ├── tools/
│ │ ├── context_extract.py
│ │ ├── generate_fix.py
│ │ ├── extract_code.py
│ │ ├── write_temp.py
│ │ └── validate.py
│ └── config.py
├── Code-Refactoring-QuixBugs/
│ ├── python_programs/
│ ├── python_testcases/
```


## Workflow

1. Extract program code and test errors.
2. Generate a code fix using LLM with context and error.
3. Extract Python code block from LLM output.
4. Write patch to a temporary file.
5. Validate it with pytest.
6. If validation fails, retry with error messages included.

## Dataset Reference

This project uses the [QuixBugs](https://github.com/RumbleJack56/Code-Refactoring-QuixBugs) dataset, a benchmark of buggy Python programs and their corresponding test cases. Each program:

- Is located under `Code-Refactoring-QuixBugs/python_programs/`
- Has a matching test suite in `python_testcases/`
- Provides reproducible bugs ranging from logic errors to incorrect conditionals
- Makes it easier to measure patch effectiveness and LLM performance

---

## Example Output

Here’s an example of how the tool-driven pipeline operates on a failing program like `hanoi`:

TOOL_CALL: extract_context(program_name='hanoi')
extract_context returned: <program code + docstring>

TOOL_CALL: generate_fix(code, error)
generate_fix returned: <new version of code>

TOOL_CALL: extract_code(llm_output)
extract_code returned: <python function>

TOOL_CALL: write_patch(program_name='hanoi', code='...')
write_patch returned: tmp/hanoi_patched.py

TOOL_CALL: validate_patch(program_name='hanoi')
validate_patch returned: pass

Patch validated successfully! Exiting loop.