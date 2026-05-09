
vehicle_side = "left"


if vehicle_side == "left":
    left_led = "RED"
    right_led = "GREEN"
elif vehicle_side == "right":
    left_led = "GREEN"
    right_led = "RED"
else:
    left_led = "GREEN"
    right_led = "GREEN"