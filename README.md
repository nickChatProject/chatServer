# Real-Time Chat App with FastAPI and WebSocket


## Features


- Websocket for real-time chat.
- Chat history.
- Add friends.
- Files & images upload
- Token-based authentication with redis
- Swagger UI
## Requirements

- Python >= 3.10
- MySQL >= 8.3

## Setup and Run locally
Create and activate virtual environment

```shell=
python -m venv <envname>
source <envname>/bin/activate
```

Install the dependencies
```shell=
pip install -r requirements.txt
```

Run the server
```shell=
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
