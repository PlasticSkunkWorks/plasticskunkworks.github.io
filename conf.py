# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DemoDocumentation'
copyright = '2025, Plastic SkunkWorks'
author = 'Plastic SkunkWorks'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
"nbsphinx",                     #to include jupyer notebooks 
"sphinx_rtd_theme",             #to use the read the docs theme  
"recommonmark",                 #to Include .MD files
"sphinx_markdown_tables"        #to was everywhere so.. why not?
   ]

### ADD ,'README.md' HERE ######################################################################################

exclude_patterns = ['_build','build','PDF', 'READMEimgs','installDependencies','commands','Thumbs.db', '.DS_Store']

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown"
}

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    #"logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "top",
    "style_external_links": True,
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": False,
    "navigation_depth": 2,
    "includehidden": True,
    "titles_only": False
}

#More Customizations :)
html_title = "Plastic SkunkWorks"
html_logo = "staticfiles/logo.jpg"
html_favicon = "staticfiles/logo.jpg"



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
