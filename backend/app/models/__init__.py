"""
Data models module
"""

from importlib import import_module

__all__ = ['TaskManager', 'TaskStatus', 'Project', 'ProjectStatus', 'ProjectManager']

_LAZY_IMPORTS = {
	'TaskManager': ('.task', 'TaskManager'),
	'TaskStatus': ('.task', 'TaskStatus'),
	'Project': ('.project', 'Project'),
	'ProjectStatus': ('.project', 'ProjectStatus'),
	'ProjectManager': ('.project', 'ProjectManager'),
}


def __getattr__(name):
	if name in _LAZY_IMPORTS:
		module_name, attr_name = _LAZY_IMPORTS[name]
		value = getattr(import_module(module_name, __name__), attr_name)
		globals()[name] = value
		return value
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

