# Sample snippet
from machine import Pin, PWM
import time

# Example for setting up PWM on one motor
motor_pwm = PWM(Pin(15))  # Adjust GPIO as per your wiring
motor_pwm.freq(1000)
motor_pwm.duty_u16(32768)  # 50% duty cycle
