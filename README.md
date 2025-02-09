# Air Quality Monitoring System(Real Time)

# Overview:
The Air Quality Monitoring System is a Python-based application that monitors and displays real-time air quality data, focusing on gas concentrations such as CO2 and CO. The system uses sensors (MQ135 for CO2 and MQ7 for CO) connected to an Arduino, collecting data that is visualized through graphs in a graphical user interface (GUI).

The system allows for real-time plotting of gas concentrations, displays air quality indicators, and logs sensor data into a CSV file for historical tracking and analysis.

# Features:
## 1. Data Collection:
  Collects data from gas sensors (MQ135 for CO2 and MQ7 for CO) connected to an Arduino.
  
  Logs the data into a CSV file for further analysis and record-keeping.
## 2. Real-Time Graphs:
  Displays real-time graphs of gas concentrations over time.
  
  Separate graphs are available for CO and CO2 levels, which update dynamically.
## 3. Air Quality Indicators:
  Categorizes the air quality based on sensor data into:
  
  1) Good: Low levels of CO and CO2.  
  2) Moderate: Moderate levels of CO and CO2.  
  3) Poor: High levels of CO and CO2.
     
The air quality is displayed in the main window with specific sensor values.
## 4. Real-Time Plotting:
  Continuously updates the gas levels in a real-time plot, allowing for constant monitoring of air quality.
  
  Displays the real-time status of the air quality (Good, Alert, or Poor).
## 5. CSV Logging:
  The sensor data is logged into a CSV file for further review and analysis.
  
  This data is used for plotting and can be accessed for historical records.
## 6. Interactive GUI:
  The user-friendly interface allows users to easily interact with the system and view air quality graphs and status.
  
  Users can see the latest gas concentrations and their corresponding air quality.
## 7. Multiple Graphing Options:
  The system provides options to view separate graphs for CO and CO2.
  
  Users can open individual graph windows to see the detailed trends of each gas.
# Usage
  When the program is launched, it will display a window with real-time graphs of the gas concentrations.
  
  You can view the status of the air quality (Good, Moderate, or Poor) based on the latest readings from the sensors.
  
  Use the menu options to display separate graphs for CO or CO2 or to monitor real-time data.

