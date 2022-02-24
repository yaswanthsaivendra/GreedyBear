# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock

directives.register_directive("code", CodeBlock)


# -- Project information -----------------------------------------------------

project = "GreedyBear"
copyright = "2021, The Honeynet Project"
author = "Matteo Lodi"

# version
version = "0.1.3"
# release - It's the full version, including alpha/beta/rc tags
release = "0.1.3"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
    "sphinxcontrib.openapi",
#     "sphinxcontrib.redoc",
]
# redoc_uri = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md"]

root_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
