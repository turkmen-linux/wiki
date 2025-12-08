# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import datetime

project = 'Türkmen Wiki'
copyright = 'Türkmen Linux '+str(datetime.datetime.now().year)
author = 'turkman'
language = 'tr'
extensions = ['sphinx.ext.autodoc', 'rst2pdf.pdfbuilder', 'sphinx_sitemap']
smartquotes = False

# -- Options for PDF output --

pdf_documents = [('index', u'rst2pdf', u'Türkmen Dokümanı', u'Türkmen Linux'),]
pdf_stylesheets = ['style-main.yaml', 'tango']
pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
pdf_style_path = [ '.', 'source/_static']
pdf_use_coverpage = False
pdf_use_toc = True
pdf_modindex = False
pdf_index = False
pdf_break_level = 1
pdf_default_dpi = 72
pdf_compressed = True
pdf_language = "tr_TR"
pdf_fit_mode = "shrink"

# -- Options for sitemap --
sitemap_filename = 'sitemap.xml'
sitemap_url_scheme= '{link}'
# -- Options for HTML output --

html_baseurl = 'https://turkmen-linux.gitlab.io/wiki/'
html_theme = 'theme'
html_static_path = ['_static']
import os
html_theme_path = ['../']
print(os.getcwd())
html_theme_options = {
    'font_family' : 'monospace',
    'footnote_bg': 'none',
    'page_width': '100%',
    'body_max_width': 'auto',
    'logo': 'logo.svg',

}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}


html_context = {
    'meta_description': 'Your meta description here',
    'meta_keywords': 'keyword1, keyword2, keyword3',
    # Add more meta tags as needed
}
