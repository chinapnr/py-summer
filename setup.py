from setuptools import setup
import io
import re

with io.open('py_summer/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='py_summer',
    version=version,
    url='https://github.com/chinapnr/py-summer',
    license='MIT',
    author='David Yi',
    author_email='wingfish@gmail.com',
    description='Simplify and strengthen the Python web server development, mainly RESTful server, use Flask as the backend.',
    packages=['py_summer', 'demo', 'test'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]

)
