from setuptools import setup

#def readme():
#    with open('README.rst') as f:
#        return f.read()
        
setup(name='NBAapi',
      version='0.4',
      description='Load data from NBA api',
      url='https://github.com/eyalshafran/NBA/NBAapi',
      author='Eyal Shafran',
      author_email='shafrane@gmail.com',
      license='MIT',
      packages=['NBAapi'],
#      install_requires=['pandas','requests','matplotlib'],
      include_package_data=True,
      zip_safe=False)