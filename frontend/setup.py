from setuptools import setup

setup(name='frontend',
      packages=['src'],
      include_package_data=True,
      install_requires=[
          'flask',
      ])