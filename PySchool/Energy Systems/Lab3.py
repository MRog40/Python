import pkgutil
search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print('\n')
print(all_modules)

# from Python_Scripts import Calculator_Mode
# import Calculator_Mode

import sys
print('\n')
print(sys.path)
