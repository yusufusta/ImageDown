from setuptools import setup
import sys

required = ['selenium', 'chromedriver_autoinstaller', 'requests']
long_description = ""
with open('README.md') as f:
    long_description += f.read()

setup(
    name='ImageDown',
    version='0.7.0',
    description='[WIP] Google Images full-photo downloader',
    long_description=long_description,
    author='Yusuf Usta',
    author_email='yusuf@fusuf.codes',
    maintainer='Yusuf Usta',
    maintainer_email='yusuf@fusuf.codes',
    url='https://github.com/quiec/ImageDown',
    license='GPL3',
    packages=['ImageDown'],
    install_requires=required,
    keywords=['Google', 'Yandex', 'Image', 'Downloader', 'Google-image'],
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
