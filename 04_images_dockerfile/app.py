# simple script that process data

import json
from datetime import datetime

data = {
    "app": "My first Docker App",
    "timestamp": datetime.now().isoformat(),
    "python_version": "3.12",
    "message": "If you see this, your Dockerfile works perfectly"
}

print(json.dumps(data, indent=2, ensure_ascii=False))