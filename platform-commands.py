import sys
import platform
from modexample import testFunction, testFunction3
# import variants; advanced qualifying for nested modules
# dir(); sys.path variable
# platform: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()

testFunction()

# The main application section
print('Platform command examples')
print('platform:')
print(platform.platform())
print(platform.platform(0, 1))
print(platform.platform(1, 0))
print('machine:')
print(platform.machine())
print('processor:')
print(platform.processor())
print('system:')
print(platform.system())
print('version:')
print(platform.version())
print('python_implementation:')
print(platform.python_implementation())
print('python_version_tuple:')
print(platform.python_version_tuple())
print(platform.python_revision())
print('dir:')
print(dir())
print('sys.path:')
print(sys.path)

