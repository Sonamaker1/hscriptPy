class haxe_xml_Printer:
    _hx_class_name = "haxe.xml.Printer"
    __slots__ = ("output", "pretty")
    _hx_fields = ["output", "pretty"]
    _hx_methods = ["writeNode", "write", "newline", "hasChildren"]
    _hx_statics = ["print"]

    def __init__(self,pretty):
        self.output = StringBuf()
        self.pretty = pretty

    def writeNode(self,value,tabs):
        _g = value.nodeType
        if (_g == 0):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<"))
            _this.b.write(s)
            if (value.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeName)
            _this.b.write(s)
            attribute = value.attributes()
            while attribute.hasNext():
                attribute1 = attribute.next()
                _this = self.output
                s = Std.string(((" " + ("null" if attribute1 is None else attribute1)) + "=\""))
                _this.b.write(s)
                input = StringTools.htmlEscape(value.get(attribute1),True)
                _this1 = self.output
                s1 = Std.string(input)
                _this1.b.write(s1)
                self.output.b.write("\"")
            if self.hasChildren(value):
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
                if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _g_current = 0
                _g_array = value.children
                while (_g_current < len(_g_array)):
                    child = _g_current
                    _g_current = (_g_current + 1)
                    child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                    self.writeNode(child1,((("null" if tabs is None else tabs) + "\t") if (self.pretty) else tabs))
                _this = self.output
                s = Std.string((("null" if tabs is None else tabs) + "</"))
                _this.b.write(s)
                if (value.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _this = self.output
                s = Std.string(value.nodeName)
                _this.b.write(s)
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
            else:
                self.output.b.write("/>")
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 1):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            nodeValue = value.nodeValue
            if (len(nodeValue) != 0):
                input = (("null" if tabs is None else tabs) + HxOverrides.stringOrNull(StringTools.htmlEscape(nodeValue)))
                _this = self.output
                s = Std.string(input)
                _this.b.write(s)
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 2):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<![CDATA["))
            _this.b.write(s)
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeValue)
            _this.b.write(s)
            self.output.b.write("]]>")
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 3):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            commentContent = value.nodeValue
            commentContent = EReg("[\n\r\t]+","g").replace(commentContent,"")
            commentContent = (("<!--" + ("null" if commentContent is None else commentContent)) + "-->")
            _this = self.output
            s = Std.string(tabs)
            _this.b.write(s)
            input = StringTools.trim(commentContent)
            _this = self.output
            s = Std.string(input)
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 4):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<!DOCTYPE " + HxOverrides.stringOrNull(value.nodeValue)) + ">"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 5):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<?" + HxOverrides.stringOrNull(value.nodeValue)) + "?>"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 6):
            if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _g_current = 0
            _g_array = value.children
            while (_g_current < len(_g_array)):
                child = _g_current
                _g_current = (_g_current + 1)
                child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                self.writeNode(child1,tabs)
        else:
            pass

    def write(self,input):
        _this = self.output
        s = Std.string(input)
        _this.b.write(s)

    def newline(self):
        if self.pretty:
            self.output.b.write("\n")

    def hasChildren(self,value):
        if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
        _g_current = 0
        _g_array = value.children
        while (_g_current < len(_g_array)):
            child = _g_current
            _g_current = (_g_current + 1)
            child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
            _g = child1.nodeType
            if ((_g == 1) or ((_g == 0))):
                return True
            elif ((_g == 3) or ((_g == 2))):
                if ((child1.nodeType == Xml.Document) or ((child1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((child1.nodeType is None)) else _Xml_XmlType_Impl_.toString(child1.nodeType))))))
                if (len(StringTools.ltrim(child1.nodeValue)) != 0):
                    return True
            else:
                pass
        return False

    @staticmethod
    def print(xml,pretty = None):
        if (pretty is None):
            pretty = False
        printer = haxe_xml_Printer(pretty)
        printer.writeNode(xml,"")
        return printer.output.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.output = None
        _hx_o.pretty = None
haxe_xml_Printer._hx_class = haxe_xml_Printer
_hx_classes["haxe.xml.Printer"] = haxe_xml_Printer

