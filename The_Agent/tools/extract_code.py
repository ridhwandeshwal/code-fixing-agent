import re

def extract_code(llm_output: str) -> str:
    match = re.search(r"```(?:python)?\s*\n(.*?)```", llm_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    lines = llm_output.splitlines()
    code_lines = [line for line in lines if line.strip().startswith("def ") or line.startswith("    ")]
    return "\n".join(code_lines).strip()