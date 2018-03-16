from setuptools import setup

setup(
    name='snipsneopixel',
    version='1.0.1',
    description='NeoPixel skill for Snips',
    author='',
    url='https://github.com/snipsco/snips-skill-neopixel',
    download_url='',
    license='MIT',
    install_requires=[
        "enum34==1.1.6",
        "pyserial"
    ],
    test_suite="tests",
    keywords=['snips', 'neopixel'],
    packages=['snipsneopixel'],
    package_data={'snipsneopixel': ['Snipsspec']},
    include_package_data=True,
)
