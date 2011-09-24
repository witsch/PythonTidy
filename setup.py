from setuptools import setup
from PythonTidy import VERSION as version

summary = 'Cleans up, regularizes, and reformats the text of Python scripts.'

setup(name='PythonTidy',
      version=version,
      description=summary,
      long_description=summary,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Topic :: Software Development :: Quality Assurance",
        ],
      keywords='indentation beautify',
      author='Charles Curtis Rhode',
      author_email='CRhode@LacusVeris.com',
      url='http://pypi.python.org/pypi/PythonTidy',
      license='GPL version 2',
      py_modules=['PythonTidy'],
      platforms='Any',
      install_requires=[
          'setuptools',
      ],
      entry_points={
          'console_scripts': ['pythontidy = PythonTidy:main'],
      },
)
