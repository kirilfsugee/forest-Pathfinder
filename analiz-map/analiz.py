from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, Line
#from kivy.clock import Clock
from kivy.config import Config
import os
if os.name == 'nt':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# задаем размер окна приложения
Config.set('graphics', 'width', '1366')
Config.set('graphics', 'height', '768')
Config.set('graphics', 'resizable', '0')
# отключам мульт тач, чтоб работала правая кнопка мыши
Config.write()

# списко точек
list_point = [(362, 192), (409, 237)]
list_connection = [(0, 1)]
list_connection_multi_line = []
list_multi_line = []


# максимальное количество перекрестков
max_count_points = 60
# статус режима вывода отладочной информации
debug = True
# поля отображения поля
x_min = 14
x_max = 809
y_min = 0
y_max = 764
# режим нажатия кнопки мыши
mouse_rejim = 0  # 0 ничего,  10 режим добавляения точки,  20 режим соединения,  30 удаления
# запомненная точка в 20 режиме
temp_i_20 = -1
# временная мультлиния
temp_multi_line =[]

class MainApp(App):
    img = Image(source='../map_forest.png')

    def build(self):

        # создаем основную раскладку
        self.layout_main = BoxLayout(padding=3)  # Отступ padding между лейаутом

        # создаем левую раскладку
        self.layout_left = BoxLayout(padding=0)
        self.layout_main.add_widget(self.layout_left)

        # создаем среднюю раскладку для отображения точек
        self.layout_midle = GridLayout(cols=1,
                                       rows=max_count_points,
                                       padding=3,
                                       size_hint=(None, None),
                                       size=(190, 768))
        self.layout_main.add_widget(self.layout_midle)

        # создаем среднюю раскладку для отображения соединений
        self.layout_midle2 = GridLayout(cols=1,
                                        rows=max_count_points,
                                        padding=3,
                                        size_hint=(None, None),
                                        size=(190, 768))
        self.layout_main.add_widget(self.layout_midle2)
        # отрисовываем всё
        self.update(self)

        # создаем правую раскладку с кнопками
        layout_right = BoxLayout(padding=3,
                                 orientation="vertical",
                                 size_hint=(None, None),
                                 size=(150, 768))
        btn_add_point = Button(text="Add point",
                               size_hint=(1, 1),
                               size=(150, 50),
                               background_color=[0, 1, 0, 1])  # rgba
        btn_add_point.bind(on_press=self.add_point)
        layout_right.add_widget(btn_add_point)

        btn_add_connection = Button(text="Add connection",
                                    size_hint=(1, 1),
                                    size=(150, 50),
                                    background_color=[0, 1, 0, 1])
        btn_add_connection.bind(on_press=self.add_connection)
        layout_right.add_widget(btn_add_connection)

        btn_add_connection_multi_line = Button(text="Add multi con",
                                    size_hint=(1, 1),
                                    size=(150, 50),
                                    background_color=[0, 1, 0, 1])
        btn_add_connection_multi_line.bind(on_press=self.add_connection_maulti_line)
        layout_right.add_widget(btn_add_connection_multi_line)


        btn_delete = Button(text="Delete",
                            size_hint=(1, 1),
                            size=(150, 50),
                            background_color=[0, 1, 0, 1])
        btn_delete.bind(on_press=self.delete)
        layout_right.add_widget(btn_delete)

        btn_export = Button(text="Export",
                            size_hint=(1, None),
                            size=(150, 50),
                            background_color=[0, 1, 0, 1])
        btn_export.bind(on_press=self.export_file)
        layout_right.add_widget(btn_export)

        self.layout_main.add_widget(layout_right)
        return self.layout_main

    def export_file(self, instance):
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку export')

    def add_point(self, instance):
        global mouse_rejim
        # функция добавить точку
        if debug: print('Вы нажали на кнопку add_point')
        if mouse_rejim == 0:
            mouse_rejim = 10

    def add_connection(self, instance):
        global mouse_rejim
        # функция добавить соединени
        if debug:
            print('Вы нажали на кнопку add_connection')
        if mouse_rejim == 0:
            mouse_rejim = 20

    def add_connection_maulti_line(self, instance):
        global mouse_rejim
        # функция добавить мульти соединение
        if debug:
            print('Вы нажали на кнопку add_connection_multi_line')
        if mouse_rejim == 0:
            mouse_rejim = 40

    def delete(self, instance):
        global mouse_rejim
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку delete')
        if mouse_rejim == 0:
            mouse_rejim = 30

    # обработчик нажатия кнопки мыши
    def on_touch_up(self, touch, p):
        global mouse_rejim, temp_i_20, list_point, temp_multi_line
        dopusk = 5
        x, y = p.pos
        x = int(x) - x_min
        y = y_max - int(y)
        if 0 < x < x_max and y_min < y < y_max and max_count_points > len(list_point) and mouse_rejim != 0:
            if debug:
                print("coords x=" + str(x) + ' y=' + str(y))

            if mouse_rejim == 10:  # добавляем точку
                list_point.append((x, y))
                self.update(self)
                mouse_rejim = 0
            elif mouse_rejim == 20:  # ожидаем первую точку
                # ищем есть ли рядом точка c x,y
                if debug:
                    print('точка in ' + str(x) + ' y ' + str(y))
                for i, (lx, ly) in enumerate(list_point):
                    if debug:
                        print('20 точка check ' + str(lx) + ' y ' + str(ly))
                    if lx - dopusk < x < lx + dopusk and ly - dopusk < y < ly + dopusk:
                        temp_i_20 = i
                        mouse_rejim = 25
                        if debug:
                            print('точка ' + str(temp_i_20))
                        break
            elif mouse_rejim == 25:  # ожидаем вторую точку
                # ищем есть ли рядом точка c x,y
                if debug:
                    print('25 точка in ' + str(x) + ' y ' + str(y))
                for i, (lx, ly) in enumerate(list_point):
                    #if debug:
                        #print('точка check ' + str(lx) + ' y ' + str(ly))
                    if lx - dopusk < x < lx + dopusk and ly - dopusk < y < ly + dopusk:
                        list_connection.append((temp_i_20, i))
                        mouse_rejim = 0
                        if debug:
                            print('добавлено соединение между ' + str(temp_i_20) + ' и ' + str(i))
                        self.update(self)
                        break
            elif mouse_rejim == 30:  # удаление
                # ищем есть ли рядом точка c x,y
                if debug:
                    print('30 точка in x ' + str(x) + ' y ' + str(y))
                for i, (lx, ly) in enumerate(list_point):
                    if lx - dopusk < x < lx + dopusk and ly - dopusk < y < ly + dopusk:
                        # провеяоем нет ли её в соединениях
                        netu = True
                        for a, b in list_connection:
                            if a==i or b==i:
                                netu = False
                                break
                        if netu:
                            list_point.pop(i)
                            self.update(self)
                # ищем на линии
                for i,(a, b) in enumerate(list_connection):
                    x1, y1 = list_point[a]
                    x2, y2 = list_point[b]
