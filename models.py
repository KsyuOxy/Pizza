from abc import ABC, abstractmethod
from tkinter import messagebox
from tkinter import *


class Pizza(ABC):  # абстрактный класс для пиццы
    def __init__(self, name: str):
        self.__name = name    # название пиццы
        self.__coast = 0.00   # стоимость пиццы (будет переопределяться)

    def base(self):
        return 'Основа для пиццы.'

    @abstractmethod       # переопределить, т.к. значение self.__coast у наследников будет изменено
    def get_coast(self):  # возвращает стоимость
        return self.__coast

    def get_name(self):  # возвращает название
        return self.__name


class Additive(Pizza):  # класс добавок для пиццы
    def __init__(self, pizza: Pizza, name: str):
        super().__init__(name)
        self.__name = name    # название
        self.__pizza = pizza  # пицца
        self.__coast = 0.00   # стоимость

    def get_coast(self):  # возвращает стоимость
        return self.__coast

    def base(self):
        return 'Основа для пиццы.'


# -------------------------------------------------------------    ИТАЛЬЯНСКАЯ ПИЦЦА    --------------------------------
class ItalianPizza(Pizza):    # класс итальянская пицца
    def __init__(self, name='Итальянская пицца'):
        super().__init__(name)
        self.__name = name
        self.__coast = 50.0  # стоимость пиццы без добавок
        # основные ингредиенты итвльянской пиццы
        self.__ingredients = ['томатный соус', 'оливковое масло', 'сыр моццарелла', 'сушёный базилик']
        # кортеж основных ингредиентов, к которым можно вернуться при необходимости
        self.__control_list = ('томатный соус', 'оливковое масло', 'сыр моццарелла', 'сушёный базилик')

    def base(self):
        return 'Классическая основа для пиццы с сырным бортиком. '

    def get_coast(self):
        return self.__coast

    def get_ingredients_pizza(self):  # возвращает строку списка ингредиентов
        return ', '.join(self.__ingredients)

    # -----------------------------------------------
    def add_ingredient(self, ingredient: Additive):  # добавляет принятый ингредиент в список ингредиентов пиццы
        self.__coast = round(self.__coast + ingredient.get_coast(), 2)  # обновляет стоимость
        return self.__ingredients.append(ingredient.get_name())  # возвращает обновлённый список ингредиентов

    # ----------------------------------------------
    def delete_ingredient(self, ingredient: Additive):  # удаляет принятый ингредиент из списка ингредиентов пиццы
        if ingredient.get_name() in self.get_ingredients_pizza():  # проверяет наличие ингредиента в списке
            self.__coast = round(self.__coast - ingredient.get_coast(), 2)  # обновляет стоимость
            self.__ingredients.remove(ingredient.get_name())  # удаляет принятый ингридиент
            return self.get_ingredients_pizza()  # возвращает строку-список ингредиентов
        else:
            messagebox.showwarning('Внимание!', 'Такого ингредиента нет, либо он в списке основных ингредиентов пиццы.')

    # ---------------------------------------------
    def del_main_ingredient(self, main_ingredient: str):  # удаляет принятый ингредиент из списка ингредиентов пиццы
        if main_ingredient in self.__ingredients[:5]:  # проверяет наличие в срезе, где могут находится основн.ингредиен
            self.__ingredients.remove(main_ingredient)  # удаление основного ингредиента (не влияет на цену)
            messagebox.showwarning('Внимание!', f'Удалён основной ингредиент {main_ingredient}.')
            return self.get_ingredients_pizza()
        else:
            messagebox.showwarning('Внимание!', 'Такого ингредиента нет в текущем списке ингредиентов пиццы.')

    # --------------------------------------------
    def original_list_ingr(self):   # сброс списка ингредиентов на изначальный(основной список)
        self.__ingredients.clear()  # очищает список ингредиентов
        self.__ingredients = [i for i in self.__control_list]  # генерирует исходный список ингредиентов из кортежа
        self.__coast = 50.0    # сбрасывает цену на начальную
        messagebox.showwarning('Внимание!', 'Список ингредиентов пиццы обновлён до основных.')
        return self.__ingredients


