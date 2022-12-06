class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
    _hx_statics = ["alloc", "ofString", "ofData", "ofHex", "fastGet"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def get(self,pos):
        return self.b[pos]

    def set(self,pos,v):
        self.b[pos] = (v & 255)

    def blit(self,pos,src,srcpos,_hx_len):
        if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

    def fill(self,pos,_hx_len,value):
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            pos1 = pos
            pos = (pos + 1)
            self.b[pos1] = (value & 255)

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def compare(self,other):
        b1 = self.b
        b2 = other.b
        _hx_len = (self.length if ((self.length < other.length)) else other.length)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (b1[i] != b2[i]):
                return (b1[i] - b2[i])
        return (self.length - other.length)

    def getDouble(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        pos1 = (pos + 4)
        v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        return haxe_io_FPHelper.i64ToDouble(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))

    def getFloat(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        return haxe_io_FPHelper.i32ToFloat(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v))

    def setDouble(self,pos,v):
        i = haxe_io_FPHelper.doubleToI64(v)
        v = i.low
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)
        pos1 = (pos + 4)
        v = i.high
        self.b[pos1] = (v & 255)
        self.b[(pos1 + 1)] = ((v >> 8) & 255)
        self.b[(pos1 + 2)] = ((v >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setFloat(self,pos,v):
        v1 = haxe_io_FPHelper.floatToI32(v)
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getUInt16(self,pos):
        return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

    def setUInt16(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)

    def getInt32(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        if (((v & -2147483648)) != 0):
            return (v | -2147483648)
        else:
            return v

    def getInt64(self,pos):
        pos1 = (pos + 4)
        v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        this1 = haxe__Int64____Int64(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))
        return this1

    def setInt32(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setInt64(self,pos,v):
        v1 = v.low
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
        pos1 = (pos + 4)
        v1 = v.high
        self.b[pos1] = (v1 & 255)
        self.b[(pos1 + 1)] = ((v1 >> 8) & 255)
        self.b[(pos1 + 2)] = ((v1 >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def readString(self,pos,_hx_len):
        return self.getString(pos,_hx_len)

    def toString(self):
        return self.getString(0,self.length)

    def toHex(self):
        s_b = python_lib_io_StringIO()
        chars = []
        _hx_str = "0123456789abcdef"
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            x = HxString.charCodeAt(_hx_str,i)
            chars.append(x)
        _g = 0
        _g1 = self.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = self.b[i]
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))])))
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))])))
        return s_b.getvalue()

    def getData(self):
        return self.b

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofHex(s):
        _hx_len = len(s)
        if (((_hx_len & 1)) != 0):
            raise haxe_Exception.thrown("Not a hex string (odd number of digits)")
        ret = haxe_io_Bytes.alloc((_hx_len >> 1))
        _g = 0
        _g1 = ret.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            index = (i * 2)
            high = (-1 if ((index >= len(s))) else ord(s[index]))
            index1 = ((i * 2) + 1)
            low = (-1 if ((index1 >= len(s))) else ord(s[index1]))
            high = (((high & 15)) + ((((((high & 64)) >> 6)) * 9)))
            low = (((low & 15)) + ((((((low & 64)) >> 6)) * 9)))
            ret.b[i] = (((((high << 4) | low)) & 255) & 255)
        return ret

    @staticmethod
    def fastGet(b,pos):
        return b[pos]

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.length = None
        _hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes
_hx_classes["haxe.io.Bytes"] = haxe_io_Bytes


