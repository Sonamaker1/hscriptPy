class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

    def __init__(self):
        self.b = bytearray()

    def get_length(self):
        return len(self.b)

    def addByte(self,byte):
        self.b.append(byte)

    def add(self,src):
        self.b.extend(src.b)

    def addString(self,v,encoding = None):
        self.b.extend(bytearray(v,"UTF-8"))

    def addInt32(self,v):
        self.b.append((v & 255))
        self.b.append(((v >> 8) & 255))
        self.b.append(((v >> 16) & 255))
        self.b.append(HxOverrides.rshift(v, 24))

    def addInt64(self,v):
        self.addInt32(v.low)
        self.addInt32(v.high)

    def addFloat(self,v):
        self.addInt32(haxe_io_FPHelper.floatToI32(v))

    def addDouble(self,v):
        self.addInt64(haxe_io_FPHelper.doubleToI64(v))

    def addBytes(self,src,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b.extend(src.b[pos:(pos + _hx_len)])

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer
_hx_classes["haxe.io.BytesBuffer"] = haxe_io_BytesBuffer

