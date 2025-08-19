# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BioSamples'
copyright = '2025'
author = 'The BioSamples Team'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'BioSamples_logo.png'
html_static_path = ['_static']


# Add the extension
extensions = [
    "sphinx.ext.autosectionlabel",
]

# Make sure the target is unique
autosectionlabel_prefix_document = True


def setup(app):
    app.add_css_file('custom.css')

# -- Options for EPUB output
epub_show_urls = 'footnote'
