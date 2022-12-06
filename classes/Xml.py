class Xml:
    _hx_class_name = "Xml"
    __slots__ = ("nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap")
    _hx_fields = ["nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap"]
    _hx_methods = ["get_nodeName", "set_nodeName", "get_nodeValue", "set_nodeValue", "get", "set", "remove", "exists", "attributes", "iterator", "elements", "elementsNamed", "firstChild", "firstElement", "addChild", "removeChild", "insertChild", "toString", "ensureElementType"]
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "parse", "createElement", "createPCData", "createCData", "createComment", "createDocType", "createProcessingInstruction", "createDocument"]

    def __init__(self,nodeType):
        self.parent = None
        self.nodeValue = None
        self.nodeName = None
        self.nodeType = nodeType
        self.children = []
        self.attributeMap = haxe_ds_StringMap()

    def get_nodeName(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeName

    def set_nodeName(self,v):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeName = v
                return self.nodeName
            return _hx_local_0()
        return _hx_local_1()

    def get_nodeValue(self):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeValue

    def set_nodeValue(self,v):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeValue = v
                return self.nodeValue
            return _hx_local_0()
        return _hx_local_1()

    def get(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.h.get(att,None)

    def set(self,att,value):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.h[att] = value

    def remove(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.remove(att)

    def exists(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (att in self.attributeMap.h)

    def attributes(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.keys()

    def iterator(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return haxe_iterators_ArrayIterator(self.children)

    def elements(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            if (child.nodeType == Xml.Element):
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def elementsNamed(self,name):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            tmp = None
            if (child.nodeType == Xml.Element):
                if (child.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((child.nodeType is None)) else _Xml_XmlType_Impl_.toString(child.nodeType))))))
                tmp = (child.nodeName == name)
            else:
                tmp = False
            if tmp:
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def firstChild(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (self.children[0] if 0 < len(self.children) else None)

    def firstElement(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = 0
        _g1 = self.children
        while (_g < len(_g1)):
            child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (child.nodeType == Xml.Element):
                return child
        return None

    def addChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            x.parent.removeChild(x)
        _this = self.children
        _this.append(x)
        x.parent = self

    def removeChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if python_internal_ArrayImpl.remove(self.children,x):
            x.parent = None
            return True
        return False

    def insertChild(self,x,pos):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            python_internal_ArrayImpl.remove(x.parent.children,x)
        self.children.insert(pos, x)
        x.parent = self

    def toString(self):
        return haxe_xml_Printer.print(self)

    def ensureElementType(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))

    @staticmethod
    def parse(_hx_str):
        return haxe_xml_Parser.parse(_hx_str)

    @staticmethod
    def createElement(name):
        xml = Xml(Xml.Element)
        if (xml.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeName = name
        return xml

    @staticmethod
    def createPCData(data):
        xml = Xml(Xml.PCData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createCData(data):
        xml = Xml(Xml.CData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createComment(data):
        xml = Xml(Xml.Comment)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocType(data):
        xml = Xml(Xml.DocType)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createProcessingInstruction(data):
        xml = Xml(Xml.ProcessingInstruction)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocument():
        return Xml(Xml.Document)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.nodeType = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.attributeMap = None
Xml._hx_class = Xml
_hx_classes["Xml"] = Xml

