__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1643447311876, "src.main": [".py", "from pyf_modules.widgets import *\n\n\n\nclass MyWebpage(Container):\n\n def __init__(self):\n  super().__init__(\n  className=\"h-screen w-screen flex flex-col justify-center text-center text-white font-mono\",\n  children=[\n  Text(\n  className=\"text-6xl font-bold\",\n  textContent=\"Welcome to PyFyre Test Website!\"\n  ),\n  Text(\n  className=\"mt-3 text-lg\",\n  textContent=\"You're now seeing a PyFyre app running on the wild. Python? Running? On the client-side web!!!!??\"\n  ),\n  Container(\n  className=\"flex flex-col mt-5 justify-center items-center md:flex-row md:mt-0\",\n  children=[\n  Text(\n  className=\"mt-3 text-lg\",\n  textContent=\"Sounds like replacing Javascript on the web. Anyways, wanna try PyFyre out?\"\n  ),\n  Anchor(\n  className=\"text-sm mt-3 ml-2 font-bold\",\n  textContent=\"https://github.com/pyfyre/pyfyre\",\n  link=\"https://github.com/pyfyre/pyfyre\"\n  )\n  ]\n  ),\n  Text(\n  className=\"mt-10 mx-auto rounded-lg py-2 w-6/12 text-xl font-bold bg-[#333333] md:w-2/12\",\n  textContent=\"pip install pyfyre\"\n  ),\n  ]\n  )\n", ["pyf_modules.widgets"]], "src": [".py", "from pyf_modules.widgets import *\nfrom pyf_modules.pyfyre import runApp\nfrom src.main import MyWebpage\n\nclass App(PyFyreApp):\n def build(self):\n  return Container(\n  className=\"root\",\n  children=[\n  MyWebpage()\n  ]\n  )\n  \nrunApp(\nApp(),\nmount=\"app-mount\"\n)\n", ["pyf_modules.pyfyre", "pyf_modules.widgets", "src.main"], 1], "src.css": [".py", "", [], 1]}
__BRYTHON__.update_VFS(scripts)