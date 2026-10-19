from views import app
from typing import Any
import sys


COMMANDS: dict[str,Any] = {
    "runserver": app.run(port=3000, debug=True)
}

if (__name__ == "__main__"):

    if (len(sys.argv) > 1):
        COMMANDS[sys.argv[0]]
            
