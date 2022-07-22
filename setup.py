from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

dev_requirements = [
    'mypy==0.942',
    'pylint==2.13.4',
]

docs_requirements = [
    'pdoc3',
]

setup(
    name='nari',
    version='0.1.0',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='A small project to parse FFXIV network event data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
    packages=find_packages(),
    package_data={'nari': ['py.typed']},
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
)
