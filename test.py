from djitellopy import Tello

tello = Tello()
tello.connect()

print(f"Batterijpercentage: {tello.get_battery()}%")

tello.takeoff()
tello.move_forward(200)  # Beweeg 50 cm naar voren
tello.land()
