class sys_io_FileInput(haxe_io_Input):
    _hx_class_name = "sys.io.FileInput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def eof(self):
        return self.impl.eof()

    def readByte(self):
        return self.impl.readByte()

    def readBytes(self,s,pos,_hx_len):
        return self.impl.readBytes(s,pos,_hx_len)

    def close(self):
        self.impl.close()

    def readAll(self,bufsize = None):
        return self.impl.readAll(bufsize)

    def readFullBytes(self,s,pos,_hx_len):
        self.impl.readFullBytes(s,pos,_hx_len)

    def read(self,nbytes):
        return self.impl.read(nbytes)

    def readUntil(self,end):
        return self.impl.readUntil(end)

    def readLine(self):
        return self.impl.readLine()

    def readFloat(self):
        return self.impl.readFloat()

    def readDouble(self):
        return self.impl.readDouble()

    def readInt8(self):
        return self.impl.readInt8()

    def readInt16(self):
        return self.impl.readInt16()

    def readUInt16(self):
        return self.impl.readUInt16()

    def readInt24(self):
        return self.impl.readInt24()

    def readUInt24(self):
        return self.impl.readUInt24()

    def readInt32(self):
        return self.impl.readInt32()

    def readString(self,_hx_len,encoding = None):
        return self.impl.readString(_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput
_hx_classes["sys.io.FileInput"] = sys_io_FileInput


