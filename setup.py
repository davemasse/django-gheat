from distutils.core import setup

setup(name='gheat',
      version='1.0',
      url='https://github.com/davemasse/django-gheat',
      packages=['gheat'],
      package_data = {
        'gheat': ['etc/color-schemes/*','etc/dots/*']
      },
      include_package_data=True,
      )