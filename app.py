import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
import paho.mqtt.client as mqtt
import json
import time
from data_generator import create_data2, create_data, print_data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import pi
from tkinter import *

broker_address = "localhost"
topic = "Temperature Sensor"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize data lists and MQTT client
        self.count = []
        self.templist = []
        self.time = []
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect(broker_address, 1883)
        self.client.subscribe(topic)
        self.client.loop_start()

        # Set up GUI window
        self.group_label1 = tk.Label(self, text="Name = Gitansh Mittal")
        self.group_label1.pack()
        self.group_label1.place(x=20, y=10)

        self.title("Temperature Data Generator")
        self.geometry("600x600")

        # Input fields for temperature range, fluctuation, and period
        tk.Label(self, text="Enter temperature range and delta:").pack()
        self.entry1 = tk.Entry(self)
        self.entry1.pack()

        tk.Label(self, text="Enter temperature fluctuation and delta:").pack()
        self.entry2 = tk.Entry(self)
        self.entry2.pack()

        tk.Label(self, text="Enter time period (seconds) and delta:").pack()
        self.entry3 = tk.Entry(self)
        self.entry3.pack()

        # Buttons to generate data and stop/restart MQTT loop
        tk.Button(self, text="Generate Data",
                  command=self.generate_data).pack()
        tk.Button(self, text="Generate Data Continuously",
                  command=self.generate_data2).pack()
        tk.Button(self, text="Stop", command=self.stop).pack()
        tk.Button(self, text="Restart", command=self.start_again).pack()

        # Labels to display current time and temperature
        self.time_label = tk.Label(self, text="Time: 0")
        self.time_label.pack()

        self.temperature_label = tk.Label(self, text="Temperature: 0")
        self.temperature_label.pack()

        # Graph to display temperature readings
        self.fig = Figure(figsize=(28, 8), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature')
        self.ax.set_title('Temperature Readings')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def generate_data(self):
        try:
            input_str1 = self.entry1.get()
            input_str2 = self.entry2.get()
            input_str3 = self.entry3.get()
            input_values1 = [int(x) for x in input_str1.split(",")]
            input_values2 = [float(x) for x in input_str2.split(",")]
            input_values3 = [float(x) for x in input_str3.split(",")]
            # input_values1 = (18,3)
            # input_values2 = (1,0.001)
            # input_values3 = (60,5)
            data = create_data2(input_values1, input_values2, input_values3)
            print_data(data)
            payload = json.dumps(data)
            print("Sent message:", payload)
            self.client.publish(topic, payload)
            print("Function executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def generate_data2(self):
        try:
            input_str1 = self.entry1.get()
            input_str2 = self.entry2.get()
            input_str3 = self.entry3.get()
            input_values1 = [int(x) for x in input_str1.split(",")]
            input_values2 = [float(x) for x in input_str2.split(",")]
            input_values3 = [float(x) for x in input_str3.split(",")]
            # input_values1 = (18,3)
            # input_values2 = (1,0.001)
            # input_values3 = (60,5)
            data = create_data2(input_values1, input_values2, input_values3)
            print_data(data)
            payload = json.dumps(data)
            print("Sent message:", payload)
            self.client.publish(topic, payload)
            self.after(1000, self.generate_data2)
            print("Function executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def stop(self):
        try:
            self.client.loop_stop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def start_again(self):
        try:
            self.client.loop_start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def on_message(self, client, userdata, message):
        try:
            payload = message.payload.decode("utf-8")
            data = json.loads(payload)
            print_data(data)
            self.count.append(data['Count'])
            self.time.append(data['Time'])
            self.templist.append(data['Temperature'])
            self.create_graph(self.count, self.templist)
            self.time_label.config(text="Time: {}".format(data['Time']))
            self.temperature_label.config(
                text="Temperature: {:.4f}".format(data['Temperature']))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def create_graph(self, lista, listb):
        try:
            self.canvas.get_tk_widget().pack_forget()
            self.ax.plot(lista, listb)
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Temperature')
            self.ax.set_title('Temperature Readings')
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
            print("Function executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
