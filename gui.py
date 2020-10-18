from tkinter.ttk import Separator
from models import *

# объекты -------------------------------------------------------------------
ital_pizza = ItalianPizza()  # итальянская пицца
bg_pizza = BulgarianPizza()  # болгапская пицца

hum_ital = HamAdditive(ital_pizza)             # добавка ветчина к ит.пицце
parmesan_ital = ParmesanAdditive(ital_pizza)   # добавка пармезан к ит.пицце
mush_ital = MushroomsAdditive(ital_pizza)      # добавка грибы к ит.пицце

hum_bg = HamAdditive(ital_pizza)               # добавка ветчина к болг.пицце
parmesan_bg = ParmesanAdditive(ital_pizza)     # добавка пармезан к болг.пицце
mush_bg = MushroomsAdditive(ital_pizza)        # добавка грибы к болг.пицце

# окно и его параметры -------------------------------------------------------
root = Tk()
root.geometry('900x680+200+100')
root.config(bg='Beige')
root.title('Pizza')

# глобальные виджеты итальянская пицца
ital_pizza_ingrts = Label()    # показывает текущий состав пиццы
ital_coast = Label()           # отображает текущую цену пиццы
ital_ingr_coast = Label()      # отображает цену текущего ингредиента
entry_del_ingr_ital = Entry()  # для ввода основного ингредиента для удаления

# глобальные виджеты болгарская пицца
bg_pizza_ingrts = Label(root)  # показывает текущий состав пиццы
bg_coast = Label()             # отображает текущую цену пиццы
bg_ingr_coast = Label()        # отображает цену текущего ингредиента
entry_del_ingr_bg = Entry()    # для ввода основного ингредиента для удаления


# виджеты-декоры и информационные
def decor_info_widgets():
    decor = Label()
    decor.config(bg='DarkSeaGreen', width=100, height=2)
    decor.place(x=260, y=630)

    decor2 = Label()
    decor2.config(bg='DarkSeaGreen', width=10, height=2)
    decor2.place(x=0, y=630)

    decor3 = Label()
    decor3.config(bg='PeachPuff', width=10, height=5)
    decor3.place(x=865, y=525)

    decor4 = Label()
    decor4.config(bg='PaleGoldenrod', width=58, height=5)
    decor4.place(x=450, y=525)

    txt_pizza = Label()
    txt_pizza.config(font='Arial 36', fg='Tomato', bg='Beige', text='PIZZA')
    txt_pizza.place(x=97, y=618)

    info_lbl = Label()
    info_lbl.config(font='Arial 10', fg='Tomato', bg='PaleGoldenrod', justify=RIGHT,
                    text='* Удаление основных ингредиентов НЕ ВЛИЯЕТ НА ЦЕНУ ПИЦЦЫ\n** Удалённые основные ингредиенты '
                         'можно восстановить в списке\nосуществив сброс ингредиентов до основных')
    info_lbl.place(x=450, y=530)


# ----------------    ИТАЛЬЯНСКАЯ ПИЦЦА    -----------------------------------------------------------------------------

# -> функции для управления итальянской пиццей (управляют ингредиентами и виджетами отображения стоимости)
def add_hum_ital():        # добавляет ветчину и отображает стоимость пиццы и ингредиента
    ital_pizza.add_ingredient(hum_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=hum_ital.get_coast())


def add_parmesan_ital():   # добавляет пармезан и отображает стоимость пиццы и ингредиента
    ital_pizza.add_ingredient(parmesan_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=parmesan_ital.get_coast())


def add_mush_ital():        # добавляет грибы и отображает стоимость пиццы и ингредиента
    ital_pizza.add_ingredient(mush_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=mush_ital.get_coast())


def del_hum_ital():         # удаляет ветчину и отображает стоимость пиццы и ингредиента
    ital_pizza.delete_ingredient(hum_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРИДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=f'-{hum_ital.get_coast()}')


def del_parmesan_ital():    # удаляет пармезан и отображает стоимость пиццы и ингредиента
    ital_pizza.delete_ingredient(parmesan_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=f'-{parmesan_ital.get_coast()}')


def del_mush_ital():         # удаляет грибы и отображает стоимость пиццы и ингредиента
    ital_pizza.delete_ingredient(mush_ital)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text=f'-{mush_ital.get_coast()}')


