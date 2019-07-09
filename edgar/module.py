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
        self.manifest = {
            'reload': self.reload,
            'exit': self.exit
        }

    def __repr__(self):
        return f'<Module {self.name}>'

    def register(self, func):
        """
        registers a function as a module command
        """
        functools.wraps(func)
        self.manifest[func.__name__] = func

    def reload(self):
        """
        reload the current module from source code
        """
        logger.info('reloading module %s', self.name)
        importlib.invalidate_caches()
        importlib.reload(_LOADED_MODULES[self.name])

    def exit(self):
        """
        exit the current module
        """


def load_module(name):
    """
    dynamically import a module from the edgar.modules package.
    """
    if name in _LOADED_MODULES:
        logger.debug('module %s already imported', name)
        return _LOADED_MODULES[name].module
    rel, package = f'.{name}', 'edgar.modules'
    logger.debug('dynamically importing %s%s', package, rel)
    _LOADED_MODULES[name] = importlib.import_module(rel, package)
    return _LOADED_MODULES[name].module
