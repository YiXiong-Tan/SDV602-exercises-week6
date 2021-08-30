"""
Presents an example based on Demo_Matplotlib_Browser
"""
import ChartExamples as ce 

import PySimpleGUI as sg
import matplotlib
import inspect
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def embedded_plt(fig_dict):
    sg.theme('LightGreen')

    figure_w, figure_h = 650, 650
    # define the form layout
    listbox_values = list(fig_dict)
    col_listbox = [[sg.Listbox(values=listbox_values, enable_events=True, size=(28, len(listbox_values)), key='-LISTBOX-')],
                [sg.Text(' ' * 12), sg.Exit(size=(5, 2))]]

    layout = [[sg.Text('Matplotlib Plot Test', font=('current 18'))],
            [sg.Col(col_listbox, pad=(5, (3, 330))), sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-') ,
            sg.MLine(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')],]

    # create the form and show it without the plot
    window = sg.Window('Our Demo Application - Embedding Matplotlib In PySimpleGUI with **kwargs', layout, grab_anywhere=False, finalize=True)
    figure_agg = None
    # The GUI Event Loop
    while True:
        event, values = window.read()
        # print(event, values)                  # helps greatly when debugging
        if event in (sg.WIN_CLOSED, 'Exit'):             # if user closed window or clicked Exit button
            break
        if figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            delete_figure_agg(figure_agg)
        choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
        print(values['-LISTBOX-'])
        func_tuple = fig_dict[choice]                         # get function to call from the dictionary
        kwargs = func_tuple[1]
        func = func_tuple[0]
        window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
        
        fig = func(**kwargs)                                    # call function to get the figure
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)  # draw the figure
    window.close()

if __name__ == "__main__":
    #ce.show_figFunc(ce.bar_chart)

    dictionary_of_figure_functions = {'Line Plot':(ce.line_plot,{'plot':[-1, -4.5, 16, 23]}),
    'Plot Dots(discrete plot)':(ce.discrete_plot,{ 'plot_dots':[-1, -4.5, 16, 23], 'plot_color':"ob"}),
    'Name and Label':(ce.names_labels,{'xlabel':'Day', 'title':'Temperature in Celsius', 'ylabel':'Temperature Graph','days':range(1, 9), 'celsius_values':[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]}),
    'Plot many Lines':(ce.multiple_plots,{'days':list(range(1, 9)),'celsius_min':[19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1],'celsius_max':[24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]}),
    'Bar Chart':(ce.bar_chart,{'years' : [str(year) for year in range(2010, 2021)],'visitors' : [1241, 50927, 162242, 222093, 665004, 2071987, 2460407, 3799215, 5399000, 5474016, 6003672]}),
    'Histogram':(ce.histogram,{'title':'Our Histogram Name'}),
    'Scatter Plots':(ce.scatter_plots,{'title':'Scatter Plot Example'}),
    'Stack Plot':(ce.stack_plot,{'title':'Stack Plot Example'}),
    'Pie Chart 1':(ce.pie_chart1,{'labels' : ['C', 'Python', 'Java', 'C++', 'C#'], 'sizes' : [13.38, 11.87, 11.74, 7.81, 4.41]}),
    'Pie Chart 2':(ce.pie_chart2,{'title':'TIOBE Index for May 2021'})}

    embedded_plt(dictionary_of_figure_functions)