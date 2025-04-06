project = 'Thermo'
copyright = '2025, Jack J. Middelburg and Lant'
author = 'Jack J. Middelburg, Lant'
release = 'v2.0'

extensions = [
    'sphinx.ext.mathjax',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}
html_static_path = []  # 如果没有静态文件，设置为空

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
]
myst_update_mathjax = True
