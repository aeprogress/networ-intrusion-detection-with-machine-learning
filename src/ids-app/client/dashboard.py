import hvplot.pandas
import numpy as np
import pandas as pd
import requests
import json

import matplotlib.pyplot as plt

import panel as pn
# hvplot.extension('matplotlib')
pn.extension('tabulator')
pn.extension(sizing_mode='stretch_width')


class Dashboard:
    def __init__(self, df):
        self.df = df
        self.idf = self.df.interactive()
        self.set_table_pipline()
        self.set_label_pipline()
        self.set_label_plot()
        self.set_template()
        self.display()

    def set_table_pipline(self):
        self.tabel_pipline = (self.idf)
        self.tabel = self.tabel_pipline.pipe(
            pn.widgets.Tabulator, pagination='remote',
            page_size=10, sizing_mode='stretch_width')

    def set_label_pipline(self):
        self.label_pipline = (
            self.idf
            .groupby(['destination_port', 'predicted_label'])['flow_duration'].size()
            .to_frame()
            .reset_index()
        )

    def set_label_plot(self):
        self.label_plot = self.label_pipline.hvplot(
            kind='bar',
            x='predicted_label',
            y='flow_duration',
            title='Detected Attacks Distribution')
        self.label_plot = self.label_plot.relabel(
            "ylabel='Custom x-label'").opts(ylabel='Label Count')
        self.label_plot = self.label_plot.relabel(
            "xlabel='Custom x-label'").opts(xlabel='Predicted Label')

    def set_template(self):
        self.template = pn.template.FastListTemplate(
            title='Intrusion Detection Dashboard',
            main=[
                pn.Row(self.label_plot.panel(width=500), margin=(0, 25)),
                pn.Row(self.tabel.panel(width=00))],
            accent_base_color='#88d8b0',
            header_background='#88d8b0')

    def display(self):
        self.template.servable()
        pn.serve(self.template)
