import sys
import os
import subprocess
from dotenv import load_dotenv


def run_tests(env_filename: str, test_folder: str, test_file: str) -> int:
    """
    Function to run tests
    """

    # Load env file
    env_path = os.path.join(os.path.dirname(__file__), env_filename)
    load_dotenv(dotenv_path=env_path)

    # Build test path
    test_path = os.path.join(
        os.environ["VIRTUAL_ENV"],
        "Lib",
        "site-packages",
        "mbu_dev_shared_components",
        "tests",
        test_folder,
        f"{test_file}.py"
    )

    # Run tests
    return subprocess.call([
        "pytest",
        "-v",
        "--disable-warnings",
        test_path
    ])


if __name__ == "__main__":
    if "--go_tests" in sys.argv:
        exit_code = run_tests("go.env", "go_tests", "go_integration_tests")

    elif "--msoffice_tests" in sys.argv:
        exit_code = run_tests("msoffice.env", "msoffice_tests", "msoffice_integration_tests")

    else:
        print("No valid test flag provided. Use --go_tests or --msoffice_tests.")
        exit_code = 1

    print(f"exit_code: {exit_code}")
    sys.exit(exit_code)
