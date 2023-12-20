from kivymd.app import MDApp
from kivy.lang import Builder

class contohApp(MDApp):
    def build(self):
        self.appKv = '''
MDScreen:
    MDLabel:
        text:'Hello world'
        multiline :True
        halign:'center'
'''
        AppScreen=Builder.load_string(self.appKv)
        return AppScreen

contohApp().run()