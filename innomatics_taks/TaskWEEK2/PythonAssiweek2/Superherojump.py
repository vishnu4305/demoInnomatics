Superhero = int(input("Enter the superhero's jump height in meters: "))
step =0
total_height = 0
for i in range(Superhero):
    step += 1
    total_height += step
    
    print(f"Step {step}: Jumped {step}m (Total: {total_height}m)")
print(f"Total height reached: {total_height}m")