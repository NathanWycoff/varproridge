from setuptools import setup

setup(name='varproridge',
      version='0.1',
      description='Variable-Projection Polynomial Ridge for UQ',
      url='https://github.com/jeffrey-hokanson/varproridge',
      author='Jeffrey Hokanson',
      author_email='jeffrey@hokanson.us',
      license='Apache',
      packages=['varproridge'],
      install_requires=[
          'joblib', 'sympy', 'numpy', 'scipy', 'pandas'
      ],
      zip_safe=False)
