from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import (Color,Ellipse,Rectangle,Line)


screen_helper = """
ScreenManager:
    MenuScreen:

    class9Screen:

    class10Screen:

    teory10Screen:

    puzzles10Screen:
    puzzles10_2Screen:
    puzzles10_3Screen:

    teory10_2Screen:
    teory10_3Screen:
    teory10_4Screen:
    teory10_5Screen:

    teory9Screen:
    teory9_2Screen:
    teory9_3Screen:

    puzzles9Screen:
    puzzles9_3Screen:

    theme9_1Screen:
        id: theme9_1
    theme9_2Screen:
        id: theme9_2
    theme9_3Screen:
        id: theme9_3

    theme10_1Screen:
        id: theme10_1        
    theme10_2Screen:
        id:theme10_2
    theme10_3Screen:
        id: theme10_3

    puzzle9_1Screen:
    puzzle9_2Screen:
    puzzle9_3Screen:
    puzzle9_4Screen:
    puzzle9_5Screen:
    puzzle9_6Screen:
    puzzle9_7Screen:
    puzzle9_8Screen:
    puzzle9_9Screen:
    puzzle9_10Screen:
    puzzle9_11Screen:
    puzzle9_12Screen:


    puzzle9_3_1Screen:
        id: puzzle9_3_1
    puzzle9_3_2Screen:
        id: puzzle9_3_2
    puzzle9_3_3Screen:
        id: puzzle9_3_3
    puzzle9_3_4Screen:
        id: puzzle9_3_4




    puzzle10_1Screen:
    puzzle10_2Screen:
    puzzle10_3Screen:
    puzzle10_4Screen:
    puzzle10_5Screen:
    puzzle10_6Screen:
    puzzle10_7Screen:
    puzzle10_8Screen:
    puzzle10_9Screen:
    puzzle10_10Screen:
    puzzle10_11Screen:
    puzzle10_12Screen:

    puzzle10_2_1Screen:
        id: puzzle10_2_1
    puzzle10_2_2Screen:
        id: puzzle10_2_2
    puzzle10_2_3Screen:
        id: puzzle10_2_3
    puzzle10_2_4Screen:
        id: puzzle10_2_4
    puzzle10_2_5Screen:
        id: puzzle10_2_5
    puzzle10_2_6Screen:
        id: puzzle10_2_6
    puzzle10_2_7Screen:
        id: puzzle10_2_7
    puzzle10_2_8Screen:
        id: puzzle10_2_8

    puzzle10_3_1Screen:
    puzzle10_3_2Screen:
    puzzle10_3_3Screen:
    puzzle10_3_4Screen:
    puzzle10_3_5Screen:
    puzzle10_3_6Screen:

    tasks9Screen:
        id: tasks9
    tasks9_2Screen:
        id: tasks9_2
    tasks9_3Screen:
        id: tasks9_3


    tasks10Screen:
        id: tasks10
    tasks10_2Screen:
        id: tasks10_2
    tasks10_3Screen:
        id: tasks10_3


    task10_1Screen:
        id: task10_1_1
    task10_2Screen:
        id: task10_2_1
    task10_3Screen:
        id: task10_3_1
    task10_4Screen:
        id: task10_4_1
    task10_5Screen:
        id: task10_5_1
    task10_6Screen:
        id: task10_6_1
    task10_7Screen:
        id: task10_7_1
    task10_8Screen:
        id: task10_8_1
    task10_9Screen:
        id: task10_9_1

    task10_2_1Screen:
        id: task10_1_2
    task10_2_2Screen:
        id: task10_2_2
    task10_2_3Screen:
        id: task10_3_2
    task10_2_4Screen:
        id: task10_4_2
    task10_2_5Screen:
        id: task10_5_2
    task10_2_6Screen:
        id: task10_6_2
    task10_2_7Screen:
        id: task10_7_2
    task10_2_8Screen:
        id: task10_8_2
    task10_2_9Screen:
        id: task10_9_2      

    task10_3_1Screen:
        id: task10_1_3
    task10_3_2Screen:
        id: task10_2_3
    task10_3_3Screen:
        id: task10_3_3
    task10_3_4Screen:
        id: task10_4_3
    task10_3_5Screen:
        id: task10_5_3
    task10_3_6Screen:
        id: task10_6_3
    task10_3_7Screen:
        id: task10_7_3
    task10_3_8Screen:
        id: task10_8_3
    task10_3_9Screen:
        id: task10_9_3

#####################################
    task9_1Screen:
        id: task9_1_1
    task9_2Screen:
        id: task9_2_1
    task9_3Screen:
        id: task9_3_1
    task9_4Screen:
        id: task9_4_1
    task9_5Screen:
        id: task9_5_1
    task9_6Screen:
        id: task9_6_1
    task9_7Screen:
        id: task9_7_1
    task9_8Screen:
        id: task9_8_1
    task9_9Screen:
        id: task9_9_1

    task9_2_1Screen:
        id: task9_1_2
    task9_2_2Screen:
        id: task9_2_2
    task9_2_3Screen:
        id: task9_3_2
    task9_2_4Screen:
        id: task9_4_2
    task9_2_5Screen:
        id: task9_5_2
    task9_2_6Screen:
        id: task9_6_2
    task9_2_7Screen:
        id: task9_7_2
    task9_2_8Screen:
        id: task9_8_2
    task9_2_9Screen:
        id: task9_9_2

    task9_3_1Screen:
        id: task9_1_3
    task9_3_2Screen:
        id: task9_2_3
    task9_3_3Screen:
        id: task9_3_3
    task9_3_4Screen:
        id: task9_4_3
    task9_3_5Screen:
        id: task9_5_3
    task9_3_6Screen:
        id: task9_6_3
    task9_3_7Screen:
        id: task9_7_3
    task9_3_8Screen:
        id: task9_8_3
    task9_3_9Screen:
        id: task9_9_3

########################################################################################################################################
########################################################################################################################################
<puzzles9_2Screen>
    name: 'puzzle9_2'

<MenuScreen>:
    name: 'menu'
    Design_menu
    MDLabel:
        text: "главное меню"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    MDLabel:
        text: "Easy"
        font_style: 'H1'
        font_size: '30'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.8}
    MDLabel:
        text: "Trigonometry"
        font_style: 'H1'
        font_size: '30'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.73}
    MDRectangleFlatButton:
        text: '9'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'class9'
    MDRectangleFlatButton:
        text: '10'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'class10'
    
<class9Screen>:
    name: 'class9'
    Design_class
    MDLabel:
        text: '9 класс'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: "меню>9класс"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'таблица тригонометрических функций'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'theme9_1'
    MDRectangleFlatButton:
        text: 'Решение треугольников'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'theme9_2'
    MDRectangleFlatButton:
        text: 'Тригонометрические теоремы'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'theme9_3'

############################
<class10Screen>:
    name: 'class10'
    MDLabel:
        text: '10 класс'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: "меню>10класс"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'формулы приведения'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'theme10_1'
    MDRectangleFlatButton:
        text: 'формулы двойного и половинного углов'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'theme10_2'
    MDRectangleFlatButton:
        text: 'формулы сложения'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'theme10_3'

###########################

<theme9_1Screen>:
    name: 'theme9_1'
    Design_themes
    MDLabel:
        text: 'таблица тригонометрических функций'
        halign: 'center'

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class9'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'teory9'
    MDRectangleFlatButton:
        text: 'Пазл'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        id: button9_1tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks9'
        
###############################

<theme9_2Screen>:
    name: 'theme9_2'
    MDLabel:
        text: 'Решение треугольников'
        halign: 'center'

    MDLabel:
        text: "меню>9класс>Решение треугольников"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class9'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'teory9_2'
    MDRectangleFlatButton:
        id: button9_2tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks9_2'
        
##############################

<theme9_3Screen>:
    name: 'theme9_3'
    MDLabel:
        text: 'тригонометрические теоремы'
        halign: 'center'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class9'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'teory9_3'
    MDRectangleFlatButton:
        text: 'Пазл'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'puzzles9_3'
    MDRectangleFlatButton:
        id: button9_3tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks9_3'

#####################################

<theme10_1Screen>:
    name: 'theme10_1'
    MDLabel:
        text: 'формулы приведения'
        halign: 'center'

    MDLabel:
        text: "меню>10класс>формулы приведения"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'teory10'
    MDRectangleFlatButton:
        text: 'Пазл'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        id: button10_1tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks10'
        
###############################

<theme10_2Screen>:
    name: 'theme10_2'
    MDLabel:
        text: 'формулы двойного и половинного углов'
        halign: 'center'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'teory10_2'
    MDRectangleFlatButton:
        text: 'Пазл'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        id: button10_2tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks10_2'
        
##############################

<theme10_3Screen>:
    name: 'theme10_3'
    MDLabel:
        text: 'формулы сложения'
        halign: 'center'

    MDLabel:
        text: "меню>10класс>формулы сложения"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'
    MDRectangleFlatButton:
        text: 'Теория'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'teory10_3'
    MDRectangleFlatButton:
        text: 'Пазл'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        id: button10_3tasks
        text: 'Задания'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'tasks10_3'
        
########################
<teory9Screen>:
    name: 'teory9'
    Design_teory
    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDLabel:
        text: '\\nОпределение' +\
                '\\n' +\
                  '\\nСинусом острого угла прямоугольного треугольника называется' +\
                    '\\nотношение противолежащего этому углу катета к гипотенузе.' +\
                        '\\n' +\
                            '\\nКосинусом острого угла прямоугольного треугольника' +\
                                '\\nназывается отношение прилежащего к этому углу катета к гипотенузе.' +\
                                    '\\n' +\
                                        '\\nТангенсом острого угла прямоугольного треугольника' +\
                                            '\\nназывается отношение противолежащего этому углу катета к прилежащему катету.' +\
                                                '\\n' +\
                                                    '\\nКотангенсом острого угла прямоугольного треугольника' +\
                                                        '\\nназывается отношение прилежащего этому углу катета к противолежащего катету.'
                  
        halign: 'center'
        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_1'     

######################

<teory9_2Screen>:
    name: 'teory9_2'


    MDLabel:
        text: "меню>9класс>Решение треугольников>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_2'
    Image:
        source:'images/teory9_2.png'
        size_hint:(0.8, 0.8)
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}        

###################

<teory9_3Screen>:
    name: 'teory9_3'
    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    Image:
        source:'images/sinus.png'
        size_hint:(0.7, 0.7)
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}    
    Image:
        source:'images/cosinus.png'
        size_hint:(0.7, 0.7)
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}    
    Image:
        source:'images/main.png'
        size_hint:(0.7, 0.7)
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}    
    Image:
        source:'images/TgCtg.png'
        size_hint:(0.7, 0.7)
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}    
        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_3'     

##########################

<teory10Screen>:
    name: 'teory10'

    MDLabel:
        text: "меню>10класс>Формулы приведения>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}


    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'

    Image:
        source:'images/teory10_11.png'
        size_hint:(1, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}  

    Image:
        source:'images/teory10_12.png'
        size_hint:(1, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.4} 

    Image:
        source:'images/teory10_13.png'
        size_hint:(1, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.6} 

<teory10_2Screen>:
    name: 'teory10_2'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_2'

    Image:
        source:'images/teory10_2.png'
        size_hint:(1, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}      

###################

<teory10_3Screen>:
    name: 'teory10_3'


    MDLabel:
        text: "меню>10класс>формулы сложения>теоретическая часть"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_3'    

    Image:
        source:'images/teory10_3.png'
        size_hint:(1, 1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}   


<puzzles9Screen>:
    name: 'puzzles9'
    Design_puzzles
    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_1'
    MDRectangleFlatButton:
        text: 'sin22°'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_1' 
    MDRectangleFlatButton:
        text: 'sin45°'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_2' 
    MDRectangleFlatButton:
        text: 'sin60°'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_3' 
    MDRectangleFlatButton:
        text: 'cos22°'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'puzzle9_4' 
    MDRectangleFlatButton:
        text: 'cos45°'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'puzzle9_5' 
    MDRectangleFlatButton:
        text: 'cos60°'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'puzzle9_6' 
    MDRectangleFlatButton:
        text: 'tg22°'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'puzzle9_7' 
    MDRectangleFlatButton:
        text: 'tg45°'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'puzzle9_8' 
    MDRectangleFlatButton:
        text: 'tg60°'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'puzzle9_9' 
    MDRectangleFlatButton:
        text: 'ctg22°'
        pos_hint: {'center_x':0.2,'center_y':0.2}
        on_press: root.manager.current = 'puzzle9_10' 
    MDRectangleFlatButton:
        text: 'ctg45°'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'puzzle9_11' 
    MDRectangleFlatButton:
        text: 'ctg60°'
        pos_hint: {'center_x':0.8,'center_y':0.2}
        on_press: root.manager.current = 'puzzle9_12'   

#########################

<puzzles9_3Screen>:
    name: 'puzzles9_3'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>пазлы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_3'
    MDRectangleFlatButton:
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_3_1' 
    MDRectangleFlatButton:
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_3_2' 
    MDRectangleFlatButton:
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'puzzle9_3_3' 
    MDRectangleFlatButton:
        text: '4'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'puzzle9_3_4' 

###########
<puzzles10Screen>:
    name: 'puzzles10'

    MDLabel:
        text: "меню>10класс>Формулы приведения>пазлы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'
    MDRectangleFlatButton:
        text: 'sinα'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_1' 
    MDRectangleFlatButton:
        text: '-sinα'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_2' 
    MDRectangleFlatButton:
        text: '-cosα'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_3' 
    MDRectangleFlatButton:
        text: '-cosα'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_4' 
    MDRectangleFlatButton:
        text: 'cosα'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_5' 
    MDRectangleFlatButton:
        text: '-sinα'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_6' 
    MDRectangleFlatButton:
        text: '-cosα'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'puzzle10_7' 
    MDRectangleFlatButton:
        text: 'sinα'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'puzzle10_8' 
    MDRectangleFlatButton:
        text: 'ctgα'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'puzzle10_9' 
    MDRectangleFlatButton:
        text: 'tgα'
        pos_hint: {'center_x':0.2,'center_y':0.2}
        on_press: root.manager.current = 'puzzle10_10' 
    MDRectangleFlatButton:
        text: '-ctgα'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'puzzle10_11' 
    MDRectangleFlatButton:
        text: '-tgα'
        pos_hint: {'center_x':0.8,'center_y':0.2}
        on_press: root.manager.current = 'puzzle10_12'  

###############

<puzzles10_2Screen>:
    name: 'puzzles10_2'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>пазлы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_2'
    MDRectangleFlatButton:
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_2_1' 
    MDRectangleFlatButton:
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_2_2' 
    MDRectangleFlatButton:
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_2_3' 
    MDRectangleFlatButton:
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_2_4' 
    MDRectangleFlatButton:
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_2_5' 
    MDRectangleFlatButton:
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_2_6'
    MDRectangleFlatButton:
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'puzzle10_2_7'
    MDRectangleFlatButton:
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'puzzle10_2_8'

    


###########

<puzzles10_3Screen>:
    name: 'puzzles10_3'

    MDLabel:
        text: "меню>10класс>формулы сложения>пазлы"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_3'
    MDRectangleFlatButton:
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_3_1' 
    MDRectangleFlatButton:
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_3_2' 
    MDRectangleFlatButton:
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'puzzle10_3_3' 
    MDRectangleFlatButton:
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_3_4' 
    MDRectangleFlatButton:
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_3_5' 
    MDRectangleFlatButton:
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'puzzle10_3_6'
#####################################

###################################################################
<tasks9Screen>:
    name: 'tasks9'
    Design_tasks
    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_1'
    MDRectangleFlatButton:
        id: button9_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task9_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task9_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task9_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task9_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task9_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task9_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task9_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task9_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_9task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task9_9' 
        disabled: True

##############

<tasks9_2Screen>:
    name: 'tasks9_2'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_2'
    MDRectangleFlatButton:
        id: button9_2_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task9_2_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task9_2_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task9_2_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task9_2_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task9_2_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task9_2_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task9_2_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task9_2_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_2_9task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task9_2_9' 
        disabled: True

#################

<tasks9_3Screen>:
    name: 'tasks9_3'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme9_3'
    MDRectangleFlatButton:
        id: button9_3_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task9_3_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task9_3_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task9_3_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task9_3_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task9_3_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task9_3_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task9_3_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task9_3_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button9_3_9task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task9_3_9' 
        disabled: True

##########################

<tasks10Screen>:
    name: 'tasks10'

    MDLabel:
        text: "меню>10класс>Формулы приведения>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'class10'
    MDRectangleFlatButton:
        id: button10_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task10_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task10_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task10_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task10_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task10_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task10_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task10_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task10_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_9task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task10_9' 
        disabled: True
    
<tasks10_2Screen>:
    name: 'tasks10_2'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_2'
    MDRectangleFlatButton:
        id: button10_2_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task10_2_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task10_2_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task10_2_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task10_2_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task10_2_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task10_2_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task10_2_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task10_2_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_2_9task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task10_2_9' 
        disabled: True

#################

<tasks10_3Screen>:
    name: 'tasks10_3'

    MDLabel:
        text: "меню>10класс>формулы сложения>задания"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'theme10_3'
    MDRectangleFlatButton:
        id: button10_3_1task
        md_bg_color: "white"
        text: '1'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'task10_3_1' 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_2task
        text: '2'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'task10_3_2'
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_3task
        text: '3'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'task10_3_3' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_4task
        text: '4'
        pos_hint: {'center_x':0.2,'center_y':0.6}
        on_press: root.manager.current = 'task10_3_4' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_5task
        text: '5'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'task10_3_5' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_6task
        text: '6'
        pos_hint: {'center_x':0.8,'center_y':0.6}
        on_press: root.manager.current = 'task10_3_6' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_7task
        text: '7'
        pos_hint: {'center_x':0.2,'center_y':0.4}
        on_press: root.manager.current = 'task10_3_7'
        disabled: True 
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_8task
        text: '8'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'task10_3_8' 
        disabled: True
    MDRectangleFlatButton:
        md_bg_color: "white"
        id: button10_3_10task
        text: '9'
        pos_hint: {'center_x':0.8,'center_y':0.4}
        on_press: root.manager.current = 'task10_3_9' 
        disabled: True
################################

<puzzle9_1Screen>:
    name: 'puzzle9_1'
    Puzzle9_1Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_2'

<puzzle9_2Screen>:
    name: 'puzzle9_2'

    Puzzle9_2Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_3'

<puzzle9_3Screen>:
    name: 'puzzle9_3'

    Puzzle9_3Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_4'

<puzzle9_4Screen>:
    name: 'puzzle9_4'

    Puzzle9_4Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_5'

<puzzle9_5Screen>:
    name: 'puzzle9_5'

    Puzzle9_5Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_6'

<puzzle9_6Screen>:
    name: 'puzzle9_6'

    Puzzle9_6Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_7'

<puzzle9_7Screen>:
    name: 'puzzle9_7'

    Puzzle9_7Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_8'

<puzzle9_8Screen>:
    name: 'puzzle9_8'

    Puzzle9_8Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_9'

<puzzle9_9Screen>:
    name: 'puzzle9_9'

    Puzzle9_9Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_10'

<puzzle9_10Screen>:
    name: 'puzzle9_10'

    Puzzle9_10Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №10"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_11'

<puzzle9_11Screen>:
    name: 'puzzle9_11'

    Puzzle9_11Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №11"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_12'

<puzzle9_12Screen>:
    name: 'puzzle9_12'

    Puzzle9_12Widget

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>пазлы>пазл №12"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9'

#####################
<puzzle9_3_1Screen>:
    name: 'puzzle9_3_1'
    Puzzle9_3_1Widget:
        id: widget9_3_1

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>пазлы>пазл №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_3_2'

    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget9_3_1.check_collision()


#####################
<puzzle9_3_2Screen>:
    name: 'puzzle9_3_2'
    Puzzle9_3_2Widget:
        id: widget9_3_2

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>пазлы>пазл №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_3_3'
    
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget9_3_2.check_collision()

#####################
<puzzle9_3_3Screen>:
    name: 'puzzle9_3_3'
    Puzzle9_3_3Widget:
        id: widget9_3_3

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>пазлы>пазл №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle9_3_4'
    
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget9_3_3.check_collision()

#####################
<puzzle9_3_4Screen>:
    name: 'puzzle9_3_4'
    Puzzle9_3_4Widget:
        id: widget9_3_4

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>пазлы>пазл №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles9_3'
    
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget9_3_4.check_collision()

######################################################################

<puzzle10_1Screen>:
    name: 'puzzle10_1'

    Puzzle10_1Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2'

<puzzle10_2Screen>:
    name: 'puzzle10_2'


    Puzzle10_2Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3'

<puzzle10_3Screen>:
    name: 'puzzle10_3'

    Puzzle10_3Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_4'

<puzzle10_4Screen>:
    name: 'puzzle10_4'

    Puzzle10_4Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_5'

<puzzle10_5Screen>:
    name: 'puzzle10_5'

    Puzzle10_5Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_6'

<puzzle10_6Screen>:
    name: 'puzzle10_6'

    Puzzle10_6Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_7'

<puzzle10_7Screen>:
    name: 'puzzle10_7'

    Puzzle10_7Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_8'

<puzzle10_8Screen>:
    name: 'puzzle10_8'

    Puzzle10_8Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_9'

<puzzle10_9Screen>:
    name: 'puzzle10_9'

    Puzzle10_9Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_10'

<puzzle10_10Screen>:
    name: 'puzzle10_10'

    Puzzle10_10Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №10"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_11'

<puzzle10_11Screen>:
    name: 'puzzle10_11'
    Puzzle10_11Widget

    MDLabel:
        text: "меню>10класс>формулы приведения>пазлы>пазл №11"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_12'

<puzzle10_12Screen>:
    name: 'puzzle10_12'

    MDLabel:
        text: "меню>10класс>таблица тригонометрических функций>пазлы>пазл №12"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    Puzzle10_12Widget
    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10'

###################




###################################################################

<puzzle10_2_1Screen>:
    name: 'puzzle10_2_1'
    Puzzle10_2_1Widget:
        id: widget10_2_1

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_2'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_1.check_collision()

#####################

<puzzle10_2_2Screen>:
    name: 'puzzle10_2_2'
    Puzzle10_2_2Widget:
        id: widget10_2_2

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_3'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_2.check_collision()

<puzzle10_2_3Screen>:
    name: 'puzzle10_2_3'
    Puzzle10_2_3Widget:
        id: widget10_2_3

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_4'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_3.check_collision()

<puzzle10_2_4Screen>:
    name: 'puzzle10_2_4'
    Puzzle10_2_4Widget:
        id: widget10_2_4

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_5'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_4.check_collision()

<puzzle10_2_5Screen>:
    name: 'puzzle10_2_5'
    Puzzle10_2_5Widget:
        id: widget10_2_5

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_6'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_5.check_collision()

<puzzle10_2_6Screen>:
    name: 'puzzle10_2_6'
    Puzzle10_2_6Widget:
        id: widget10_2_6

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_7'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_6.check_collision()

<puzzle10_2_7Screen>:
    name: 'puzzle10_2_7'
    Puzzle10_2_7Widget:
        id: widget10_2_7

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_2_8'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_7.check_collision()

<puzzle10_2_8Screen>:
    name: 'puzzle10_2_8'
    Puzzle10_2_8Widget:
        id: widget10_2_8

    MDLabel:
        text: "меню>9класс>формулы двойного и половинного углов>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_2'
    MDRectangleFlatButton:
        text: 'проверить'
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: widget10_2_8.check_collision()
###############################################################################

<puzzle10_3_1Screen>:
    name: 'puzzle10_3_1'
    Puzzle10_3_1Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3_2'

#####################

<puzzle10_3_2Screen>:
    name: 'puzzle10_3_2'
    Puzzle10_3_2Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3_3'

<puzzle10_3_3Screen>:
    name: 'puzzle10_3_3'
    Puzzle10_3_3Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3_4'

<puzzle10_3_4Screen>:
    name: 'puzzle10_3_4'
    Puzzle10_3_4Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3_5'

<puzzle10_3_5Screen>:
    name: 'puzzle10_3_5'
    Puzzle10_3_5Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'
    MDRectangleFlatButton:
        text: 'далее'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'puzzle10_3_6'

<puzzle10_3_6Screen>:
    name: 'puzzle10_3_6'
    Puzzle10_3_6Widget

    MDLabel:
        text: "меню>9класс>формулы сложения>пазлы>пазл №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'меню'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'puzzles10_3'


######################################################################################

<task10_1Screen>
    name: 'task10_1'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_1
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_1()

    MDTextField:
        id: text_field_error10_12
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_12()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Решите: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_1()
    
    MDRectangleFlatButton:
        id: next10_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_1.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_2Screen>
    name: 'task10_2'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_2
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_2()

    MDTextField:
        id: text_field_error10_22
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_22()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2()
    
    MDRectangleFlatButton:
        id: next10_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_2.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

############

<task10_3Screen>
    name: 'task10_3'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_3
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_3()

    MDTextField:
        id: text_field_error10_32
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_32()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3()
    
    MDRectangleFlatButton:
        id: next10_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_4'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_3.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###############

<task10_4Screen>
    name: 'task10_4'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_4
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_4()

    MDTextField:
        id: text_field_error10_42
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_42()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_4()
    
    MDRectangleFlatButton:
        id: next10_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_5'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_4.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

######################

<task10_5Screen>
    name: 'task10_5'

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_5
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_5()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_5()
    
    MDRectangleFlatButton:
        id: next10_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_6'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_5.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###############################

<task10_6Screen>
    name: 'task10_6'

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_6
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_6()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_6()
    
    MDRectangleFlatButton:
        id: next10_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_7'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_6.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_7Screen>
    name: 'task10_7'

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_7
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_7()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_7()
    
    MDRectangleFlatButton:
        id: next10_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_8'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_7.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

####################

<task10_8Screen>
    name: 'task10_8'

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_8
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_8()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_8()
    
    MDRectangleFlatButton:
        id: next10_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_9'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_8.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

#################

<task10_9Screen>
    name: 'task10_9'

    MDLabel:
        text: "меню>10класс>формулы приведения>задание>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10'

    MDTextField:
        id: text_field_error10_9
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_9()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_9()
    
    MDRectangleFlatButton:
        id: next10_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks10'
        disabled: True

    Image:
        id: image10_1
        source:'images/task10_1_9.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

############################################################

<task10_2_1Screen>
    name: 'task10_2_1'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_1
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_2_1()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_1()
    
    MDRectangleFlatButton:
        id: next10_2_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_2'
        disabled: True

    Image:
        source:'images/task10_2_1.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_2_2Screen>
    name: 'task10_2_2'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_2
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_2_2()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_2()
    
    MDRectangleFlatButton:
        id: next10_2_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_3'
        disabled: True

    Image:
        source:'images/task10_2_2.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

############

<task10_2_3Screen>
    name: 'task10_2_3'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_3
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_2_3()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_3()
    
    MDRectangleFlatButton:
        id: next10_2_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_4'
        disabled: True

    Image:
        source:'images/task10_2_3.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###############

<task10_2_4Screen>
    name: 'task10_2_4'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_4
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_2_4()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_4()
    
    MDRectangleFlatButton:
        id: next10_2_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_5'
        disabled: True

    Image:
        source:'images/task10_2_4.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

######################

<task10_2_5Screen>
    name: 'task10_2_5'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_5
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_2_5()

    MDTextField:
        id: text_field_error10_2_52
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_2_5()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_5()
    
    MDRectangleFlatButton:
        id: next10_2_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_6'
        disabled: True

    Image:
        source:'images/task10_2_5.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###############################

<task10_2_6Screen>
    name: 'task10_2_6'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_6
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .2
        on_text_validate: app.set_error_message10_2_6()

    MDTextField:
        id: text_field_error10_2_62
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_2_62()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_6()
    
    MDRectangleFlatButton:
        id: next10_2_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_7'
        disabled: True

    Image:
        source:'images/task10_2_6.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_2_7Screen>
    name: 'task10_2_7'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_7
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .2
        on_text_validate: app.set_error_message10_2_7()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_7()
    
    MDRectangleFlatButton:
        id: next10_2_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_8'
        disabled: True

    Image:
        source:'images/task10_2_7.png'
        size_hint:(0.6, 0.6)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

####################

<task10_2_8Screen>
    name: 'task10_2_8'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_8
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .2
        on_text_validate: app.set_error_message10_2_8()

    MDTextField:
        id: text_field_error10_2_82
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_2_82()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_8()
    
    MDRectangleFlatButton:
        id: next10_2_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_2_9'
        disabled: True

    Image:
        source:'images/task10_2_8.png'
        size_hint:(0.45, 0.45)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

#################

<task10_2_9Screen>
    name: 'task10_2_9'

    MDLabel:
        text: "меню>10класс>формулы двойного и половинного углов>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_2'

    MDTextField:
        id: text_field_error10_2_9
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_2_9()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_2_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_2_9()
    
    MDRectangleFlatButton:
        id: next10_2_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks10_2'
        disabled: True

    Image:
        source:'images/task10_2_9.png'
        size_hint:(0.55, 0.55)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}
##################################################################

<task10_3_1Screen>
    name: 'task10_3_1'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_1
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_1()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}

    MDRectangleFlatButton:
        id: submit10_3_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_1()
    
    MDRectangleFlatButton:
        id: next10_3_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_2'
        disabled: True

    Image:
        source:'images/task10_3_1.png'
        size_hint:(0.55, 0.55)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_3_2Screen>
    name: 'task10_3_2'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_2
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_2()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_2()
    
    MDRectangleFlatButton:
        id: next10_3_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_3'
        disabled: True

    Image:
        source:'images/task10_3_2.png'
        size_hint:(0.65, 0.65)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

############

<task10_3_3Screen>
    name: 'task10_3_3'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_3
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_3()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_3()
    
    MDRectangleFlatButton:
        id: next10_3_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_4'
        disabled: True

    Image:
        source:'images/task10_3_3.png'
        size_hint:(0.65, 0.65)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}  

###############

<task10_3_4Screen>
    name: 'task10_3_4'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы сложения>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_4
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .2
        on_text_validate: app.set_error_message10_3_4()

    MDTextField:
        id: text_field_error10_3_42
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_3_42()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_4()
    
    MDRectangleFlatButton:
        id: next10_3_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_5'
        disabled: True

    Image:
        source:'images/task10_3_4.png'
        size_hint:(0.55, 0.55)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

######################

<task10_3_5Screen>
    name: 'task10_3_5'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_5
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_5()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_5()
    
    MDRectangleFlatButton:
        id: next10_3_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_6'
        disabled: True

    Image:
        source:'images/task10_3_5.png'
        size_hint:(0.55, 0.55)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###############################

<task10_3_6Screen>
    name: 'task10_3_6'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_6
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_6()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_6()
    
    MDRectangleFlatButton:
        id: next10_3_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_7'
        disabled: True

    Image:
        source:'images/task10_3_6.png'
        size_hint:(0.55, 0.55)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

###################

<task10_3_7Screen>
    name: 'task10_3_7'
    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}
    MDLabel:
        text: "меню>10класс>формулы сложения>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_7
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .2
        on_text_validate: app.set_error_message10_3_7()

    MDTextField:
        id: text_field_error10_3_72
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message10_3_72()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_7()
    
    MDRectangleFlatButton:
        id: next10_3_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_8'
        disabled: True

    Image:
        source:'images/task10_3_7.png'
        size_hint:(0.65, 0.65)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

####################

<task10_3_8Screen>
    name: 'task10_3_8'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_8
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_8()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.12, 'center_y': 0.25}

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_8()
    
    MDRectangleFlatButton:
        id: next10_3_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task10_3_9'
        disabled: True

    Image:
        source:'images/task10_3_8.png'
        size_hint:(0.65, 0.65)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}

#################

<task10_3_9Screen>
    name: 'task10_3_9'

    MDLabel:
        text: "меню>10класс>формулы сложения>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks10_3'

    MDTextField:
        id: text_field_error10_3_9
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message10_3_9()

    MDLabel:
        text: "Упростите выражение: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit10_3_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer10_3_9()
    
    MDRectangleFlatButton:
        id: next10_3_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks10_3'
        disabled: True

    Image:
        source:'images/task10_3_9.png'
        size_hint:(0.65, 0.65)
        pos_hint:{'center_x': 0.4, 'center_y': 0.75}


#####################################################
#####################################################


<task9_1Screen>
    name: 'task9_1'
    Design_task
    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95} 

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_1
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_1()

    MDLabel:
        text: "Вычислите: tg22° * Ctg22°"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_1()
    
    MDRectangleFlatButton:
        id: next9_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2'
        disabled: True



###################

<task9_2Screen>
    name: 'task9_2'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    
        
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_2
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_2()

    MDTextField:
        id: text_field_error9_22
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_22()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}



    MDLabel:
        text: "Вычислите: sin45°*Ctg60°"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2()
    
    MDRectangleFlatButton:
        id: next9_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3'
        disabled: True

############

<task9_3Screen>
    name: 'task9_3'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_3
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3()

    MDTextField:
        id: text_field_error9_32
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_32()


    MDLabel:
        text: "Вычислите: tg22°*sin60°: "
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3()
    
    MDRectangleFlatButton:
        id: next9_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_4'
        disabled: True
 

###############

<task9_4Screen>
    name: 'task9_4'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_4
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_4()

    MDTextField:
        id: text_field_error9_42
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_42()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: tg45°*cos22°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_4()
    
    MDRectangleFlatButton:
        id: next9_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_5'
        disabled: True

######################

<task9_5Screen>
    name: 'task9_5'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_5
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_5()

    MDTextField:
        id: text_field_error9_52
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_52()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: cos45°*cos22°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_5()
    
    MDRectangleFlatButton:
        id: next9_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_6'
        disabled: True

###############################

<task9_6Screen>
    name: 'task9_6'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_6
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_6()

    MDTextField:
        id: text_field_error9_62
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_62()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: sin22°*Ctg22°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_6()
    
    MDRectangleFlatButton:
        id: next9_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_7'
        disabled: True

###################

<task9_7Screen>
    name: 'task9_7'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_7
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_7()

    MDTextField:
        id: text_field_error9_72
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_72()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: cos60°*tg22°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_7()
    
    MDRectangleFlatButton:
        id: next9_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_8'
        disabled: True

####################

<task9_8Screen>
    name: 'task9_8'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDTextField:
        id: text_field_error9_8
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_8()

    MDTextField:
        id: text_field_error9_82
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_82()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: tg60°*sin60°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_8()
    
    MDRectangleFlatButton:
        id: next9_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_9'
        disabled: True


#################

<task9_9Screen>
    name: 'task9_9'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>таблица тригонометрических функций>задания>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9'

    MDTextField:
        id: text_field_error9_9
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_9()

    MDTextField:
        id: text_field_error9_92
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_92()

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

    MDLabel:
        text: "Вычислите: sin22°*Ctg60°*sin60°:"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_9()
    
    MDRectangleFlatButton:
        id: next9_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks9'
        disabled: True


############################################################

<task9_2_1Screen>
    name: 'task9_2_1'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_1
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_1()

    MDLabel:
        text: "В треугольнике ABC  угол C  равен 90°, AC=15, cosA=: 5/7. Найдите AB."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_1()
    
    MDRectangleFlatButton:
        id: next9_2_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_2'
        disabled: True

    Image:
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

###################

<task9_2_2Screen>
    name: 'task9_2_2'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_2
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_2()

    MDLabel:
        text: "В треугольнике ABC  угол C  равен 90°, BC=12, sinA=4/11. Найдите AB."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_2()
    
    MDRectangleFlatButton:
        id: next9_2_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_3'
        disabled: True

    Image:
        id: image9_2_2
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

############

<task9_2_3Screen>
    name: 'task9_2_3'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_3
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_3()

    MDLabel:
        text: "Катеты прямоугольного треугольника равны  корень из 15 и 1. Найдите синус наименьшего угла этого треугольника."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_3()
    
    MDRectangleFlatButton:
        id: next9_2_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_4'
        disabled: True

    Image:
        id: image9_2_3
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}   

###############

<task9_2_4Screen>
    name: 'task9_2_4'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_4
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_4()

    MDLabel:
        text: "Площадь прямоугольного треугольника равна 32 корень из 3. Один из острых углов равен 22°. Найдите длину гипотенузы."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_4()
    
    MDRectangleFlatButton:
        id: next9_2_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_5'
        disabled: True

    Image:
        id: image9_2_4
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

######################

<task9_2_5Screen>
    name: 'task9_2_5'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_5
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_5()

    MDLabel:
        text: "В треугольнике ABC угол C равен 90°, AC  =  4, tg A  =  0,75. Найдите BC."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_5()
    
    MDRectangleFlatButton:
        id: next9_2_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_6'
        disabled: True

    Image:
        id: image9_2_5
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

###############################

<task9_2_6Screen>
    name: 'task9_2_6'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_6
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_6()

    MDLabel:
        text: "В прямоугольном треугольнике катет и гипотенуза равны 40 и 41 соответственно. Найдите другой катет этого треугольника."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_6()
    
    MDRectangleFlatButton:
        id: next9_2_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_7'
        disabled: True

    Image:
        id: image9_2_6
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

###################

<task9_2_7Screen>
    name: 'task9_2_7'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_7
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_7()

    MDLabel:
        text: "В треугольнике ABC угол C равен 90°, AC  =  6, AB  =  10. Найдите  синус B."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_7()
    
    MDRectangleFlatButton:
        id: next9_2_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_8'
        disabled: True

    Image:
        id: image9_2_7
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

####################

<task9_2_8Screen>
    name: 'task9_2_8'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_8
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_8()

    MDLabel:
        text: "В треугольнике ABC угол C равен 90°, BC  =  5, AC  =  2. Найдите  тангенс B."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_2_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_8()
    
    MDRectangleFlatButton:
        id: next9_2_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_2_9'
        disabled: True

    Image:
        id: image9_2_8
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

#################

<task9_2_9Screen>
    name: 'task9_2_9'

    MDLabel:
        text: "меню>9класс>Решение треугольников>задания>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_2'

    MDTextField:
        id: text_field_error9_2_9
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_2_9()

    MDLabel:
        text: "В треугольнике ABC угол C равен 90°,  косинус B= дробь: числитель: 2, знаменатель: 5 конец дроби , AB=10. Найдите BC."
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_2_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_2_9()
    
    MDRectangleFlatButton:
        id: next9_2_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks9_2'
        disabled: True

    Image:
        id: image9_2_9
        source:'images/triangle_cab.png'
        size_hint:(0.3, 0.3)
        pos_hint:{'center_x': 0.8, 'center_y': 0.8}

##################################################################


<task9_3_1Screen>
    name: 'task9_3_1'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №1"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}

    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_1
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_1()

    MDTextField:
        id: text_field_error9_3_12
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_12()

    MDLabel:
        text: "В треугольнике ABC, BC=5, AC=3. Если sin(ABC)=2/5, найдите sin(BAC)-?"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_3_1
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_1()
    
    MDRectangleFlatButton:
        id: next9_3_1
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_2'
        disabled: True

###################

<task9_3_2Screen>
    name: 'task9_3_2'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №2"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_2
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_3_2()

    MDLabel:
        text: "Найдите неизвестную сторону треугольника, если AB=5, BC=8, а угол B=60°"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_3_2
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_2()
    
    MDRectangleFlatButton:
        id: next9_3_2
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_3'
        disabled: True

############

<task9_3_3Screen>
    name: 'task9_3_3'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №3"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_3
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_3()

    MDTextField:
        id: text_field_error9_3_32
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_32()

    MDLabel:
        text: "Вычислите Cos(α), если sin(α)=5/13"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_3_3
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_3()
    
    MDRectangleFlatButton:
        id: next9_3_3
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_4'
        disabled: True 

###############

<task9_3_4Screen>
    name: 'task9_3_4'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №4"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_4
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_4()

    MDTextField:
        id: text_field_error9_3_42
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_42()

    MDLabel:
        text: "В треугольнике ABC, BC=5, AC=9. Если sin(ABC)=3/5, найдите sin(BAC)-?"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_3_4
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_4()
    
    MDRectangleFlatButton:
        id: next9_3_4
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_5'
        disabled: True


######################

<task9_3_5Screen>
    name: 'task9_3_5'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №5"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_5
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_5()

    MDLabel:
        text: "Найдите неизвестную сторону треугольника, если AB=3, BC=2√2, а угол B=135°"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_3_5
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_5()
    
    MDRectangleFlatButton:
        id: next9_3_5
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_6'
        disabled: True

    MDLabel:
        text: "√"
        font_size: '45'
        size_hint:(0.2, 0.2)
        pos_hint: {'center_x': 0.09, 'center_y': 0.28}

###############################

<task9_3_6Screen>
    name: 'task9_3_6'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}    

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №6"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_6
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_6()

    MDTextField:
        id: text_field_error9_3_62
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_62()

    MDLabel:
        text: "Вычислите Sin(α), если cos(α)=9/15"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_3_6
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_6()
    
    MDRectangleFlatButton:
        id: next9_3_6
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_7'
        disabled: True

###################

<task9_3_7Screen>
    name: 'task9_3_7'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №7"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_7
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_7()

    MDTextField:
        id: text_field_error9_3_72
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_72()

    MDLabel:
        text: "В треугольнике ABC, BC=5, AC=9. Если (ABC)=3/5, найдите sin(BAC)-?"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_3_7
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_7()
    
    MDRectangleFlatButton:
        id: next9_3_7
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_8'
        disabled: True

####################

<task9_3_8Screen>
    name: 'task9_3_8'

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №8"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_8
        hint_text: "Ответ:"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .3, "center_y": .25}
        size_hint_x: .5
        on_text_validate: app.set_error_message9_3_8()

    MDLabel:
        text: "Найдите неизвестную сторону треугольника, если DE=3, DF=2√3, а угол D=22°"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
    
    MDRectangleFlatButton:
        id: submit9_3_8
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_8()
    
    MDRectangleFlatButton:
        id: next9_3_8
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'task9_3_9'
        disabled: True

#################

<task9_3_9Screen>
    name: 'task9_3_9'

    Image:
        source:'images/line.png'
        size_hint:(.05, 4)
        pos_hint:{'center_x': 0.1, 'center_y': 0.24}

    MDLabel:
        text: "меню>9класс>Тригонометрические теоремы>задания>задание №9"
        font_style: 'H1'
        font_size: '13'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.45, "center_y": 0.95}
    
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'tasks9_3'

    MDTextField:
        id: text_field_error9_3_9
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .28}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_9()

    MDTextField:
        id: text_field_error9_3_92
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .1, "center_y": .2}
        size_hint_x: .05
        on_text_validate: app.set_error_message9_3_92()

    MDLabel:
        text: "Найдите tg(α), если Ctg(α)= 4"
        font_style: 'H1'
        font_size: '22'
        halign: 'center'
        size_hint:(0.65, 0.3)
        pos_hint: {"center_x": 0.35, "center_y": 0.85}
    
    MDRectangleFlatButton:
        id: submit9_3_9
        text: "Сохранить"
        pos_hint:{"center_x": 0.8, "center_y": 0.2}
        on_release: app.check_answer9_3_9()
    
    MDRectangleFlatButton:
        id: next9_3_9
        text: "Следущий"
        pos_hint:{"center_x": 0.8, "center_y": 0.1}
        on_release: root.manager.current = 'tasks9_3'
        disabled: True


"""

