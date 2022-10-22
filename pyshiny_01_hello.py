# File     : pyshiny_01_hello.py
# Author   : Ming-Chang Lee
# Date     : 2022.10.22
# Email    : alan9956@gmail.com
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Encoding : UTF-8

# Python codes reference: https://shiny.rstudio.com/py/api/reference/shiny.ui.layout_sidebar.html#shiny.ui.layout_sidebar
# rdatasets package: https://github.com/vincentarelbundock/Rdatasets
# running with: shiny run --reload pyshiny_01_hello/pyshiny_01_hello.py

from shiny import App, render, ui
from rdatasets import data
# datasets list: https://vincentarelbundock.github.io/Rdatasets/datasets.html

df = data("faithful")

app_ui = ui.page_fluid(
    ui.h3("RWEPA - Hello Shiny for Python-v.22.10.22, alan9956@gmail.com, http://rwepa.blogspot.com/"),
    ui.layout_sidebar(
        ui.panel_sidebar(ui.input_slider("bins", "Bins size", min=0, max=100, value=30)),
        ui.panel_main(ui.output_plot("plot")),
    ),
)

def server(input, output, session):
    @output
    @render.plot(alt="A histogram")
    def plot():
        
        # df['waiting'].plot(kind='hist', alpha=0.5, bins=30, title='Histogram of waiting times', grid=True)
        myplot = df['waiting'].plot(kind='hist', alpha=0.5, bins=input.bins(), title='Histogram of waiting times', grid=True)     
        return myplot

app = App(app_ui, server)
# end
