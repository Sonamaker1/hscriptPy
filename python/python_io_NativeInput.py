class python_io_NativeInput(haxe_io_Input):
    _hx_class_name = "python.io.NativeInput"
    __slots__ = ("stream", "wasEof")
    _hx_fields = ["stream", "wasEof"]
    _hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        self.wasEof = None
        self.stream = s
        self.set_bigEndian(False)
        self.wasEof = False
        if (not self.stream.readable()):
            raise haxe_Exception.thrown("Write-only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def tell(self):
        return self.stream.tell()

    def throwEof(self):
        self.wasEof = True
        raise haxe_Exception.thrown(haxe_io_Eof())

    def eof(self):
        return self.wasEof

    def readinto(self,b):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def seek(self,p,mode):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def readBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        ba = bytearray(_hx_len)
        ret = self.readinto(ba)
        if (ret == 0):
            self.throwEof()
        s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
        return ret

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
        _hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput
_hx_classes["python.io.NativeInput"] = python_io_NativeInput