red_color = (1,0,0,1)

green_color = (0,1,0,1)

x = Window.height//5
y = Window.width//5

x2 = Window.height
y2 = Window.width

pos1_x = Window.height//4
pos1_y = Window.width//4

pos2_y = Window.height//4
pos2_x = Window.width//5*3

pos3_y = Window.height//4*2
pos3_x = Window.width//5*3

pos4_y = Window.height//4*3
pos4_x = Window.width//5*3


rect_size = (x,y)

rect_pos1 = (pos1_x,pos1_y)
rect_pos2 = (pos2_x,pos2_y)
rect_pos3 = (pos3_x,pos3_y)
rect_pos4 = (pos4_x,pos4_y)
#######################################################
class Design_menu(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.7))
            self.rect1 = Ellipse(pos=pos_design1, rgba=(0, 1, 0, 1),size = (20,20))
            self.rect1 = Ellipse(pos=pos_design2, rgba=(0, 1, 1, 1),size = (24,24))
            self.rect1 = Ellipse(pos=pos_design3, rgba=(0, 1, 0, 1),size = (28,28))
            self.rect1 = Ellipse(pos=pos_design4, rgba=(0, 1, 0, 1),size = (32,32))
            self.rect1 = Ellipse(pos=pos_design5, rgba=(0, 1, 0, 1),size = (36,36))
            self.rect1 = Ellipse(pos=pos_design6, rgba=(0, 1, 0, 1),size = (40,40))
            self.rect1 = Ellipse(pos=pos_design7, rgba=(0, 1, 0, 1),size = (44,44))
            self.rect1 = Ellipse(pos=pos_design8, rgba=(0, 1, 0, 1),size = (48,48))
            self.rect1 = Ellipse(pos=pos_design9, rgba=(0, 1, 0, 1),size = (52,52))
            self.rect1 = Ellipse(pos=pos_design10, rgba=(0, 1, 0, 1),size = (56,56))
            self.rect1 = Ellipse(pos=pos_design11, rgba=(0, 1, 0, 1),size = (60,60))
            self.rect1 = Ellipse(pos=pos_design12, rgba=(0, 1, 0, 1),size = (64,64))

            self.line = Line(points=[rightlineup,rightlinedown], rgba=(0, 1, 0, 1), width=4)
        

