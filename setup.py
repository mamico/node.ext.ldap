from setuptools import setup, find_packages
import sys, os

version = '0.9b19'
shortdesc = "Node based LDAP support"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()

setup(name='node.ext.ldap',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='https://github.com/bluedynamics/node.ext.ldap',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['node', 'node.ext'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'python-ldap',
          'smbpasswd',
          'bda.cache',
          'node.ext.ugm',
      ],
      extras_require={
          'test': [
              'interlude',
              'plone.testing',
              'unittest2',
              'zope.configuration',
              'zope.testing',
          ]
      },
      entry_points="""
      [console_scripts]
      testldap = node.ext.ldap.main:slapd
      """,
      )
