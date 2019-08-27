from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as py
import pandas as pd
import json
import numpy as np
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploaderPlotly', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        myf = request.files['file']
        fn = secure_filename(myf.filename)
        myf.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        df = pd.read_csv(fn)
        x = df['x']
        y = df['y']
        plot = go.Scatter(x=x, y=y)
        plot = [plot]
        plotJSON = json.dumps(plot, cls = plotly.utils.PlotlyJSONEncoder)
        return render_template('home2.html', x=plotJSON)

@app.route('/uploaderMatplotlib', methods=['GET','POST'])
def upload2():
    if request.method == 'POST':
        myf = request.files['file']
        fn = secure_filename(myf.filename)
        myf.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        df = pd.read_csv(fn)
        x = df['x']
        y = df['y']
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot(x,y)
        plt.style.use('seaborn')
        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        # f"<img src='data:image/png;base64,{data}'/>"
        return render_template('home3.html', data=data)


if __name__ == '__main__':
    app.run(
        debug = True)