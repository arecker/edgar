import functools
import importlib

from edgar import logger


_LOADED_MODULES = {}


class Module:
    def __init__(self, name):
        self.name = name
        self.manifest = {
            'help': self.help,
            'reload': self.reload,
        }

    def __repr__(self):
        return f'<Module {self.name}>'

    def console_prompt(self):
        text = self.name.split('.')[-1].upper()
        return f'{text}> '

    def register(self, func):
        functools.wraps(func)
        self.manifest[func.__name__] = func

    def reload(self):
        """
        reload the current module from source code
        """
        logger.info('reloading module %s', self.name)
        importlib.invalidate_caches()
        importlib.reload(_LOADED_MODULES[self.name])

    def help(self):
        """
        print available commands
        """
        cmdlist = map(lambda t: _to_help_line(*t), self.manifest.items())
        output = '\n'.join(sorted(cmdlist, key=lambda t: t[0]))
        print(f'Available Commands:\n{output}\n')


def load_module(name):
    _LOADED_MODULES[name] = importlib.import_module(f'.{name}', 'edgar.modules')
    return _LOADED_MODULES[name].module


def _to_help_line(name, func):
    doc = getattr(func, '__doc__', '').strip()
    return f'{name.ljust(20)} {doc.ljust(20)}'
