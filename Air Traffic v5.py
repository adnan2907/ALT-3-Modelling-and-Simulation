# Starting v4 

def Airbus_Stopping_distance(Landing_Speed):
    Final_Velocity = 0
    delta_velocity = Final_Velocity - Landing_Speed
    time_to_Stop =  delta_velocity / 3
    
    Landing_speed_in_km = Landing_Speed * 1.85
    Runway_Distance_Taken = 1/2 * Landing_speed_in_km + Final_Velocity * time_to_Stop
    return Runway_Distance_Taken

# Starting v1 
        # A380 landing

# Final Velocity = v 

# Initial Velocity in kts = u 

# Change in velocity 


# Deceleration Rate = usually between 3 and 6 We'll take as 3, (Same as acceleration)
#Deceleration = 3

# Time taken to stop the A380


# ABS() = take negative value to positve 
#print("Landing speed for a A380: ", abs(delta_velocity))
#print(" ")
#print("It will take", abs(round(time_to_Stop)), "seconds to stop the aircraft")
#print(" ")
    # Starting v2 
    # Making user input more than 1300 in length and less than 18500

    
# s = 1/2(u+v)t
# s = displacement == distance to stop the aircraft

        # Math Operation working but not correct values
        # Before values were the same when changing runway length

# Converting knots to km/h
#one_knot = 1.85

#print("Landing Speed in Km/h: ", Landing_speed_in_km)
#print(" ")
#print("Runway distance is: ", Runway_Distance_Taken, "taken")

 # Starting v3
 # genertating graph - runway distace vs speed input

#x_speed = []

#x_speed.append(Landing_speed_in_km)
#y_distance.append(Runway_Distance_Taken)

#print("Distances : ", y_distance)

#print(" ")

#print("speeds: ", x_speed)
 
# Starting v5 
# Range of speed between 140 and 221 (Landing Speed) // going up by 5

y_distance = []

for i in range(140, 220, 4):
     y_distance.append(Airbus_Stopping_distance(i))
    
import pygal

line_chart = pygal.Line(x_title='Distances Taken When Landed (in thousands) ', y_title='Landing Speed')
line_chart.title = 'Runway distance Taken vs Landing Speed'
line_chart.x_labels = map(str, range(0, 21, 1))
line_chart.y_labels = map(str, range(130, 220, 10))
line_chart.add('Airbus Landing distances', y_distance)
line_chart.render_to_file('Runway Distance vs Landing Speed.svg')

line_chart.render_in_browser()


