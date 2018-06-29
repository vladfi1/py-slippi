# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'slippi'
author = 'melkor'

version = '1.0.0'
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# needs_sphinx = '1.0'
extensions = ['sphinx.ext.napoleon']
templates_path = ['_templates']
source_suffix = ['.rst']
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    #"github_user": "?",
    #"github_repo": "?",
    'fixed_sidebar': True,
}

html_static_path = ['_static']

# default: [localtoc.html, relations.html, sourcelink.html, searchbox.html]
#html_sidebars = {
#    "**": [
#        "about.html",
#        "localtoc.html",
#        "relations.html",
#        "searchbox.html",
#    ]
#}


# -- Extension configuration -------------------------------------------------

from sphinx.ext.autodoc import ClassLevelDocumenter, InstanceAttributeDocumenter

autodoc_member_order = 'bysource'

def skip(app, what, name, obj, skip, options):
    if name == '__init__' and obj.__doc__:
        return False
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# remove the useless " = None" after every ivar
def iad_add_directive_header(self, sig):
    ClassLevelDocumenter.add_directive_header(self, sig)

InstanceAttributeDocumenter.add_directive_header = iad_add_directive_header