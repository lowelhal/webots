"""Sample Webots controller for the pick and place benchmark."""

from controller import Robot

# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Inizialize base motors.
wheels = []
wheels.append(robot.getDevice("wheel1"))
wheels.append(robot.getDevice("wheel2"))
wheels.append(robot.getDevice("wheel3"))
wheels.append(robot.getDevice("wheel4"))
for wheel in wheels:
    # Activate controlling the motors setting the velocity.
    # Otherwise by default the motor expects to be controlled in force or position,
    # and setVelocity will set the maximum motor velocity instead of the target velocity.
    wheel.setPosition(float('+inf'))



# Move forward.
for wheel in wheels:
    wheel.setVelocity(7.0)
# Wait until the robot is in front of the box.
robot.step(520 * timestep)


# Rotate the robot.
wheels[0].setVelocity(-7)
wheels[1].setVelocity(7)
wheels[2].setVelocity(-7)
wheels[3].setVelocity(7)
robot.step(500 * timestep)


# Stop
for wheel in wheels:
    wheel.setVelocity(0.0)

