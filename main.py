#Author: Omar Darwish
#Assignment Title: Program 26
#Assignment Description: GUI - Pie Chart
#Date Created: 11/15/2023
#Due Date: 11/17/2023

import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Pie Chart Generator")

        self.data = {}
        self.load_button = tk.Button(root, text = "Load Data", command = self.load_data)
        self.load_button.pack()

        self.plot_button = tk.Button(root, text = "Plot Pie Chart", command = self.plot_pie_chart)
        self.plot_button.pack()

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes = [("CSV files", "*.csv")])
        if file_path:
            self.read_csv(file_path)
    def read_csv(self, file_path):
        self.data = {}
        with open(file_path, newline = '') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                category, value = row
                self.data[category] = float(value.strip('"'))
    def plot_pie_chart(self):
        labels = self.data.keys()
        sizes = self.data.values()

        fig, ax = plt.subplots()
        ax.pie(sizes, labels = labels, autopct = '%1.1f%%')
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master = self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PieChartApp(root)
    root.mainloop()


