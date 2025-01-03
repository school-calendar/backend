class CalenderException(Exception):
	"""Default Exception class for Calendar module"""

	def __init__(self, message: str) -> None:
		self.message = message
		super().__init__(self.message)

class ScheduleException(CalenderException):
	"""Exception class for Schedule module"""

class UserException(CalenderException):
	"""Exception class for User module"""

class ScheduleNotFoundException(ScheduleException):
	"""Exception class for Schedule not found"""

class ScheduleCreationException(ScheduleException):
	"""Exception class for Schedule creation"""

class ScheduleUpdateException(ScheduleException):
	"""Exception class for Schedule update"""

class ScheduleDeleteException(ScheduleException):
	"""Exception class for Schedule delete"""

class ScheduleDateException(ScheduleException):
	"""Exception class for Schedule date"""

class UserNotFoundException(UserException):
	"""Exception class for User not found"""