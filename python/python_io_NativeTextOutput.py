class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def seek(self,p,pos):
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.buffer.write(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput
_hx_classes["python.io.NativeTextOutput"] = python_io_NativeTextOutput


