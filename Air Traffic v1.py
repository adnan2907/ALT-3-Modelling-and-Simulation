        # Starting v1 
        # A380 landing

# Final Velocity 
Final_Velocity = 0

# Initial Velocity in kts
Landing_Speed = 140

# Change in velocity 
delta_velocity = Final_Velocity - Landing_Speed

# Deceleration Rate = usually between 3 and 6 We'll take as 3 
Deceleration = 3

# Time taken to stop the A380
time_to_Stop =  delta_velocity / 3

# ABS() = take negative value to positve 
print("Landing speed for a A380: ", abs(delta_velocity))
print("It will take", abs(round(time_to_Stop)), "seconds to stop the aircraft")

