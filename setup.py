from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='nettime_py',
    version='0.0.1',
    description='Python package to consume netTime application by SPEC, SA.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],

    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=[
        'requests',
        'pydantic',
        'aiohttp'
    ],

    extra_require={
        'dev': [
            'pytest>=3.8',
        ],
    },

    url='https://gitlab.com/spec-sa-ar/nettime-py',
    author='Lucas Lucyk',
    author_email='lucaslucyk@gmail.com',
)
