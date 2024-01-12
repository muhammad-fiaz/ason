from setuptools import setup, find_packages

VERSION = "0.0.1"

DESCRIPTION = 'ASON: Adaptive Structure Object Notation - Python library for handling structured data with flexibility and ease.'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="ason",
    version=VERSION,
    author="Muhammad Fiaz",
    author_email="",  # Add your email address
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/muhammad-fiaz/ason.git',
    packages=find_packages(),
    keywords=[
        'ason', 'json', 'serialization', 'structured data', 'python'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',
    install_requires=[
        # Add any dependencies your project may have
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    license='MIT License',
    project_urls={
        'Source Code': 'https://github.com/muhammad-fiaz/ason.git',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/ason/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/ason#readme',
    },
)

print("Happy Coding!")
