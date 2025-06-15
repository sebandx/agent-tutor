import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def run_code(code: str) -> dict:
    """
    Executes a given string of Racket code.
    Use this tool to run, test, or evaluate a student's Racket code.
    """
    logging.info("Attemping to run Racket code locally...")

    command = ["racket", "-e", code]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        logging.info("Local execution completed")

        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    
    except subprocess.TimeoutExpired:
        logging.warning("Racket code execution timed out.")
        return {"error": "Execution timed out. The code took to long to run."}
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": f"An unexpected error occured: {str(e)}"}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    good_code = "(+ 10 5)"
    print("\n Good Code")
    good_result = run_code(good_code)
    print(f"Result: {good_result}")

    bad_code = "(define x)"
    print("\n Bad Code")
    bad_result = run_code(bad_code)
    print(f"\n Result: {bad_result}")

    infinite_loop_code = "(let loop () (loop))"
    print("\n Infinite Loop")
    timeout_result = run_code(infinite_loop_code)
    print(f"\n Result: {timeout_result}")

