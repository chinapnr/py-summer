from setuptools import setup
import io
import re

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('summer/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='py_summer',
    version=version,
    install_requires=['pytest', 'Flask', 'SQLAlchemy', 'fishbase', 'click'],
    url='https://github.com/chinapnr/py-summer',
    license='MIT',
    author='David Yi',
    author_email='wingfish@gmail.com',
    description='一个快速生成 Python Web 项目框架的工具',
    long_description=readme,
    packages=['summer', 'demo', 'test'],
    package_data={
        "summer": ["tpl/*", "tpl/.*"],
    },
    entry_points={"console_scripts": ["summer=summer:cli"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]

)
