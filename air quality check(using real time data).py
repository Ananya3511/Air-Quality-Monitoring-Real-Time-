
import time
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import threading
import numpy as np
import serial as sr
import matplotlib.pyplot as plt 
from tkinter import *
import csv 
from PIL import ImageTk, Image

  

csv_filename="realtime_data.csv"

root = tk.Tk()
root.title('Air Quality Monitoring')
root.geometry('200x100')



######## data analysis using csv file ##########
 ##############################################
                 
# Set your log file name


log_file = "E:/python/GASLOG14.CSV"


in_min=0.1
in_max=0.5
out_min=0
out_max= 100


# Conversion function based on sensor calibration
def convert_to_ppm( raw_value):
    #ppm_value = sensor_slope * raw_value + sensor_intercept
    ppm_value=((raw_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)/1000
    
    return ppm_value

# Create a function to read the log file and update the graphs
def update_graph():
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            time_data = []
            gas_data_sensor1 = []
            gas_data_sensor2 = []
            for line in lines[1:]:  # Skip the header
                parts = line.strip().split(',')
                time_data.append(int(parts[0]))
                raw_value_sensor1 = int(parts[3])
                ppm_value_sensor1 = convert_to_ppm( raw_value_sensor1)
                gas_data_sensor1.append(ppm_value_sensor1)

                raw_value_sensor2 = int(parts[4]) 
                ppm_value_sensor2 = convert_to_ppm( raw_value_sensor2)
                gas_data_sensor2.append(ppm_value_sensor2)

        ax1.cla()  # Clear the previous plot for sensor 1
        ax1.plot(time_data, gas_data_sensor1, label='MQ135 (CO2 values)', color='green')  # Updated
        ax1.set_xlabel('Time (milliseconds)')
        ax1.set_ylabel('CO2 (ppm)')
        ax1.legend() 

        ax2.cla()  # Clear the previous plot for sensor 2
        ax2.plot(time_data, gas_data_sensor2, label='MQ7 (CO values)', color='blue')  # Updated
        ax2.set_xlabel('Time (milliseconds)')
        ax2.set_ylabel('CO (ppm)')
        ax2.legend()  

        # Update the information labels
        info_label1.config(text=f"CO2 values in ppm for MQ7 Sensor: {gas_data_sensor1[-1]:.2f}ppm")  # Updated
        info_label2.config(text=f"CO values in ppm for MQ135 Sensor: {gas_data_sensor2[-1]:.2f}ppm")  # Updated

        canvas.draw()

        # Update the air quality table
        update_air_quality_table(gas_data_sensor1[-1], gas_data_sensor2[-1])  # Updated

    except FileNotFoundError:
        pass

# Function to update the air quality table based on CO and CO2 values
def update_air_quality_table(co2_value, co_value):  # Updated
    # Simple air quality calculation (you may need to adjust these thresholds)
    if co_value < 5 and co2_value < 400:
        air_quality_label.config(text="Good", foreground="green")
    elif co_value < 10 and co2_value < 800:
        air_quality_label.config(text="Moderate", foreground="orange")
    else:
        air_quality_label.config(text="Poor", foreground="red")


# Function to show the graphs and labels when the button is clicked
def show_graph():
    update_graph()
    root.after(1000, show_graph)  # Call the show_graph function every second

# Create the main application window


# Create a frame for the graphs
frame = ttk.Frame(root, borderwidth=4)
frame.place(x=10,y=110)

# Create Matplotlib figures for both sensors
fig = Figure(figsize=(12, 6), dpi=100)

ax1 = fig.add_subplot(121)  # 2 rows, 1 column, 1st subplot
ax2 = fig.add_subplot(122)  # 2 rows, 1 column, 2nd subplot

# Create a canvas to display the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

#Create label for the title 
label=tk.Label(root,text="Air Quality Monitoring System",font=("Roboto",45),relief='sunken')
label.place(x=400,y=10)



# present the air of that region 
label1=tk.Label(root,text="Air quality: ",font=("Roboto",25),relief='sunken',fg='white',bg='black',border=4)
label1.place(x=1300,y=200)



# Create labels for information inside the frame
info_label1 = ttk.Label(frame, text="", font=("Helvetica", 12))
info_label1.place(x=190,y=40)

info_label2 = ttk.Label(frame, text="", font=("Helvetica", 12))
info_label2.place(x=700,y=40)

# Create a frame for air quality calculation
quality_frame = ttk.Frame(root, borderwidth=4, relief="sunken")
quality_frame.place(x=1300,y=300)

# Create a label for air quality inside the frame
air_quality_label = ttk.Label(quality_frame, text="", font=("Helvetica", 16, "bold"))
air_quality_label.pack(pady=10)

# Create a button to trigger graph update
show_graph_button = ttk.Button(root, text="Show Graph", command=show_graph, width=20, style='TButton')
show_graph_button.place(x=1250,y=400)


# Configure the style for the button
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), foreground='red', background='blue',relief="sunken")


