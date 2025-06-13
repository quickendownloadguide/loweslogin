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
copyright = '2025, Lowe’s / Synchrony'
author = 'Lowe’s / Synchrony Financial'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Lowes.syf.com Login – Access Your Lowe’s Synchrony Account Online"

# Optional short title (e.g., for nav bar)
html_short_title = "Lowes Login Portal"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment one if needed)
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
    'collapse_navigation': False,
    'navigation_depth': 3,
    'style_nav_header_background': '#002f6c',
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have static assets

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
