# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Lowes.syf.com Login Guide'
copyright = '2025, Lowe’s Synchrony'
author = 'Lowe’s / Synchrony Financial'

# Full version info
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# List of Sphinx extensions (you can add more if needed)
extensions = []

# Paths to templates
templates_path = ['_templates']

# Files and folders to ignore when searching for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# HTML title (shown in browser tab and top of page)
html_title = "Lowes.syf.com Login – Access Lowe’s Synchrony Account Online"

# Short title for nav bar or top-left corner
html_short_title = "Lowes.syf.com Login"

# Favicon (ensure favicon.ico is in the root or _static folder)
html_favicon = 'favicon.ico'

# Theme (choose one, or uncomment to use Sphinx default)
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML blocks inside .rst files
html_allow_unsafe = True

# Theme-specific options
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
    'style_nav_header_background': '#002f6c',
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'show_powered_by': False,
}

# Custom static files (CSS, JavaScript, etc.)
# html_static_path = ['_static']
