# Write your code here :-)
from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo = 17, trigger = 4, threshold_distance=0.5)
while True:
    ultrasonic.wait_for_in_range()
    print("IN range")
    ultrasonic.wait_for_out_of_range()
    print("Out of range")
