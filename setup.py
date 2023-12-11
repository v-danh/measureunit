from pathlib import Path
from setuptools import find_packages, setup


def get_version():
    versionpy = (Path('measureunit') / 'version.py').read_text()
    locals_dict = {}
    exec(versionpy, globals(), locals_dict)
    return locals_dict['__version__']

VERSION = get_version()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='measureunit',
    version=VERSION,
    description='A Python library of the measurement conversion',
    packages=find_packages(exclude=(['test*', 'dist*'])),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='v.d.anh',
    author_email='vdanhvt2000@gmail.com',
    url='https://github.com/v-danh/measureunit',
    license='MIT',
    keywords=['measureunit', 'conversion'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    extras_require={
        'dev': ['pytest>=7.0', 'twine>=4.0.2'],
    },
    python_requires='>=3',
)