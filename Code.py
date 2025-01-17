from pitop import Pitop, LED, UltrasonicSensor
from pitop.pma import EncoderMotor, ForwardDirection, BrakingType
from time import sleep

pitop = Pitop()
screen = pitop.miniscreen
dist_sensor1 = UltrasonicSensor(“D7”)
dist_sensor2 = UltrasonicSensor(“D0”)
signalLed1 = LED(“D6”)
signalLed2 = LED(“D1”)
blinkLed = LED(“D2”)

motor_left = EncoderMotor(“M2”, ForwardDirection.COUNTER_CLOCKWISE)
motor_right = EncoderMotor(“M1”, ForwardDirection.CLOCKWISE)

rpm_speed = 50

while True:
	d1 = dist_sensor1.distance
	d2 = dist_sensor2.distance

	blinkLed.on()

	if d1 < 0.5 and d2 > 0.5:
		#go left and turn left signal on
		signalLed2.on()
		motor_left.set_target_rpm(rpm_speed)
		motor_right.stop()
		signalLed2.off()
	elif d2 < 0.5 and d1 > 0.5:
		#go right and turn right signal on
		signalLed1.on()
		motor_right.set_target_rpm(rpm_speed)
		motor_right.stop()
		signalLed1.off()
	elif d1 < 0.5 and d2 < 0.5:
		#back up and turn left or right
		signalLed1.on()
		signalLed2.on()
		if d1 < d2:
			motor_right.set_target_rpm(-rpm_speed)
			motor_left.set_target_rpm(-rpm_speed/2)
		else:
			motor_right.set_target_rpm(-rpm_speed/2)
			motor_left.set_target_rpm(-rpm_speed)
		signalLed1.off()
		signalLed2.off()
	else:
		#go straight
		motor_left.set_target_rpm(rpm_speed)
		motor_right.set_target_rpm(rpm_speed)
	blinkLed.off()
	sleep(0.05)
