class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def write(self,s):
        l = s.length
        p = 0
        while (l > 0):
            k = self.writeBytes(s,p,l)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            l = (l - k)

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeFloat(self,x):
        self.writeInt32(haxe_io_FPHelper.floatToI32(x))

    def writeDouble(self,x):
        i64 = haxe_io_FPHelper.doubleToI64(x)
        if self.bigEndian:
            self.writeInt32(i64.high)
            self.writeInt32(i64.low)
        else:
            self.writeInt32(i64.low)
            self.writeInt32(i64.high)

    def writeInt8(self,x):
        if ((x < -128) or ((x >= 128))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeByte((x & 255))

    def writeInt16(self,x):
        if ((x < -32768) or ((x >= 32768))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt16((x & 65535))

    def writeUInt16(self,x):
        if ((x < 0) or ((x >= 65536))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 8))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte((x >> 8))

    def writeInt24(self,x):
        if ((x < -8388608) or ((x >= 8388608))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt24((x & 16777215))

    def writeUInt24(self,x):
        if ((x < 0) or ((x >= 16777216))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 16))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x >> 16))

    def writeInt32(self,x):
        if self.bigEndian:
            self.writeByte(HxOverrides.rshift(x, 24))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(HxOverrides.rshift(x, 24))

    def prepare(self,nbytes):
        pass

    def writeInput(self,i,bufsize = None):
        if (bufsize is None):
            bufsize = 4096
        buf = haxe_io_Bytes.alloc(bufsize)
        try:
            while True:
                _hx_len = i.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                p = 0
                while (_hx_len > 0):
                    k = self.writeBytes(buf,p,_hx_len)
                    if (k == 0):
                        raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                    p = (p + k)
                    _hx_len = (_hx_len - k)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output
_hx_classes["haxe.io.Output"] = haxe_io_Output


