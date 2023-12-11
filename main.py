import uvicorn
from os import getenv

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("app.api:app", host="localhost", port=port, reload=True)