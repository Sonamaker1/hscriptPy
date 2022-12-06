class haxe_xml__Access_Access_Impl_:
    _hx_class_name = "haxe.xml._Access.Access_Impl_"
    __slots__ = ()
    _hx_statics = ["get_x", "get_name", "get_node", "get_nodes", "get_att", "get_has", "get_hasNode", "get_elements", "_new", "get_innerData", "get_innerHTML"]
    x = None
    name = None
    innerData = None
    innerHTML = None
    node = None
    nodes = None
    att = None
    has = None
    hasNode = None
    elements = None

    @staticmethod
    def get_x(this1):
        return this1

    @staticmethod
    def get_name(this1):
        if (this1.nodeType == Xml.Document):
            return "Document"
        else:
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            return this1.nodeName

    @staticmethod
    def get_node(this1):
        return this1

    @staticmethod
    def get_nodes(this1):
        return this1

    @staticmethod
    def get_att(this1):
        return this1

    @staticmethod
    def get_has(this1):
        return this1

    @staticmethod
    def get_hasNode(this1):
        return this1

    @staticmethod
    def get_elements(this1):
        return this1.elements()

    @staticmethod
    def _new(x):
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1

    @staticmethod
    def get_innerData(this1):
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        it_current = 0
        it_array = this1.children
        if (it_current >= len(it_array)):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        v = it_current
        it_current = (it_current + 1)
        v1 = (it_array[v] if v >= 0 and v < len(it_array) else None)
        if (it_current < len(it_array)):
            n = it_current
            it_current = (it_current + 1)
            n1 = (it_array[n] if n >= 0 and n < len(it_array) else None)
            tmp = None
            if ((v1.nodeType == Xml.PCData) and ((n1.nodeType == Xml.CData))):
                if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
                tmp = (StringTools.trim(v1.nodeValue) == "")
            else:
                tmp = False
            if tmp:
                if (it_current >= len(it_array)):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
                n2 = it_current
                it_current = (it_current + 1)
                n21 = (it_array[n2] if n2 >= 0 and n2 < len(it_array) else None)
                tmp = None
                if (n21.nodeType == Xml.PCData):
                    if ((n21.nodeType == Xml.Document) or ((n21.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n21.nodeType is None)) else _Xml_XmlType_Impl_.toString(n21.nodeType))))))
                    tmp = (StringTools.trim(n21.nodeValue) == "")
                else:
                    tmp = False
                if (tmp and ((it_current >= len(it_array)))):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not only have data"))
        if ((v1.nodeType != Xml.PCData) and ((v1.nodeType != Xml.CData))):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
        return v1.nodeValue

    @staticmethod
    def get_innerHTML(this1):
        s_b = python_lib_io_StringIO()
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        _g_current = 0
        _g_array = this1.children
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            s_b.write(Std.string(haxe_xml_Printer.print(x1)))
        return s_b.getvalue()
haxe_xml__Access_Access_Impl_._hx_class = haxe_xml__Access_Access_Impl_
_hx_classes["haxe.xml._Access.Access_Impl_"] = haxe_xml__Access_Access_Impl_


