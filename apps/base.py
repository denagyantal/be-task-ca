# Here we could build the DAG for each application
# import modules here

class ApplicationBase:
    name = 'unknown_app'

    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def bootstrap(self, init_resource=True):
        pass

    @abstractmethod
    def reload_config(self, init_resource=True):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class ApplicationOne(ApplicationBase):
    # use whatever modules you need here or build IoC container if we need (only in large codebase)
    pass

