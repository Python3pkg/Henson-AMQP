from setuptools import find_packages, setup

setup(
    name='Henson-AMQP',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'Henson>=0.5.0',
        'aioamqp>=0.5.1',
    ],
    tests_require=[
        'tox',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
