class Serviceable:
    """ Serviceable interface"""

    def needs_service(self) -> bool:
        raise NotImplementedError
