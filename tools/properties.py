class _Property(ABC):
	''' Шаблон '''

	def __set_name__(self, owner, name):
		self.public_name = name
		self.private_name = '_' + name

	def __get__(self, instance, name):
		return instance.__dict__.get(self.private_name, name)

	@abstractclassmethod
	def __set__(self, instance, value):
		pass


class StringProperty(_Property):
	''' Целое число '''

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise AttributeError

		self.value = value
		instance.__dict__[self.private_name] = self.value