#  GNU General Public License version 2
#
#  Copyright (C) 2019-2020 JetBrains s.r.o.
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License version 2 only, as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""projector-installer setup file."""

from shutil import copyfile
from os.path import isfile
from setuptools import setup
from setuptools import Command


def copy_license():
    """Copy license file to package"""
    if isfile('LICENSE.txt'):
        copyfile('LICENSE.txt', 'projector_installer/LICENSE.txt')


try:
    copy_license()
except IOError:
    pass

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


class CopyLicenseCommand(Command):
    """Command for copy license to package."""
    description = "Copy LICENSE.txt to package."
    user_options = []

    def initialize_options(self):
        """Override abstract method"""

    def finalize_options(self):
        """Override abstract method"""

    # pylint: disable=R0201
    def run(self):
        """Execute copy_license"""
        copy_license()


setup(
    install_requires=requirements,
    package_data={
        'projector-installer': [
            'LICENSE.txt',
            'compatible_ide.json'
        ],
    },
    cmdclass=dict(
        copy_license=CopyLicenseCommand,
    ),
)
