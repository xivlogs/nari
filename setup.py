from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

dev_requirements = [
    'mypy',
    'pylint==2.13.4',
]

docs_requirements = [
    'pdoc3',
]

setup(
    name='nari',
    version='0.0.1',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='A small project to parse ACT network log files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
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
