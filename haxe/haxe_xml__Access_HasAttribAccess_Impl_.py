class haxe_xml__Access_HasAttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.HasAttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        return this1.exists(name)
haxe_xml__Access_HasAttribAccess_Impl_._hx_class = haxe_xml__Access_HasAttribAccess_Impl_
_hx_classes["haxe.xml._Access.HasAttribAccess_Impl_"] = haxe_xml__Access_HasAttribAccess_Impl_


