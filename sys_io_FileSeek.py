class sys_io_FileSeek(Enum):
    __slots__ = ()
    _hx_class_name = "sys.io.FileSeek"
    _hx_constructs = ["SeekBegin", "SeekCur", "SeekEnd"]
sys_io_FileSeek.SeekBegin = sys_io_FileSeek("SeekBegin", 0, ())
sys_io_FileSeek.SeekCur = sys_io_FileSeek("SeekCur", 1, ())
sys_io_FileSeek.SeekEnd = sys_io_FileSeek("SeekEnd", 2, ())
sys_io_FileSeek._hx_class = sys_io_FileSeek
_hx_classes["sys.io.FileSeek"] = sys_io_FileSeek

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

haxe_SysTools.winMetaCharacters = [32, 40, 41, 37, 33, 94, 34, 60, 62, 38, 124, 10, 13, 44, 59]
StringTools.winMetaCharacters = haxe_SysTools.winMetaCharacters
Sys._programPath = sys_FileSystem.fullPath(python_lib_Inspect.getsourcefile(Sys))
_Xml_XmlType_Impl_.Element = 0
_Xml_XmlType_Impl_.PCData = 1
_Xml_XmlType_Impl_.CData = 2
_Xml_XmlType_Impl_.Comment = 3
_Xml_XmlType_Impl_.DocType = 4
_Xml_XmlType_Impl_.ProcessingInstruction = 5
_Xml_XmlType_Impl_.Document = 6
Xml.Element = 0
Xml.PCData = 1
Xml.CData = 2
Xml.Comment = 3
Xml.DocType = 4
Xml.ProcessingInstruction = 5
Xml.Document = 6
def _hx_init_haxe_io_FPHelper_i64tmp():
    def _hx_local_0():
        this1 = haxe__Int64____Int64(0,0)
        return this1
    return _hx_local_0()
haxe_io_FPHelper.i64tmp = _hx_init_haxe_io_FPHelper_i64tmp()
haxe_io_FPHelper.LN2 = 0.6931471805599453
def _hx_init_haxe_xml_Parser_escapes():
    def _hx_local_0():
        h = haxe_ds_StringMap()
        h.h["lt"] = "<"
        h.h["gt"] = ">"
        h.h["amp"] = "&"
        h.h["quot"] = "\""
        h.h["apos"] = "'"
        return h
    return _hx_local_0()
haxe_xml_Parser.escapes = _hx_init_haxe_xml_Parser_escapes()
hscript_Async.nullExpr = None
hscript_Async.nullId = hscript_Expr.EIdent("null")
hscript_Parser.p1 = 0
hscript_Parser.tokenMin = 0
hscript_Parser.tokenMax = 0
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
python_Lib.lineEnd = ("\r\n" if ((Sys.systemName() == "Windows")) else "\n")

TestHScript.main()