# with open('data_collection','w',newline='')as csvfile:
#     csv_writer =csv.writer(csvfile)
#     csv_writer.writerow(['Data'])

#     while True:
      
#         data = s_mq7.readline().decode("utf-8").strip()
       
#         csv_writer.writerow([data])
#         time.sleep(0.0001)


# # Create a frame for MQ7 sensor (CO)
# frame_mq7 = ttk.Frame(root)
# frame_mq7.place(x=930,y=130)

# # Create a Matplotlib figure for MQ7 sensor (CO)
# fig_mq7 = plt.Figure(figsize=(6,6),dpi=100)
# ax_mq7 = fig_mq7.add_subplot()

# plt.ion()  # Turn on interactive mode

# # Create a canvas to display the Matplotlib figure for MQ7 sensor (CO)
# canvas_mq7 = FigureCanvasTkAgg(fig_mq7, master=frame_mq7)
# canvas_mq7.get_tk_widget().pack()

#To startt the data collection through arduino
# start_button = ttk.Button(root, text="Start Data Collection", command=start_data_collection)
# start_button.place(x=685,y=650)
 




#########""""""""Menu Bar"""""""#########
##########################################

menubar = Menu(root) 
  
#for seperated CO graph plot

def plot_CO():
    # Create a new window for CO Graph
    co_graph_window = Toplevel(root)
    co_graph_window.title('CO Graph')
    
    # Create a Matplotlib figure for CO Graph
    fig_co = Figure(figsize=(6, 6), dpi=100)
    ax_co = fig_co.add_subplot()

    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            time_data = []
            gas_data_sensor1 = []
            for line in lines[1:]:  # Skip the header
                parts = line.strip().split(',')
                time_data.append(int(parts[0]))
                raw_value_sensor1 = int(parts[3])
                ppm_value_sensor1 = convert_to_ppm( raw_value_sensor1)
                gas_data_sensor1.append(ppm_value_sensor1)

        ax_co.plot(time_data, gas_data_sensor1, label='MQ7 (CO values)', color='blue')
        ax_co.set_xlabel('Time (milliseconds)')
        ax_co.set_ylabel('Gas Level (ppm)')
        ax_co.legend()  # Add legend to display label
        ax_co.grid(True)

        canvas_co = FigureCanvasTkAgg(fig_co, master=co_graph_window)
        canvas_co.get_tk_widget().pack()
        canvas_co.draw()  # Update the canvas
        
        info_label1.config(text=f"CO values in ppm for MQ7 Sensor: {gas_data_sensor1[-1]:.2f}ppm")
        

    except FileNotFoundError:
        pass


def plot_CO2():
    co2_graph_window = Toplevel(root)
    co2_graph_window.title('CO2 Graph')
    
    # Create a Matplotlib figure for CO Graph
    fig_co2 = Figure(figsize=(6, 6), dpi=100)
    ax_co2 = fig_co2.add_subplot()

    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            time_data = []
            gas_data_sensor2 = []
            for line in lines[1:]:  # Skip the header
                parts = line.strip().split(',')
                time_data.append(int(parts[0]))
                raw_value_sensor2 = int(parts[3])
                ppm_value_sensor2 = convert_to_ppm( raw_value_sensor2)
                gas_data_sensor2.append(ppm_value_sensor2)

        ax_co2.plot(time_data, gas_data_sensor2, label='MQ135 (CO2 values)', color='green')  # Fix: Plot gas_data_sensor2
        ax_co2.set_xlabel('Time (milliseconds)')
        ax_co2.set_ylabel('Gas Level (ppm)')
        ax_co2.legend()  # Add legend to display label
        ax_co2.grid(True)

        canvas_co2 = FigureCanvasTkAgg(fig_co2, master=co2_graph_window)
        canvas_co2.get_tk_widget().pack()
        canvas_co2.draw()  # Update the canvas
        
        info_label2.config(text=f"CO2 values in ppm for MQ135 Sensor: {gas_data_sensor2[-1]:.2f}ppm")


    except FileNotFoundError:
        pass

