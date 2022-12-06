class hscript_Error(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Error"
    _hx_constructs = ["EInvalidChar", "EUnexpected", "EUnterminatedString", "EUnterminatedComment", "EInvalidPreprocessor", "EUnknownVariable", "EInvalidIterator", "EInvalidOp", "EInvalidAccess", "ECustom"]

    @staticmethod
    def EInvalidChar(c):
        return hscript_Error("EInvalidChar", 0, (c,))

    @staticmethod
    def EUnexpected(s):
        return hscript_Error("EUnexpected", 1, (s,))

    @staticmethod
    def EInvalidPreprocessor(msg):
        return hscript_Error("EInvalidPreprocessor", 4, (msg,))

    @staticmethod
    def EUnknownVariable(v):
        return hscript_Error("EUnknownVariable", 5, (v,))

    @staticmethod
    def EInvalidIterator(v):
        return hscript_Error("EInvalidIterator", 6, (v,))

    @staticmethod
    def EInvalidOp(op):
        return hscript_Error("EInvalidOp", 7, (op,))

    @staticmethod
    def EInvalidAccess(f):
        return hscript_Error("EInvalidAccess", 8, (f,))

    @staticmethod
    def ECustom(msg):
        return hscript_Error("ECustom", 9, (msg,))
hscript_Error.EUnterminatedString = hscript_Error("EUnterminatedString", 2, ())
hscript_Error.EUnterminatedComment = hscript_Error("EUnterminatedComment", 3, ())
hscript_Error._hx_class = hscript_Error
_hx_classes["hscript.Error"] = hscript_Error

