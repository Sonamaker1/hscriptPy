class haxe_xml__Access_NodeListAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeListAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        l = []
        x = this1.elementsNamed(name)
        while x.hasNext():
            x1 = x.next()
            if ((x1.nodeType != Xml.Document) and ((x1.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x1.nodeType is None)) else _Xml_XmlType_Impl_.toString(x1.nodeType))))))
            this1 = x1
            l.append(this1)
        return l
haxe_xml__Access_NodeListAccess_Impl_._hx_class = haxe_xml__Access_NodeListAccess_Impl_
_hx_classes["haxe.xml._Access.NodeListAccess_Impl_"] = haxe_xml__Access_NodeListAccess_Impl_


