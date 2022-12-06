class python_io_NativeBytesInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def readinto(self,b):
        return self.stream.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput
_hx_classes["python.io.NativeBytesInput"] = python_io_NativeBytesInput


