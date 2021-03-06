from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import *
from kivy.uix.button import Button

from realbutton import RealButton

'''
simple tutorial mechanics working with states mapped in two dictionaries
state_texts and state_actions
'''


class Tutorial_Label(FloatLayout):

    label = ObjectProperty(None)
    menupanel = ObjectProperty(None)

    nextbutton = ObjectProperty(None)
    backbutton = ObjectProperty(None)

    state = NumericProperty(0)

    def __init__(self, iconsize, iconratio, **kwargs):
        super(Tutorial_Label, self).__init__(**kwargs)
        self.iconsize = iconsize
        self.iconratio = iconratio
        self.build_interface()
        self.state_texts = {
            0: 'Welcome to tutorial of PocketCosmos!',
            1: 'This tutorial will show the basic functions of this sandbox. It can be deactivated in the settings dialogue.',
            2: 'Lets start by adding some planets. Note, that the add-planet mode has already been selected from the left panel.',
            3: 'To add a planet to the simulation, wipe over the screen.',
            4: 'The line you draw wiping over the screen indicates the trajectory of the planet added.',
            5: 'This slider on the bottom gives you additional options depending on the mode you\'re in.',
            6: 'The same principle applies to the "add-sun"-mode, try it out!',
            7: 'The multi-shot mode works the same way, but the trajectory shown might not be very accurate.',
            8: 'The next mode is the delete-mode',
            9: 'If you now tap on any body in the simulation, it will be deleted.',
            10: 'The next mode shown in this tutorial is the zoom-mode.',
            11: 'If you wipe over the screen now, you can scroll the view on the simulation.',
            12: 'You can also zoom and rotate the view using two fingers!',
            13: 'If you tap on a planet in this mode, you select it, giving you further options.',
            14: 'Please select a planet or a sun now!',
            15: 'On the top right of the screen you see an infobox giving you additional information about the planet selected.',
            16: 'On the bottom right you see icons to manipulate the selected body.',
            17: 'You can fix a body to prevent it from moving...very useful!',
            18: 'The delete icon is used to delete the body selectted.',
            19: 'The icons further on the right can be used to add or subtract mass from the selected body',
            20: 'Use the eye-icon to focus the view on the body selected.',
            21: 'Thank you for completing the tutorial, now have fun messing around with gravity!'
        }

        self.state_actions = {
            2: 'add_planet',
            6: 'add_sun',
            7: 'multi',
            8: 'del',
            10: 'zoom'
        }

        self.state = 0
        self.label.text = self.state_texts[self.state]

    def on_state(self, instance, value):
        if value in self.state_texts.keys():
            self.label.text = self.state_texts[value]
            if self.nextbutton not in self.children:
                self.add_widget(self.nextbutton)
            if self.backbutton not in self.children:
                self.add_widget(self.backbutton)
            if value == min(self.state_texts.keys()):
                self.remove_widget(self.backbutton)
            if value == max(self.state_texts.keys()):
                self.remove_widget(self.nextbutton)
        if value in self.state_actions.keys():
            self.menupanel.press_button(self.state_actions[value])

    def register_menupanel(self, menupanel):
        self.menupanel = menupanel

    def build_interface(self):
        self.label = Label(
            size_hint=(0.8, 1),
            pos_hint={'x': 0, 'y': 0},
            text_size=(self.iconsize * 6, self.iconsize * 3),
            halign='left'
        )

        self.backbutton = RealButton(
            './media/icons/arrowleft.png',
            './media/icons/arrowleft_pressed.png',
            self.back_state,
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            pos_hint={'x': 0.75, 'y': 0},
            source='./media/icons/arrowleft.png',
            always_release=True
        )

        self.nextbutton = RealButton(
            './media/icons/arrow.png',
            './media/icons/arrow_pressed.png',
            self.next_state,
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            pos_hint={'x': 0.875, 'y': 0},
            source='./media/icons/arrow.png',
            always_release=True
        )

        self.add_widget(self.backbutton)
        self.add_widget(self.nextbutton)
        self.add_widget(self.label)

    def next_state(self, instance):
        self.state += 1

    def back_state(self, instance):
        self.state -= 1
