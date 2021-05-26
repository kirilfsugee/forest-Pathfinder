from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

from kivy.config import Config

# задаем размер окна приложения
Config.set('graphics', 'width', '1400')
Config.set('graphics', 'height', '1000')
Config.set('graphics', 'resizable', '0')
# отключам мульт тач, чтоб работала правая кнопка мыши
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.write()

# списко точек
list_point=[(470,249)]
list_connection=[]
# максимальное количество перекрестков
max_count_points = 60
# статус режима вывода отладочной информации
debug = True
# поля отображения поля
x_min = 5
x_max = 1050
y_min = 0
y_max = 995
# режим нажатия кнопки мыши
mouse_rejim = 0    # 0 ничего,  10 режим добавляения точки,  20 режим соединения

class MainApp(App):
    def build(self):
        #создаем основную раскладку
        self.layout_main = BoxLayout(padding=3)  # Отступ padding между лейаутом


        #добавлялем изображение
        img = Image(source='../map_forest.png',
                    #size_hint=(1, 1),
                    #pos_hint={'center_x': .5, 'center_y': .5},
                    #pos=(100, 110)
                    )
        img.bind(on_touch_up = self.on_touch_up)
        self.layout_main.add_widget(img)


        # отображаем точки из списка
        for x,y in list_point:
            with self.layout_main.canvas:
                Color(1, 0, 1, 1)
                self.rect = Rectangle(pos=(x_min + x - 5, y_max - y - 5),
                                      size=(10, 10))


        #создаем среднюю раскладку для отображения точек
        count_points = len(list_point)
        self.layout_midle = GridLayout(cols=1,
                                  rows=max_count_points,
                                  padding=3,
                                  size_hint=( None, None),
                                  size= (190, 1000))
        for i in range(count_points):
            self.layout_midle.add_widget(Label(text='point '+str(list_point[i])))

        self.layout_main.add_widget(self.layout_midle)


        #создаем правую раскладку
        layout_right = BoxLayout(padding=3,
                                 orientation="vertical",
                                 size_hint=( None, None),
                                 size= (150, 1000))
        btn_add_point = Button(text="Add point",
                               size_hint=(1, 1),
                               size=(150, 50),
                               background_color=[0,1,0,1]) #rgba
        btn_add_point.bind(on_press=self.add_point)
        layout_right.add_widget(btn_add_point)

        btn_add_connection = Button(text="Add connection",
                                    size_hint=(1, 1),
                                    size=(150, 50),
                                    background_color=[0,1,0,1])
        btn_add_connection.bind(on_press=self.add_connection)
        layout_right.add_widget(btn_add_connection)

        btn_delete = Button(text="Delete",
                            size_hint=(1, 1),
                            size=(150, 50),
                            background_color=[0,1,0,1])
        btn_delete.bind(on_press=self.delete)
        layout_right.add_widget(btn_delete)


        btn_export = Button(text="Export",
                            size_hint=(1, None),
                            size=(150, 50),
                            background_color=[0,1,0,1])
        btn_export.bind(on_press=self.export_file)
        layout_right.add_widget(btn_export)


        self.layout_main.add_widget(layout_right)
        return self.layout_main


    def export_file(self, instance):
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку export')

    def add_point(self, instance):
        global mouse_rejim
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку add_point')
        if mouse_rejim == 0: mouse_rejim = 10

    def add_connection(self, instance):
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку add_connection')

    def delete(self, instance):
        # функция экспорта кортежей
        if debug: print('Вы нажали на кнопку delete')

    # обработчик нажатия кнопки мыши
    def on_touch_up(self, touch,p):
        global mouse_rejim
        x,y = p.pos
        x = int(x) - x_min
        y = y_max - int(y)
        if 0 < x < x_max and y_min < y < y_max and max_count_points > len(list_point) and mouse_rejim!=0:

            if debug: print("coords x="+str(x)+ ' y='+str(y) )

            if mouse_rejim == 10:
                list_point.append((x,y))

                lb = Label(text='point ('+str(x)+','+str(y)+')')
                self.layout_midle.add_widget(lb)

                with self.layout_main.canvas:
                    Color(1, 0, 1, 1)  #
                    self.rect = Rectangle(pos=(x_min+x-5,y_max-y-5),
                                          size=(10,10))
                mouse_rejim = 0



if __name__ == '__main__':
    app = MainApp()
    app.run()