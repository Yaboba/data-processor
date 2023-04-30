from setuptools import setup
from setuptools import find_packages

# Loads _version.py module without importing the whole package.
def get_version_and_cmdclass(pkg_path):
    import os
    from importlib.util import module_from_spec, spec_from_file_location

    spec = spec_from_file_location(
        'version',
        os.path.join(pkg_path, '_version.py'),
    )
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__, module.get_cmdclass(pkg_path)


version, cmdclass = get_version_and_cmdclass('dataLoader')

setup(
    name='dataLoader',
    version=version,
    cmdclass=cmdclass,
    packages=find_packages(),
    entry_points={'console_scripts': ['clidl = dataLoader.cli.app:App.run']},
    description='Data Loader cli'
    )