class python_NativeStringTools:
    _hx_class_name = "python.NativeStringTools"
    __slots__ = ()
    _hx_statics = ["format", "encode", "contains", "strip", "rpartition", "startswith", "endswith"]

    @staticmethod
    def format(s,args):
        return s.format(*args)

    @staticmethod
    def encode(s,encoding = None,errors = None):
        if (encoding is None):
            encoding = "utf-8"
        if (errors is None):
            errors = "strict"
        return s.encode(encoding, errors)

    @staticmethod
    def contains(s,e):
        return (e in s)

    @staticmethod
    def strip(s,chars = None):
        return s.strip(chars)

    @staticmethod
    def rpartition(s,sep):
        return s.rpartition(sep)

    @staticmethod
    def startswith(s,prefix):
        return s.startswith(prefix)

    @staticmethod
    def endswith(s,suffix):
        return s.endswith(suffix)
python_NativeStringTools._hx_class = python_NativeStringTools
_hx_classes["python.NativeStringTools"] = python_NativeStringTools


