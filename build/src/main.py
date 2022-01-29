from pyf_modules.widgets import *

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class MyWebpage(Container):
    
    def __init__(self):
        super().__init__(
            className = "h-screen w-screen flex flex-col justify-center text-center text-white font-mono",
            children = [
                Text(
                    className = "text-6xl font-bold",
                    textContent = "Welcome to PyFyre Test Website!"
                ),
                Text(
                    className = "mt-3 text-lg",
                    textContent = "You're now seeing a PyFyre app running on the wild. Python? Running? On the client-side web!!!!??"
                ),
            ]
        )