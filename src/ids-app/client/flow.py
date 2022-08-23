import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import numpy as np
import pandas as pd
import requests
import json

from feature_extractor import Features_Extractor


class UI:
    def __init__(self):
        self.file = None
        self.df = None

        self.win = tk.Tk()
        self.display()

    # Create a window object and a label and button.
    def display(self):
        self.win.geometry("450x100")  # Size of the window
        self.win.title('IDS')
        font1 = ('Helvetica', 18, 'bold')
        self.l1 = tk.Label(
            self.win,
            text='Upload ".pcap" File',
            width=30,
            font=font1)

        self.l1.grid(row=2, column=1)
        b1 = tk.Button(
            self.win,
            text='Upload',
            width=20,
            command=lambda: self.upload_file())

        b1.grid(row=3, column=1)
        self.win.mainloop()  # Keep the window open

    # On button click ask user for "pcap"
    def upload_file(self):
        self.file = filedialog.askopenfilename()
        self.l1.config(text='Loading...')

        # Extract features from selected "pcap" file.
        fe = Features_Extractor(self.file)
        df = fe.df
        print(df)
        data = df.to_dict('records')

        # Send the extracted feature to the deployed model for label predictions.
        # url = 'http://127.0.0.1:8081/predict'
        url = 'https://intrusion-detection-classifier.herokuapp.com/predict'
        req = requests.post(url, json=data)
        results = json.loads(json.loads(req.text)[0])
        req.close()
        df['predicted_label'] = results
        self.df = df
        self.win.destroy()
