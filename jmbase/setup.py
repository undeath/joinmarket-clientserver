from setuptools import setup


setup(name='joinmarketbase',
      version='0.3.5',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/Joinmarket-Org/joinmarket-clientserver/jmbase',
      author='',
      author_email='',
      license='GPL',
      packages=['jmbase'],
      install_requires=['twisted==18.9.0', 'service-identity==17.0.0'],
      zip_safe=False)
