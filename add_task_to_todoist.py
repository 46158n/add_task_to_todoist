import os
import sys

from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Invalid argument")
        sys.exit(1)

    load_dotenv()
    TOKEN = os.getenv("TODOIST_API_KEY")
    api = TodoistAPI(TOKEN)

    content = " ".join(sys.argv[1:])
    try:
        task = api.add_task(content=content)
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)
