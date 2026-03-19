"""
Business services module
"""

from importlib import import_module

__all__ = [
    'OntologyGenerator', 
    'GraphBuilderService', 
    'TextProcessor',
    'KuzuEntityReader',
    'EntityNode',
    'FilteredEntities',
    'OasisProfileGenerator',
    'OasisAgentProfile',
    'SimulationManager',
    'SimulationState',
    'SimulationStatus',
    'SimulationConfigGenerator',
    'SimulationParameters',
    'AgentActivityConfig',
    'TimeSimulationConfig',
    'EventConfig',
    'PlatformConfig',
    'SimulationRunner',
    'SimulationRunState',
    'RunnerStatus',
    'AgentAction',
    'RoundSummary',
    'KuzuGraphMemoryUpdater',
    'KuzuGraphMemoryManager',
    'AgentActivity',
    'SimulationIPCClient',
    'SimulationIPCServer',
    'IPCCommand',
    'IPCResponse',
    'CommandType',
    'CommandStatus',
]

_LAZY_IMPORTS = {
    'OntologyGenerator': ('.ontology_generator', 'OntologyGenerator'),
    'GraphBuilderService': ('.graph_builder', 'GraphBuilderService'),
    'TextProcessor': ('.text_processor', 'TextProcessor'),
    'KuzuEntityReader': ('.kuzu_entity_reader', 'KuzuEntityReader'),
    'EntityNode': ('.kuzu_entity_reader', 'EntityNode'),
    'FilteredEntities': ('.kuzu_entity_reader', 'FilteredEntities'),
    'OasisProfileGenerator': ('.oasis_profile_generator', 'OasisProfileGenerator'),
    'OasisAgentProfile': ('.oasis_profile_generator', 'OasisAgentProfile'),
    'SimulationManager': ('.simulation_manager', 'SimulationManager'),
    'SimulationState': ('.simulation_manager', 'SimulationState'),
    'SimulationStatus': ('.simulation_manager', 'SimulationStatus'),
    'SimulationConfigGenerator': ('.simulation_config_generator', 'SimulationConfigGenerator'),
    'SimulationParameters': ('.simulation_config_generator', 'SimulationParameters'),
    'AgentActivityConfig': ('.simulation_config_generator', 'AgentActivityConfig'),
    'TimeSimulationConfig': ('.simulation_config_generator', 'TimeSimulationConfig'),
    'EventConfig': ('.simulation_config_generator', 'EventConfig'),
    'PlatformConfig': ('.simulation_config_generator', 'PlatformConfig'),
    'SimulationRunner': ('.simulation_runner', 'SimulationRunner'),
    'SimulationRunState': ('.simulation_runner', 'SimulationRunState'),
    'RunnerStatus': ('.simulation_runner', 'RunnerStatus'),
    'AgentAction': ('.simulation_runner', 'AgentAction'),
    'RoundSummary': ('.simulation_runner', 'RoundSummary'),
    'KuzuGraphMemoryUpdater': ('.kuzu_graph_memory_updater', 'KuzuGraphMemoryUpdater'),
    'KuzuGraphMemoryManager': ('.kuzu_graph_memory_updater', 'KuzuGraphMemoryManager'),
    'AgentActivity': ('.kuzu_graph_memory_updater', 'AgentActivity'),
    'SimulationIPCClient': ('.simulation_ipc', 'SimulationIPCClient'),
    'SimulationIPCServer': ('.simulation_ipc', 'SimulationIPCServer'),
    'IPCCommand': ('.simulation_ipc', 'IPCCommand'),
    'IPCResponse': ('.simulation_ipc', 'IPCResponse'),
    'CommandType': ('.simulation_ipc', 'CommandType'),
    'CommandStatus': ('.simulation_ipc', 'CommandStatus'),
}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        module_name, attr_name = _LAZY_IMPORTS[name]
        value = getattr(import_module(module_name, __name__), attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