pos_design1 = (Window.width *0.2, Window.height*0.1)
pos_design2 = (Window.width *0.24, Window.height*0.1)
pos_design3 = (Window.width *0.28, Window.height*0.1)
pos_design4 = (Window.width *0.32, Window.height*0.1)
pos_design5 = (Window.width *0.36, Window.height*0.1)
pos_design6 = (Window.width *0.40, Window.height*0.1)
pos_design7 = (Window.width *0.46, Window.height*0.1)
pos_design8 = (Window.width *0.52, Window.height*0.1)
pos_design9 = (Window.width *0.56, Window.height*0.1)
pos_design10 = (Window.width *0.62, Window.height*0.1)
pos_design11 = (Window.width *0.68, Window.height*0.1)
pos_design12 = (Window.width *0.74, Window.height*0.1)

class Design_themes(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.7))
            self.rect1 = Ellipse(pos=pos_design1_1, rgba=(0, 1, 0, 1),size = (55,55))
            self.rect1 = Ellipse(pos=pos_design2_1, rgba=(0, 1, 0, 1),size = (55,55))
            self.rect1 = Ellipse(pos=pos_design3_1, rgba=(0, 1, 0, 1),size = (55,55))
            self.rect1 = Ellipse(pos=pos_design4_1, rgba=(0, 1, 0, 1),size = (55,55))

pos_design1_1 = (Window.width *0.1, Window.height*0.1)
pos_design2_1 = (Window.width *0.1, Window.height*0.9)
pos_design3_1 = (Window.width *0.9, Window.height*0.1)
pos_design4_1 = (Window.width *0.9, Window.height*0.9)

 

rightlineup = (Window.width *0.95, Window.height*0.05)
rightlinedown = (Window.width *0.95, Window.height*0.95)

class Design_class(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.7))
            self.line1 = Line(points=[pos_class1,pos_class3], rgba=(0, 1, 0, 1), width=3)
            self.line1 = Line(points=[pos_class1,pos_class4], rgba=(0, 1, 0, 1), width=3)
            self.line1 = Line(points=[pos_class2,pos_class3], rgba=(0, 1, 0, 1), width=3)
            self.line1 = Line(points=[pos_class2,pos_class4], rgba=(0, 1, 0, 1), width=3)

pos_class1 = (Window.width *0.3, Window.height*0.05)
pos_class2 = (Window.width *0.7, Window.height*0.55)
pos_class3 = (Window.width *0.3, Window.height*0.55)
pos_class4 = (Window.width *0.7, Window.height*0.05)

class Design_teory(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.3))
            self.rect1 = Ellipse(pos=pos_teory1, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory2, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory3, rgba=(0, 1, 0, 1),size = (75,75))

pos_teory1 = (Window.width *0.2, Window.height*0.75)
pos_teory2 = (Window.width *0.7, Window.height*0.55)
pos_teory3 = (Window.width *0.6, Window.height*0.22)

class Design_tasks(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.3))
            self.rect1 = Ellipse(pos=pos_teory1, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory2, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory3, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory4, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory5, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory6, rgba=(0, 1, 0, 1),size = (75,75))
            
pos_teory4 = (Window.width *0.2, Window.height*0.45)
pos_teory5 = (Window.width *0.25, Window.height*0.15)
pos_teory6 = (Window.width *0.5, Window.height*0.65)

class Design_task(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.3))
            self.line = Line(points=[leftlineup,leftlinedown], rgba=(0, 1, 0, 1), width=2)
            self.rect1 = Ellipse(pos=pos_task1, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_task2, rgba=(0, 1, 0, 1),size = (75,75))


pos_task1 = (Window.width *0.7, Window.height*0.45)
pos_task2 = (Window.width *0.25, Window.height*0.15)
leftlineup = (Window.width *0.05, Window.height*0.05)
leftlinedown = (Window.width *0.05, Window.height*0.95)

class Design_puzzles(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.3))
            self.line = Line(points=[leftlineup,leftlinedown], rgba=(0, 1, 0, 1), width=2)
            self.rect1 = Ellipse(pos=pos_teory1, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory2, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory3, rgba=(0, 1, 0, 1),size = (75,75))

