from setuptools import setup, find_packages
from ssd1306_oled import __version__ as VERSION

requirements = [
        'pillow>=7.2.0',
]

test_requirements = [
]

setup(
    name                = 'ssd1306-oled',
    version             = VERSION,
    description         = 'ssd1306 package.',
    author              = "leeyunjai",
    author_email        = 'leeyunjai1982@gmail.com',
    url                 = 'https://github.com/leeyunjai/ssd1306-oled',
    packages            = find_packages(),
    install_requires    = requirements,
    keywords            = 'ssd1306-oled',
    classifiers         = [
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite          = 'tests',
    tests_require       = test_requirements
)
