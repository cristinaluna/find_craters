# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FindCraters
                                 A QGIS plugin
 Find Craters in a selected layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-25
        copyright            : (C) 2024 by Cristina Luna
        email                : cristina.luna@live.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FindCraters class from file FindCraters.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .find_craters import FindCraters
    return FindCraters(iface)
