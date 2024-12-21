# Constants for surface gravity factors
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

# Get name and weight from user input
sName = input("Enter your name: ")
sEarthWeight = input("Enter your weight on Earth (in lbs): ")

# Convert the entered weight to a float
nEarthWeight = float(sEarthWeight)

# Calculate weights on other planets
nMercuryWeight = nEarthWeight * MERCURY_GRAVITY
nVenusWeight = nEarthWeight * VENUS_GRAVITY
nMoonWeight = nEarthWeight * MOON_GRAVITY
nMarsWeight = nEarthWeight * MARS_GRAVITY
nJupiterWeight = nEarthWeight * JUPITER_GRAVITY
nSaturnWeight = nEarthWeight * SATURN_GRAVITY
nUranusWeight = nEarthWeight * URANUS_GRAVITY
nNeptuneWeight = nEarthWeight * NEPTUNE_GRAVITY
nPlutoWeight = nEarthWeight * PLUTO_GRAVITY

# Output the results
print(f"\n{sName}'s Weight on the Planets of the Solar System:")
print(f"{'Mercury:':<12}{nMercuryWeight:>10.2f}")
print(f"{'Venus:':<12}{nVenusWeight:>10.2f}")
print(f"{'Moon:':<12}{nMoonWeight:>10.2f}")
print(f"{'Mars:':<12}{nMarsWeight:>10.2f}")
print(f"{'Jupiter:':<12}{nJupiterWeight:>10.2f}")
print(f"{'Saturn:':<12}{nSaturnWeight:>10.2f}")
print(f"{'Uranus:':<12}{nUranusWeight:>10.2f}")
print(f"{'Neptune:':<12}{nNeptuneWeight:>10.2f}")
print(f"{'Pluto:':<12}{nPlutoWeight:>10.2f}")