def del_main_ingr_ital():     # удаляет указанный основной ингредиент
    ingr = entry_del_ingr_ital.get().strip().lower()  # получает название ингредиента от пользователя
    ital_pizza.del_main_ingredient(ingr)
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')


def reset_ital():             # сбрасывает список ингредиентов на основной и отображает стоимость пиццы
    ital_pizza.original_list_ingr()
    ital_pizza_ingrts.config(text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}')
    ital_coast.config(text=ital_pizza.get_coast())
    ital_ingr_coast.config(text='')


# виджеты и параметры итальянской пиццы
def ital_pizza_widgets_config():
    # -> декоративные элементы -----------------------------------------
    color_lbl1 = Label()
    color_lbl1.config(bg='DarkSeaGreen', width=130, height=4)
    color_lbl1.place(x=0, y=0)

    color_lbl1 = Label()
    color_lbl1.config(bg='DarkSeaGreen', width=2, height=40)
    color_lbl1.place(x=0, y=80)  # ------------------------------------

    ital_pizza_title = Label()   # отображает название пиццы
    ital_pizza_title.config(bg='DarkSeaGreen', font=('Comic Sans Ms', 30), text=ital_pizza.get_name(), fg='SeaGreen')
    ital_pizza_title.place(x=52, y=0)

    Separator(root, orient='horizontal').place(x=0, y=6, relwidth=20)
    Separator(root, orient='horizontal').place(x=0, y=57, relwidth=20)

    add_lbl = Label()  # отображает ДОБАВИТЬ
    add_lbl.config(bg='Beige', font=('Comic Sans Ms', 11), text='ДОБАВИТЬ', fg='SeaGreen')
    add_lbl.place(x=50, y=75)

    del_lbl = Label()   # отображает УДАЛИТЬ
    del_lbl.config(bg='Beige', font=('Comic Sans Ms', 11), text='УДАЛИТЬ', fg='Tomato')
    del_lbl.place(x=155, y=75)

    txt_lbl_coast_pizza = Label()   # отображает 'цена пиццы:'
    txt_lbl_coast_pizza.config(text='цена пиццы:', font=('Comic Sans Ms', 8), fg='DarkOliveGreen', bg='Beige')
    txt_lbl_coast_pizza.place(x=360, y=66)

    txt_lbl_coast_ingr = Label()   # отображает 'ингредиента:'
    txt_lbl_coast_ingr.config(text='ингредиента:', font=('Comic Sans Ms', 8), fg='DarkOliveGreen', bg='Beige')
    txt_lbl_coast_ingr.place(x=627, y=66)

    # параметры виджета отображающего состав пиццы
    ital_pizza_ingrts.config(width=45, height=7, font=('Comic Sans Ms', 11), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                             text=f'{ital_pizza.base()}\nИНГРЕДИЕНТЫ:\n{ital_pizza.get_ingredients_pizza().lower()}',
                             wraplength=300, justify=LEFT)
    ital_pizza_ingrts.place(x=450, y=103)

    # параметры виджета отображающего цену пиццы
    ital_coast.config(width=15, height=1, font=('Comic Sans Ms', 13), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                      text=ital_pizza.get_coast())
    ital_coast.place(x=450, y=70)

    # параметры виджета отображающего цену ингредиента
    ital_ingr_coast.config(width=15, height=1, font=('Comic Sans Ms', 13), fg='DarkOliveGreen', relief=RIDGE, bd=2)
    ital_ingr_coast.place(x=705, y=70)

    input_name_ingr = Label()   # отображает 'введите название'
    input_name_ingr.config(text='введите название', font=('Comic Sans Ms', 9), fg='DarkOliveGreen', bg='Beige')
    input_name_ingr.place(x=260, y=156)

    # параметры виджета для ввода основного ингредиента
    entry_del_ingr_ital.config(width=18, font=('Comic Sans Ms', 11), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                               justify=CENTER)
    entry_del_ingr_ital.place(x=260, y=178)


