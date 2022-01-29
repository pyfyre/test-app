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
                Container(
                    className="flex justify-center items-center",
                    children=[
                        Text(
                            className = "mt-3 text-lg",
                            textContent = "Sounds like replacing Javascript on the web. Anyways, wanna try PyFyre out?"
                        ),
                        Anchor(
                            className="text-sm mt-3 ml-2 font-bold",
                            textContent="https://github.com/pyfyre/pyfyre",
                            link="https://github.com/pyfyre/pyfyre"
                        )
                    ]
                ),
                Text(
                    className = "mt-10 mx-auto rounded-lg py-2 w-2/12 text-xl font-bold bg-[#333333]",
                    textContent = "pip install pyfyre"
                ),
            ]
        )