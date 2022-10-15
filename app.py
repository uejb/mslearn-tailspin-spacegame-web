#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from fastapi import FastAPI
from pydantic import Json

app = FastAPI()

@app.get("/")
async def root() -> Json:
    """Dummy function to make an endpoint available

    :returns: (JSON) Hello World
    """
    return {"message":"Hello World"}

@app.get("/healthz")
async def healthz() -> Json:
    """Dummy function to make an endpoint for health-checking available
    
    :returns: (JSON) {"message":"ok", "code":200}
    """
    return {"message":"ok", "code":200}

if __name__ == '__main__':
    print(__name__)
    print("Hello Python world!")
    