# кнопки управления итальянской пиццей
def ital_block_button():
    ital_add_hum = ButtonAdd()  # добавление вечины
    ital_add_hum.config('ветчину', 50, 105, add_hum_ital)  # -> кнопка

    ital_add_parm = ButtonAdd()  # добавление пармезана
    ital_add_parm.config('пармезан', 50, 139, add_parmesan_ital)  # -> кнопка

    ital_add_mush = ButtonAdd()  # добавление грибов
    ital_add_mush.config('грибы', 50, 173, add_mush_ital)  # -> кнопка

    ital_del_hum = ButtonDel()  # удаление ветчины
    ital_del_hum.config('ветчину', 150, 105, del_hum_ital)  # -> кнопка

    ital_del_parm = ButtonDel()  # удаление пармезана
    ital_del_parm.config('пармезан', 150, 139, del_parmesan_ital)  # -> кнопка

    ital_del_mush = ButtonDel()  # удаление грибов
    ital_del_mush.config('грибы', 150, 173, del_mush_ital)  # -> кнопка

    del_main_ingr_ital_btn = Button()  # удаление основного ингредиента
    del_main_ingr_ital_btn.config(bg='white', width=20, height=2, font=('Comic Sans Ms', 10), fg='DarkSeaGreen',
                                  text='Удалить основной\nингредиент', activebackground='PapayaWhip',
                                  activeforeground='LightSalmon', command=del_main_ingr_ital)
    del_main_ingr_ital_btn.place(x=260, y=105)

    reset_list_ingr = Button()  # сброс списка ингредиентов до основного списка
    reset_list_ingr.config(bg='white', width=46, height=1, font=('Comic Sans Ms', 10), fg='DarkSeaGreen',
                           text='Сбросить список ингредиентов до основных', activebackground='PapayaWhip',
                           activeforeground='LightSalmon', command=reset_ital)
    reset_list_ingr.place(x=50, y=215)


# ------------------   БОЛГАРСКАЯ ПИЦЦА  -------------------------------------------------------------------------------

# виджеты и параметры болгарской пиццы
def bg_pizza_widgets_config():
    # -> декоративные элементы -----------------------------------------
    color_lbl1 = Label()
    color_lbl1.config(bg='DarkSeaGreen', width=130, height=4)
    color_lbl1.place(x=0, y=267)

    bg_pizza_title = Label()
    bg_pizza_title.config(bg='DarkSeaGreen', font=('Comic Sans Ms', 30), text=bg_pizza.get_name(), fg='SeaGreen')
    bg_pizza_title.place(x=65, y=267)

    Separator(root, orient='horizontal').place(x=0, y=273, relwidth=20)
    Separator(root, orient='horizontal').place(x=0, y=324, relwidth=20)
    # -------------------------------------------------------------------

    # параметры виджета отображения состава пиццы
    bg_pizza_ingrts.config(width=45, height=7, font=('Comic Sans Ms', 11), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                           text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}',
                           wraplength=300, justify=LEFT)
    bg_pizza_ingrts.place(x=450, y=370)

    txt_lbl_coast_pizza = Label()   # отображает 'цена пиццы:'
    txt_lbl_coast_pizza.config(text='цена пиццы:', font=('Comic Sans Ms', 8), fg='DarkOliveGreen', bg='Beige')
    txt_lbl_coast_pizza.place(x=360, y=335)

    txt_lbl_coast_ingr = Label()   # отображает 'ингредиента:'
    txt_lbl_coast_ingr.config(text='ингредиента:', font=('Comic Sans Ms', 8), fg='DarkOliveGreen', bg='Beige')
    txt_lbl_coast_ingr.place(x=627, y=333)

    # параметры виджета стоимости пиццы
    bg_coast.config(width=15, height=1, font=('Comic Sans Ms', 13), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                    text=bg_pizza.get_coast())
    bg_coast.place(x=450, y=337)

    # параметры виджета стоимости ингредиента
    bg_ingr_coast.config(width=15, height=1, font=('Comic Sans Ms', 13), fg='DarkOliveGreen', relief=RIDGE, bd=2,)
    bg_ingr_coast.place(x=705, y=337)

    add_lbl = Label()   # отображает 'ДОБАВИТЬ'
    add_lbl.config(bg='Beige', font=('Comic Sans Ms', 11), text='ДОБАВИТЬ', fg='SeaGreen')
    add_lbl.place(x=50, y=340)

    del_lbl = Label()   # отображает 'УДАЛИТЬ'
    del_lbl.config(bg='Beige', font=('Comic Sans Ms', 11), text='УДАЛИТЬ', fg='Tomato')
    del_lbl.place(x=155, y=340)

    input_name_ingr = Label()   # отображает 'введите название'
    input_name_ingr.config(text='введите название', font=('Comic Sans Ms', 9), fg='DarkOliveGreen', bg='Beige')
    input_name_ingr.place(x=260, y=421)

    # параметры виджета ввода основного ингредиента для удаления
    entry_del_ingr_bg.config(width=18, font=('Comic Sans Ms', 11), fg='DarkOliveGreen', relief=RIDGE, bd=2,
                             justify=CENTER)
    entry_del_ingr_bg.place(x=260, y=443)


