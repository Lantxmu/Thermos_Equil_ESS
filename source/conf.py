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
     'sphinx.ext.mathjax',
     'myst_parser'
 ]

templates_path = ['_templates']
exclude_patterns = []
mathjax_options = {
    'tex': {'texTags': True, 'packages': ['base', 'ams']},
}
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}
html_static_path = '_static'

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
myst_enable_extensions = [
    "amsmath",
    "dollarmath",  # 支持 $...$ 行内公式
    "colon_fence",  # 支持 ```math 代码块

    ]
myst_update_mathjax = True  # 确保 MathJax 配置更新
