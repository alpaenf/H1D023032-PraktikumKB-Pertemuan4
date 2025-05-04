import os

pythonpath = os.environ.get('PYTHONPATH')
if pythonpath:
    paths = pythonpath.split(os.pathsep)
    print(paths)
else:
    print("PYTHONPATH is not set.")
