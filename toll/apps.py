from django.apps import AppConfig
from threading import Thread
import time
from puc.models import PUC

def check_pucs():
	for puc in PUC.objects.all():
		

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
			
			time.sleep(24*60*60)

	scheduleTime()