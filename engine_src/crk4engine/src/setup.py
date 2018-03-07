from distutils.core import setup
from distutils.extension import Extension

'''
# build cplanet library
python setup.py build
'''

# Test if Cython is available
try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

print "USE_CYTHON =", USE_CYTHON

# If no Cython, we assume a 'crect.c' compiled with: 'cython crect.pyx'
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension('crk4engine', ['crk4engine' + ext], language="c")]

# Select Extension
if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)
else:
    # No Cython, append 'rect.c' to sources
    extensions[0].sources.append('rk4engine.c')

setup(
    name="crk4engine",
    ext_modules=extensions
)