class Design_puzzle(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(rgba=(0,0,1,0.3))
            self.line = Line(points=[leftlineup,leftlinedown], rgba=(0, 1, 0, 1), width=2)
            self.rect1 = Ellipse(pos=pos_teory1, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory2, rgba=(0, 1, 0, 1),size = (75,75))
            self.rect1 = Ellipse(pos=pos_teory3, rgba=(0, 1, 0, 1),size = (75,75))









#######################################################
pos1 = (Window.width*0.1, Window.height*0.57)
pos1_1 = (Window.width *0.1, Window.height*0.4)
pos2 = (Window.width *0.45, Window.height*0.57)
pos1_2 = (Window.width *0.45, Window.height*0.4)
pos3 = (Window.width *0.8, Window.height*0.57)
pos1_3 = (Window.width *0.8, Window.height*0.4)

l_pos1 = [Window.width *0.1, Window.height*0.54, Window.width *0.23, Window.height*0.54]
l_pos2 = [Window.width *0.45, Window.height*0.54, Window.width *0.58, Window.height*0.54]
l_pos3 = [Window.width *0.8, Window.height*0.54, Window.width *0.93, Window.height*0.54]
l_pos1_1 = [Window.width *0.25, Window.height*0.52, Window.width *0.42, Window.height*0.52]
l_pos1_2 = [Window.width *0.25, Window.height*0.56, Window.width *0.42, Window.height*0.56]
l_pos2_1 = [Window.width *0.60, Window.height*0.52, Window.width *0.77, Window.height*0.52]
l_pos2_2 = [Window.width *0.60, Window.height*0.56, Window.width *0.77, Window.height*0.56]

r_pos1_1 = (Window.width*0.1, Window.height*0.1)
r_pos1_2 = (Window.width*0.3, Window.height*0.25)
r_pos1_3 = (Window.width*0.25, Window.height*0.1)
r_pos1_4 = (Window.width*0.5, Window.height*0.25)
r_pos1_5 = (Window.width*0.7, Window.height*0.1)
r_pos1_6 = (Window.width*0.9, Window.height*0.25)


#######################################################
aspect_ratio = Window.width / Window.height

pos2_1 = (Window.width * 0, Window.height * 0.57)
pos2_2 = (Window.width * 0.13, Window.height * 0.57)
pos2_3 = (Window.width * 0.26, Window.height * 0.57)
pos2_4 = (Window.width * 0.39, Window.height * 0.57)
pos2_5 = (Window.width * 0.52, Window.height * 0.57)
pos2_6 = (Window.width * 0.65, Window.height * 0.57)
pos2_7 = (Window.width * 0.78, Window.height * 0.57)
pos2_8 = (Window.width * 0.91, Window.height * 0.57)

r_pos2_1 = (0, Window.height * 0.1)
r_pos2_2 = (Window.width * 0.2, Window.height * 0.25)
r_pos2_3 = (Window.width * 0.45, Window.height * 0.1)
r_pos2_4 = (Window.width * 0.6, Window.height * 0.25)
r_pos2_5 = (Window.width * 0.85, Window.height * 0.1)
r_pos2_6 = (Window.width, Window.height * 0.25)

d_size = (Window.width*0.1, Window.height*0.075)

c_size = (Window.width*0.1+20, Window.height*0.075+20)
#######################################################
pos3_1 = (Window.width * 0, Window.height * 0.57)
pos3_2 = (Window.width * 0.20, Window.height * 0.57)
pos3_3 = (Window.width * 0.40, Window.height * 0.57)
pos3_4 = (Window.width * 0.61, Window.height * 0.57)
pos3_5 = (Window.width * 0.82, Window.height * 0.57)

r_pos3_1 = (0, Window.height * 0.1)
r_pos3_2 = (Window.width * 0.2, Window.height * 0.25)
r_pos3_3 = (Window.width * 0.45, Window.height * 0.1)
r_pos3_4 = (Window.width * 0.6, Window.height * 0.25)
r_pos3_5 = (Window.width * 0.85, Window.height * 0.1)
#######################################################
pos10_2_1_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_1_2 = (Window.width * 0.167, Window.height * 0.57)
pos10_2_1_3 = (Window.width * 0.334, Window.height * 0.57)
pos10_2_1_4 = (Window.width * 0.501, Window.height * 0.57)
pos10_2_1_5 = (Window.width * 0.668, Window.height * 0.57)
pos10_2_1_6 = (Window.width * 0.835, Window.height * 0.57)

r_pos10_2_1_1 = (0, Window.height * 0.1)
r_pos10_2_1_2 = (Window.width * 0.167, Window.height * 0.25)
r_pos10_2_1_3 = (Window.width * 0.334, Window.height * 0.1)
r_pos10_2_1_4 = (Window.width * 0.501, Window.height * 0.25)
r_pos10_2_1_5 = (Window.width * 0.668, Window.height * 0.1)
r_pos10_2_1_6 = (Window.width * 0.835, Window.height * 0.25)
#######################################################
pos10_2_2_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_2_2 = (Window.width * 0.2, Window.height * 0.57)
pos10_2_2_3 = (Window.width * 0.4, Window.height * 0.57)
pos10_2_2_4 = (Window.width * 0.6, Window.height * 0.57)
pos10_2_2_5 = (Window.width * 0.8, Window.height * 0.57)


r_pos10_2_2_1 = (0, Window.height * 0.1)
r_pos10_2_2_2 = (Window.width * 0.2, Window.height * 0.25)
r_pos10_2_2_3 = (Window.width * 0.4, Window.height * 0.1)
r_pos10_2_2_4 = (Window.width * 0.6, Window.height * 0.25)
r_pos10_2_2_5 = (Window.width * 0.8, Window.height * 0.1)
#######################################################
pos10_2_3_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_3_2 = (Window.width * 0.167, Window.height * 0.57)
pos10_2_3_3 = (Window.width * 0.334, Window.height * 0.57)
pos10_2_3_4 = (Window.width * 0.501, Window.height * 0.57)
pos10_2_3_5 = (Window.width * 0.668, Window.height * 0.57)
pos10_2_3_6 = (Window.width * 0.835, Window.height * 0.57)

r_pos10_2_3_1 = (0, Window.height * 0.1)
r_pos10_2_3_2 = (Window.width * 0.167, Window.height * 0.25)
r_pos10_2_3_3 = (Window.width * 0.334, Window.height * 0.1)
r_pos10_2_3_4 = (Window.width * 0.501, Window.height * 0.25)
r_pos10_2_3_5 = (Window.width * 0.668, Window.height * 0.1)
r_pos10_2_3_6 = (Window.width * 0.835, Window.height * 0.25)
#######################################################
pos10_2_4_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_4_2 = (Window.width * 0.167, Window.height * 0.57)
pos10_2_4_3 = (Window.width * 0.334, Window.height * 0.57)
pos10_2_4_4 = (Window.width * 0.501, Window.height * 0.57)
pos10_2_4_5 = (Window.width * 0.668, Window.height * 0.57)
pos10_2_4_6 = (Window.width * 0.835, Window.height * 0.57)

r_pos10_2_4_1 = (0, Window.height * 0.1)
r_pos10_2_4_2 = (Window.width * 0.167, Window.height * 0.25)
r_pos10_2_4_3 = (Window.width * 0.334, Window.height * 0.1)
r_pos10_2_4_4 = (Window.width * 0.501, Window.height * 0.25)
r_pos10_2_4_5 = (Window.width * 0.668, Window.height * 0.1)
r_pos10_2_4_6 = (Window.width * 0.835, Window.height * 0.25)
#######################################################
drobd_size = (Window.width*0.5, Window.height*0.04)

drobc_size = (Window.width*0.5+20, Window.height*0.04+20)

pos10_2_5_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_5_2 = (Window.width * 0.2, Window.height * 0.57)
pos10_2_5_3 = (Window.width * 0.4, Window.height * 0.57)
pos10_2_5_4 = (Window.width * 0.4, Window.height * 0.67)
pos10_2_5_5 = (Window.width * 0.6, Window.height * 0.67)
pos10_2_5_6 = (Window.width * 0.4, Window.height * 0.44)
pos10_2_5_7 = (Window.width * 0.6, Window.height * 0.44)
pos10_2_5_8 = (Window.width * 0.8, Window.height * 0.44)

r_pos10_2_5_1 = (0, Window.height * 0.1)
r_pos10_2_5_2 = (Window.width * 0.125, Window.height * 0.25)
r_pos10_2_5_3 = (Window.width * 0.250, Window.height * 0.1)
r_pos10_2_5_4 = (Window.width * 0.375, Window.height * 0.25)
r_pos10_2_5_5 = (Window.width * 0.500, Window.height * 0.1)
r_pos10_2_5_6 = (Window.width * 0.625, Window.height * 0.25)
r_pos10_2_5_7 = (Window.width * 0.750, Window.height * 0.1)
r_pos10_2_5_8 = (Window.width * 0.875, Window.height * 0.25)

#######################################################
pos10_2_6_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_6_2 = (Window.width * 0.2, Window.height * 0.57)
pos10_2_6_3 = (Window.width * 0.4, Window.height * 0.57)
pos10_2_6_4 = (Window.width * 0.4, Window.height * 0.67)
pos10_2_6_5 = (Window.width * 0.6, Window.height * 0.67)
pos10_2_6_6 = (Window.width * 0.8, Window.height * 0.67)
pos10_2_6_7 = (Window.width * 0.4, Window.height * 0.44)
pos10_2_6_8 = (Window.width * 0.6, Window.height * 0.44)


r_pos10_2_6_1 = (0, Window.height * 0.1)
r_pos10_2_6_2 = (Window.width * 0.125, Window.height * 0.25)
r_pos10_2_6_3 = (Window.width * 0.250, Window.height * 0.1)
r_pos10_2_6_4 = (Window.width * 0.375, Window.height * 0.25)
r_pos10_2_6_5 = (Window.width * 0.500, Window.height * 0.1)
r_pos10_2_6_6 = (Window.width * 0.625, Window.height * 0.25)
r_pos10_2_6_7 = (Window.width * 0.750, Window.height * 0.1)
r_pos10_2_6_8 = (Window.width * 0.875, Window.height * 0.25)

#######################################################
pos10_2_7_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_7_2 = (Window.width * 0.2, Window.height * 0.57)
pos10_2_7_3 = (Window.width * 0.4, Window.height * 0.57)
pos10_2_7_4 = (Window.width * 0.4, Window.height * 0.67)
pos10_2_7_5 = (Window.width * 0.6, Window.height * 0.67)
pos10_2_7_6 = (Window.width * 0.8, Window.height * 0.67)
pos10_2_7_7 = (Window.width * 0.6, Window.height * 0.44)



r_pos10_2_7_1 = (0, Window.height * 0.1)
r_pos10_2_7_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_2_7_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_2_7_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_2_7_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_2_7_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_2_7_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_2_8_1 = (Window.width * 0, Window.height * 0.57)
pos10_2_8_2 = (Window.width * 0.2, Window.height * 0.57)
pos10_2_8_3 = (Window.width * 0.4, Window.height * 0.57)
pos10_2_8_4 = (Window.width * 0.4, Window.height * 0.67)
pos10_2_8_5 = (Window.width * 0.6, Window.height * 0.67)
pos10_2_8_6 = (Window.width * 0.8, Window.height * 0.67)
pos10_2_8_7 = (Window.width * 0.6, Window.height * 0.44)



r_pos10_2_8_1 = (0, Window.height * 0.1)
r_pos10_2_8_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_2_8_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_2_8_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_2_8_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_2_8_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_2_8_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_3_1_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_1_2 = (Window.width * 0.142, Window.height * 0.57)
pos10_3_1_3 = (Window.width * 0.284, Window.height * 0.57)
pos10_3_1_4 = (Window.width * 0.426, Window.height * 0.57)
pos10_3_1_5 = (Window.width * 0.568, Window.height * 0.57)
pos10_3_1_6 = (Window.width * 0.71, Window.height * 0.57)
pos10_3_1_7 = (Window.width * 0.852, Window.height * 0.57)



r_pos10_3_1_1 = (0, Window.height * 0.1)
r_pos10_3_1_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_3_1_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_3_1_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_3_1_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_3_1_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_3_1_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_3_2_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_2_2 = (Window.width * 0.142, Window.height * 0.57)
pos10_3_2_3 = (Window.width * 0.284, Window.height * 0.57)
pos10_3_2_4 = (Window.width * 0.426, Window.height * 0.57)
pos10_3_2_5 = (Window.width * 0.568, Window.height * 0.57)
pos10_3_2_6 = (Window.width * 0.71, Window.height * 0.57)
pos10_3_2_7 = (Window.width * 0.852, Window.height * 0.57)



r_pos10_3_2_1 = (0, Window.height * 0.1)
r_pos10_3_2_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_3_2_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_3_2_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_3_2_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_3_2_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_3_2_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_3_3_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_3_2 = (Window.width * 0.142, Window.height * 0.57)
pos10_3_3_3 = (Window.width * 0.284, Window.height * 0.57)
pos10_3_3_4 = (Window.width * 0.426, Window.height * 0.57)
pos10_3_3_5 = (Window.width * 0.568, Window.height * 0.57)
pos10_3_3_6 = (Window.width * 0.71, Window.height * 0.57)
pos10_3_3_7 = (Window.width * 0.852, Window.height * 0.57)



r_pos10_3_3_1 = (0, Window.height * 0.1)
r_pos10_3_3_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_3_3_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_3_3_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_3_3_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_3_3_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_3_3_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_3_4_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_4_2 = (Window.width * 0.142, Window.height * 0.57)
pos10_3_4_3 = (Window.width * 0.284, Window.height * 0.57)
pos10_3_4_4 = (Window.width * 0.426, Window.height * 0.57)
pos10_3_4_5 = (Window.width * 0.568, Window.height * 0.57)
pos10_3_4_6 = (Window.width * 0.71, Window.height * 0.57)
pos10_3_4_7 = (Window.width * 0.852, Window.height * 0.57)



r_pos10_3_4_1 = (0, Window.height * 0.1)
r_pos10_3_4_2 = (Window.width * 0.142, Window.height * 0.25)
r_pos10_3_4_3 = (Window.width * 0.284, Window.height * 0.1)
r_pos10_3_4_4 = (Window.width * 0.426, Window.height * 0.25)
r_pos10_3_4_5 = (Window.width * 0.568, Window.height * 0.1)
r_pos10_3_4_6 = (Window.width * 0.71, Window.height * 0.25)
r_pos10_3_4_7 = (Window.width * 0.852, Window.height * 0.1)
#######################################################
pos10_3_5_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_5_2 = (Window.width * 0.166, Window.height * 0.57)
pos10_3_5_3 = (Window.width * 0.332, Window.height * 0.57)
pos10_3_5_4 = (Window.width * 0.332, Window.height * 0.67)
pos10_3_5_5 = (Window.width * 0.498, Window.height * 0.67)
pos10_3_5_6 = (Window.width * 0.664, Window.height * 0.67)
pos10_3_5_7 = (Window.width * 0.332, Window.height * 0.4)
pos10_3_5_8 = (Window.width * 0.498, Window.height * 0.4)
pos10_3_5_9 = (Window.width * 0.664, Window.height * 0.4)
pos10_3_5_10 = (Window.width * 0.830, Window.height * 0.4)


r_pos10_3_5_1 = (0, Window.height * 0.1)
r_pos10_3_5_2 = (Window.width * 0.1, Window.height * 0.25)
r_pos10_3_5_3 = (Window.width * 0.2, Window.height * 0.1)
r_pos10_3_5_4 = (Window.width * 0.3, Window.height * 0.25)
r_pos10_3_5_5 = (Window.width * 0.4, Window.height * 0.1)
r_pos10_3_5_6 = (Window.width * 0.5, Window.height * 0.25)
r_pos10_3_5_7 = (Window.width * 0.6, Window.height * 0.1)
r_pos10_3_5_8 = (Window.width * 0.7, Window.height * 0.25)
r_pos10_3_5_9 = (Window.width * 0.8, Window.height * 0.1)
r_pos10_3_5_10 = (Window.width * 0.9, Window.height * 0.25)
#######################################################
pos10_3_6_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_6_2 = (Window.width * 0.166, Window.height * 0.57)
pos10_3_6_3 = (Window.width * 0.332, Window.height * 0.57)
pos10_3_6_4 = (Window.width * 0.332, Window.height * 0.67)
pos10_3_6_5 = (Window.width * 0.498, Window.height * 0.67)
pos10_3_6_6 = (Window.width * 0.664, Window.height * 0.67)
pos10_3_6_7 = (Window.width * 0.332, Window.height * 0.4)
pos10_3_6_8 = (Window.width * 0.498, Window.height * 0.4)
pos10_3_6_9 = (Window.width * 0.664, Window.height * 0.4)
pos10_3_6_10 = (Window.width * 0.830, Window.height * 0.4)


r_pos10_3_6_1 = (0, Window.height * 0.1)
r_pos10_3_6_2 = (Window.width * 0.1, Window.height * 0.25)
r_pos10_3_6_3 = (Window.width * 0.2, Window.height * 0.1)
r_pos10_3_6_4 = (Window.width * 0.3, Window.height * 0.25)
r_pos10_3_6_5 = (Window.width * 0.4, Window.height * 0.1)
r_pos10_3_6_6 = (Window.width * 0.5, Window.height * 0.25)
r_pos10_3_6_7 = (Window.width * 0.6, Window.height * 0.1)
r_pos10_3_6_8 = (Window.width * 0.7, Window.height * 0.25)
r_pos10_3_6_9 = (Window.width * 0.8, Window.height * 0.1)
r_pos10_3_6_10 = (Window.width * 0.9, Window.height * 0.25)
#######################################################
pos10_3_7_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_7_2 = (Window.width * 0.166, Window.height * 0.57)
pos10_3_7_3 = (Window.width * 0.332, Window.height * 0.57)
pos10_3_7_4 = (Window.width * 0.332, Window.height * 0.67)
pos10_3_7_5 = (Window.width * 0.498, Window.height * 0.67)
pos10_3_7_6 = (Window.width * 0.664, Window.height * 0.67)
pos10_3_7_7 = (Window.width * 0.830, Window.height * 0.67)
pos10_3_7_8 = (Window.width * 0.332, Window.height * 0.4)
pos10_3_7_9 = (Window.width * 0.498, Window.height * 0.4)
pos10_3_7_10 = (Window.width * 0.664, Window.height * 0.4)



r_pos10_3_7_1 = (0, Window.height * 0.1)
r_pos10_3_7_2 = (Window.width * 0.1, Window.height * 0.25)
r_pos10_3_7_3 = (Window.width * 0.2, Window.height * 0.1)
r_pos10_3_7_4 = (Window.width * 0.3, Window.height * 0.25)
r_pos10_3_7_5 = (Window.width * 0.4, Window.height * 0.1)
r_pos10_3_7_6 = (Window.width * 0.5, Window.height * 0.25)
r_pos10_3_7_7 = (Window.width * 0.6, Window.height * 0.1)
r_pos10_3_7_8 = (Window.width * 0.7, Window.height * 0.25)
r_pos10_3_7_9 = (Window.width * 0.8, Window.height * 0.1)
r_pos10_3_7_10 = (Window.width * 0.9, Window.height * 0.25)
#######################################################
pos10_3_8_1 = (Window.width * 0, Window.height * 0.57)
pos10_3_8_2 = (Window.width * 0.166, Window.height * 0.57)
pos10_3_8_3 = (Window.width * 0.332, Window.height * 0.57)
pos10_3_8_4 = (Window.width * 0.332, Window.height * 0.67)
pos10_3_8_5 = (Window.width * 0.498, Window.height * 0.67)
pos10_3_8_6 = (Window.width * 0.664, Window.height * 0.67)
pos10_3_8_7 = (Window.width * 0.830, Window.height * 0.67)
pos10_3_8_8 = (Window.width * 0.332, Window.height * 0.4)
pos10_3_8_9 = (Window.width * 0.498, Window.height * 0.4)
pos10_3_8_10 = (Window.width * 0.664, Window.height * 0.4)



r_pos10_3_8_1 = (0, Window.height * 0.1)
r_pos10_3_8_2 = (Window.width * 0.1, Window.height * 0.25)
r_pos10_3_8_3 = (Window.width * 0.2, Window.height * 0.1)
r_pos10_3_8_4 = (Window.width * 0.3, Window.height * 0.25)
r_pos10_3_8_5 = (Window.width * 0.4, Window.height * 0.1)
r_pos10_3_8_6 = (Window.width * 0.5, Window.height * 0.25)
r_pos10_3_8_7 = (Window.width * 0.6, Window.height * 0.1)
r_pos10_3_8_8 = (Window.width * 0.7, Window.height * 0.25)
r_pos10_3_8_9 = (Window.width * 0.8, Window.height * 0.1)
r_pos10_3_8_10 = (Window.width * 0.9, Window.height * 0.25)

#######################################################
def collides(rect1, rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True
    else:
        return False

def collides_puzzle2(rect1, rect2):
    r1x = rect1.pos[0]
    r1y = rect1.pos[1]
    r2x = rect2.pos[0]
    r2y = rect2.pos[1]
    r1w = rect1.size[0]
    r1h = rect1.size[1]
    r2w = rect2.size[0]
    r2h = rect2.size[1]

    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True
    else:
        return False
#виджеты 8 класс пазлы

class DraggableRectangle(Widget):
    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self.color = Color(0, 0, 0)
            self.image = Image(source=source, pos=self.pos, size=self.size)
            self.rect = Rectangle(pos=self.pos, size=self.size, source=source)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.pos = (touch.x - self.width / 2, touch.y - self.height / 2)
            return True

        return super().on_touch_move(touch)

    def update_rect(self, *args):
        self.image.pos = self.pos
        self.image.size = self.size
        self.rect.pos = self.pos
        self.rect.size = self.size

class Puzzle9_1Widget(Widget):

    def __init__(self, **kwargs):
        super(Puzzle9_1Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/sin30.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/3-3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/2-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_1Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_1Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2_cor.png"))
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/2-2_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-3_incor.png"))
            
            return True

        return super(Puzzle9_1Widget, self).on_touch_move(touch)

#виджеты 9 класс пазлы

# тема 1


class Puzzle9_2Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_2Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/sin45.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(1,0,1), size = (rect_size), source="images/3-3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,0,1), size = (rect_size), source="images/2-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_2Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_2Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/2-2_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-3_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1_incor.png"))
            
            return True

        return super(Puzzle9_2Widget, self).on_touch_move(touch)

class Puzzle9_3Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_3Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/sin60.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(1,0,1), size = (rect_size), source="images/3-3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,0,1), size = (rect_size), source="images/3-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_3Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_3Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-2_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-3_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1-2_incor.png"))
            
            return True

        return super(Puzzle9_3Widget, self).on_touch_move(touch)

class Puzzle9_4Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_4Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/cos30.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(1,0,1), size = (rect_size), source="images/3-3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,0,1), size = (rect_size), source="images/1-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/3-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_4Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_4Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/3-2_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/1-2_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                

                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-3_incor.png"))

            return True

        return super(Puzzle9_4Widget, self).on_touch_move(touch)

class Puzzle9_5Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_5Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/cos45.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/3-2.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/2-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_5Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_5Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                

                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/2-2_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-2_incor.png"))    

            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1-2_incor.png"))
            
                


            return True

        return super(Puzzle9_5Widget, self).on_touch_move(touch)

class Puzzle9_6Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_6Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/cos60.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/1.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_6Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_6Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1-2_cor.png"))
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-2_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/1_incor.png"))

            return True

        return super(Puzzle9_6Widget, self).on_touch_move(touch)

class Puzzle9_7Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_7Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/tg30.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/1.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-3.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/3-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_7Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            
            return True

        return super(Puzzle9_7Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-3_cor.png"))

                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/1_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/3-2_incor.png"))
            return True

        return super(Puzzle9_7Widget, self).on_touch_move(touch)

class Puzzle9_8Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_8Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/tg45.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/2-2.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-3.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_8Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_8Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1_cor.png"))
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-3_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/2-2_incor.png"))
            
                


            return True

        return super(Puzzle9_8Widget, self).on_touch_move(touch)

class Puzzle9_9Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_9Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/tg60.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-3.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_9Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_9Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3_cor.png"))

                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-3_incor.png"))
                
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1-2_incor.png"))

            return True

        return super(Puzzle9_9Widget, self).on_touch_move(touch)

class Puzzle9_10Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_10Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/Ctg30.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/3-3.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-2.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/3.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_10Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_10Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/3_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-2_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):

                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-3_incor.png"))
            
            return True

        return super(Puzzle9_10Widget, self).on_touch_move(touch)

class Puzzle9_11Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_11Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/Ctg45.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/1.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-3.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/1-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_11Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_11Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/1_cor.png"))       


                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-3_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/1-2_incor.png"))
            
                


            return True

        return super(Puzzle9_11Widget, self).on_touch_move(touch)

class Puzzle9_12Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle9_12Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/Ctg60.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/3-2.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/3-3.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/2-2.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle9_12Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle9_12Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/3-3_cor.png"))
            

                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/3-2_incor.png"))
                
                

            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                

                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/2-2_incor.png"))
            
            return True

        return super(Puzzle9_12Widget, self).on_touch_move(touch)

#тема 3
class Puzzle9_3_1Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1_check = Rectangle(pos=pos1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect1_2_check = Rectangle(pos=pos1_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2_check = Rectangle(pos=pos2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2_1_check = Rectangle(pos=pos1_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3_check = Rectangle(pos=pos3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3_1_check = Rectangle(pos=pos1_3, rgba=(0, 0, 1, 1), size=c_size)
           self.c2 = Color(rgba=(0,0,0,1))
           self.line1 = Line(points=l_pos1, width=3)
           self.line2 = Line(points=l_pos2, width=3)
           self.line3 = Line(points=l_pos3, width=3)
           self.line4 = Line(points=l_pos1_1, width=3)
           self.line5 = Line(points=l_pos1_2, width=3)
           self.line6 = Line(points=l_pos2_1, width=3)
           self.line7 = Line(points=l_pos2_2, width=3)

        self.rect1 = DraggableRectangle(source = "images/a.png", pos=r_pos1_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos1_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/b.png", pos=r_pos1_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/sin_b.png", pos=r_pos1_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/c.png", pos=r_pos1_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_c.png", pos=r_pos1_6, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)

    def check_collision(self):
        if collides_puzzle2(self.rect1, self.rect1_check) and collides_puzzle2(self.rect2, self.rect1_2_check) and collides_puzzle2(self.rect3, self.rect2_check) and collides_puzzle2(self.rect4, self.rect2_1_check)and collides_puzzle2(self.rect5, self.rect3_check)and collides_puzzle2(self.rect6, self.rect3_1_check):
            self.rect1.color.rgba = (0, 1, 0, 1)
            self.c1.rgba = green_color
            print('yes')
        else:
            self.rect1.color.rgba = (1, 0, 0, 1)
            self.c1.rgba = red_color
            print('no')
            
class Puzzle9_3_2Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self.c1 = Color(rgba=(0,0,1,0.5))
            self.rect1_check = Rectangle(pos=pos2_1, rgba=(0, 0, 1, 1), size=c_size)
            self.rect2_check = Rectangle(pos=pos2_2, rgba=(0, 0, 1, 1), size=c_size, source='images/ravno.png')
            self.rect3_check = Rectangle(pos=pos2_3, rgba=(0, 0, 1, 1), size=c_size)
            self.rect4_check = Rectangle(pos=pos2_4, rgba=(0, 0, 1, 1), size=c_size, source='images/plus.png')
            self.rect5_check = Rectangle(pos=pos2_5, rgba=(0, 0, 1, 1), size=c_size)
            self.rect6_check = Rectangle(pos=pos2_6, rgba=(0, 0, 1, 1), size=c_size)
            self.rect7_check = Rectangle(pos=pos2_7, rgba=(0, 0, 1, 1), size=c_size, source='images/umnozit.png')
            self.rect8_check = Rectangle(pos=pos2_8, rgba=(0, 0, 1, 1), size=c_size)

        self.rect1 = DraggableRectangle(source = "images/a2.png", pos=r_pos2_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/b2.png", pos=r_pos2_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/c2.png", pos=r_pos2_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/2cb.png", pos=r_pos2_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos2_5, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)


    def check_collision(self):
        if collides_puzzle2(self.rect1, self.rect1_check) and collides_puzzle2(self.rect2, self.rect5_check) and collides_puzzle2(self.rect3, self.rect3_check) and collides_puzzle2(self.rect4, self.rect6_check)and collides_puzzle2(self.rect5, self.rect8_check):
            self.rect1.color.rgba = (0, 1, 0, 1)
            self.c1.rgba = green_color
            print('yes')
        else:
            self.rect1.color.rgba = (1, 0, 0, 1)
            self.c1.rgba = red_color
            print('no')

class Puzzle9_3_3Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos3_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos3_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos3_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos3_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos3_5, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/sin2a.png", pos=r_pos3_4, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/plus.png", pos=r_pos3_1, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cos2a.png", pos=r_pos3_2, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos3_3, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos3_5, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)

    def check_collision(self):
       if (collides_puzzle2(self.rect1, self.rect1check) or collides_puzzle2(self.rect1, self.rect3check)) and collides_puzzle2(self.rect2, self.rect2check) and (collides_puzzle2(self.rect3, self.rect1check) or collides_puzzle2(self.rect3, self.rect3check))and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

class Puzzle9_3_4Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos3_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos3_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos3_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos3_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos3_5, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/tga.png", pos=r_pos3_3, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/umnozit.png", pos=r_pos3_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/ctga.png", pos=r_pos3_4, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos3_5, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos3_1, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)

    def check_collision(self):
       if (collides_puzzle2(self.rect1, self.rect1check) or collides_puzzle2(self.rect1, self.rect3check)) and collides_puzzle2(self.rect2, self.rect2check) and (collides_puzzle2(self.rect3, self.rect1check) or collides_puzzle2(self.rect3, self.rect3check)) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

class Puzzle10_2_1Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_1_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_1_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_1_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_2_1_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_1_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_1_6, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/sin_2a.png", pos=r_pos10_2_1_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_1_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_1_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_1_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_2_1_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos10_2_1_6, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)

    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect5check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect4check) and collides_puzzle2(self.rect6, self.rect6check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_2_2Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_2_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_2_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_2_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_2_2_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_2_5, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/cos_2a.png", pos=r_pos10_2_2_4, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_2_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cos2a.png", pos=r_pos10_2_2_5, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_2_1, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/sin2a.png", pos=r_pos10_2_2_3, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)


    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect4check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect5check) :
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_2_3Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_3_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_3_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_3_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_2_3_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_3_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_3_6, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/cos_2a.png", pos=r_pos10_2_3_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_3_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_3_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_3_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_3_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/cos2a.png", pos=r_pos10_2_3_6, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)

    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect5check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect6check) and collides_puzzle2(self.rect6, self.rect4check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_2_4Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_4_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_4_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_4_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_2_4_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_4_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_4_6, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/cos_2a.png", pos=r_pos10_2_4_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_4_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_4_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_4_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_4_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin2a.png", pos=r_pos10_2_4_6, size=d_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)

    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect4check) and  collides_puzzle2(self.rect3, self.rect5check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect3check) and collides_puzzle2(self.rect6, self.rect6check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_2_5Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_5_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_5_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_5_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_2_5_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_5_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_5_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_2_5_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_2_5_8, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/tg2a.png", pos=r_pos10_2_5_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_5_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_5_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_5_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_5_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/tga.png", pos=r_pos10_2_5_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/tg_2a.png", pos=r_pos10_2_5_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_2_5_8, size=drobd_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)


    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect7check) and  collides_puzzle2(self.rect3, self.rect4check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect6check) and collides_puzzle2(self.rect6, self.rect5check) and collides_puzzle2(self.rect7, self.rect8check) and collides_puzzle2(self.rect8, self.rect3check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

class Puzzle10_2_6Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_6_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_6_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_6_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_2_6_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_6_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_6_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_2_6_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_2_6_8, rgba=(0, 0, 1, 1), size=c_size)


        self.rect1 = DraggableRectangle(source = "images/ctg2a.png", pos=r_pos10_2_6_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_6_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_6_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_6_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_6_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/ctga.png", pos=r_pos10_2_6_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/ctg_2a.png", pos=r_pos10_2_6_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_2_6_8, size=drobd_size)

        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)


    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect5check) and  collides_puzzle2(self.rect3, self.rect7check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect6check) and collides_puzzle2(self.rect6, self.rect8check) and collides_puzzle2(self.rect7, self.rect4check) and collides_puzzle2(self.rect8, self.rect3check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_2_7Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_7_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_7_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_7_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_2_7_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_7_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_7_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_2_7_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/cos_2a_2.png", pos=r_pos10_2_7_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_2_7_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_2_7_3, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_7_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_2_7_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_7_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_7_7, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect6check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect7check) and collides_puzzle2(self.rect7, self.rect4check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

class Puzzle10_2_8Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_2_8_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_2_8_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_2_8_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_2_8_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_2_8_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_2_8_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_2_8_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/sin_2a_2.png", pos=r_pos10_2_8_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_2_8_4, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_2_8_5, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_2_8_2, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_2_8_3, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/2.png", pos=r_pos10_2_8_7, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_2_8_6, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect6check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect2check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect7check) and collides_puzzle2(self.rect7, self.rect4check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

class Puzzle10_3_1Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_1_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_1_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_1_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_3_1_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_1_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_1_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_1_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/cos_a+b.png", pos=r_pos10_3_1_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_1_4, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_3_1_5, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/cos_b.png", pos=r_pos10_3_1_2, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_1_3, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos10_3_1_7, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/sin_b.png", pos=r_pos10_3_1_6, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
        if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check):
            self.rect1.color.rgba = (0, 1, 0, 1)
            self.c1.rgba = green_color
            print('yes')
        else:
            self.rect1.color.rgba = (1, 0, 0, 1)
            self.c1.rgba = red_color
            print('no')

class Puzzle10_3_2Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_2_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_2_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_2_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_3_2_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_2_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_2_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_2_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/cos_a-b.png", pos=r_pos10_3_2_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_2_3, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_3_2_5, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/cos_b.png", pos=r_pos10_3_2_2, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_2_4, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos10_3_2_7, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/sin_b.png", pos=r_pos10_3_2_6, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_3Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_3_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_3_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_3_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_3_3_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_3_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_3_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_3_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/sin_a+b.png", pos=r_pos10_3_3_7, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_3_5, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_3_3_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/cos_b.png", pos=r_pos10_3_3_1, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_3_2, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos10_3_3_4, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/sin_b.png", pos=r_pos10_3_3_6, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect6check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect3check) and collides_puzzle2(self.rect7, self.rect7check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_4Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_4_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_4_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_4_3, rgba=(0, 0, 1, 1), size=c_size)
           self.rect4check = Rectangle(pos=pos10_3_4_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_4_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_4_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_4_7, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/sin_a+b.png", pos=r_pos10_3_4_7, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_4_5, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/cosa_2.png", pos=r_pos10_3_4_3, size=d_size)
        self.rect4 = DraggableRectangle(source = "images/cos_b.png", pos=r_pos10_3_4_1, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_4_6, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/sin_a.png", pos=r_pos10_3_4_4, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/sin_b.png", pos=r_pos10_3_4_2, size=d_size)


        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect6check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect3check) and collides_puzzle2(self.rect7, self.rect7check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_5Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_5_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_5_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_5_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_3_5_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_5_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_5_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_5_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_3_5_8, rgba=(0, 0, 1, 1), size=c_size)
           self.rect9check = Rectangle(pos=pos10_3_5_9, rgba=(0, 0, 1, 1), size=c_size)
           self.rect10check = Rectangle(pos=pos10_3_5_10, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/tg_a+b.png", pos=r_pos10_3_5_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_5_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_3_5_3, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/tg_a.png", pos=r_pos10_3_5_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_5_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/tg_b.png", pos=r_pos10_3_5_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_3_5_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_5_8, size=d_size)
        self.rect9 = DraggableRectangle(source = "images/tg_a.png", pos=r_pos10_3_5_9, size=d_size)
        self.rect10 = DraggableRectangle(source = "images/tg_b.png", pos=r_pos10_3_5_10, size=d_size)



        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)
        self.add_widget(self.rect9)
        self.add_widget(self.rect10)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check) and collides_puzzle2(self.rect8, self.rect8check) and collides_puzzle2(self.rect9, self.rect9check) and collides_puzzle2(self.rect10, self.rect10check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_6Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_6_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_6_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_6_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_3_6_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_6_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_6_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_6_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_3_6_8, rgba=(0, 0, 1, 1), size=c_size)
           self.rect9check = Rectangle(pos=pos10_3_6_9, rgba=(0, 0, 1, 1), size=c_size)
           self.rect10check = Rectangle(pos=pos10_3_6_10, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/tg_a-b.png", pos=r_pos10_3_6_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_6_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_3_6_3, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/tg_a.png", pos=r_pos10_3_6_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_6_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/tg_b.png", pos=r_pos10_3_6_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_3_6_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_6_8, size=d_size)
        self.rect9 = DraggableRectangle(source = "images/tg_a.png", pos=r_pos10_3_6_9, size=d_size)
        self.rect10 = DraggableRectangle(source = "images/tg_b.png", pos=r_pos10_3_6_10, size=d_size)



        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)
        self.add_widget(self.rect9)
        self.add_widget(self.rect10)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check) and collides_puzzle2(self.rect8, self.rect8check) and collides_puzzle2(self.rect9, self.rect9check) and collides_puzzle2(self.rect10, self.rect10check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_7Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_7_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_7_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_7_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_3_7_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_7_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_7_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_7_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_3_7_8, rgba=(0, 0, 1, 1), size=c_size)
           self.rect9check = Rectangle(pos=pos10_3_7_9, rgba=(0, 0, 1, 1), size=c_size)
           self.rect10check = Rectangle(pos=pos10_3_7_10, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/ctg_a+b.png", pos=r_pos10_3_7_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_7_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_3_7_3, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/ctg_a.png", pos=r_pos10_3_7_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/ctg_b.png", pos=r_pos10_3_7_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_7_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_3_7_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/ctg_a.png", pos=r_pos10_3_7_8, size=d_size)
        self.rect9 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_7_9, size=d_size)
        self.rect10 = DraggableRectangle(source = "images/ctg_b.png", pos=r_pos10_3_7_10, size=d_size)



        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)
        self.add_widget(self.rect9)
        self.add_widget(self.rect10)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check) and collides_puzzle2(self.rect8, self.rect8check) and collides_puzzle2(self.rect9, self.rect9check) and collides_puzzle2(self.rect10, self.rect10check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')
class Puzzle10_3_8Widget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
           self.c1 = Color(rgba=(0,0,1,0.5))
           self.rect1check = Rectangle(pos=pos10_3_8_1, rgba=(0, 0, 1, 1), size=c_size)
           self.rect2check = Rectangle(pos=pos10_3_8_2, rgba=(0, 0, 1, 1), size=c_size)
           self.rect3check = Rectangle(pos=pos10_3_8_3, rgba=(0, 0, 1, 1), size=drobc_size)
           self.rect4check = Rectangle(pos=pos10_3_8_4, rgba=(0, 0, 1, 1), size=c_size)
           self.rect5check = Rectangle(pos=pos10_3_8_5, rgba=(0, 0, 1, 1), size=c_size)
           self.rect6check = Rectangle(pos=pos10_3_8_6, rgba=(0, 0, 1, 1), size=c_size)
           self.rect7check = Rectangle(pos=pos10_3_8_7, rgba=(0, 0, 1, 1), size=c_size)
           self.rect8check = Rectangle(pos=pos10_3_8_8, rgba=(0, 0, 1, 1), size=c_size)
           self.rect9check = Rectangle(pos=pos10_3_8_9, rgba=(0, 0, 1, 1), size=c_size)
           self.rect10check = Rectangle(pos=pos10_3_8_10, rgba=(0, 0, 1, 1), size=c_size)



        self.rect1 = DraggableRectangle(source = "images/ctg_a-b.png", pos=r_pos10_3_8_1, size=d_size)
        self.rect2 = DraggableRectangle(source = "images/ravno.png", pos=r_pos10_3_8_2, size=d_size)
        self.rect3 = DraggableRectangle(source = "images/drob.png", pos=r_pos10_3_8_3, size=drobd_size)
        self.rect4 = DraggableRectangle(source = "images/ctg_a.png", pos=r_pos10_3_8_4, size=d_size)
        self.rect5 = DraggableRectangle(source = "images/ctg_b.png", pos=r_pos10_3_8_5, size=d_size)
        self.rect6 = DraggableRectangle(source = "images/plus.png", pos=r_pos10_3_8_6, size=d_size)
        self.rect7 = DraggableRectangle(source = "images/1.png", pos=r_pos10_3_8_7, size=d_size)
        self.rect8 = DraggableRectangle(source = "images/ctg_a.png", pos=r_pos10_3_8_8, size=d_size)
        self.rect9 = DraggableRectangle(source = "images/minus.png", pos=r_pos10_3_8_9, size=d_size)
        self.rect10 = DraggableRectangle(source = "images/ctg_b.png", pos=r_pos10_3_8_10, size=d_size)



        self.add_widget(self.rect1)
        self.add_widget(self.rect2)
        self.add_widget(self.rect3)
        self.add_widget(self.rect4)
        self.add_widget(self.rect5)
        self.add_widget(self.rect6)
        self.add_widget(self.rect7)
        self.add_widget(self.rect8)
        self.add_widget(self.rect9)
        self.add_widget(self.rect10)



    def check_collision(self):
       if collides_puzzle2(self.rect1, self.rect1check) and collides_puzzle2(self.rect2, self.rect2check) and  collides_puzzle2(self.rect3, self.rect3check) and collides_puzzle2(self.rect4, self.rect4check)and collides_puzzle2(self.rect5, self.rect5check) and collides_puzzle2(self.rect6, self.rect6check) and collides_puzzle2(self.rect7, self.rect7check) and collides_puzzle2(self.rect8, self.rect8check) and collides_puzzle2(self.rect9, self.rect9check) and collides_puzzle2(self.rect10, self.rect10check):
           self.rect1.color.rgba = (0, 1, 0, 1)
           self.c1.rgba = green_color
           print('yes')
       else:
           self.rect1.color.rgba = (1, 0, 0, 1)
           self.c1.rgba = red_color
           print('no')

#виджеты 9 класс пазлы

#тема 1

class Puzzle10_1Widget(Widget):


    def __init__(self, **kwargs):
        super(Puzzle10_1Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/sina.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/sin180+a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/sin180-a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/cos180-a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_1Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_1Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/sin180-a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/sin180+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/cos180-a_incor.png"))
            
            return True

        return super(Puzzle10_1Widget, self).on_touch_move(touch)

class Puzzle10_2Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_2Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-sina.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/cos180-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/cos180+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/sin180+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_2Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_2Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):   

                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/sin180+a_cor.png"))

                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):

                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/cos180+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/cos180-a_incor.png"))
            
            return True

        return super(Puzzle10_2Widget, self).on_touch_move(touch)

