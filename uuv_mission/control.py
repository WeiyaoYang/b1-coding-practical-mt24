import numpy as np

class PDController:
	def __init__(self, kp: float = 0.15, kd: float = 0.6):
		self.kp = kp
		self.kd = kd
		self.previous_error = 0.0

	def reset(self) -> None:
		self.previous_error = 0.0

	def compute_control_action(self, current_error: float) -> float:
		proportional = self.kp * current_error
		derivative = self.kd * (current_error - self.previous_error)
		control_action = proportional + derivative
        
		self.previous_error = current_error
        
		return control_action