#                    print (x, ' ', y,' ', x1,' ',x2,' ',y1,' ',y2)
#                    print(abs((x - x1) * (y2 - y1) - (x2 - x1) * (y - y1)))
                    #print("abs ", abs((x - x1) / (x2 - x1 + 0.00000000000001) - (y - y1) / (y2 - y1 + 0.000000000000001)))
                    if abs((x - x1) / (x2 - x1+0.00001) - (y - y1) / (y2 - y1+0.00001))<0.46:
                        list_connection.pop(i)
                        self.update(self)
                mouse_rejim = 0
            elif mouse_rejim == 40:  # добавить мульт лаин    ожидаем первую точку
                if debug:
                    print('точка in ' + str(x) + ' y ' + str(y))
                for i, (lx, ly) in enumerate(list_point):
                    if debug:
                        print('40 точка check ' + str(lx) + ' y ' + str(ly))
                    if lx - dopusk < x < lx + dopusk and ly - dopusk < y < ly + dopusk:
                        temp_i_20 = i
                        mouse_rejim = 45
                        if debug:
                            print('точка ' + str(temp_i_20))
                        break
            elif mouse_rejim == 45:  # ожидаем рисование линий
                # ищем есть ли рядом точка c x,y
                if debug:
                    print('45 точка in ' + str(x) + ' y ' + str(y))

                for i, (lx, ly) in enumerate(list_point):  # если попали в точку конец мультлинии
                    #if debug:
                        #print('точка check ' + str(lx) + ' y ' + str(ly))
                    if lx - dopusk < x < lx + dopusk and ly - dopusk < y < ly + dopusk:
                        # добавляем наш список точек в лист
                        list_multi_line.append(tuple(temp_multi_line))
                        # очищаем текущий
                        temp_multi_line = []
                        # добавляем в список соединений мульти линии
                        list_connection_multi_line.append((temp_i_20, i))
                        mouse_rejim = 0
                        if debug:
                            print('добавлено мульти соединение между ' + str(temp_i_20) + ' и ' + str(i))
                        self.update(self)
                        break
                    else:
                        # добавляем очередную точку
                        temp_multi_line.append((x,y))
                        self.update(self)

    def update(self,p):
        self.layout_left.canvas.clear()
        self.layout_left.remove_widget(self.img)
        self.img.bind(on_touch_up=self.on_touch_up)
        self.layout_left.add_widget(self.img)

        # отображаем точки из списка
        for x, y in list_point:
            with self.layout_left.canvas:
                Color(1, 0, 1, 1)
                self.rect = Rectangle(pos=(x_min + x - 5, y_max - y - 5),
                                      size=(10, 10))

        # отображаем линий соединения из списка
        for a, b in list_connection:
            x1, y1 = list_point[a]
            x2, y2 = list_point[b]
            if list_point[a] == list_point[b]:
                pass
            else:
                with self.layout_left.canvas:
                    Color(0, 0, 1, 1)  # rgba
                    Line(points=[x_min + x1, y_max - y1, x_min + x2, y_max - y2], width=2)

        # отображаем временную мультилиний соединения из списка
        x1,y1 = list_point[temp_i_20]
        print(temp_multi_line)
        for x,y in temp_multi_line:
            with self.layout_left.canvas:
                Color(0, 0, 1, 1)  # rgba
                Line(points=[x_min + x1, y_max - y1, x_min + x, y_max - y], width=2)
                x1,y1 =x,y

        # отображаем мультилиний соединения из списка

