class InvalidWordException(Exception):
    """
    Exception for a non-existing word (in WordNet).
    """
    def __init__(self, message):
        super(InvalidWordException, self).__init__(message)

