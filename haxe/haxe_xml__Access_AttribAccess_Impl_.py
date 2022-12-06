class haxe_xml__Access_AttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.AttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve", "_hx_set"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        v = this1.get(name)
        if (v is None):
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            raise haxe_Exception.thrown(((HxOverrides.stringOrNull(this1.nodeName) + " is missing attribute ") + ("null" if name is None else name)))
        return v

    @staticmethod
    def _hx_set(this1,name,value):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        this1.set(name,value)
        return value
haxe_xml__Access_AttribAccess_Impl_._hx_class = haxe_xml__Access_AttribAccess_Impl_
_hx_classes["haxe.xml._Access.AttribAccess_Impl_"] = haxe_xml__Access_AttribAccess_Impl_


