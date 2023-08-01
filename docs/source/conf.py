# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MBU WIKI'
copyright = '2023, Markus Bursch'
author = 'Markus Bursch'

release = '0.1'
version = '0.1.0'

# -- General configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
#    'sphinx_design',
]

#myst_enable_extensions = ["colon_fence"]
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_css_files = [ "custom.css", ]
html_static_path = ['_static']

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
