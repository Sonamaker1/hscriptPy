class haxe_xml__Access_NodeAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        x = this1.elementsNamed(name).next()
        if (x is None):
            xname = None
            if (this1.nodeType == Xml.Document):
                xname = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                xname = this1.nodeName
            raise haxe_Exception.thrown(((("null" if xname is None else xname) + " is missing element ") + ("null" if name is None else name)))
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1
haxe_xml__Access_NodeAccess_Impl_._hx_class = haxe_xml__Access_NodeAccess_Impl_
_hx_classes["haxe.xml._Access.NodeAccess_Impl_"] = haxe_xml__Access_NodeAccess_Impl_


