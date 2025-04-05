# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thermo'
copyright = '2025, Jack J. Middelburg and Lant'
author = '  Jack J. Middelburg;Lant'
release = 'v2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions =  extensions = [
     'recommonmark',
     'sphinx.ext.mathjax',
     'sphinx.ext.jsmath',
     'sphinx.ext.mathjax',
     'sphinx_markdown_tables'
 ]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = 'sphinx_rtd_theme'
extensions = ["myst_parser"]
