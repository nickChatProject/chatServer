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
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Create table and import test data in MySQL

Enter into sql folder and import tables.sql and test_data.sql to your database.
```shell=
cd sql
mysql -u username -p databasename < tables.sql
mysql -u username -p databasename < test_data.sql
```
