from django.apps import AppConfig
from threading import Thread
import sched, time, os

class TollConfig(AppConfig):
	name = 'toll'

	def postpone(function):
		def decorator(*args, **kwargs):
			t = Thread(target = function, args=args, kwargs=kwargs)
			t.daemon = True
			t.start()
		return decorator

	@postpone
	def scheduleTime():
		while True:
			# os.system('notify-send "Hello"')
			time.sleep(60)

	scheduleTime()