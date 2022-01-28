from pyf_modules.widgets import *

class Header(Container):
    def __init__(self, greet):
        super().__init__(
            className = "test",
            children = [
                Text(
                    className = "header-text",
                    textContent = f"{greet}, I'm a header component!"
                )
            ]
        )