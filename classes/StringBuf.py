class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

    def add(self,x):
        s = Std.string(x)
        self.b.write(s)

    def add1(self,s):
        self.b.write(s)

    def addChar(self,c):
        s = "".join(map(chr,[c]))
        self.b.write(s)

    def addSub(self,s,pos,_hx_len = None):
        s1 = (HxString.substr(s,pos,None) if ((_hx_len is None)) else HxString.substr(s,pos,_hx_len))
        self.b.write(s1)

    def toString(self):
        return self.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
StringBuf._hx_class = StringBuf
_hx_classes["StringBuf"] = StringBuf


