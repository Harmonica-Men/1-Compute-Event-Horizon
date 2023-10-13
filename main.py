# Compute Circumference of Event Horizon

G = 1.327E11
pi = 3.14159
c = 2.998E5


SolarMass = float(input("How many solar masses do you wanna start: "))
S = int(SolarMass)

for m in range(S, 500, 100):
    C = 4*pi*G*m / (c*c)
    print("Hole Mass: ", m , "solar masses")
    print("Circumference: ", C ,"kilometers\n")

