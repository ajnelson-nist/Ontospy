from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import os

here = path.abspath(path.dirname(__file__))

# trick to manage package versions in one place only
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
import re
VERSIONFILE="ontospy/VERSION.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSIONSTRING = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))



# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Get the requirements from txt file
REQUIREMENTS_DATA = []
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    for l in f.readlines():
        if not l.startswith("#"):
            if (">=" in l):
                REQUIREMENTS_DATA.append([l.split(">=")[0]])
            elif ("=" in l):
                REQUIREMENTS_DATA.append([l.split("=")[0]])




def get_package_folders(top_folder, root_path):
    """
    Utility to generate dynamically the list of folders needed by the package_data setting
    ..
        package_data={
             'ontospy': ['viz/static/*.*', 'viz/templates/*.*', 'viz/templates/shared/*.*', 'viz/templates/splitter/*.*', 'viz/templates/markdown/*.*'],
        },
    ...
    """
    _dirs = []
    out = []
    for root, dirs, files in os.walk(top_folder):
        for dir in dirs:
            _dirs.append(os.path.join(root, dir))
    for d in _dirs:
        _d = os.path.join(d, "*.*")
        out.append(_d.replace(root_path+"/", ""))
    return out


package_data_folders = []



setup(
    name='ontospy',
    version=VERSIONSTRING,
    description=
    'Query, inspect and visualize knowledge models encoded as RDF/OWL ontologies.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lambdamusic/ontospy',
    author='Michele Pasin',
    author_email='michele.pasin@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='ontology semantic web linked data rdf owl',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # http://python-packaging-user-guide.readthedocs.org/en/latest/requirements/
    # NOTE: packages are installed in reverse order
    install_requires=REQUIREMENTS_DATA,
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'SHELL': ['readline'],
        'HTML': ['Django>=1.10.3', 'Pygments==2.1.3'],
    },
    package_data={
        'ontospy': package_data_folders
        },
    entry_points={
        'console_scripts': [
            # 'ontospy-sketch=ontospy.extras.sketch:main',
            'ontospy=ontospy.cli:main_cli'
        ],
    },
)