data_real = np.array([])

##############################plotting of real data of co2 gas######################################
def Realtimeplot():
   
    realtime_graph_window = tk.Toplevel(root)
    realtime_graph_window.title('Real Time Data Plotting ')
    
    fig_real = Figure(figsize=(13, 13), dpi=100)
    ax_real = fig_real.add_subplot()

    canvas_real = FigureCanvasTkAgg(fig_real, master=realtime_graph_window)
    canvas_real.get_tk_widget().pack()
    
    co_threshold = 110
    
    status_label = tk.Label(realtime_graph_window, text="", font=("Helvetica", 16, "bold"))
    status_label.place(x=1000, y=100)  

    
    def update_plot_realtime():
        global data_real

        try:
            a = s_mq7.readline().decode()
            data = a.split(',')[0].split(':')[-1]
            data = float(data)
            ppm_value = convert_to_ppm( data)
            data_real = np.append(data_real, ppm_value)
            ax_real.cla()
            ax_real.plot(data_real, label='CO(ppm)')
            ax_real.set_title('Real-Time CO2 Plot')
            ax_real.set_xlabel('Time(sec)')
            ax_real.set_ylabel('CO2 (ppm)')
            ax_real.legend()
            canvas_real.draw()
            
            if ppm_value > co_threshold:
                status_label.config(text="Status: Poor", foreground="red")
            if 100<ppm_value>150:
                status_label.config(text="Status: Alert", foreground="orange")
            else:
                status_label.config(text="Status: GOOD", foreground="green")

            root.after(1, update_plot_realtime)  # Schedule the next update
        except ValueError:
            pass
        
    s_mq7 = sr.Serial('COM3', 9600)                                  #COM
    update_plot_realtime()

def start_data_collection():
    global thread_mq7
    # Run data collection in a separate thread for each sensor
    thread_mq7 = threading.Thread(target=Realtimeplot)
    thread_mq7.start()



def Arduino():
    Arduino_window = tk.Toplevel(root)
    Arduino_window.title('Arduino Use')
    #for writing the working of arduino in project
    arduino_label_text = "With the help of arduino we have taken the sensor values to build a csv file and showcased that values in the form of graph in ourGUI i.e Graphical User Interface.\n"

    arduino_label = tk.Label(Arduino_window, text=arduino_label_text, font=("Helvetica", 12))
    arduino_label.pack(padx=10, pady=10)

def GUI():
    GUI_window=tk.Toplevel(root)
    GUI_window.title('GUI use')
    GUI_label_text = "\n\nOur GUI is builded user friendly which can be runned by people easily.\n\n\nMAIN PAGE:-\n       The gui contains some graphs which shows the gas level detected by the sensor(MQ--) beforhand and got saved as a csv file,through these values a average Air Quality is measured\n"
    GUI_label = tk.Label(GUI_window, text=GUI_label_text, font=("Helvetica", 12))
    GUI_label.pack(padx=10, pady=10)
    

# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Plot', menu = file) 
file.add_command(label ='CO Graph', command = plot_CO) 
file.add_separator() 
file.add_command(label ='CO2 Graph', command = plot_CO2) 
 

# Adding Real Time plot Menu 
Real = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Real Time plot', menu = Real) 
Real.add_command(label ='MQ7 real plot', command = Realtimeplot) 


# Adding Help Menu 
About = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='About', menu = About) 
About.add_command(label ='Arduino use', command = Arduino) 
About.add_command(label ='GUI', command = GUI) 
  

# display Menu 
root.config(menu = menubar) 






root.mainloop()