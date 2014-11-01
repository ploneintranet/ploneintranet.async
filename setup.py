
from setuptools import setup, find_packages

version = '0.1.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='ploneintranet.async',
      version=version,
      description="Plone Intranet asyncronous tasks support",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Plone Intranet Consortium',
      author_email='',
      url='https://github.com/ploneintranet/ploneintranet.async',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['ploneintranet', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'collective.celery'
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ],
          'develop': [
              'Sphinx',
              'zest.releaser',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
