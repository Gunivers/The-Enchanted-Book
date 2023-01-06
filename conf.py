# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Enchanted Book'
copyright = '2023, Gunivers'
author = 'Gunivers'
language="fr"

html_theme_options = {
    "home_page_in_toc": False,
    "github_url": "https://github.com/Gunivers/The-Enchanted-Book",
    "repository_url": "https://github.com/Gunivers/The-Enchanted-Book",
    "repository_branch": "EN",
    "use_repository_button": True,
    "use_edit_page_button": True,
}

html_logo = "logo.gif"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
]

myst_enable_extensions = [
    "amsmath",
    # "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
