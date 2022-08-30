class Tire:
    """ An tire interface
    """

    def __init__(self):
        pass

    def needs_service(self) -> bool:
        raise NotImplementedError