class Puzzle10_3Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_3Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-cosa.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/cos180-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/cos135+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/cos180+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_3Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_3Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/cos180-a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/cos135+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/cos180+a_incor.png"))
            
            return True

        return super(Puzzle10_3Widget, self).on_touch_move(touch)

class Puzzle10_4Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_4Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-cosa.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/sin180-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/cos180+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/cos135+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_4Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_4Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/cos180+a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               

                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/sin180-a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/cos135+a_incor.png"))
            
            return True

        return super(Puzzle10_4Widget, self).on_touch_move(touch)

class Puzzle10_5Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_5Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/cosa.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/sin180+a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/sin100-a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/cos100+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_5Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_5Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/sin100-a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/sin180+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/sin100+a_incor.png"))
            
            return True

        return super(Puzzle10_5Widget, self).on_touch_move(touch)

class Puzzle10_6Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_6Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-sina.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/cos100-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/sin100-a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/cos100+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_6Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_6Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/sin100+a.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):

                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/sin100-a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):

                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/cos100-a_incor.png"))
            
            return True

        return super(Puzzle10_6Widget, self).on_touch_move(touch)

class Puzzle10_7Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_7Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-cosa.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/sin135-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/cos135+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/sin100-a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_7Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_7Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):

                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/sin135-a_cor.png"))

            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):

                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/cos135+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/sin100-a_incor.png"))
            
            return True

        return super(Puzzle10_7Widget, self).on_touch_move(touch)

class Puzzle10_8Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_8Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/sina.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/sin180+a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/cos135+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/sin135-a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_8Widget, self).on_touch_down(touch)


    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_8Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/sin135+a_cor.png"))

            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/sin180+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/sin135-a_incor.png"))
            
            return True

        return super(Puzzle10_8Widget, self).on_touch_move(touch)

class Puzzle10_9Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_9Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/ctga.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/Ctg90-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/tg90-a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/tg90+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_9Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_9Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/tg90-a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/Ctg90-a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/tg90+a_incor.png"))
            
            return True

        return super(Puzzle10_9Widget, self).on_touch_move(touch)

class Puzzle10_10Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_10Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/tga.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/tg90+a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/Ctg90+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/Ctg90-a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_10Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_10Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/Ctg90-a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/Ctg90+a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/tg90+a_incor.png"))
            
            return True

        return super(Puzzle10_10Widget, self).on_touch_move(touch)

class Puzzle10_11Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_11Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-ctga.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/tg90+a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/Ctg90-a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/Ctg90+a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_11Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_11Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/tg90+a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/Ctg90-a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/Ctg90+a_incor.png"))
            
            return True

        return super(Puzzle10_11Widget, self).on_touch_move(touch)

