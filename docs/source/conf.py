import os
import sys
sys.path.insert(0, os.path.abspath("../../")) # Where the module is located

project = 'nari'
copyright = '2020, Oowazu Nonowazu'
author = 'Oowazu Nonowazu'

release = '0.1.0'
version = '0.1.0'

extensions = ['sphinx.ext.autodoc']

autodoc_typehints = 'description'
html_theme = 'sphinx_rtd_theme'
