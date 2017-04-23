from abc import ABCMeta, abstractmethod

class Observer(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def update(self, *args, **kwargs):
		pass

class Observable(object):

	def __init__(self):
		self.observers = []
		
	def add_observer(self, observer):
		if not observer in self.observers:
			self.observers.append(observer)
			
	def delete_observer(self, observer):
		if observer in self.observers:
			self.observers.remove(observer)
			
	def delete_observers(self):
		if self.observers:
			del self.observers[:]
			
	def notify_observers(self, *args, **kwargs):
		for observer in self.observers:
			observer.update(*args, **kwargs)
