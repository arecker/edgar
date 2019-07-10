"""
supports module creation and loading
"""

import functools
import importlib

from edgar import logger


_LOADED_MODULES = {}


class Module:
    """
    Class that manages the functions and metadata around an edgar
    module.  Create and register the functions in an edgar module like
    this:

    # edgar.modules.my_module
    module = Module('my_module')

    @module.register
    def mycommand():
        # ...
    """

    def __init__(self, name):
        self.name = name
        self.manifest = {}

    def __repr__(self):
        return f'<Module {self.name}>'

    def register(self, func):
        """
        registers a function as a module command
        """
        functools.wraps(func)
        self.manifest[func.__name__] = func


def load_module(name):
    """
    dynamically import a module from the edgar.modules package.

    If it has already been loaded, reload it.
    """
    if name in _LOADED_MODULES:
        logger.info('reloading module %s', name)
        importlib.invalidate_caches()
        _LOADED_MODULES[name] = importlib.reload(_LOADED_MODULES[name])
    else:
        rel, package = f'.{name}', 'edgar.modules'
        logger.debug('dynamically importing %s%s', package, rel)
        _LOADED_MODULES[name] = importlib.import_module(rel, package)

    return _LOADED_MODULES[name].module
