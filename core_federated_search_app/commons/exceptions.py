""" Core Federated search exceptions
"""


class ExploreFederatedSearchAjaxError(Exception):
    """
        Exception raised by the curate package from views.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
