# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""

PROJECTNAME = 'ploneconf2014.policy'

PRODUCT_DEPENDENCIES = [
    'plone.api',
    'collective.plonetruegallery',
    'collective.geo.bundle',
    'Products.PloneFormGen',
    ]

PACKAGE_DEPENDENCIES = [
#    'ploneconf2014.contenttypes',
#    'ploneconf2014.theme',
    ]

DEPENDENCIES = PRODUCT_DEPENDENCIES + PACKAGE_DEPENDENCIES