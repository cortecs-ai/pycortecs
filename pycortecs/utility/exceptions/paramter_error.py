class ParameterError(Exception):

    def __init__(self, param):
        self.param = param

    def __str__(self):
        if self.param == 'since':
            return "{}: since has to be a valid date in format YYYY-mm-dd".format(self.__class__.__name__)
        if self.param == 'until':
            return "{}: until has to be a valid date in format YYYY-mm-dd".format(self.__class__.__name__)
