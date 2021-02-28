from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

dev_requirements = [
    'mypy==0.812',
    'pylint==2.6.2',
]

docs_requirements = [
    'pdoc3',
]

setup(
    name='nari',
    version='0.0.1',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='A small project to parse FFXIV network event data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nari=nari.cli.client:main'
        ]
    },
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
)
