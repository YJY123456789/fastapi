from fastapi import FastAPI
from flask import render_template

app = FastAPI()


@app.route('/')
def get():
    return render_template('index.html')