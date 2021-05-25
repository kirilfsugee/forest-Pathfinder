from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# задаем размер окна приложения
Config.set('graphics', 'width', '1400')
Config.set('graphics', 'height', '800')
# отключам мульт тач, чтоб работала правая кнопка мыши
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.write()

# списко точек
list_point=[]


class MainApp(App):
    def build(self):
        #создаем основную раскладку
        layout_main = BoxLayout(padding=3)  # Отступ padding между лейаутом


        #добавлялем изображение
        img = Image(source='../map_forest.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x': .5, 'center_y': .5})
        img.bind(on_touch_up = self.on_touch_up)
        layout_main.add_widget(img)



        #создаем среднюю раскладку для отображения точек
        count_points = len(list_point)
        layout_midle = GridLayout(cols=1, rows=count_points, padding=3,  size_hint=( None, None),
                                size= (150, 800))
        for i in range(count_points):
            layout_midle.add_widget(Label(text='point '+str(list_point[i])))

        layout_main.add_widget(layout_midle)


        #создаем правую раскладку
        layout_right = BoxLayout(padding=3, orientation="vertical", size_hint=( None, None),
                                size= (150, 800))
        btn_add_point = Button(text="Add point",size_hint=(1, 1), size=(150, 50),
                     background_color=[0,1,0,1])
        btn_add_point.bind(on_press=self.add_point)
        layout_right.add_widget(btn_add_point)

        btn_add_connection = Button(text="Add connection",size_hint=(1, 1), size=(150, 50),
                     background_color=[0,1,0,1]
                     )
        btn_add_connection.bind(on_press=self.add_connection)
        layout_right.add_widget(btn_add_connection)

        btn_delete = Button(text="Delete",size_hint=(1, 1), size=(150, 50),
                     background_color=[0,1,0,1]
                     )
        btn_delete.bind(on_press=self.delete)
        layout_right.add_widget(btn_delete)


        btn_export = Button(text="Export",size_hint=(1, None), size=(150, 50),
                     background_color=[0,1,0,1]
                     )
        btn_export.bind(on_press=self.export_file)
        layout_right.add_widget(btn_export)


        layout_main.add_widget(layout_right)
        return layout_main


    def export_file(self, instance):
        # функция экспорта кортежей
        print('Вы нажали на кнопку export')

    def add_point(self, instance):
        # функция экспорта кортежей
        print('Вы нажали на кнопку add_point')

    def add_connection(self, instance):
        # функция экспорта кортежей
        print('Вы нажали на кнопку add_connection')

    def delete(self, instance):
        # функция экспорта кортежей
        print('Вы нажали на кнопку delete')

    # обработчик нажатия кнопки мыши
    def on_touch_up(self, touch,p):
        x_min = 130
        x_max = 940
        y_min = 9
        y_max = 800
        x,y = p.pos
        x = int(x)
        y = y_max - int(y)
        if x_min < x < x_max and y_min < y < y_max:
            print("coords x="+str(x)+ ' y='+str(y) )
            list_point.append((x,y))



if __name__ == '__main__':
    app = MainApp()
    app.run()