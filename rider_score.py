# Sample ride data
harsh_brakes = 2
sudden_acceleration = 1
overspeed_events = 1
unsafe_turns = 1
proximity_alerts = 2

# Initial score
score = 100

# Penalty calculation
score -= 5 * harsh_brakes
score -= 4 * sudden_acceleration
score -= 6 * overspeed_events
score -= 3 * unsafe_turns
score -= 2 * proximity_alerts

# Risk level classification
if score >= 85:
    risk = "Safe Rider"
elif score >= 70:
    risk = "Moderate Risk"
else:
    risk = "Unsafe Rider"

# LED logic
left_led = "RED"
right_led = "GREEN"

# Output
print("Rider Score:", score)
print("Risk Level:", risk)
print("Left LED:", left_led)
print("Right LED:", right_led)

