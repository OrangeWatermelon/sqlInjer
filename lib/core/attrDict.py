class attrDict(dict):
    def __init__(self, indict=None, attribute=None):
        if indict is None:
            indict = {}
        self.attribute = attribute
        dict.__init__(self, indict)
        self.__initialised = True

    def __getattr__(self, item):

        try:
            return self.__getitem__(item)
        except KeyError:
            return None
    def __setattr__(self, item, value):
        if "_AttribDict__initialised" not in self.__dict__:
            return dict.__setattr__(self, item, value)
        elif item in self.__dict__:
            dict.__setattr__(self, item, value)
        else:
            self.__setitem__(item, value)
var = attrDict()