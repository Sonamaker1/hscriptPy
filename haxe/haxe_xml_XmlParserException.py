class haxe_xml_XmlParserException:
    _hx_class_name = "haxe.xml.XmlParserException"
    __slots__ = ("message", "lineNumber", "positionAtLine", "position", "xml")
    _hx_fields = ["message", "lineNumber", "positionAtLine", "position", "xml"]
    _hx_methods = ["toString"]

    def __init__(self,message,xml,position):
        self.xml = xml
        self.message = message
        self.position = position
        self.lineNumber = 1
        self.positionAtLine = 0
        _g = 0
        _g1 = position
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(xml))) else ord(xml[i]))
            if (c == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.lineNumber
                _hx_local_0.lineNumber = (_hx_local_1 + 1)
                _hx_local_1
                self.positionAtLine = 0
            elif (c != 13):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.positionAtLine
                _hx_local_2.positionAtLine = (_hx_local_3 + 1)
                _hx_local_3

    def toString(self):
        return ((((((HxOverrides.stringOrNull(Type.getClassName(Type.getClass(self))) + ": ") + HxOverrides.stringOrNull(self.message)) + " at line ") + Std.string(self.lineNumber)) + " char ") + Std.string(self.positionAtLine))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.message = None
        _hx_o.lineNumber = None
        _hx_o.positionAtLine = None
        _hx_o.position = None
        _hx_o.xml = None
haxe_xml_XmlParserException._hx_class = haxe_xml_XmlParserException
_hx_classes["haxe.xml.XmlParserException"] = haxe_xml_XmlParserException


