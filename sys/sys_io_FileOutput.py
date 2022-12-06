class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def flush(self):
        self.impl.flush()

    def close(self):
        self.impl.close()

    def write(self,s):
        self.impl.write(s)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeFloat(self,x):
        self.impl.writeFloat(x)

    def writeDouble(self,x):
        self.impl.writeDouble(x)

    def writeInt8(self,x):
        self.impl.writeInt8(x)

    def writeInt16(self,x):
        self.impl.writeInt16(x)

    def writeUInt16(self,x):
        self.impl.writeUInt16(x)

    def writeInt24(self,x):
        self.impl.writeInt24(x)

    def writeUInt24(self,x):
        self.impl.writeUInt24(x)

    def writeInt32(self,x):
        self.impl.writeInt32(x)

    def prepare(self,nbytes):
        self.impl.prepare(nbytes)

    def writeInput(self,i,bufsize = None):
        self.impl.writeInput(i,bufsize)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput
_hx_classes["sys.io.FileOutput"] = sys_io_FileOutput