#        print(list_connection_multi_line)
#        print(list_multi_line)
        for point, multi in list(zip(list_connection_multi_line,list_multi_line)):
            # получаем начальную и последнюю точку
            a,b = point
            xs, ys = list_point[a]
            xe, ye = list_point[b]
            l =list(multi)
            xp, yp = l.pop(0)
            # отрисовываем первую линию
            with self.layout_left.canvas:
                Color(0, 0, 1, 1)  # rgba
                Line(points=[x_min + xs, y_max - ys, x_min + xp, y_max - yp], width=2)
            while l:
                x2, y2 = l.pop(0)
                with self.layout_left.canvas:
                    Color(0, 0, 1, 1)  # rgba
                    Line(points=[x_min + xp, y_max - yp, x_min + x2, y_max - y2], width=2)
                xp, yp =x2, y2
            # отрисовываем последнюю
            with self.layout_left.canvas:
                Color(0, 0, 1, 1)  # rgba
                Line(points=[x_min + xp, y_max - yp, x_min + xe, y_max - ye], width=2)


        # отображаем список точек
        self.layout_midle.clear_widgets()
        for x, y in list_point:
            self.layout_midle.add_widget(Label(text='point ' + str(x)+','+str(y)))

        if list_point[a] == list_point[b]:
            list_connection.remove((a,b))

        self.layout_midle2.clear_widgets()
        for a, b in list_connection:
            self.layout_midle2.add_widget(Label(text='con ' + str(a)+ ','+str(b)))
        for a, b in list_connection_multi_line:
            self.layout_midle2.add_widget(Label(text='m_con ' + str(a)+ ','+str(b)))


if __name__ == '__main__':
    app = MainApp()
    app.run()

