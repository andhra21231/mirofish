"""Composable workbench tools."""

from importlib import import_module

__all__ = [
    "BuildGraphTool",
    "GenerateOntologyTool",
    "GenerateReportTool",
    "PrepareSimulationTool",
    "RunSimulationTool",
    "check_simulation_prepared",
]

_LAZY_IMPORTS = {
    "BuildGraphTool": (".build_graph", "BuildGraphTool"),
    "GenerateOntologyTool": (".generate_ontology", "GenerateOntologyTool"),
    "GenerateReportTool": (".generate_report", "GenerateReportTool"),
    "PrepareSimulationTool": (".prepare_simulation", "PrepareSimulationTool"),
    "RunSimulationTool": (".run_simulation", "RunSimulationTool"),
    "check_simulation_prepared": (".simulation_support", "check_simulation_prepared"),
}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        module_name, attr_name = _LAZY_IMPORTS[name]
        value = getattr(import_module(module_name, __name__), attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
