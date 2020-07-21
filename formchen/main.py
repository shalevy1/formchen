import pathlib
import importlib.util
import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# TODO: Use Starlette, not FastAPI?
app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")
app.mount("/formchen", StaticFiles(directory="formchen"), name="formchen")

origin = pathlib.Path(importlib.util.find_spec('gridchen').origin)
directory = origin.parent.as_posix()
logging.info('Mount ' + directory)
app.mount("/gridchen", StaticFiles(directory=directory), name="gridchen")