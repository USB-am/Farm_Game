class InventoryFilledError(Exception):
	''' Ошибка перезаполнения инвентаря '''


class InventoryOverSizeError(Exception):
	''' Ошибка присвоения числа больше max_value в ScaleProperty '''


class InventoryElementCountError(Exception):
	''' Ошибка при попытке получения количества элементов ячейки инвентаря > имеющегося '''
