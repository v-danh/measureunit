from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='measureunit',
    version='0.0.1-r2',
    description='A Python library of the measurement conversion',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/v-danh/measureunit',
    author='v.d.anh',
    license='MIT',
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