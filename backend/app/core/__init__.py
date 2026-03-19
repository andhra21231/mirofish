"""Core workbench runtime primitives."""

from importlib import import_module

__all__ = [
    "ResourceLoader",
    "WorkbenchResources",
    "SessionManager",
    "WorkbenchSessionState",
    "Task",
    "TaskManager",
    "TaskStatus",
    "WorkbenchSession",
]

_LAZY_IMPORTS = {
    "ResourceLoader": (".resource_loader", "ResourceLoader"),
    "WorkbenchResources": (".resource_loader", "WorkbenchResources"),
    "SessionManager": (".session_manager", "SessionManager"),
    "WorkbenchSessionState": (".session_manager", "WorkbenchSessionState"),
    "Task": (".task_manager", "Task"),
    "TaskManager": (".task_manager", "TaskManager"),
    "TaskStatus": (".task_manager", "TaskStatus"),
    "WorkbenchSession": (".workbench_session", "WorkbenchSession"),
}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        module_name, attr_name = _LAZY_IMPORTS[name]
        value = getattr(import_module(module_name, __name__), attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
