class InventoryFilledError(Exception):
	''' Ошибка перезаполнения инвентаря '''
	pass


class InventoryOverSizeError(Exception):
	''' Ошибка присвоения числа больше max_value в ScaleProperty '''
	pass
