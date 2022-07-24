from setuptools import setup, find_namespace_packages
from setuptools_rust import Binding, RustExtension

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
    name='nari-act',
    version='0.1.0',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='ACT-specific additions for nari',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
    packages=find_namespace_packages(include=['nari.ext.*']),
    package_data={'nari.ext.act': ['py.typed']},
    rust_extensions=[RustExtension("nari-act_ext", debug=False, quiet=True, binding=Binding.PyO3)],
    zip_safe=False,
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
)
