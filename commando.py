from djitellopy import Tello
import time  # Importeer time om pauzes toe te voegen tussen bewegingen

# Maak verbinding met de Tello drone
tello = Tello()
tello.connect()

# Print het batterijpercentage
print(f"Batterijpercentage: {tello.get_battery()}%")

# Laat de drone opstijgen
tello.takeoff()

# Beweeg 200 cm naar voren
tello.move_forward(200)

# Draai 90 graden naar links
tello.rotate_counter_clockwise(90)

# Beweeg 100 cm naar rechts
tello.move_right(100)

# Stijg 50 cm omhoog
tello.move_up(50)

# Pauzeer 2 seconden
time.sleep(2)

# Beweeg 50 cm naar achteren
tello.move_back(50)

# Draai 180 graden naar rechts
tello.rotate_clockwise(180)

# Beweeg 100 cm naar links
tello.move_left(100)

# Daal 50 cm
tello.move_down(50)

# Pauzeer 2 seconden
time.sleep(2)

# Land de drone
tello.land()
