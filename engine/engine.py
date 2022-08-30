class Engine:
    """ An engine interface
    """

    def __init__(self):
        pass

    def needs_service(self) -> bool:
        raise NotImplementedError
