class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

    @staticmethod
    def createFileInputFromText(t):
        return sys_io_FileInput(python_io_FileTextInput(t))

    @staticmethod
    def createFileInputFromBytes(t):
        return sys_io_FileInput(python_io_FileBytesInput(t))

    @staticmethod
    def createFileOutputFromText(t):
        return sys_io_FileOutput(python_io_FileTextOutput(t))

    @staticmethod
    def createFileOutputFromBytes(t):
        return sys_io_FileOutput(python_io_FileBytesOutput(t))

    @staticmethod
    def seekInTextMode(stream,tell,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            p = (tell() + p)
            pos1 = 0
        elif (pos2 == 2):
            stream.seek(0,2)
            p = (tell() + p)
            pos1 = 0
        else:
            pass
        stream.seek(p,pos1)

    @staticmethod
    def seekInBinaryMode(stream,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            pos1 = 1
        elif (pos2 == 2):
            pos1 = 2
        else:
            pass
        stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools
_hx_classes["python.io.IoTools"] = python_io_IoTools


