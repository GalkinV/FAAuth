from app import app
import uvicorn
from app import logging

if __name__ == '__main__':
    uvicorn.run(app, log_level="debug")
