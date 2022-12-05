import os
import sys

sys.path.insert(0, os.path.abspath("../../")) # Where the module is located

from nari import __version__ as nari_version

project = 'nari'
copyright = '2020, Oowazu Nonowazu'
author = 'Oowazu Nonowazu'

release = '0.1.0' # TODO: figure out how to automate this later - gh action?
version = nari_version

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser'
]

autodoc_typehints = 'description'
html_theme = 'sphinx_rtd_theme'
