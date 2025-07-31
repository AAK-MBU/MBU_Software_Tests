import sys
import os
import asyncio

import subprocess

from dotenv import load_dotenv

from automation_server_client import AutomationServer


async def run_go_tests():
    # Load .env file
    env_path = os.path.join(os.path.dirname(__file__), "go.env")
    load_dotenv(dotenv_path=env_path)

    print()
    print("Running tests using:")
    print(" - GO_API_ENDPOINT:", os.getenv("GO_API_ENDPOINT"))
    print(" - TEST_PERSON_FULL_NAME:", os.getenv("DADJ_FULL_NAME"))
    print()

    # Construct full path to installed test file
    shared_test_path = os.path.join(
        os.environ["VIRTUAL_ENV"],
        "Lib",
        "site-packages",
        "mbu_dev_shared_components",
        "tests",
        "go_tests",
        "go_integration_tests.py"
    )

    # Run the test file using full path
    exit_code = subprocess.call([
        "pytest",
        "-v",
        "--disable-warnings",
        shared_test_path
    ])

    sys.exit(exit_code)


# async def run_msoffice_tests():
#     # Load .env file
#     env_path = os.path.join(os.path.dirname(__file__), "msoffice.env")
#     load_dotenv(dotenv_path=env_path)

#     print()
#     print("Running tests using:")
#     print(" - GO_API_ENDPOINT:", os.getenv("GO_API_ENDPOINT"))
#     print(" - TEST_PERSON_FULL_NAME:", os.getenv("DADJ_FULL_NAME"))
#     print()

#     # Construct full path to installed test file
#     shared_test_path = os.path.join(
#         os.environ["VIRTUAL_ENV"],
#         "Lib",
#         "site-packages",
#         "mbu_dev_shared_components",
#         "tests",
#         "go_tests",
#         "go_integration_tests.py"
#     )

#     # Run the test file using full path
#     exit_code = subprocess.call([
#         "pytest",
#         "-v",
#         "--disable-warnings",
#         shared_test_path
#     ])

#     sys.exit(exit_code)


if __name__ == "__main__":
    ats = AutomationServer.from_environment()

    workqueue = ats.workqueue()

    if "--go_tests" in sys.argv:
        asyncio.run(run_go_tests())

        exit(0)

    # if "--msoffice_tests" in sys.argv:
    #     asyncio.run(run_msoffice_tests())

    #     exit(0)
