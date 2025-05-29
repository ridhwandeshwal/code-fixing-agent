import os
import re
def extract_code(llm_output: str) -> str:
    match = re.search(r"```(?:python)?\s*\n(.*?)```", llm_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    lines = llm_output.splitlines()
    code_lines = [line for line in lines if line.strip().startswith("def ") or line.startswith("    ")]
    return "\n".join(code_lines).strip()
def write_patch(program_name: str, code: str) -> str:
    extracted_code=extract_code(code)
    os.makedirs("tmp", exist_ok=True)
    temp_path = f"tmp/{program_name}_patched.py"
    with open(temp_path, "w") as f:
        f.write(extracted_code)
    return temp_path