# -> функции для управления болгарской пиццей (управляют ингредиентами и виджетами отображения стоимости)
def add_hum_bg():  # добавляет ветчину и отображает стоимость пиццы и ингредиента
    bg_pizza.add_ingredient(hum_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=hum_bg.get_coast())


def add_parmesan_bg():  # добавляет пармезан и отображает стоимость пиццы и ингредиента
    bg_pizza.add_ingredient(parmesan_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=parmesan_bg.get_coast())


def add_mush_bg():  # добавляет грибы и отображает стоимость пиццы и ингредиента
    bg_pizza.add_ingredient(mush_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=mush_bg.get_coast())


def del_hum_bg():  # удаляет ветчину и отображает стоимость пиццы и ингредиента
    bg_pizza.delete_ingredient(hum_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=f'-{hum_bg.get_coast()}')


def del_parmesan_bg():  # удаляет пармезан и отображает стоимость пиццы и ингредиента
    bg_pizza.delete_ingredient(parmesan_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=f'-{parmesan_bg.get_coast()}')


def del_mush_bg():  # удаляет грибы и отображает стоимость пиццы и ингредиента
    bg_pizza.delete_ingredient(mush_bg)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text=f'-{mush_bg.get_coast()}')


def del_main_ingr_bg():  # удаляет основной ингредиент
    ingr = entry_del_ingr_bg.get().strip().lower()
    bg_pizza.del_main_ingredient(ingr)
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')


def reset_bg():   # сбрасывает список ингредиентов на основной и отображает стоимость пиццы
    bg_pizza.original_list_ingr()
    bg_pizza_ingrts.config(text=f'{bg_pizza.base()}\nИНГРЕДИЕНТЫ:\n{bg_pizza.get_ingredients_pizza().lower()}')
    bg_coast.config(text=bg_pizza.get_coast())
    bg_ingr_coast.config(text='')


# кнопки управления болгарской пиццей
def bg_block_button():
    bg_add_hum = ButtonAdd()  # добавление ветчины
    bg_add_hum.config('ветчину', 50, 370, add_hum_bg)  # -> кнопка

    bg_add_parm = ButtonAdd()  # добавление пармезана
    bg_add_parm.config('пармезан', 50, 404, add_parmesan_bg)  # -> кнопка

    bg_add_mush = ButtonAdd()  # добавление грибов
    bg_add_mush.config('грибы', 50, 438, add_mush_bg)  # -> кнопка

    bg_del_hum = ButtonDel()  # удаление ветчины
    bg_del_hum.config('ветчину', 150, 370, del_hum_bg)  # -> кнопка

    bg_del_parm = ButtonDel()  # удаление пармезана
    bg_del_parm.config('пармезан', 150, 404, del_parmesan_bg)  # -> кнопка

    bg_del_mush = ButtonDel()  # удаление грибов
    bg_del_mush.config('грибы', 150, 438, del_mush_bg)  # -> кнопка

    del_main_ingr_bg_btn = Button()  # удаление основного ингредиента
    del_main_ingr_bg_btn.config(bg='white', width=20, height=2, font=('Comic Sans Ms', 10), fg='DarkSeaGreen',
                                text='Удалить основной\nингредиент', activebackground='PapayaWhip',
                                activeforeground='LightSalmon', command=del_main_ingr_bg)
    del_main_ingr_bg_btn.place(x=260, y=370)

    reset_list_ingr_bg = Button()  # сброс списка ингредиентов до основного списка
    reset_list_ingr_bg.config(bg='white', width=46, height=1, font=('Comic Sans Ms', 10), fg='DarkSeaGreen',
                              text='Сбросить список ингредиентов до основных', activebackground='PapayaWhip',
                              activeforeground='LightSalmon', command=reset_bg)
    reset_list_ingr_bg.place(x=50, y=480)
