class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def readAll(self,bufsize = None):
        if (bufsize is None):
            bufsize = 16384
        buf = haxe_io_Bytes.alloc(bufsize)
        total = haxe_io_BytesBuffer()
        try:
            while True:
                _hx_len = self.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                total.b.extend(buf.b[0:_hx_len])
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return total.getBytes()

    def readFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.readBytes(s,pos,_hx_len)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def read(self,nbytes):
        s = haxe_io_Bytes.alloc(nbytes)
        p = 0
        while (nbytes > 0):
            k = self.readBytes(s,p,nbytes)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            nbytes = (nbytes - k)
        return s

    def readUntil(self,end):
        buf = haxe_io_BytesBuffer()
        last = None
        while True:
            last = self.readByte()
            if (not ((last != end))):
                break
            buf.b.append(last)
        return buf.getBytes().toString()

    def readLine(self):
        buf = haxe_io_BytesBuffer()
        last = None
        s = None
        try:
            while True:
                last = self.readByte()
                if (not ((last != 10))):
                    break
                buf.b.append(last)
            s = buf.getBytes().toString()
            if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
                s = HxString.substr(s,0,-1)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,haxe_io_Eof):
                e = _g1
                s = buf.getBytes().toString()
                if (len(s) == 0):
                    raise haxe_Exception.thrown(e)
            else:
                raise _g
        return s

    def readFloat(self):
        return haxe_io_FPHelper.i32ToFloat(self.readInt32())

    def readDouble(self):
        i1 = self.readInt32()
        i2 = self.readInt32()
        if self.bigEndian:
            return haxe_io_FPHelper.i64ToDouble(i2,i1)
        else:
            return haxe_io_FPHelper.i64ToDouble(i1,i2)

    def readInt8(self):
        n = self.readByte()
        if (n >= 128):
            return (n - 256)
        return n

    def readInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        n = ((ch2 | ((ch1 << 8))) if (self.bigEndian) else (ch1 | ((ch2 << 8))))
        if (((n & 32768)) != 0):
            return (n - 65536)
        return n

    def readUInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        if self.bigEndian:
            return (ch2 | ((ch1 << 8)))
        else:
            return (ch1 | ((ch2 << 8)))

    def readInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        n = (((ch3 | ((ch2 << 8))) | ((ch1 << 16))) if (self.bigEndian) else ((ch1 | ((ch2 << 8))) | ((ch3 << 16))))
        if (((n & 8388608)) != 0):
            return (n - 16777216)
        return n

    def readUInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        if self.bigEndian:
            return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
        else:
            return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

    def readInt32(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        ch4 = self.readByte()
        n = ((((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24))) if (self.bigEndian) else (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24))))
        if (((n & -2147483648)) != 0):
            return (n | -2147483648)
        else:
            return n

    def readString(self,_hx_len,encoding = None):
        b = haxe_io_Bytes.alloc(_hx_len)
        self.readFullBytes(b,0,_hx_len)
        return b.getString(0,_hx_len,encoding)

    def getDoubleSig(self,_hx_bytes):
        return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input
_hx_classes["haxe.io.Input"] = haxe_io_Input


