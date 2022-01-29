from pyf_modules.widgets import *
from pyf_modules.pyfyre import runApp
from src.main import MyWebpage

class App(PyFyreApp):
    def build(self):
        return Container(
            className = "root",
            children = [
                MyWebpage()
            ]
        )
        
runApp(
    App(),
    mount="app-mount"
)