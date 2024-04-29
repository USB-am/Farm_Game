class InventoryFilledError(Exception):
	''' Ошибка перезаполнения инвентаря '''


class InventoryOverSizeError(Exception):
	''' Ошибка присвоения числа больше max_value в ScaleProperty '''


class InventoryElementCountError(Exception):
	''' Ошибка при попытке получения количества элементов ячейки инвентаря > имеющегося '''


class InventoryElementTypeError(Exception):
	''' Ошибка при попытке добавления к InventoryCell элемента другого типа '''
