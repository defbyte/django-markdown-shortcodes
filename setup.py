import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-markdown-shortcodes',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='Utility adding WordPress-like shortcodes for Markdown authoring in Django.',
    long_description=README,
    url='https://github.com/defbyte/django-markdown-shortcodes',
    author='Chris Davis',
    author_email='defbyte@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['django>=1.3']
)