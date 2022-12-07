import globalClasses

def classesinmodule(module):
    md = module.__dict__
    return [
        md[c] for c in md if (
            _hx_AnonObject({c: md[c]})
            #isinstance(md[c], type) and md[c].__module__ == module.__name__
        )
    ]

class _hx_AnonObject:
    global _hx_classes 
    _hx_classes = globalClasses._hx_classes
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False


_hx_classes = globalClasses._hx_classes
