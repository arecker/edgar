"""
root edgar module
"""

from edgar import Module, load_module
from edgar.console import main


module = Module('edgar')


@module.register
def load(name):
    main(name)
    
