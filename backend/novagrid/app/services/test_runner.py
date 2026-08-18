import subprocess, time
from app.core.config import settings

def run_tests(working_directory: str = ".") -> dict:
    started = time.time()
    try:
        result = subprocess.run(settings.test_command, cwd=working_directory, shell=True, capture_output=True, text=True, timeout=settings.test_timeout_seconds)
        return {"passed":result.returncode == 0,"exit_code":result.returncode,"output":(result.stdout+"\n"+result.stderr)[-20000:],"duration_seconds":round(time.time()-started,2)}
    except subprocess.TimeoutExpired:
        return {"passed":False,"exit_code":-1,"output":"Test execution timed out.","duration_seconds":settings.test_timeout_seconds}
