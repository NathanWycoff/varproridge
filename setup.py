from setuptools import setup

setup(name='varproridge',
      version='0.1',
      description='Variable-Projection Polynomial Ridge for UQ',
      url='https://github.com/jeffrey-hokanson/varproridge',
      author='Jeffrey Hokanson; Nathan Wycoff',
      author_email='jeffrey@hokanson.us',
      license='Apache',
      packages=['varproridge'],
      install_requires=[
          'joblib',
      ],
      zip_safe=False)
