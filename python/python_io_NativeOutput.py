class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = ["get_canSeek", "close", "prepare", "flush", "tell"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def flush(self):
        self.stream.flush()

    def tell(self):
        return self.stream.tell()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput
_hx_classes["python.io.NativeOutput"] = python_io_NativeOutput


