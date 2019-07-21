from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=15, lat=35.681382, lon=139.766084)
        return mapview
MapViewApp().run()
