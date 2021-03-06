# KIVY
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
from kivy.core.window import Window
from kivy.animation import Animation

# CUSTOM
from logic import Logic
from realbutton import RealButton
from realbutton import RealToggleButton
from realbutton import RealMenuToggleButton
from realbutton import RealTimedButton

'''
buttons shown on the right bottom when a planet is selected. needs to be
updated depending on planet data (fixed) and logic fixview mode
'''


class Seltoggles(FloatLayout):

    logic = ObjectProperty(None)

    planet_fix_button = ObjectProperty(None)
    planet_del_button = ObjectProperty(None)

    planet_addmass_button = ObjectProperty(None)
    planet_submass_button = ObjectProperty(None)

    planet_fixview_button = ObjectProperty(None)

    visible = BooleanProperty(True)

    def __init__(self, iconsize, iconratio, **kwargs):
        super(Seltoggles, self).__init__(**kwargs)
        self.logic = App.get_running_app().logic
        self.iconsize = iconsize
        self.iconratio = iconratio
        self.build_interface()

    def build_interface(self):

        self.planet_fix_button = RealToggleButton(
            './media/icons/fix.png',
            './media/icons/fix_pressed.png',
            self.logic.fix_selected,
            pos_hint={'x': 0, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/fix.png',
            always_release=True
        )

        self.planet_del_button = RealButton(
            './media/icons/delete.png',
            './media/icons/delete_pressed.png',
            self.logic.delete_selected,
            pos_hint={'x': 1.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/delete.png',
            always_release=True
        )

        self.planet_addmass_button = RealTimedButton(
            './media/icons/weightplus.png',
            './media/icons/weightplus_pressed.png',
            self.logic.addmass_selected,
            pos_hint={'x': 2.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/weightplus.png',
            always_release=True
        )

        self.planet_submass_button = RealTimedButton(
            './media/icons/weightminus.png',
            './media/icons/weightminus_pressed.png',
            self.logic.submass_selected,
            pos_hint={'x': 3.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/weightminus.png',
            always_release=True
        )

        self.planet_fixview_button = RealToggleButton(
            './media/icons/view.png',
            './media/icons/view_pressed.png',
            self.logic.fixview_selected,
            pos_hint={'x': 4.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/view.png',
            always_release=True
        )

        self.show_orbit_button = RealToggleButton(
            './media/icons/showorbit.png',
            './media/icons/showorbit_pressed.png',
            self.logic.show_orbit_selected,
            pos_hint={'x': 5.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/showorbit.png',
            always_release=True
        )

        self.show_hide_button = RealToggleButton(
            './media/icons/down.png',
            './media/icons/up.png',
            self.show_hide,
            pos_hint={'x': 6.0 / 7, 'y': 0},
            size_hint=(None, None),
            size=(self.iconsize, self.iconsize),
            source='./media/icons/down.png',
            always_release=True
        )

        self.add_widget(self.show_hide_button)

        self.add_widget(self.planet_fix_button)
        self.add_widget(self.planet_del_button)
        self.add_widget(self.planet_addmass_button)
        self.add_widget(self.planet_submass_button)
        self.add_widget(self.planet_fixview_button)
        self.add_widget(self.show_orbit_button)

        self.hide_items = [
            self.planet_fix_button, self.planet_del_button,
            self.planet_addmass_button, self.planet_submass_button,
            self.planet_fixview_button, self.show_orbit_button
        ]

    def update(self, **kwargs):
        # update buttons depending in planet selected. kwargs contain
        # complete planet dictionary and fixview flag from logic
        fixed = kwargs.get('fixed', False)
        fixview = kwargs.get('fixview', False)
        show_orbit = kwargs.get('show_orbit', False)
        fixbutton = self.planet_fix_button
        fixview_button = self.planet_fixview_button
        show_orbit_button = self.show_orbit_button
        if fixbutton:
            if fixed:
                fixbutton.pressed = True
                fixbutton.source = fixbutton.realtexture_pressed
                fixbutton.reload()
            else:
                fixbutton.pressed = False
                fixbutton.source = fixbutton.realtexture
                fixbutton.reload()
        if fixview_button:
            if fixview:
                fixview_button.pressed = True
                fixview_button.source = fixview_button.realtexture_pressed
                fixview_button.reload()
            else:
                fixview_button.pressed = False
                fixview_button.source = fixview_button.realtexture
                fixview_button.reload()
        if show_orbit_button:
            if show_orbit:
                show_orbit_button.pressed = True
                show_orbit_button.source = show_orbit_button.realtexture_pressed
                show_orbit_button.reload()
            else:
                show_orbit_button.pressed = False
                show_orbit_button.source = show_orbit_button.realtexture
                show_orbit_button.reload()

    def show_hide(self, instance):
        if self.visible:
            for item in self.hide_items:
                scrolldown = Animation(
                    pos_hint={
                        'y': -1
                    },
                    duration=0.5,
                    t='out_bounce'
                )
                scrolldown.start(item)
            self.visible = False
        else:
            for item in self.hide_items:
                scrolldown = Animation(
                    pos_hint={
                        'y': 0
                    },
                    duration=0.5,
                    t='out_bounce'
                )
                scrolldown.start(item)
            self.visible = True