class Puzzle10_12Widget(Widget):
    def __init__(self, **kwargs):
        super(Puzzle10_12Widget, self).__init__(**kwargs)
        self.size = (200, 100)
        with self.canvas:
            
            self.rect1 = Rectangle(pos=(rect_pos1),color=(1,1,1), size = (rect_size), source="images/-tga.png")
            self.rect2 = Rectangle(pos=(rect_pos2),color=(0,1,1), size = (rect_size), source="images/Ctg90-a.png")
            self.rect3 = Rectangle(pos=(rect_pos3),color=(1,1,0), size = (rect_size), source="images/Ctg90+a.png")
            self.rect4 = Rectangle(pos=(rect_pos4),color=(1,0,1), size = (rect_size), source="images/tg90-a.png")

        self.bind(pos=self.redraw, size=self.redraw)
    def Правильно (self):
        self.unbind(pos=self.redraw, size=self.redraw)

    def collide_widget(self, wid):
        print('col')
        return super().collide_widget(wid)

    def redraw(self, *args):
        
        self.rect1.pos = self.pos
        

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            

            return True

        return super(Puzzle10_12Widget, self).on_touch_down(touch)

    def on_touch_up(self, touch):
       
        if touch.grab_current is self:
           
            touch.ungrab(self)
            

            return True

        return super(Puzzle10_12Widget, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        
        if touch.grab_current is self:
            self.pos = touch.pos
            
            if collides((self.rect1.pos, self.rect1.size),(self.rect3.pos, self.rect3.size)):
                
                self.canvas.add(Rectangle(pos=(rect_pos3), size = (rect_size), source="images/Ctg90+a_cor.png"))
            
                self.Правильно()

            if collides((self.rect1.pos, self.rect1.size),(self.rect2.pos, self.rect2.size)):
               
                self.canvas.add(Rectangle(pos=(rect_pos2), size = (rect_size), source="images/Ctg90-a_incor.png"))
                
            if collides((self.rect1.pos, self.rect1.size),(self.rect4.pos, self.rect4.size)):
                

                self.canvas.add(Rectangle(pos=(rect_pos4), size = (rect_size), source="images/tg90-a_incor.png"))
            
            return True

        return super(Puzzle10_12Widget, self).on_touch_move(touch)

#задания 9 класс:

class MenuScreen(Screen):
    pass

class class9Screen(Screen):
    pass

class class10Screen(Screen):
    pass

class teory9Screen(Screen):
    pass
class teory9_2Screen(Screen):
    pass
class teory9_3Screen(Screen):
    pass

class teory10Screen(Screen):
    pass
class teory10_2Screen(Screen):
    pass
class teory10_3Screen(Screen):
    pass
class teory10_4Screen(Screen):
    pass
class teory10_5Screen(Screen):
    pass



class puzzles9Screen(Screen):
    pass
class puzzles9_2Screen(Screen):
    pass
class puzzles9_3Screen(Screen):
    pass

class puzzles10Screen(Screen):
    pass
class puzzles10_2Screen(Screen):
    pass
class puzzles10_3Screen(Screen):
    pass
class puzzles10_4Screen(Screen):
    pass
class puzzles10_5Screen(Screen):
    pass
class puzzle9_1Screen(Screen):
    pass
class puzzle9_2Screen(Screen):
    pass
class puzzle9_3Screen(Screen):
    pass
class puzzle9_4Screen(Screen):
    pass
class puzzle9_5Screen(Screen):
    pass
class puzzle9_6Screen(Screen):
    pass
class puzzle9_7Screen(Screen):
    pass
class puzzle9_8Screen(Screen):
    pass
class puzzle9_9Screen(Screen):
    pass
class puzzle9_10Screen(Screen):
    pass
class puzzle9_11Screen(Screen):
    pass
class puzzle9_12Screen(Screen):
    pass
class puzzle9_3_1Screen(Screen):
    pass
class puzzle9_3_2Screen(Screen):
    pass
class puzzle9_3_3Screen(Screen):
    pass
class puzzle9_3_4Screen(Screen):
    pass
class puzzle10_1Screen(Screen):
    pass
class puzzle10_2Screen(Screen):
    pass
class puzzle10_3Screen(Screen):
    pass
class puzzle10_4Screen(Screen):
    pass
class puzzle10_5Screen(Screen):
    pass
class puzzle10_6Screen(Screen):
    pass
class puzzle10_7Screen(Screen):
    pass
class puzzle10_8Screen(Screen):
    pass
class puzzle10_9Screen(Screen):
    pass
class puzzle10_10Screen(Screen):
    pass
class puzzle10_11Screen(Screen):
    pass
class puzzle10_12Screen(Screen):
    pass
class puzzle10_2_1Screen(Screen):
    pass
class puzzle10_2_2Screen(Screen):
    pass
class puzzle10_2_3Screen(Screen):
    pass
class puzzle10_2_4Screen(Screen):
    pass
class puzzle10_2_5Screen(Screen):
    pass
class puzzle10_2_6Screen(Screen):
    pass
class puzzle10_2_7Screen(Screen):
    pass
class puzzle10_2_8Screen(Screen):
    pass
class puzzle10_3_1Screen(Screen):
    pass
class puzzle10_3_2Screen(Screen):
    pass
class puzzle10_3_3Screen(Screen):
    pass
class puzzle10_3_4Screen(Screen):
    pass
class puzzle10_3_5Screen(Screen):
    pass
class puzzle10_3_6Screen(Screen):
    pass
class tasks10Screen(Screen):
    pass
class tasks10_2Screen(Screen):
    pass
class tasks10_3Screen(Screen):
    pass
class tasks9Screen(Screen):
    pass
class tasks9_2Screen(Screen):
    pass
class tasks9_3Screen(Screen):
    pass
class task10_1Screen(Screen):
    pass
class task10_2Screen(Screen):
    pass
class task10_3Screen(Screen):
    pass
class task10_4Screen(Screen):
    pass
class task10_5Screen(Screen):
    pass
class task10_6Screen(Screen):
    pass
class task10_7Screen(Screen):
    pass
class task10_8Screen(Screen):
    pass
class task10_9Screen(Screen):
    pass
class task9_1Screen(Screen):
    pass
class task9_2Screen(Screen):
    pass
class task9_3Screen(Screen):
    pass
class task9_4Screen(Screen):
    pass
class task9_5Screen(Screen):
   pass
class task9_6Screen(Screen):
    pass
class task9_7Screen(Screen):
    pass
class task9_8Screen(Screen):
    pass
class task9_9Screen(Screen):
    pass
class task9_1Screen(Screen):
    pass
class task9_2Screen(Screen):
    pass
class task9_3Screen(Screen):
    pass
class task9_4Screen(Screen):
    pass
class task9_5Screen(Screen):
    pass
class task9_6Screen(Screen):
    pass
class task9_7Screen(Screen):
    pass
class task9_8Screen(Screen):
    pass
class task9_9Screen(Screen):
    pass
class task9_2_1Screen(Screen):
    pass
class task9_2_2Screen(Screen):
    pass
class task9_2_3Screen(Screen):
    pass
class task9_2_4Screen(Screen):
    pass
class task9_2_5Screen(Screen):
    pass
class task9_2_6Screen(Screen):
    pass
class task9_2_7Screen(Screen):
    pass
class task9_2_8Screen(Screen):
    pass
class task9_2_9Screen(Screen):
    pass
class task9_3_1Screen(Screen):
    pass
class task9_3_2Screen(Screen):
    pass
class task9_3_3Screen(Screen):
    pass
class task9_3_4Screen(Screen):
    pass
class task9_3_5Screen(Screen):
    pass
class task9_3_6Screen(Screen):
    pass
class task9_3_7Screen(Screen):
    pass
class task9_3_8Screen(Screen):
    pass
class task9_3_9Screen(Screen):
    pass
class theme9_1Screen(Screen):
    pass
class theme9_2Screen(Screen):
    pass
class theme9_3Screen(Screen):
    pass
class theme10_1Screen(Screen):
    pass
class theme10_2Screen(Screen):
    pass
class theme10_3Screen(Screen):
    pass
class task10_2_1Screen(Screen):
    pass
class task10_2_2Screen(Screen):
    pass
class task10_2_3Screen(Screen):
    pass
class task10_2_4Screen(Screen):
    pass
class task10_2_5Screen(Screen):
    pass
class task10_2_6Screen(Screen):
    pass
class task10_2_7Screen(Screen):
    pass
class task10_2_8Screen(Screen):
    pass
class task10_2_9Screen(Screen):
    pass
class task10_3_1Screen(Screen):
    pass
class task10_3_2Screen(Screen):
    pass
class task10_3_3Screen(Screen):
    pass
class task10_3_4Screen(Screen):
    pass
class task10_3_5Screen(Screen):
    pass
class task10_3_6Screen(Screen):
    pass
class task10_3_7Screen(Screen):
    pass
class task10_3_8Screen(Screen):
    pass
class task10_3_9Screen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(class9Screen(name='profile'))
sm.add_widget(class10Screen(name='upload')) 
sm.add_widget(theme9_1Screen(name='theme9_1'))
sm.add_widget(theme9_2Screen(name='theme9_2'))
sm.add_widget(theme9_3Screen(name='theme9_3'))
sm.add_widget(theme10_1Screen(name='theme10_1'))
sm.add_widget(theme10_2Screen(name='theme10_2'))
sm.add_widget(theme10_3Screen(name='theme10_3'))
sm.add_widget(teory9Screen(name='teory9'))
sm.add_widget(teory9_2Screen(name='teory9_2'))
sm.add_widget(teory9_3Screen(name='teory9_3'))
sm.add_widget(teory10Screen(name='teory10'))
sm.add_widget(teory10_2Screen(name='teory10_2'))
sm.add_widget(teory10_3Screen(name='teory10_3'))
sm.add_widget(teory10_4Screen(name='teory10_4'))
sm.add_widget(teory10_5Screen(name='teory10_5'))
sm.add_widget(puzzles9Screen(name='puzzles9'))
sm.add_widget(puzzles9_3Screen(name='puzzles9_3'))
sm.add_widget(puzzles10Screen(name='puzzles10'))
sm.add_widget(puzzles10_2Screen(name='puzzles10_2'))
sm.add_widget(puzzles10_3Screen(name='puzzles9_3'))
sm.add_widget(puzzles10_4Screen(name='puzzles10_4'))
sm.add_widget(puzzles10_5Screen(name='puzzles9_5'))
sm.add_widget(tasks9Screen(name='tasks9'))
sm.add_widget(tasks9_2Screen(name='tasks9_2'))
sm.add_widget(tasks9_3Screen(name='tasks9_3'))
sm.add_widget(tasks10Screen(name='tasks10'))
sm.add_widget(tasks10_2Screen(name='tasks10_2'))
sm.add_widget(tasks10_3Screen(name='tasks10_3'))
sm.add_widget(puzzle9_1Screen(name='puzzle9_1'))
sm.add_widget(puzzle9_2Screen(name='puzzle9_2'))
sm.add_widget(puzzle9_3Screen(name='puzzle9_3'))
sm.add_widget(puzzle9_4Screen(name='puzzle9_4'))
sm.add_widget(puzzle9_5Screen(name='puzzle9_5'))
sm.add_widget(puzzle9_6Screen(name='puzzle9_6'))
sm.add_widget(puzzle9_7Screen(name='puzzle9_7'))
sm.add_widget(puzzle9_8Screen(name='puzzle9_8'))
sm.add_widget(puzzle9_9Screen(name='puzzle9_9'))
sm.add_widget(puzzle9_10Screen(name='puzzle9_10'))
sm.add_widget(puzzle9_11Screen(name='puzzle9_11'))
sm.add_widget(puzzle9_12Screen(name='puzzle9_12'))
sm.add_widget(puzzle9_3_1Screen(name='puzzle9_3_1'))
sm.add_widget(puzzle9_3_2Screen(name='puzzle9_3_2'))
sm.add_widget(puzzle9_3_3Screen(name='puzzle9_3_3'))
sm.add_widget(puzzle9_3_4Screen(name='puzzle9_3_4'))
sm.add_widget(puzzle10_1Screen(name='puzzle10_1'))
sm.add_widget(puzzle10_2Screen(name='puzzle10_2'))
sm.add_widget(puzzle10_3Screen(name='puzzle10_3'))
sm.add_widget(puzzle10_4Screen(name='puzzle10_4'))
sm.add_widget(puzzle10_5Screen(name='puzzle10_5'))
sm.add_widget(puzzle10_6Screen(name='puzzle10_6'))
sm.add_widget(puzzle10_7Screen(name='puzzle10_7'))
sm.add_widget(puzzle10_8Screen(name='puzzle10_8'))
sm.add_widget(puzzle10_9Screen(name='puzzle10_9'))
sm.add_widget(puzzle10_10Screen(name='puzzle10_10'))
sm.add_widget(puzzle10_11Screen(name='puzzle10_11'))
sm.add_widget(puzzle10_12Screen(name='puzzle10_12'))
sm.add_widget(puzzle10_2_1Screen(name='puzzle10_2_1'))
sm.add_widget(puzzle10_2_2Screen(name='puzzle10_2_2'))
sm.add_widget(puzzle10_2_3Screen(name='puzzle10_2_3'))
sm.add_widget(puzzle10_2_4Screen(name='puzzle10_2_4'))
sm.add_widget(puzzle10_2_5Screen(name='puzzle10_2_5'))
sm.add_widget(puzzle10_2_6Screen(name='puzzle10_2_6'))
sm.add_widget(puzzle10_2_7Screen(name='puzzle10_2_7'))
sm.add_widget(puzzle10_2_8Screen(name='puzzle10_2_8'))
sm.add_widget(puzzle10_3_1Screen(name='puzzle10_3_1'))
sm.add_widget(puzzle10_3_2Screen(name='puzzle10_3_2'))
sm.add_widget(puzzle10_3_3Screen(name='puzzle10_3_3'))
sm.add_widget(puzzle10_3_4Screen(name='puzzle10_3_4'))
sm.add_widget(puzzle10_3_5Screen(name='puzzle10_3_5'))
sm.add_widget(puzzle10_3_6Screen(name='puzzle10_3_6'))
sm.add_widget(task10_1Screen(name='task10_1'))
sm.add_widget(task10_2Screen(name='task10_2'))
sm.add_widget(task10_3Screen(name='task10_3'))
sm.add_widget(task10_4Screen(name='task10_4'))
sm.add_widget(task10_5Screen(name='task10_5'))
sm.add_widget(task10_6Screen(name='task10_6'))
sm.add_widget(task10_7Screen(name='task10_7'))
sm.add_widget(task10_8Screen(name='task10_8'))
sm.add_widget(task10_9Screen(name='task10_9'))
sm.add_widget(task10_2_1Screen(name='task10_2_1'))
sm.add_widget(task10_2_2Screen(name='task10_2_2'))
sm.add_widget(task10_2_3Screen(name='task10_2_3'))
sm.add_widget(task10_2_4Screen(name='task10_2_4'))
sm.add_widget(task10_2_5Screen(name='task10_2_5'))
sm.add_widget(task10_2_6Screen(name='task10_2_6'))
sm.add_widget(task10_2_7Screen(name='task10_2_7'))
sm.add_widget(task10_2_8Screen(name='task10_2_8'))
sm.add_widget(task10_2_9Screen(name='task10_2_9'))
sm.add_widget(task10_3_1Screen(name='task10_3_1'))
sm.add_widget(task10_3_2Screen(name='task10_3_2'))
sm.add_widget(task10_3_3Screen(name='task10_3_3'))
sm.add_widget(task10_3_4Screen(name='task10_3_4'))
sm.add_widget(task10_3_5Screen(name='task10_3_5'))
sm.add_widget(task10_3_6Screen(name='task10_3_6'))
sm.add_widget(task10_3_7Screen(name='task10_3_7'))
sm.add_widget(task10_3_8Screen(name='task10_3_8'))
sm.add_widget(task10_3_9Screen(name='task10_3_9'))
sm.add_widget(task9_1Screen(name='task9_1'))
sm.add_widget(task9_2Screen(name='task9_2'))
sm.add_widget(task9_3Screen(name='task9_3'))
sm.add_widget(task9_4Screen(name='task9_4'))
sm.add_widget(task9_5Screen(name='task9_5'))
sm.add_widget(task9_6Screen(name='task9_6'))
sm.add_widget(task9_7Screen(name='task9_7'))
sm.add_widget(task9_8Screen(name='task9_8'))
sm.add_widget(task9_9Screen(name='task9_9'))
sm.add_widget(task9_2_1Screen(name='task9_2_1'))
sm.add_widget(task9_2_2Screen(name='task9_2_2'))
sm.add_widget(task9_2_3Screen(name='task9_2_3'))
sm.add_widget(task9_2_4Screen(name='task9_2_4'))
sm.add_widget(task9_2_5Screen(name='task9_2_5'))
sm.add_widget(task9_2_6Screen(name='task9_2_6'))
sm.add_widget(task9_2_7Screen(name='task9_2_7'))
sm.add_widget(task9_2_8Screen(name='task9_2_8'))
sm.add_widget(task9_2_9Screen(name='task9_2_9'))
sm.add_widget(task9_3_1Screen(name='task9_3_1'))
sm.add_widget(task9_3_2Screen(name='task9_3_2'))
sm.add_widget(task9_3_3Screen(name='task9_3_3'))
sm.add_widget(task9_3_4Screen(name='task9_3_4'))
sm.add_widget(task9_3_5Screen(name='task9_3_5'))
sm.add_widget(task9_3_6Screen(name='task9_3_6'))
sm.add_widget(task9_3_7Screen(name='task9_3_7'))
sm.add_widget(task9_3_8Screen(name='task9_3_8'))
sm.add_widget(task9_3_9Screen(name='task9_3_9'))






class DemoApp(MDApp):

    
    def build(self):
        self.screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        self.answer9_1 = '1'#сделано
        self.answer9_2 = '6'
        self.answer9_22 = '6'
        self.answer9_3 = '1'
        self.answer9_32 = '2'
        self.answer9_4 = '3'
        self.answer9_42 = '2'
        self.answer9_5 = '6'
        self.answer9_52 = '4'
        self.answer9_6 = '3'
        self.answer9_62 = '2'
        self.answer9_7 = '3'
        self.answer9_72 = '6'
        self.answer9_8 = '3'
        self.answer9_82 = '2'
        self.answer9_9 = '3'
        self.answer9_92 = '4'

        self.answer9_2_1 = '21'
        self.answer9_2_2 = '33'
        self.answer9_2_3 = '0,25'
        self.answer9_2_4 = '16'
        self.answer9_2_5 = '3'
        self.answer9_2_6 = '9'
        self.answer9_2_7 = '0,6'
        self.answer9_2_8 = '0,4'
        self.answer9_2_9 = '4'

        self.answer9_3_1 = '2'
        self.answer9_3_12 = '3'
        self.answer9_3_2 = '13'
        self.answer9_3_3 = '12'
        self.answer9_3_32 = '13'
        self.answer9_3_4 = '5'
        self.answer9_3_42 = '14'
        self.answer9_3_5 = '29'
        self.answer9_3_6 = '4'
        self.answer9_3_62 = '5'
        self.answer9_3_7 = '1'
        self.answer9_3_72 = '3'
        self.answer9_3_8 = '2'
        self.answer9_3_9 = '1'
        self.answer9_3_92 = '4'


        self.answer10_1 = '2'
        self.answer10_12 = '-2'
        self.answer10_2 = '3'
        self.answer10_22 = '2'
        self.answer10_3 = '2'
        self.answer10_32 = '-2'
        self.answer10_4 = '1'
        self.answer10_42 = '-2'
        self.answer10_5 = '-cos(a)'
        self.answer10_6 = '1'
        self.answer10_7 = '2'
        self.answer10_8 = '1'
        self.answer10_9 = '2'

        self.answer10_2_1 = 'cos^2(a)'
        self.answer10_2_2 = 'sin25'
        self.answer10_2_3 = 'sin(a)+cos(a)'
        self.answer10_2_4 = 'cos(0,5a)'
        self.answer10_2_5 = '1'
        self.answer10_2_52 = '2'
        self.answer10_2_6 = 'tg(2a)'
        self.answer10_2_62 = '2'
        self.answer10_2_7 = 'sin(2a)'
        self.answer10_2_8 = 'ctg(2a)'
        self.answer10_2_82 = '-2'
        self.answer10_2_9 = '1'

        self.answer10_3_1 = 'sin(5a)'
        self.answer10_3_2 = '0'
        self.answer10_3_3 = 'cos(b)'
        self.answer10_3_4 = '3'
        self.answer10_3_42 = '2'
        self.answer10_3_5 = 'cos(a-b)'
        self.answer10_3_6 = 'cos(8a)'
        self.answer10_3_7 = '3'
        self.answer10_3_72 = '2'
        self.answer10_3_8 = '3'
        self.answer10_3_9 = 'cos(a+b)'




        return self.screen
    def check_answer9_1(self):
        user_answer = self.screen.ids.task9_1_1.ids.text_field_error9_1.text
        if user_answer == self.answer9_1:
            self.screen.ids.task9_1_1.ids.submit9_1.text = "Правильно"
            self.screen.ids.task9_1_1.ids.next9_1.disabled = False
            self.screen.ids.tasks9.ids.button9_2task.disabled = False
            self.screen.ids.tasks9.ids.button9_1task.md_bg_color = 'lightgreen'
            
        else:
            self.screen.ids.task9_1_1.ids.submit9_1.text = "Попробуй ещё раз"
            self.screen.ids.task9_1_1.ids.text_field_error9_1.text = ""
            self.screen.ids.task9_1_1.ids.text_field_error9_1.helper_text = "Ошибка"
            self.screen.ids.tasks9.ids.button9_1task.md_bg_color = "red"



########################################################################################################################################


    def check_answer9_2(self):
        user_answer = self.screen.ids.task9_2_1.ids.text_field_error9_2.text
        user_answer_2 = self.screen.ids.task9_2_1.ids.text_field_error9_22.text

        if user_answer == self.answer9_2 and user_answer_2 == self.answer9_22:
            self.screen.ids.task9_2_1.ids.submit9_2.text = "Правильно"
            self.screen.ids.task9_2_1.ids.next9_2.disabled =False
            self.screen.ids.tasks9.ids.button9_3task.disabled = False

            self.screen.ids.tasks9.ids.button9_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_2_1.ids.submit9_2.text = "Попробуй ещё раз"
            self.screen.ids.task9_2_1.ids.text_field_error9_2.text = ""
            self.screen.ids.task9_2_1.ids.text_field_error9_22.text = ""

            self.screen.ids.task9_2_1.ids.text_field_error9_2.helper_text = "Ошибка"
            self.screen.ids.tasks9.ids.button9_2task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_3(self):
        user_answer = self.screen.ids.task9_3_1.ids.text_field_error9_3.text
        user_answer_2 = self.screen.ids.task9_3_1.ids.text_field_error9_32.text
        if user_answer == self.answer9_3 and user_answer_2 == self.answer9_32:
            self.screen.ids.task9_3_1.ids.submit9_3.text = "Правильно"
            self.screen.ids.task9_3_1.ids.next9_3.disabled = False
            self.screen.ids.tasks9.ids.button9_4task.disabled = False

            self.screen.ids.tasks9.ids.button9_3task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_3_1.ids.submit9_3.text = "Попробуй ещё раз"
            self.screen.ids.task9_3_1.ids.text_field_error9_3.text = ""
            self.screen.ids.task9_3_1.ids.text_field_error9_32.text = ""
            
            self.screen.ids.task9_3_1.ids.text_field_error9_3.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_3task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_4(self):
        user_answer = self.screen.ids.task9_4_1.ids.text_field_error9_4.text
        user_answer_2 = self.screen.ids.task9_4_1.ids.text_field_error9_42.text
        if user_answer == self.answer9_4 and user_answer_2 == self.answer9_42:
            self.screen.ids.task9_4_1.ids.submit9_4.text = "Правильно"
            self.screen.ids.task9_4_1.ids.next9_4.disabled = False
            self.screen.ids.tasks9.ids.button9_5task.disabled = False

            self.screen.ids.tasks9.ids.button9_4task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_4_1.ids.submit9_4.text = "Попробуй ещё раз"
            self.screen.ids.task9_4_1.ids.text_field_error9_4.text = ""
            self.screen.ids.task9_4_1.ids.text_field_error9_42.text = ""
            self.screen.ids.task9_4_1.ids.text_field_error9_4.helper_text = "Ошибка"
            self.screen.ids.tasks9.ids.button9_4task.md_bg_color = "red"
########################################################################################################################################

    def check_answer9_5(self):
        user_answer = self.screen.ids.task9_5_1.ids.text_field_error9_5.text
        user_answer_2 = self.screen.ids.task9_5_1.ids.text_field_error9_52.text
        if user_answer == self.answer9_5 and user_answer_2 == self.answer9_52:
            self.screen.ids.task9_5_1.ids.submit9_5.text = "Правильно"

            self.screen.ids.task9_5_1.ids.next9_5.disabled = False
            self.screen.ids.tasks9.ids.button9_6task.disabled = False

            self.screen.ids.tasks9.ids.button9_5task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_5_1.ids.submit9_5.text = "Попробуй ещё раз"

            self.screen.ids.task9_5_1.ids.text_field_error9_5.text = ""
            self.screen.ids.task9_5_1.ids.text_field_error9_52.text = ""
            self.screen.ids.task9_5_1.ids.text_field_error9_5.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_5task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_6(self):
        user_answer = self.screen.ids.task9_6_1.ids.text_field_error9_6.text
        user_answer_2 = self.screen.ids.task9_6_1.ids.text_field_error9_62.text
        if user_answer == self.answer9_6 and user_answer_2 == self.answer9_62:
            self.screen.ids.task9_6_1.ids.submit9_6.text = "Правильно"

            self.screen.ids.task9_6_1.ids.next9_6.disabled = False
            self.screen.ids.tasks9.ids.button9_7task.disabled = False

            self.screen.ids.tasks9.ids.button9_6task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_6_1.ids.submit9_6.text = "Попробуй ещё раз"

            self.screen.ids.task9_6_1.ids.text_field_error9_6.text = ""
            self.screen.ids.task9_6_1.ids.text_field_error9_62.text = ""
            self.screen.ids.task9_6_1.ids.text_field_error9_6.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_6task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_7(self):
        user_answer = self.screen.ids.task9_7_1.ids.text_field_error9_7.text
        user_answer_2 = self.screen.ids.task9_7_1.ids.text_field_error9_72.text
        if user_answer == self.answer9_7 and user_answer_2 == self.answer9_72:
            self.screen.ids.task9_7_1.ids.submit9_7.text = "Правильно"
            self.screen.ids.task9_7_1.ids.next9_7.disabled = False
            self.screen.ids.tasks9.ids.button9_8task.disabled = False

            self.screen.ids.tasks9.ids.button9_7task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_7_1.ids.submit9_7.text = "Попробуй ещё раз"
            self.screen.ids.task9_7_1.ids.text_field_error9_7.text = ""
            self.screen.ids.task9_7_1.ids.text_field_error9_72.text = ""

            self.screen.ids.task9_7_1.ids.text_field_error9_7.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_7task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_8(self):
        user_answer = self.screen.ids.task9_8_1.ids.text_field_error9_8.text
        user_answer_2 = self.screen.ids.task9_8_1.ids.text_field_error9_82.text
        if user_answer == self.answer9_8 and user_answer_2 == self.answer9_82:
            self.screen.ids.task9_8_1.ids.submit9_8.text = "Правильно"
            self.screen.ids.task9_8_1.ids.next9_8.disabled = False
            self.screen.ids.tasks9.ids.button9_9task.disabled = False

            self.screen.ids.tasks9.ids.button9_8task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_8_1.ids.submit9_8.text = "Попробуй ещё раз"
            self.screen.ids.task9_8_1.ids.text_field_error9_8.text = ""
            self.screen.ids.task9_8_1.ids.text_field_error9_82.text = ""
            self.screen.ids.task9_8_1.ids.text_field_error9_8.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_8task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_9(self):
        user_answer = self.screen.ids.task9_9_1.ids.text_field_error9_9.text
        user_answer_2 = self.screen.ids.task9_9_1.ids.text_field_error9_92.text
        if user_answer == self.answer9_9 and user_answer_2 == self.answer9_92:
            self.screen.ids.task9_9_1.ids.submit9_9.text = "Правильно"
            self.screen.ids.task9_9_1.ids.next9_9.disabled = False

            self.screen.ids.tasks9.ids.button9_9task.md_bg_color = "lightgreen"
            self.screen.ids.theme9_1.ids.button9_1tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_9_1.ids.submit9_9.text = "Попробуй ещё раз"
            self.screen.ids.task9_9_1.ids.text_field_error9_9.text = ""
            self.screen.ids.task9_9_1.ids.text_field_error9_92.text = ""
            self.screen.ids.task9_9_1.ids.text_field_error9_9.helper_text = "Ошибка"

            self.screen.ids.tasks9.ids.button9_9task.md_bg_color = "red"

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

    def check_answer9_2_1(self):
        user_answer = self.screen.ids.task9_1_2.ids.text_field_error9_2_1.text
        if user_answer == self.answer9_2_1:
            self.screen.ids.task9_1_2.ids.submit9_2_1.text = "Правильно"
            self.screen.ids.task9_1_2.ids.next9_2_1.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_2task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_1task.md_bg_color = 'lightgreen'
            
        else:
            self.screen.ids.task9_1_2.ids.submit9_2_1.text = "Попробуй ещё раз"
            self.screen.ids.task9_1_2.ids.text_field_error9_2_1.text = ""
            self.screen.ids.task9_1_2.ids.text_field_error9_2_1.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_1task.md_bg_color = 'red'


########################################################################################################################################


    def check_answer9_2_2(self):
        user_answer = self.screen.ids.task9_2_2.ids.text_field_error9_2_2.text
        if user_answer == self.answer9_2_2:
            self.screen.ids.task9_2_2.ids.submit9_2_2.text = "Правильно"
            self.screen.ids.task9_2_2.ids.next9_2_2.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_3task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_2_2.ids.submit9_2_2.text = "Попробуй ещё раз"
            self.screen.ids.task9_2_2.ids.text_field_error9_2_2.text = ""
            self.screen.ids.task9_2_2.ids.text_field_error9_2_2.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_2task.md_bg_color = 'red'


########################################################################################################################################

    def check_answer9_2_3(self):
        user_answer = self.screen.ids.task9_3_2.ids.text_field_error9_2_3.text
        if user_answer == self.answer9_2_3:
            self.screen.ids.task9_3_2.ids.submit9_2_3.text = "Правильно"
            self.screen.ids.task9_3_2.ids.next9_2_3.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_4task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_3task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_3_2.ids.submit9_2_3.text = "Попробуй ещё раз"
            self.screen.ids.task9_3_2.ids.text_field_error9_2_3.text = ""
            self.screen.ids.task9_3_2.ids.text_field_error9_2_3.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_3task.md_bg_color = 'red'


########################################################################################################################################

    def check_answer9_2_4(self):
        user_answer = self.screen.ids.task9_4_2.ids.text_field_error9_2_4.text
        if user_answer == self.answer9_2_4:
            self.screen.ids.task9_4_2.ids.submit9_2_4.text = "Правильно"
            self.screen.ids.task9_4_2.ids.next9_2_4.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_5task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_4task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_4_2.ids.submit9_2_4.text = "Попробуй ещё раз"
            self.screen.ids.task9_4_2.ids.text_field_error9_2_4.text = ""
            self.screen.ids.task9_4_2.ids.text_field_error9_2_4.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_4task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_2_5(self):
        user_answer = self.screen.ids.task9_5_2.ids.text_field_error9_2_5.text
        if user_answer == self.answer9_2_5:
            self.screen.ids.task9_5_2.ids.submit9_2_5.text = "Правильно"
            self.screen.ids.task9_5_2.ids.next9_2_5.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_6task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_5task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_5_2.ids.submit9_2_5.text = "Попробуй ещё раз"
            self.screen.ids.task9_5_2.ids.text_field_error9_2_5.text = ""
            self.screen.ids.task9_5_2.ids.text_field_error9_2_5.helper_text = "Ошибка"
            self.screen.ids.tasks9_2.ids.button9_2_5task.md_bg_color = 'red'
            


########################################################################################################################################

    def check_answer9_2_6(self):
        user_answer = self.screen.ids.task9_6_2.ids.text_field_error9_2_6.text
        if user_answer == self.answer9_2_6:
            self.screen.ids.task9_6_2.ids.submit9_2_6.text = "Правильно"
            self.screen.ids.task9_6_2.ids.next9_2_6.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_7task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_6task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_6_2.ids.submit9_2_6.text = "Попробуй ещё раз"
            self.screen.ids.task9_6_2.ids.text_field_error9_2_6.text = ""
            self.screen.ids.task9_6_2.ids.text_field_error9_2_6.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_6task.md_bg_color = 'red'


########################################################################################################################################

    def check_answer9_2_7(self):
        user_answer = self.screen.ids.task9_7_2.ids.text_field_error9_2_7.text
        if user_answer == self.answer9_2_7:
            self.screen.ids.task9_7_2.ids.submit9_2_7.text = "Правильно"
            self.screen.ids.task9_7_2.ids.next9_2_7.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_8task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_7task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_7_2.ids.submit9_2_7.text = "Попробуй ещё раз"
            self.screen.ids.task9_7_2.ids.text_field_error9_2_7.text = ""
            self.screen.ids.task9_7_2.ids.text_field_error9_2_7.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_7task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer9_2_8(self):
        user_answer = self.screen.ids.task9_8_2.ids.text_field_error9_2_8.text
        if user_answer == self.answer9_2_8:
            self.screen.ids.task9_8_2.ids.submit9_2_8.text = "Правильно"
            self.screen.ids.task9_8_2.ids.next9_2_8.disabled = False
            self.screen.ids.tasks9_2.ids.button9_2_9task.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_8task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_8_2.ids.submit9_2_8.text = "Попробуй ещё раз"
            self.screen.ids.task9_8_2.ids.text_field_error9_2_8.text = ""
            self.screen.ids.task9_8_2.ids.text_field_error9_2_8.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_8task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer9_2_9(self):
        user_answer = self.screen.ids.task9_9_2.ids.text_field_error9_2_9.text
        if user_answer == self.answer9_2_9:
            self.screen.ids.task9_9_2.ids.submit9_2_9.text = "Правильно"
            self.screen.ids.task9_9_2.ids.next9_2_9.disabled = False
            
            self.screen.ids.tasks9_2.ids.button9_2_9task.md_bg_color = 'lightgreen'
            self.screen.ids.theme9_2.ids.button9_2tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_9_2.ids.submit9_2_9.text = "Попробуй ещё раз"
            self.screen.ids.task9_9_2.ids.text_field_error9_2_9.text = ""
            self.screen.ids.task9_9_2.ids.text_field_error9_2_9.helper_text = "Ошибка"

            self.screen.ids.tasks9_2.ids.button9_2_9task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer9_3_1(self):
        user_answer = self.screen.ids.task9_1_3.ids.text_field_error9_3_1.text
        user_answer_2 = self.screen.ids.task9_1_3.ids.text_field_error9_3_12.text
        if user_answer == self.answer9_3_1 and user_answer_2 == self.answer9_3_12:
            self.screen.ids.task9_1_3.ids.submit9_3_1.text = "Правильно"
            self.screen.ids.task9_1_3.ids.next9_3_1.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_2task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_1task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_1_3.ids.submit9_3_1.text = "Попробуй ещё раз"
            self.screen.ids.task9_1_3.ids.text_field_error9_3_1.text = ""
            self.screen.ids.task9_1_3.ids.text_field_error9_3_12.text = ""
            self.screen.ids.task9_1_3.ids.text_field_error9_3_1.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_1task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_3_2(self):
        user_answer = self.screen.ids.task9_2_3.ids.text_field_error9_3_2.text
        if user_answer == self.answer9_3_2:
            self.screen.ids.task9_2_3.ids.submit9_3_2.text = "Правильно"
            self.screen.ids.task9_2_3.ids.next9_3_2.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_3task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_2_3.ids.submit9_3_2.text = "Попробуй ещё раз"
            self.screen.ids.task9_2_3.ids.text_field_error9_3_2.text = ""
            self.screen.ids.task9_2_3.ids.text_field_error9_3_2.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_2task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_3_3(self):
        user_answer = self.screen.ids.task9_3_3.ids.text_field_error9_3_3.text
        user_answer_2 = self.screen.ids.task9_3_3.ids.text_field_error9_3_32.text
        if user_answer == self.answer9_3_3 and user_answer_2 == self.answer9_3_32:
            self.screen.ids.task9_3_3.ids.submit9_3_3.text = "Правильно"
            self.screen.ids.task9_3_3.ids.next9_3_3.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_4task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_3task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_3_3.ids.submit9_3_3.text = "Попробуй ещё раз"
            self.screen.ids.task9_3_3.ids.text_field_error9_3_3.text = ""
            self.screen.ids.task9_3_3.ids.text_field_error9_3_32.text = ""
            self.screen.ids.task9_3_3.ids.text_field_error9_3_3.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_3task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_3_4(self):
        user_answer = self.screen.ids.task9_4_3.ids.text_field_error9_3_4.text
        user_answer_2 = self.screen.ids.task9_4_3.ids.text_field_error9_3_42.text
        if user_answer == self.answer9_3_4 and user_answer_2 == self.answer9_3_42:
            self.screen.ids.task9_4_3.ids.submit9_3_4.text = "Правильно"
            self.screen.ids.task9_4_3.ids.next9_3_4.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_5task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_4task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_4_3.ids.submit9_3_4.text = "Попробуй ещё раз"
            self.screen.ids.task9_4_3.ids.text_field_error9_3_4.text = ""
            self.screen.ids.task9_4_3.ids.text_field_error9_3_42.text = ""
            self.screen.ids.task9_4_3.ids.text_field_error9_3_4.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_4task.md_bg_color = "red"


########################################################################################################################################

    def check_answer9_3_5(self):
        user_answer = self.screen.ids.task9_5_3.ids.text_field_error9_3_5.text
        if user_answer == self.answer9_3_5:
            self.screen.ids.task9_5_3.ids.submit9_3_5.text = "Правильно"
            self.screen.ids.task9_5_3.ids.next9_3_5.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_6task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_5task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_5_3.ids.submit9_3_5.text = "Попробуй ещё раз"
            self.screen.ids.task9_5_3.ids.text_field_error9_3_5.text = ""
            self.screen.ids.task9_5_3.ids.text_field_error9_3_5.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_5task.md_bg_color = "red"


########################################################################################################################################
    def check_answer9_3_6(self):
        user_answer = self.screen.ids.task9_6_3.ids.text_field_error9_3_6.text
        user_answer_2 = self.screen.ids.task9_6_3.ids.text_field_error9_3_62.text
        if user_answer == self.answer9_3_6 and user_answer_2 == self.answer9_3_62:
            self.screen.ids.task9_6_3.ids.submit9_3_6.text = "Правильно"
            self.screen.ids.task9_6_3.ids.next9_3_6.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_7task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_6task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_6_3.ids.submit9_3_6.text = "Попробуй ещё раз"
            self.screen.ids.task9_6_3.ids.text_field_error9_3_6.text = ""
            self.screen.ids.task9_6_3.ids.text_field_error9_3_62.text = ""
            self.screen.ids.task9_6_3.ids.text_field_error9_3_6.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_6task.md_bg_color = "red"

########################################################################################################################################

    def check_answer9_3_7(self):
        user_answer = self.screen.ids.task9_7_3.ids.text_field_error9_3_7.text
        user_answer_2 = self.screen.ids.task9_7_3.ids.text_field_error9_3_72.text
        if user_answer == self.answer9_3_7 and user_answer_2 == self.answer9_3_72:
            self.screen.ids.task9_7_3.ids.submit9_3_7.text = "Правильно"
            self.screen.ids.task9_7_3.ids.next9_3_7.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_8task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_7task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_7_3.ids.submit9_3_7.text = "Попробуй ещё раз"
            self.screen.ids.task9_7_3.ids.text_field_error9_3_7.text = ""
            self.screen.ids.task9_7_3.ids.text_field_error9_3_72.text = ""
            self.screen.ids.task9_7_3.ids.text_field_error9_3_7.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_7task.md_bg_color = "red"

########################################################################################################################################

    def check_answer9_3_8(self):
        user_answer = self.screen.ids.task9_8_3.ids.text_field_error9_3_8.text
        if user_answer == self.answer9_3_8:
            self.screen.ids.task9_8_3.ids.submit9_3_8.text = "Правильно"
            self.screen.ids.task9_8_3.ids.next9_3_8.disabled = False
            self.screen.ids.tasks9_3.ids.button9_3_9task.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_8task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task9_8_3.ids.submit9_3_8.text = "Попробуй ещё раз"
            self.screen.ids.task9_8_3.ids.text_field_error9_3_8.text = ""
            self.screen.ids.task9_8_3.ids.text_field_error9_3_8.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_8task.md_bg_color = "red"

########################################################################################################################################

    def check_answer9_3_9(self):
        user_answer = self.screen.ids.task9_9_3.ids.text_field_error9_3_9.text
        user_answer_2 = self.screen.ids.task9_9_3.ids.text_field_error9_3_92.text
        if user_answer == self.answer9_3_9 and user_answer_2 == self.answer9_3_92:
            self.screen.ids.task9_9_3.ids.submit9_3_9.text = "Правильно"
            self.screen.ids.task9_9_3.ids.next9_3_9.disabled = False
            
            self.screen.ids.tasks9_3.ids.button9_3_9task.md_bg_color = 'lightgreen'
            self.screen.ids.theme9_3.ids.button9_3tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task9_9_3.ids.submit9_3_9.text = "Попробуй ещё раз"
            self.screen.ids.task9_9_3.ids.text_field_error9_3_9.text = ""
            self.screen.ids.task9_9_3.ids.text_field_error9_3_92.text = ""
            self.screen.ids.task9_9_3.ids.text_field_error9_3_9.helper_text = "Ошибка"

            self.screen.ids.tasks9_3.ids.button9_3_9task.md_bg_color = "red"
########################################################################################################################################

    def check_answer10_1(self):
        user_answer = self.screen.ids.task10_1_1.ids.text_field_error10_1.text
        user_answer_2 = self.screen.ids.task10_1_1.ids.text_field_error10_12.text
        if user_answer == self.answer10_1 and user_answer_2 == self.answer10_12:
            self.screen.ids.task10_1_1.ids.submit10_1.text = "Правильно"
            self.screen.ids.task10_1_1.ids.next10_1.disabled = False
            self.screen.ids.tasks10.ids.button10_2task.disabled = False
            
            self.screen.ids.tasks10.ids.button10_1task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_1_1.ids.submit10_1.text = "Попробуй ещё раз"
            self.screen.ids.task10_1_1.ids.text_field_error10_1.text = ""
            self.screen.ids.task10_1_1.ids.text_field_error10_12.text = ""
            self.screen.ids.task10_1_1.ids.text_field_error10_1.helper_text = "Ошибка"
            self.screen.ids.tasks10.ids.button10_1task.md_bg_color = "red"


########################################################################################################################################


    def check_answer10_2(self):
        user_answer = self.screen.ids.task10_2_1.ids.text_field_error10_2.text
        user_answer_2 = self.screen.ids.task10_2_1.ids.text_field_error10_22.text
        if user_answer == self.answer10_2 and user_answer_2 == self.answer10_22:
            self.screen.ids.task10_2_1.ids.submit10_2.text = "Правильно"
            self.screen.ids.task10_2_1.ids.next10_2.disabled =False
            self.screen.ids.tasks10.ids.button10_3task.disabled = False

            self.screen.ids.tasks10.ids.button10_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_2_1.ids.submit10_2.text = "Попробуй ещё раз"
            self.screen.ids.task10_2_1.ids.text_field_error10_2.text = ""
            self.screen.ids.task10_2_1.ids.text_field_error10_22.text = ""
            self.screen.ids.task10_2_1.ids.text_field_error10_2.helper_text = "Ошибка"
            self.screen.ids.tasks10.ids.button10_2task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_3(self):
        user_answer = self.screen.ids.task10_3_1.ids.text_field_error10_3.text
        user_answer_2 = self.screen.ids.task10_3_1.ids.text_field_error10_32.text
        if user_answer == self.answer10_3 and user_answer_2 == self.answer10_32:
            self.screen.ids.task10_3_1.ids.submit10_3.text = "Правильно"
            self.screen.ids.task10_3_1.ids.next10_3.disabled = False
            self.screen.ids.tasks10.ids.button10_4task.disabled = False

            self.screen.ids.tasks10.ids.button10_3task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_3_1.ids.submit10_3.text = "Попробуй ещё раз"
            self.screen.ids.task10_3_1.ids.text_field_error10_3.text = ""
            self.screen.ids.task10_3_1.ids.text_field_error10_32.text = ""
            
            self.screen.ids.task10_3_1.ids.text_field_error10_3.helper_text = "Ошибка"
            self.screen.ids.tasks10.ids.button10_3task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_4(self):
        user_answer = self.screen.ids.task10_4_1.ids.text_field_error10_4.text
        user_answer_2 = self.screen.ids.task10_4_1.ids.text_field_error10_42.text
        if user_answer == self.answer10_4 and user_answer_2 == self.answer10_42:
            self.screen.ids.task10_4_1.ids.submit10_4.text = "Правильно"
            self.screen.ids.task10_4_1.ids.next10_4.disabled = False
            self.screen.ids.tasks10.ids.button10_5task.disabled = False

            self.screen.ids.tasks10.ids.button10_4task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_4_1.ids.submit10_4.text = "Попробуй ещё раз"
            self.screen.ids.task10_4_1.ids.text_field_error10_4.text = ""
            self.screen.ids.task10_4_1.ids.text_field_error10_42.text = ""
            self.screen.ids.task10_4_1.ids.text_field_error10_4.helper_text = "Ошибка"
            self.screen.ids.tasks10.ids.button10_4task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_5(self):
        user_answer = self.screen.ids.task10_5_1.ids.text_field_error10_5.text
        if user_answer == self.answer10_5:
            self.screen.ids.task10_5_1.ids.submit10_5.text = "Правильно"

            self.screen.ids.task10_5_1.ids.next10_5.disabled = False
            self.screen.ids.tasks10.ids.button10_6task.disabled = False

            self.screen.ids.tasks10.ids.button10_5task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_5_1.ids.submit10_5.text = "Попробуй ещё раз"

            self.screen.ids.task10_5_1.ids.text_field_error10_5.text = ""
            self.screen.ids.task10_5_1.ids.text_field_error10_5.helper_text = "Ошибка"

            self.screen.ids.tasks10.ids.button10_5task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_6(self):
        user_answer = self.screen.ids.task10_6_1.ids.text_field_error10_6.text
        if user_answer == self.answer10_6:
            self.screen.ids.task10_6_1.ids.submit10_6.text = "Правильно"

            self.screen.ids.task10_6_1.ids.next10_6.disabled = False
            self.screen.ids.tasks10.ids.button10_7task.disabled = False

            self.screen.ids.tasks10.ids.button10_6task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_6_1.ids.submit10_6.text = "Попробуй ещё раз"

            self.screen.ids.task10_6_1.ids.text_field_error10_6.text = ""
            self.screen.ids.task10_6_1.ids.text_field_error10_6.helper_text = "Ошибка"

            self.screen.ids.tasks10.ids.button10_6task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_7(self):
        user_answer = self.screen.ids.task10_7_1.ids.text_field_error10_7.text
        if user_answer == self.answer10_7:
            self.screen.ids.task10_7_1.ids.submit10_7.text = "Правильно"
            self.screen.ids.task10_7_1.ids.next10_7.disabled = False
            self.screen.ids.tasks10.ids.button10_8task.disabled = False

            self.screen.ids.tasks10.ids.button10_7task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_7_1.ids.submit10_7.text = "Попробуй ещё раз"
            self.screen.ids.task10_7_1.ids.text_field_error10_7.text = ""
            self.screen.ids.task10_7_1.ids.text_field_error10_7.helper_text = "Ошибка"

            self.screen.ids.tasks10.ids.button10_7task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_8(self):
        user_answer = self.screen.ids.task10_8_1.ids.text_field_error10_8.text
        if user_answer == self.answer10_8:
            self.screen.ids.task10_8_1.ids.submit10_8.text = "Правильно"
            self.screen.ids.task10_8_1.ids.next10_8.disabled = False
            self.screen.ids.tasks10.ids.button10_9task.disabled = False

            self.screen.ids.tasks10.ids.button10_8task.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_8_1.ids.submit10_8.text = "Попробуй ещё раз"
            self.screen.ids.task10_8_1.ids.text_field_error10_8.text = ""
            self.screen.ids.task10_8_1.ids.text_field_error10_8.helper_text = "Ошибка"

            self.screen.ids.tasks10.ids.button10_8task.md_bg_color = "red"


########################################################################################################################################

    def check_answer10_9(self):
        user_answer = self.screen.ids.task10_9_1.ids.text_field_error10_9.text
        if user_answer == self.answer10_9:
            self.screen.ids.task10_9_1.ids.submit10_9.text = "Правильно"
            self.screen.ids.task10_9_1.ids.next10_9.disabled = False

            self.screen.ids.tasks10.ids.button10_9task.md_bg_color = "lightgreen"
            self.screen.ids.theme10_1.ids.button10_1tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_9_1.ids.submit10_9.text = "Попробуй ещё раз"
            self.screen.ids.task10_9_1.ids.text_field_error10_9.text = ""
            self.screen.ids.task10_9_1.ids.text_field_error10_9.helper_text = "Ошибка"

            self.screen.ids.tasks10.ids.button10_9task.md_bg_color = "red"


############################################################################################

    def check_answer10_2_1(self):
        user_answer = self.screen.ids.task10_1_2.ids.text_field_error10_2_1.text
        if user_answer == self.answer10_2_1:
            self.screen.ids.task10_1_2.ids.submit10_2_1.text = "Правильно"
            self.screen.ids.task10_1_2.ids.next10_2_1.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_2task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_1task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_1_2.ids.submit10_2_1.text = "Попробуй ещё раз"
            self.screen.ids.task10_1_2.ids.text_field_error10_2_1.text = ""
            self.screen.ids.task10_1_2.ids.text_field_error10_2_1.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_1task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_2(self):
        user_answer = self.screen.ids.task10_2_2.ids.text_field_error10_2_2.text
        if user_answer == self.answer10_2_2:
            self.screen.ids.task10_2_2.ids.submit10_2_2.text = "Правильно"
            self.screen.ids.task10_2_2.ids.next10_2_2.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_3task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_2_2.ids.submit10_2_2.text = "Попробуй ещё раз"
            self.screen.ids.task10_2_2.ids.text_field_error10_2_2.text = ""
            self.screen.ids.task10_2_2.ids.text_field_error10_2_2.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_2task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_3(self):
        user_answer = self.screen.ids.task10_3_2.ids.text_field_error10_2_3.text
        if user_answer == self.answer10_2_3:
            self.screen.ids.task10_3_2.ids.submit10_2_3.text = "Правильно"
            self.screen.ids.task10_3_2.ids.next10_2_3.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_4task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_3task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_3_2.ids.submit10_2_3.text = "Попробуй ещё раз"
            self.screen.ids.task10_3_2.ids.text_field_error10_2_3.text = ""
            self.screen.ids.task10_3_2.ids.text_field_error10_2_3.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_3task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_4(self):
        user_answer = self.screen.ids.task10_4_2.ids.text_field_error10_2_4.text
        if user_answer == self.answer10_2_4:
            self.screen.ids.task10_4_2.ids.submit10_2_4.text = "Правильно"
            self.screen.ids.task10_4_2.ids.next10_2_4.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_5task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_4task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_4_2.ids.submit10_2_4.text = "Попробуй ещё раз"
            self.screen.ids.task10_4_2.ids.text_field_error10_2_4.text = ""
            self.screen.ids.task10_4_2.ids.text_field_error10_2_4.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_4task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_2_5(self):
        user_answer = self.screen.ids.task10_5_2.ids.text_field_error10_2_5.text
        user_answer_2 = self.screen.ids.task10_5_2.ids.text_field_error10_2_52.text
        if user_answer == self.answer10_2_5 and user_answer_2 == self.answer10_2_52:
            self.screen.ids.task10_5_2.ids.submit10_2_5.text = "Правильно"
            self.screen.ids.task10_5_2.ids.next10_2_5.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_6task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_5task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_5_2.ids.submit10_2_5.text = "Попробуй ещё раз"
            self.screen.ids.task10_5_2.ids.text_field_error10_2_5.text = ""
            self.screen.ids.task10_5_2.ids.text_field_error10_2_52.text = ""
            self.screen.ids.task10_5_2.ids.text_field_error10_2_5.helper_text = "Ошибка"
            self.screen.ids.tasks10_2.ids.button10_2_5task.md_bg_color = 'red'
            

########################################################################################################################################

    def check_answer10_2_6(self):
        user_answer = self.screen.ids.task10_6_2.ids.text_field_error10_2_6.text
        user_answer_2 = self.screen.ids.task10_6_2.ids.text_field_error10_2_62.text
        if user_answer == self.answer10_2_6 and user_answer_2 == self.answer10_2_62:
            self.screen.ids.task10_6_2.ids.submit10_2_6.text = "Правильно"
            self.screen.ids.task10_6_2.ids.next10_2_6.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_7task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_6task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_6_2.ids.submit10_2_6.text = "Попробуй ещё раз"
            self.screen.ids.task10_6_2.ids.text_field_error10_2_6.text = ""
            self.screen.ids.task10_6_2.ids.text_field_error10_2_62.text = ""
            self.screen.ids.task10_6_2.ids.text_field_error10_2_6.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_6task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_7(self):
        user_answer = self.screen.ids.task10_7_2.ids.text_field_error10_2_7.text
        if user_answer == self.answer10_2_7:
            self.screen.ids.task10_7_2.ids.submit10_2_7.text = "Правильно"
            self.screen.ids.task10_7_2.ids.next10_2_7.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_8task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_7task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_7_2.ids.submit10_2_7.text = "Попробуй ещё раз"
            self.screen.ids.task10_7_2.ids.text_field_error10_2_7.text = ""
            self.screen.ids.task10_7_2.ids.text_field_error10_2_7.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_7task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_8(self):
        user_answer = self.screen.ids.task10_8_2.ids.text_field_error10_2_8.text
        user_answer_2 = self.screen.ids.task10_8_2.ids.text_field_error10_2_82.text
        if user_answer == self.answer10_2_8 and user_answer_2 == self.answer10_2_82:
            self.screen.ids.task10_8_2.ids.submit10_2_8.text = "Правильно"
            self.screen.ids.task10_8_2.ids.next10_2_8.disabled = False
            self.screen.ids.tasks10_2.ids.button10_2_9task.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_8task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_8_2.ids.submit10_2_8.text = "Попробуй ещё раз"
            self.screen.ids.task10_8_2.ids.text_field_error10_2_8.text = ""
            self.screen.ids.task10_8_2.ids.text_field_error10_2_82.text = ""
            self.screen.ids.task10_8_2.ids.text_field_error10_2_8.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_8task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_2_9(self):
        user_answer = self.screen.ids.task10_9_2.ids.text_field_error10_2_9.text
        if user_answer == self.answer10_2_9:
            self.screen.ids.task10_9_2.ids.submit10_2_9.text = "Правильно"
            self.screen.ids.task10_9_2.ids.next10_2_9.disabled = False
            
            self.screen.ids.tasks10_2.ids.button10_2_9task.md_bg_color = 'lightgreen'
            self.screen.ids.theme10_2.ids.button10_2tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_9_2.ids.submit10_2_9.text = "Попробуй ещё раз"
            self.screen.ids.task10_9_2.ids.text_field_error10_2_9.text = ""
            self.screen.ids.task10_9_2.ids.text_field_error10_2_9.helper_text = "Ошибка"

            self.screen.ids.tasks10_2.ids.button10_2_9task.md_bg_color = 'red'

########################################################################################################################################

    def check_answer10_3_1(self):
        user_answer = self.screen.ids.task10_1_3.ids.text_field_error10_3_1.text
        if user_answer == self.answer10_3_1:
            self.screen.ids.task10_1_3.ids.submit10_3_1.text = "Правильно"
            self.screen.ids.task10_1_3.ids.next10_3_1.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_2task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_1task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_1_3.ids.submit10_3_1.text = "Попробуй ещё раз"
            self.screen.ids.task10_1_3.ids.text_field_error10_3_1.text = ""
            self.screen.ids.task10_1_3.ids.text_field_error10_3_1.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_1task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_2(self):
        user_answer = self.screen.ids.task10_2_3.ids.text_field_error10_3_2.text
        if user_answer == self.answer10_3_2:
            self.screen.ids.task10_2_3.ids.submit10_3_2.text = "Правильно"
            self.screen.ids.task10_2_3.ids.next10_3_2.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_3task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_2task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_2_3.ids.submit10_3_2.text = "Попробуй ещё раз"
            self.screen.ids.task10_2_3.ids.text_field_error10_3_2.text = ""
            self.screen.ids.task10_2_3.ids.text_field_error10_3_2.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_2task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_3(self):
        user_answer = self.screen.ids.task10_3_3.ids.text_field_error10_3_3.text
        if user_answer == self.answer10_3_3:
            self.screen.ids.task10_3_3.ids.submit10_3_3.text = "Правильно"
            self.screen.ids.task10_3_3.ids.next10_3_3.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_4task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_3task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_3_3.ids.submit10_3_3.text = "Попробуй ещё раз"
            self.screen.ids.task10_3_3.ids.text_field_error10_3_3.text = ""
            self.screen.ids.task10_3_3.ids.text_field_error10_3_3.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_3task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_4(self):
        user_answer = self.screen.ids.task10_4_3.ids.text_field_error10_3_4.text
        user_answer_2 = self.screen.ids.task10_4_3.ids.text_field_error10_3_42.text
        if user_answer == self.answer10_3_4 and user_answer_2 == self.answer10_3_42:
            self.screen.ids.task10_4_3.ids.submit10_3_4.text = "Правильно"
            self.screen.ids.task10_4_3.ids.next10_3_4.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_5task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_4task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_4_3.ids.submit10_3_4.text = "Попробуй ещё раз"
            self.screen.ids.task10_4_3.ids.text_field_error10_3_4.text = ""
            self.screen.ids.task10_4_3.ids.text_field_error10_3_42.text = ""
            self.screen.ids.task10_4_3.ids.text_field_error10_3_4.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_4task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_5(self):
        user_answer = self.screen.ids.task10_5_3.ids.text_field_error10_3_5.text
        if user_answer == self.answer10_3_5:
            self.screen.ids.task10_5_3.ids.submit10_3_5.text = "Правильно"
            self.screen.ids.task10_5_3.ids.next10_3_5.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_6task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_5task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_5_3.ids.submit10_3_5.text = "Попробуй ещё раз"
            self.screen.ids.task10_5_3.ids.text_field_error10_3_5.text = ""
            self.screen.ids.task10_5_3.ids.text_field_error10_3_5.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_5task.md_bg_color = "red"

########################################################################################################################################
    def check_answer10_3_6(self):
        user_answer = self.screen.ids.task10_6_3.ids.text_field_error10_3_6.text
        if user_answer == self.answer10_3_6:
            self.screen.ids.task10_6_3.ids.submit10_3_6.text = "Правильно"
            self.screen.ids.task10_6_3.ids.next10_3_6.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_7task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_6task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_6_3.ids.submit10_3_6.text = "Попробуй ещё раз"
            self.screen.ids.task10_6_3.ids.text_field_error10_3_6.text = ""
            self.screen.ids.task10_6_3.ids.text_field_error10_3_6.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_6task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_7(self):
        user_answer = self.screen.ids.task10_7_3.ids.text_field_error10_3_7.text
        user_answer_2 = self.screen.ids.task10_7_3.ids.text_field_error10_3_72.text
        if user_answer == self.answer10_3_7 and user_answer_2 == self.answer10_3_72:
            self.screen.ids.task10_7_3.ids.submit10_3_7.text = "Правильно"
            self.screen.ids.task10_7_3.ids.next10_3_7.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_8task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_7task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_7_3.ids.submit10_3_7.text = "Попробуй ещё раз"
            self.screen.ids.task10_7_3.ids.text_field_error10_3_7.text = ""
            self.screen.ids.task10_7_3.ids.text_field_error10_3_72.text = ""
            self.screen.ids.task10_7_3.ids.text_field_error10_3_7.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_7task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_8(self):
        user_answer = self.screen.ids.task10_8_3.ids.text_field_error10_3_8.text
        if user_answer == self.answer10_3_8:
            self.screen.ids.task10_8_3.ids.submit10_3_8.text = "Правильно"
            self.screen.ids.task10_8_3.ids.next10_3_8.disabled = False
            self.screen.ids.tasks10_3.ids.button10_3_10task.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_8task.md_bg_color = 'lightgreen'
        else:
            self.screen.ids.task10_8_3.ids.submit10_3_8.text = "Попробуй ещё раз"
            self.screen.ids.task10_8_3.ids.text_field_error10_3_8.text = ""
            self.screen.ids.task10_8_3.ids.text_field_error10_3_8.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_8task.md_bg_color = "red"

########################################################################################################################################

    def check_answer10_3_9(self):
        user_answer = self.screen.ids.task10_9_3.ids.text_field_error10_3_9.text
        if user_answer == self.answer10_3_9:
            self.screen.ids.task10_9_3.ids.submit10_3_9.text = "Правильно"
            self.screen.ids.task10_9_3.ids.next10_3_9.disabled = False
            
            self.screen.ids.tasks10_3.ids.button10_3_10task.md_bg_color = 'lightgreen'
            self.screen.ids.theme10_3.ids.button10_3tasks.md_bg_color = "lightgreen"
        else:
            self.screen.ids.task10_9_3.ids.submit10_3_9.text = "Попробуй ещё раз"
            self.screen.ids.task10_9_3.ids.text_field_error10_3_9.text = ""
            self.screen.ids.task10_9_3.ids.text_field_error10_3_9.helper_text = "Ошибка"

            self.screen.ids.tasks10_3.ids.button10_3_10task.md_bg_color = "red"

################################################################################################




DemoApp().run()
