from flask import Flask, render_template, request, redirect
import os
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    files_path = 'uploaded_files/'
    list_files = os.listdir(files_path)
    list_excel = []
    # Проверка и отбор только файлов .xlsx
    for i in list_files:
        if i.endswith('.xlsx'):
            list_excel.append(i)
    return render_template('home.html', list_excel=list_excel)
    # return list_excel


@app.route("/otzav")
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        fw = open(f'./files/{file_name}', 'w')
        fw.write(file_context)
        fw.close()

    return render_template('created.html', message=file_name)


@app.route('/show')
def show():
    files_paths = os.listdir('./files')
    files_paths.remove('deleted_files')
    return render_template('show.html', list_files=files_paths)


@app.route('/file/<name>')
def file_fn(name):
    path = f'./files/{name}'
    file_context = open(path, 'r').read()
    return render_template('file.html', file_name=path, file_context=file_context)