from setuptools import setup

#def readme():
#    with open('README.rst') as f:
#        return f.read()
        
setup(name='NBAapi',
      version='0.6',
      description='Load data from NBA api',
      url='https://github.com/eyalshafran/NBA/NBAapi',
      author='Eyal Shafran',
      author_email='shafrane@gmail.com',
      license='MIT',
      packages=['NBAapi'],
 	 package_dir={'NBAapi': 'NBAapi'},
	 package_data = {'NBAapi': ['data/*']},
#      install_requires=['pandas','requests','matplotlib'],
      include_package_data=True,
      zip_safe=False)