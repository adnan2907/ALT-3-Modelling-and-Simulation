        # Starting v1 
        # A380 landing

# Final Velocity = v 
Final_Velocity = 0

# Initial Velocity in kts = u 
Landing_Speed = int(input("Enter a landing speed: "))

# Change in velocity 
delta_velocity = Final_Velocity - Landing_Speed

# Deceleration Rate = usually between 3 and 6 We'll take as 3, (Same as acceleration)
Deceleration = 3

# Time taken to stop the A380
time_to_Stop =  delta_velocity / 3

# ABS() = take negative value to positve 
print("Landing speed for a A380: ", abs(delta_velocity))
print(" ")
print("It will take", abs(round(time_to_Stop)), "seconds to stop the aircraft")
print(" ")
    # Starting v2 
    # Making user input more than 1300 in length and less than 18500

'''while True:
    
    Total_runway_length = int(input("Enter runway length: "))
    
    if Total_runway_length <= 1300:
        print("Runway too short, Try again")
        continue
    if Total_runway_length >= 18500:
        print("Runway too long, Try again")
        continue
    else:
        break'''
    
# s = 1/2(u+v)t
# s = displacement == distance to stop the aircraft

        # Math Operation working but not correct values
        # Before values were the same when changing runway length

# Converting knots to km/h
one_knot = 1.85
Landing_speed_in_km = Landing_Speed * 1.85
print("Landing Speed in Km/h: ", Landing_speed_in_km)
Runway_Distance_Taken = 1/2 * Landing_speed_in_km + Final_Velocity * time_to_Stop

print(" ")

print("Runway distance is: ", Runway_Distance_Taken, "taken")

 # Starting v3
 # genertating graph - runway distace vs speed input

x_speed = []
y_distance = []

x_speed.append(Landing_speed_in_km)
y_distance.append(Runway_Distance_Taken)

print("Distances : ", y_distance)

print(" ")

print("speeds: ", x_speed)
 
    
import pygal

line_chart = pygal.Line()
line_chart.title = 'Runway distance Taken vs Landing Speed'
line_chart.add('speeds', x_speed)
line_chart.add('Distances', y_distance)
line_chart.render_to_file('Runway Distance vs Landing Speed.svg')
 
'''def graph(Landing_speed_in_km, Runway_Distance_Taken):
    


graph()'''
