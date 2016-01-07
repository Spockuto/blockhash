try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(name='blockhash',
    description='Speed up your SHA. A different hash style',
    version='0.1.1',
	author="Venkkatesh_Sekar",
	author_email="venkythesupersaiyan@gmail.com",
    packages=['blockhash'],
    entry_points={
        'console_scripts': ['blockhash=blockhash:main'],
    },
    test_suite='tests',
    url="https://github.com/Spockuto/blockhash",
    keywords=[ 'CLI', 'python'],
    classifiers=[
        'Operating System :: POSIX',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
],)
