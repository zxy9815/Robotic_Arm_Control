# Robotic_Arm_Control
Control Programs for Soft Endoscopic Robotic Arm

```
Arduino: Control of Pneumatic Systems and Circuits (Back-end)
  - Button_Control: Operate Pneumatic Systems, Binary Control of Soft Actuators:
      This Arduino Program receives messages from GUI through Serial Port and then send digital signals to the Relays. It also reads        Pressure values from sensors and defines a pressure threshold.
      Generally, when you click a button to pressurize actuators:
         if pressure < threshold, it switches relays to turn ON Compressed Air and Solenoid Valves
         else if pressure > threshold, it switches relays to turn OFF Solenoid Valves
      When you want to retract air from an actuator, it switches to turn ON the Vacuum and Solenoid Valves
  
  - Pressure_Sensor: Pressure Sensor Testing (Honeywell 100PGAA5):
      For testing pressure value output from Pressure Sensors.

Python: Graphical User Interface and Serial Communication (Front-end)
  - ControlGUI: GUI for Surgeons:
      Use Python3 to run this program.
      Make sure computer is connected to Arduino before running this program.
      Make sure to change the Serial Port Path.
  ```
