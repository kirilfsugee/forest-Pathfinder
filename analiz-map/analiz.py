from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class MainApp(App):
    def build(self):
        #создаем основную раскладку
        layout_main = BoxLayout(padding=3)  # Отступ padding между лейаутом

        #добавлялем изображение
        img = Image(source='../map_forest.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x': .5, 'center_y': .5})
        layout_main.add_widget(img)

        #создаем правую раскладку
        layout_right = BoxLayout(padding=3, orientation="vertical" )

        btn_add_point = Button(text="Add point",size_hint=(1, 1), size=(150, 50),
                     background_color=[0,1,0,1]
                     )
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

        # label = Label(text='Hello from Kivy',
        #               size_hint=(.5, .5),
        #               pos_hint={'center_x': .5, 'center_y': .5})
        #
        # return label


if __name__ == '__main__':
    app = MainApp()
    app.run()