# ----------------------------------------------------------   БОЛГАРСКАЯ ПИЦЦА  ---------------------------------------
class BulgarianPizza(Pizza):  # класс болгарская пицца
    def __init__(self, name='Болгарская пицца'):
        super().__init__(name)
        self.__name = name
        self.__coast = 65.0  # стоимость пиццы без добавок
        # основные ингредиенты болгарской пиццы
        self.__ingredients = ['томатный соус острый', 'помидоры', 'перец паприка', 'лук', 'сыр моццарелла']
        # кортеж основных ингредиентов, к которым можно вернуться при необходимости
        self.__control_list = ('томатный соус острый', 'помидоры', 'перец паприка', 'лук', 'сыр моццарелла')

    def base(self):
        return 'Классическая основа для пиццы с мясным бортиком. '

    def get_coast(self):
        return self.__coast

    def get_ingredients_pizza(self):  # возвращает строку из списка ингредиентов
        return ', '.join(self.__ingredients)

    # --------------------------------------------
    def add_ingredient(self, ingredient: Additive):  # добавляет принятый ингредиент в список ингредиентов пиццы
        self.__coast = round(self.__coast + ingredient.get_coast(), 2)  # обновляет стоимость
        return self.__ingredients.append(ingredient.get_name())  # возвращает обновлённый список ингредиентов

    # -------------------------------------------
    def delete_ingredient(self, ingredient: Additive):  # удаляет принятый ингредиент из списка ингредиентов пиццы
        if ingredient.get_name() in self.__ingredients:  # проверяет наличие ингредиента в списке
            self.__coast = round(self.__coast - ingredient.get_coast(), 2)  # обновляет стоимость
            self.__ingredients.remove(ingredient.get_name())  # удаляет принятый ингредиент
            return self.get_ingredients_pizza()
        else:
            messagebox.showwarning('Внимание!', 'Такого ингредиента нет, либо он в списке основных ингредиентов пиццы.')

    # -------------------------------------------
    def del_main_ingredient(self, main_ingredient: str):  # удаляет принятый ингредиент из списка ингридиентов пиццы
        if main_ingredient in self.__ingredients[:6]:  # проверяет наличие в срезе, где могут находится основн.ингредиен
            self.__ingredients.remove(main_ingredient)  # удаление основного ингредиента
            messagebox.showwarning('Внимание!', f'Удалён ингредиент {main_ingredient}.')
            return self.get_ingredients_pizza()
        else:
            messagebox.showwarning('Внимание!', 'Такого ингредиента нет в текущем списке ингредиентов пиццы.')

    # -------------------------------------------
    def original_list_ingr(self):   # сброс списка ингредиентов на изначальный(основной список)
        self.__ingredients.clear()  # очищает список ингредиентов
        self.__ingredients = [i for i in self.__control_list]  # генерирует исходный список ингредиентов из кортежа
        self.__coast = 65.0    # сбрасывает цену на начальную
        messagebox.showwarning('Внимание!', 'Список ингредиентов пиццы обновлён до основных.')
        return self.__ingredients


# ----------------------------------------------------------------------------------------------------------------------
class HamAdditive(Additive):  # добавка ветчина
    def __init__(self, pizza: Pizza, name='ветчина'):
        super().__init__(pizza, name)
        self.__pizza = pizza
        self.__name = name
        self.__coast = 20.90

    def get_coast(self):
        return self.__coast

    def add_coast(self):  # для проверки стоимости пиццы с добавлением ингредиента (правда в графике не пригодилось)
        return f'С ветчиной будет стоить {round(self.__coast + self.__pizza.get_coast(), 2)}'


class MushroomsAdditive(Additive):  # добавка грибы
    def __init__(self, pizza: Pizza, name='грибы'):
        super().__init__(pizza, name)
        self.__pizza = pizza
        self.__name = name
        self.__coast = 15.50

    def get_coast(self):
        return self.__coast

    def add_coast(self):  # для проверки стоимости пиццы с добавлением ингредиента (правда в графике не пригодилось)
        return f'С грибами будет стоить {round(self.__coast + self.__pizza.get_coast(), 2)}'


class ParmesanAdditive(Additive):  # добавка пармезан
    def __init__(self, pizza: Pizza, name='сыр пармезан'):
        super().__init__(pizza, name)
        self.__pizza = pizza
        self.__name = name
        self.__coast = 17.40

    def get_coast(self):
        return self.__coast

    def add_coast(self):  # для проверки стоимости пиццы с добавлением ингредиента (правда в графике не пригодилось)
        return f'С сыром пармезан будет стоить {round(self.__coast + self.__pizza.get_coast(), 2)}'


class ButtonAdd(Button):  # кнопка добаления ингредиента
    def __init__(self):
        super().__init__()
        self.__button = Button()

    def config(self, ingr, x, y, comm):
        self.__button.config(bg='PaleGoldenrod', width=10, height=1, font=('Comic Sans Ms', 10), text=ingr,
                             fg='SeaGreen', activebackground='LightCyan', activeforeground='Aquamarine',
                             command=comm)
        self.__button.place(x=x, y=y)


class ButtonDel(Button):  # кнопка удаления ингредиента
    def __init__(self):
        super().__init__()
        self.__button = Button()

    def config(self, ingr, x, y, comm):
        self.__button.config(bg='PeachPuff', width=10, height=1, font=('Comic Sans Ms', 10), text=ingr,
                             fg='Tomato', activebackground='PapayaWhip', activeforeground='LightSalmon',
                             command=comm)
        self.__button.place(x=x, y=y)
