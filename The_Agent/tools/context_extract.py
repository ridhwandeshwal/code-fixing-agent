import subprocess
from pathlib import Path
from config import BUGGY_CODE_DIR

def read_buggy_code(program_name):
    path = Path(f"{BUGGY_CODE_DIR}/{program_name}.py")
    return path.read_text()

def run_test_and_capture_error(program_name):
    test_file = f"../Code-Refactoring-QuixBugs/python_testcases/test_{program_name}.py"
    result = subprocess.run([
        "pytest", test_file
    ], capture_output=True, text=True)
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    full_output = f"{stdout}\n{stderr}".strip()
    return stdout, full_output

def extract_context(program_name):
    buggy_code = read_buggy_code(program_name)
    stdout, stderr = run_test_and_capture_error(program_name)
    error_message = stderr if "Traceback" in stderr else stdout
    return buggy_code, error_message