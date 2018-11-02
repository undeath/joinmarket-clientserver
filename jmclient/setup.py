from setuptools import setup


setup(name='joinmarketclient',
      version='0.3.5',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/Joinmarket-Org/joinmarket-clientserver/jmclient',
      author='',
      author_email='',
      license='GPL',
      packages=['jmclient'],
      install_requires=['joinmarketbase==0.3.5', 'mnemonic==0.18',
                        'qt4reactor==1.6', 'argon2_cffi==18.3.0',
                        'bencoder.pyx==1.2.1', 'pyaes==1.6.1'],
      zip_safe=False)
