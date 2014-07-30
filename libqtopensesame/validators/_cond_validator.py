#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4 import QtCore, QtGui
from _base_validator import base_validator

class cond_validator(base_validator):

	"""
	desc:
		A validator for conditional statements.
	"""

	def __init__(self, main_window, default=u'always'):

		self.default = default
		super(cond_validator, self).__init__(main_window)

	def validate(self, val, pos):

		try:
			self.experiment.compile_cond(unicode(val))
			return (self.Acceptable, pos)
		except:
			return (self.Intermediate, pos)

	def fixup(self, val):

		if val.trimmed() == u'':
			val.remove(0, len(val))
			val.insert(0, self.default)
			return
		try:
			self.experiment.compile_cond(unicode(val))
		except Exception as e:
			val.remove(0, len(val))
			val.insert(0, self.default)
