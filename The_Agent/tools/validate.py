import shutil
import subprocess

def validate_patch(program_name: str) -> str:
    original = f"../Code-Refactoring-QuixBugs/python_programs/{program_name}.py"
    patched = f"tmp/{program_name}_patched.py"
    backup = f"tmp/{program_name}_original_backup.py"
    test_file = f"../Code-Refactoring-QuixBugs/python_testcases/test_{program_name}.py"

    shutil.copyfile(original, backup)
    shutil.copyfile(patched, original)

    result = subprocess.run(["pytest", test_file], capture_output=True, text=True)
    shutil.move(backup, original)
    return "pass" if result.returncode == 0 else "fail"
