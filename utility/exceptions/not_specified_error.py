class EndpointNotSpecifiedError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'EndpointNotSpecifiedError, {0} '.format(self.message)
        else:
            return 'EndpointNotSpecifiedError, Endpoint must be specified! Twitter, News or Reddit'


class ModelNotSpecifiedError(EndpointNotSpecifiedError):
    def __init__(self, *args):
        super.__init__(*args)

    def __str__(self):
        if self.message:
            return 'ModelNotSpecifiedError, {0} '.format(self.message)
        else:
            return 'ModelNotSpecifiedError, Model must be specified! Sentiment, Volume, Balance or Dominance'
