# RC-robo-race-car
Welcome to our GitHub documentation for our RC-Controlled Car designed specifically for competitive Robo Races! This project is a custom-built, high-torque, fast-response RC car built using powerful DC motors, motor drivers, and the Raspberry Pi Pico microcontroller.

| Component             | Details                                     |
| --------------------- | ------------------------------------------- |
| **Chassis**           | Custom-built PVC body (lightweight & rigid) |
| **Motors**            | 4 × Johnson Motors (300 RPM, high torque)   |
| **Motor Drivers**     | 2 × BTS7960 (High-power H-bridge driver)    |
| **Microcontroller**   | Raspberry Pi Pico (RP2040)                  |
| **Power Source**      | 3S 2000mAh LiPo Battery (11.1V)             |
| **Control Mechanism** | RC (via RF module / custom controller)      |

 Features
High Torque & Speed: Ideal for sharp turns, quick acceleration, and obstacle navigation in Robo Race.

Dual Motor Driver Setup: Enables independent control of left and right side motors (tank steering configuration).

Lightweight & Modular Design: Easy to modify, repair, or upgrade.

Custom Code: Built from scratch for precise motor control using PWM and GPIO of Raspberry Pi Pico.

 Software Overview
Our control code is written in MicroPython (can also be adapted to C/C++ using the Pico SDK) and includes:

PWM motor control

Direction switching logic

RF signal parsing (if RF-controlled)

Failsafe logic (optional)

 Power Management
3S LiPo provides 11.1V which is fed into BTS7960 motor drivers.

Motors are wired in left-right pairs (2 motors per side), controlled via two motor drivers.

Raspberry Pi Pico powered via buck converter or onboard regulator from LiPo (depending on configuration).

Build Highlights
The PVC chassis was heat-shaped and assembled to provide both flexibility and strength.

Motors were securely mounted with custom clamps.

Wiring was kept modular using bullet connectors and screw terminals for easy troubleshooting.

Performance
Tested on grass, concrete, and ramps.

Can reach ~2.5–3 m/s on straight paths.

Takes sharp turns with differential power control.

Battery lasts for ~20–25 mins continuous racing.
