import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def bering_to_vector(bearing,speed):
  """
    Convert navigation bearing + speed -> (vx_east, vy_north)

    Bearing convention:
      - 0 deg = North
      - 90 deg = East
      - increases clockwise

    Returns a numpy array [vx_east, vy_north] (m/s)
    """
  theeta = math.radians(90 - bearing)
  vx = speed * math.cos(theeta)
  vy = speed * math.sin(theeta)
  return np.arrar([vx,vy])
def vector_to_bearing(vx,vy):
  
  theeta = math.atan2(vx,vy) 
  bearing = (90 - math.degrees(theeta)) % 360.0
  magnitude = math.hypot(vx,vy)
  return bearing, magnitude
def required_air_vector_for_ground_target(target_bearing_degree,desired_ground_speed,wind_beairing,wind_speed):
 """
  Thing	                     Meaning
  AIR	     The direction and speed the drone tries to fly to make GROUND = DESIRED
  WIND	   The direction and speed the air pushes the drone
  GROUND	 The direction and speed the drone actually moves on the map

  Physics: AIR + WIND = GROUND
  Goal: GROUND = DESIRED
  So solve: AIR = DESIRED − WIND → this makes AIR + WIND = DESIRED.
  """

  desired_ground_vec = bearing_to_vector(target_bearing_degree,desired_ground_speed)
  wind_vec = bearing_to_vector(wind_bearing,wind_speed)
  air_vec = desired_ground_vec - wind_vec
  air_bearing_degree, air_speed = bearing_to_vector(air_vec[0],air_vec[1])
  return air_vec, air_bearing_degree, air_speed
"CODE IS DONE HERE"

def simple_drone_sim():
  
    target_bearing = 45
    desired_ground_speed = 12
    wind_bearing = 210
    wind_speed = 6
    duration = 30
    dt = 1
    initial_air_vec = bearing_to_vector(target_bearing, desired_ground_speed)
    wind_vec = bearing_to_vector(wind_bearing, wind_speed)
    air_corrected = required_air_vector(target_bearing, desired_ground_speed,
                                       wind_bearing, wind_speed)

    steps = duration + 1
    drift = np.zeros((steps, 2))
    corrected = np.zeros((steps, 2))

    for i in range(1, steps):
        drift[i] = drift[i - 1] + (initial_air_vec + wind_vec) * dt
        corrected[i] = corrected[i - 1] + (air_corrected + wind_vec) * dt

    plt.figure(figsize=(7,7))
    plt.plot(drift[:,0], drift[:,1], 'o-', label="Drift path")
    plt.plot(corrected[:,0], corrected[:,1], 'o-', label="Corrected path")
    plt.scatter(0,0, marker='s', label="Start")
    plt.axis('equal'); plt.grid(True)
    plt.title("Simple Drone Wind Correction")
    plt.xlabel("East (m)")
    plt.ylabel("North (m)")
    plt.legend()
    plt.show()
  
  
  
  

