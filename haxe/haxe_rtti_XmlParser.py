class haxe_rtti_XmlParser:
    _hx_class_name = "haxe.rtti.XmlParser"
    _hx_fields = ["root", "curplatform"]
    _hx_methods = ["sort", "sortFields", "process", "mergeRights", "mergeDoc", "mergeFields", "newField", "mergeClasses", "mergeEnums", "mergeTypedefs", "mergeAbstracts", "merge", "mkPath", "mkTypeParams", "mkRights", "xerror", "xroot", "processElement", "xmeta", "xoverloads", "xpath", "xclass", "xclassfield", "xenum", "xenumfield", "xabstract", "xtypedef", "xtype", "xtypeparams", "defplat"]

    def __init__(self):
        self.curplatform = None
        self.root = list()

    def sort(self,l = None):
        if (l is None):
            l = self.root
        def _hx_local_0(e1,e2):
            n1 = None
            if (e1.index == 0):
                _g = e1.params[1]
                _g = e1.params[2]
                p = e1.params[0]
                n1 = (" " + ("null" if p is None else p))
            else:
                n1 = haxe_rtti_TypeApi.typeInfos(e1).path
            n2 = None
            if (e2.index == 0):
                _g = e2.params[1]
                _g = e2.params[2]
                p = e2.params[0]
                n2 = (" " + ("null" if p is None else p))
            else:
                n2 = haxe_rtti_TypeApi.typeInfos(e2).path
            if (n1 > n2):
                return 1
            return -1
        l.sort(key= python_lib_Functools.cmp_to_key(_hx_local_0))
        _g = 0
        while (_g < len(l)):
            x = (l[_g] if _g >= 0 and _g < len(l) else None)
            _g = (_g + 1)
            tmp = x.index
            if (tmp == 0):
                _g1 = x.params[0]
                _g2 = x.params[1]
                l1 = x.params[2]
                self.sort(l1)
            elif (tmp == 1):
                c = x.params[0]
                self.sortFields(c.fields)
                self.sortFields(c.statics)
            elif (tmp == 2):
                _g3 = x.params[0]
            elif (tmp == 3):
                _g4 = x.params[0]
            elif (tmp == 4):
                _g5 = x.params[0]
            else:
                pass

    def sortFields(self,a):
        def _hx_local_0(f1,f2):
            v1 = haxe_rtti_TypeApi.isVar(f1.type)
            v2 = haxe_rtti_TypeApi.isVar(f2.type)
            if (v1 and (not v2)):
                return -1
            if (v2 and (not v1)):
                return 1
            if (f1.name == "new"):
                return -1
            if (f2.name == "new"):
                return 1
            if (f1.name > f2.name):
                return 1
            return -1
        a.sort(key= python_lib_Functools.cmp_to_key(_hx_local_0))

    def process(self,x,platform):
        self.curplatform = platform
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        self.xroot(this1)

    def mergeRights(self,f1,f2):
        if ((((f1.get == haxe_rtti_Rights.RInline) and ((f1.set == haxe_rtti_Rights.RNo))) and ((f2.get == haxe_rtti_Rights.RNormal))) and ((f2.set == haxe_rtti_Rights.RMethod))):
            f1.get = haxe_rtti_Rights.RNormal
            f1.set = haxe_rtti_Rights.RMethod
            return True
        if Type.enumEq(f1.get,f2.get):
            return Type.enumEq(f1.set,f2.set)
        else:
            return False

    def mergeDoc(self,f1,f2):
        if (f1.doc is None):
            f1.doc = f2.doc
        elif (f2.doc is None):
            f2.doc = f1.doc
        return True

    def mergeFields(self,f,f2):
        if (not haxe_rtti_TypeApi.fieldEq(f,f2)):
            if (((f.name == f2.name) and ((self.mergeRights(f,f2) or self.mergeRights(f2,f)))) and self.mergeDoc(f,f2)):
                return haxe_rtti_TypeApi.fieldEq(f,f2)
            else:
                return False
        else:
            return True

    def newField(self,c,f):
        pass

    def mergeClasses(self,c,c2):
        if (c.isInterface != c2.isInterface):
            return False
        if (self.curplatform is not None):
            _this = c.platforms
            x = self.curplatform
            _this.append(x)
        if (c.isExtern != c2.isExtern):
            c.isExtern = False
        _g = 0
        _g1 = c2.fields
        while (_g < len(_g1)):
            f2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = c.fields
            while (_g2 < len(_g3)):
                f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if self.mergeFields(f,f2):
                    found = f
                    break
            if (found is None):
                self.newField(c,f2)
                _this = c.fields
                _this.append(f2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        _g = 0
        _g1 = c2.statics
        while (_g < len(_g1)):
            f2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = c.statics
            while (_g2 < len(_g3)):
                f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if self.mergeFields(f,f2):
                    found = f
                    break
            if (found is None):
                self.newField(c,f2)
                _this = c.statics
                _this.append(f2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        return True

    def mergeEnums(self,e,e2):
        if (e.isExtern != e2.isExtern):
            return False
        if (self.curplatform is not None):
            _this = e.platforms
            x = self.curplatform
            _this.append(x)
        _g = 0
        _g1 = e2.constructors
        while (_g < len(_g1)):
            c2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = e.constructors
            while (_g2 < len(_g3)):
                c = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if haxe_rtti_TypeApi.constructorEq(c,c2):
                    found = c
                    break
            if (found is None):
                _this = e.constructors
                _this.append(c2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        return True

    def mergeTypedefs(self,t,t2):
        if (self.curplatform is None):
            return False
        _this = t.platforms
        x = self.curplatform
        _this.append(x)
        t.types.h[self.curplatform] = t2.type
        return True

    def mergeAbstracts(self,a,a2):
        if (self.curplatform is None):
            return False
        if ((len(a.to) != len(a2.to)) or ((len(a._hx_from) != len(a2._hx_from)))):
            return False
        _g = 0
        _g1 = len(a.to)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not haxe_rtti_TypeApi.typeEq((a.to[i] if i >= 0 and i < len(a.to) else None).t,(a2.to[i] if i >= 0 and i < len(a2.to) else None).t)):
                return False
        _g = 0
        _g1 = len(a._hx_from)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not haxe_rtti_TypeApi.typeEq((a._hx_from[i] if i >= 0 and i < len(a._hx_from) else None).t,(a2._hx_from[i] if i >= 0 and i < len(a2._hx_from) else None).t)):
                return False
        if (a2.impl is not None):
            self.mergeClasses(a.impl,a2.impl)
        _this = a.platforms
        x = self.curplatform
        _this.append(x)
        return True

    def merge(self,t):
        inf = haxe_rtti_TypeApi.typeInfos(t)
        _this = inf.path
        pack = _this.split(".")
        cur = self.root
        curpack = list()
        if (len(pack) != 0):
            pack.pop()
        _g = 0
        while (_g < len(pack)):
            p = (pack[_g] if _g >= 0 and _g < len(pack) else None)
            _g = (_g + 1)
            found = False
            _g1 = 0
            while (_g1 < len(cur)):
                pk = (cur[_g1] if _g1 >= 0 and _g1 < len(cur) else None)
                _g1 = (_g1 + 1)
                if (pk.index == 0):
                    _g2 = pk.params[1]
                    pname = pk.params[0]
                    subs = pk.params[2]
                    if (pname == p):
                        found = True
                        cur = subs
                        break
            curpack.append(p)
            if (not found):
                pk1 = list()
                x = haxe_rtti_TypeTree.TPackage(p,".".join([python_Boot.toString1(x1,'') for x1 in curpack]),pk1)
                cur.append(x)
                cur = pk1
        _g = 0
        while (_g < len(cur)):
            ct = (cur[_g] if _g >= 0 and _g < len(cur) else None)
            _g = (_g + 1)
            tmp = None
            if (ct.index == 0):
                _g1 = ct.params[0]
                _g2 = ct.params[1]
                _g3 = ct.params[2]
                tmp = True
            else:
                tmp = False
            if tmp:
                continue
            tinf = haxe_rtti_TypeApi.typeInfos(ct)
            if (tinf.path == inf.path):
                sameType = True
                if ((tinf.doc is None) != ((inf.doc is None))):
                    if (inf.doc is None):
                        inf.doc = tinf.doc
                    else:
                        tinf.doc = inf.doc
                if (tinf.path == "haxe._Int64.NativeInt64"):
                    continue
                if (((tinf.module == inf.module) and ((tinf.doc == inf.doc))) and ((tinf.isPrivate == inf.isPrivate))):
                    tmp1 = ct.index
                    if (tmp1 == 0):
                        _g4 = ct.params[0]
                        _g5 = ct.params[1]
                        _g6 = ct.params[2]
                        sameType = False
                    elif (tmp1 == 1):
                        c = ct.params[0]
                        if (t.index == 1):
                            c2 = t.params[0]
                            if self.mergeClasses(c,c2):
                                return
                        else:
                            sameType = False
                    elif (tmp1 == 2):
                        e = ct.params[0]
                        if (t.index == 2):
                            e2 = t.params[0]
                            if self.mergeEnums(e,e2):
                                return
                        else:
                            sameType = False
                    elif (tmp1 == 3):
                        td = ct.params[0]
                        if (t.index == 3):
                            td2 = t.params[0]
                            if self.mergeTypedefs(td,td2):
                                return
                    elif (tmp1 == 4):
                        a = ct.params[0]
                        if (t.index == 4):
                            a2 = t.params[0]
                            if self.mergeAbstracts(a,a2):
                                return
                        else:
                            sameType = False
                    else:
                        pass
                msg = (((("module " + HxOverrides.stringOrNull(inf.module)) + " should be ") + HxOverrides.stringOrNull(tinf.module)) if ((tinf.module != inf.module)) else ("documentation is different" if ((tinf.doc != inf.doc)) else ("private flag is different" if ((tinf.isPrivate != inf.isPrivate)) else ("type kind is different" if ((not sameType)) else "could not merge definition"))))
                _this = tinf.platforms
                raise haxe_Exception.thrown((((((((("Incompatibilities between " + HxOverrides.stringOrNull(tinf.path)) + " in ") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + " and ") + HxOverrides.stringOrNull(self.curplatform)) + " (") + ("null" if msg is None else msg)) + ")"))
        cur.append(t)

    def mkPath(self,p):
        return p

    def mkTypeParams(self,p):
        pl = p.split(":")
        if ((pl[0] if 0 < len(pl) else None) == ""):
            return list()
        return pl

    def mkRights(self,r):
        r1 = r
        _hx_local_0 = len(r1)
        if (_hx_local_0 == 4):
            if (r1 == "null"):
                return haxe_rtti_Rights.RNo
            else:
                return haxe_rtti_Rights.RCall(r)
        elif (_hx_local_0 == 7):
            if (r1 == "dynamic"):
                return haxe_rtti_Rights.RDynamic
            else:
                return haxe_rtti_Rights.RCall(r)
        elif (_hx_local_0 == 6):
            if (r1 == "inline"):
                return haxe_rtti_Rights.RInline
            elif (r1 == "method"):
                return haxe_rtti_Rights.RMethod
            else:
                return haxe_rtti_Rights.RCall(r)
        else:
            return haxe_rtti_Rights.RCall(r)

    def xerror(self,c):
        tmp = None
        if (c.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (c.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c.nodeType is None)) else _Xml_XmlType_Impl_.toString(c.nodeType))))))
            tmp = c.nodeName
        raise haxe_Exception.thrown(("Invalid " + ("null" if tmp is None else tmp)))

    def xroot(self,x):
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            self.merge(self.processElement(c1))

    def processElement(self,x):
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        c = this1
        _g = None
        if (c.nodeType == Xml.Document):
            _g = "Document"
        else:
            if (c.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c.nodeType is None)) else _Xml_XmlType_Impl_.toString(c.nodeType))))))
            _g = c.nodeName
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "class"):
                return haxe_rtti_TypeTree.TClassdecl(self.xclass(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 4):
            if (_g1 == "enum"):
                return haxe_rtti_TypeTree.TEnumdecl(self.xenum(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 7):
            if (_g1 == "typedef"):
                return haxe_rtti_TypeTree.TTypedecl(self.xtypedef(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 8):
            if (_g1 == "abstract"):
                return haxe_rtti_TypeTree.TAbstractdecl(self.xabstract(c))
            else:
                return self.xerror(c)
        else:
            return self.xerror(c)

    def xmeta(self,x):
        ml = []
        _g = 0
        _g1 = haxe_xml__Access_NodeListAccess_Impl_.resolve(x,"m")
        while (_g < len(_g1)):
            m = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            pl = []
            _g2 = 0
            _g3 = haxe_xml__Access_NodeListAccess_Impl_.resolve(m,"e")
            while (_g2 < len(_g3)):
                p = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                x = haxe_xml__Access_Access_Impl_.get_innerHTML(p)
                pl.append(x)
            x1 = _hx_AnonObject({'name': haxe_xml__Access_AttribAccess_Impl_.resolve(m,"n"), 'params': pl})
            ml.append(x1)
        return ml

    def xoverloads(self,x):
        l = list()
        m = x.elements()
        while m.hasNext():
            m1 = m.next()
            x = self.xclassfield(m1)
            l.append(x)
        return l

    def xpath(self,x):
        path = self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path"))
        params = list()
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            x = self.xtype(c1)
            params.append(x)
        return _hx_AnonObject({'path': path, 'params': params})

    def xclass(self,x):
        csuper = None
        doc = None
        tdynamic = None
        interfaces = list()
        fields = list()
        statics = list()
        meta = []
        isInterface = x.exists("interface")
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 10):
                if (_g1 == "implements"):
                    x3 = self.xpath(c1)
                    interfaces.append(x3)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 12):
                if (_g1 == "haxe_dynamic"):
                    x2 = c1.firstElement()
                    if ((x2.nodeType != Xml.Document) and ((x2.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x2.nodeType is None)) else _Xml_XmlType_Impl_.toString(x2.nodeType))))))
                    this1 = x2
                    tdynamic = self.xtype(this1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 4):
                if (_g1 == "meta"):
                    meta = self.xmeta(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 7):
                if (_g1 == "extends"):
                    if isInterface:
                        x1 = self.xpath(c1)
                        interfaces.append(x1)
                    else:
                        csuper = self.xpath(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif c1.exists("static"):
                x4 = self.xclassfield(c1)
                statics.append(x4)
            else:
                x5 = self.xclassfield(c1)
                fields.append(x5)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'isExtern': x.exists("extern"), 'isFinal': x.exists("final"), 'isInterface': isInterface, 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'superClass': csuper, 'interfaces': interfaces, 'fields': fields, 'statics': statics, 'tdynamic': tdynamic, 'platforms': self.defplat(), 'meta': meta})

    def xclassfield(self,x,defPublic = None):
        if (defPublic is None):
            defPublic = False
        e = x.elements()
        t = self.xtype(e.next())
        doc = None
        meta = []
        overloads = None
        c = e
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 9):
                if (_g1 == "overloads"):
                    overloads = self.xoverloads(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 4):
                if (_g1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                else:
                    self.xerror(c1)
            else:
                self.xerror(c1)
        tmp = None
        if (x.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            tmp = x.nodeName
        return _hx_AnonObject({'name': tmp, 'type': t, 'isPublic': (x.exists("public") or defPublic), 'isFinal': x.exists("final"), 'isOverride': x.exists("override"), 'line': (Std.parseInt(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"line")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"line")) else None), 'doc': doc, 'get': (self.mkRights(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"get")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"get")) else haxe_rtti_Rights.RNormal), 'set': (self.mkRights(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"set")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"set")) else haxe_rtti_Rights.RNormal), 'params': (self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"params")) else []), 'platforms': self.defplat(), 'meta': meta, 'overloads': overloads, 'expr': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"expr") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"expr")) else None)})

    def xenum(self,x):
        cl = list()
        doc = None
        meta = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            tmp = None
            if (c1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                tmp = c1.nodeName
            if (tmp == "haxe_doc"):
                doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
            else:
                tmp1 = None
                if (c1.nodeType == Xml.Document):
                    tmp1 = "Document"
                else:
                    if (c1.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                    tmp1 = c1.nodeName
                if (tmp1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    x1 = self.xenumfield(c1)
                    cl.append(x1)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'isExtern': x.exists("extern"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'constructors': cl, 'platforms': self.defplat(), 'meta': meta})

    def xenumfield(self,x):
        args = None
        docElements = x.elementsNamed("haxe_doc")
        xdoc = (docElements.next() if (docElements.hasNext()) else None)
        meta = (self.xmeta(haxe_xml__Access_NodeAccess_Impl_.resolve(x,"meta")) if (haxe_xml__Access_HasNodeAccess_Impl_.resolve(x,"meta")) else [])
        if haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"a"):
            _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"a")
            names = _this.split(":")
            elts = x.elements()
            args = list()
            _g = 0
            while (_g < len(names)):
                c = (names[_g] if _g >= 0 and _g < len(names) else None)
                _g = (_g + 1)
                opt = False
                if ((("" if ((0 >= len(c))) else c[0])) == "?"):
                    opt = True
                    c = HxString.substr(c,1,None)
                x1 = _hx_AnonObject({'name': c, 'opt': opt, 't': self.xtype(elts.next())})
                args.append(x1)
        tmp = None
        if (x.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            tmp = x.nodeName
        tmp1 = None
        if (xdoc is None):
            tmp1 = None
        else:
            if ((xdoc.nodeType != Xml.Document) and ((xdoc.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((xdoc.nodeType is None)) else _Xml_XmlType_Impl_.toString(xdoc.nodeType))))))
            this1 = xdoc
            tmp1 = haxe_xml__Access_Access_Impl_.get_innerData(this1)
        return _hx_AnonObject({'name': tmp, 'args': args, 'doc': tmp1, 'meta': meta, 'platforms': self.defplat()})

    def xabstract(self,x):
        doc = None
        impl = None
        athis = None
        meta = []
        to = []
        _hx_from = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 4):
                if (_g1 == "from"):
                    t = c1.elements()
                    while t.hasNext():
                        t1 = t.next()
                        x1 = t1.firstElement()
                        if ((x1.nodeType != Xml.Document) and ((x1.nodeType != Xml.Element))):
                            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x1.nodeType is None)) else _Xml_XmlType_Impl_.toString(x1.nodeType))))))
                        this1 = x1
                        x2 = self.xtype(this1)
                        x3 = (haxe_xml__Access_AttribAccess_Impl_.resolve(t1,"field") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(t1,"field")) else None)
                        _hx_from.append(_hx_AnonObject({'t': x2, 'field': x3}))
                elif (_g1 == "impl"):
                    impl = self.xclass(haxe_xml__Access_NodeAccess_Impl_.resolve(c1,"class"))
                elif (_g1 == "meta"):
                    meta = self.xmeta(c1)
                elif (_g1 == "this"):
                    x4 = c1.firstElement()
                    if ((x4.nodeType != Xml.Document) and ((x4.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x4.nodeType is None)) else _Xml_XmlType_Impl_.toString(x4.nodeType))))))
                    this2 = x4
                    athis = self.xtype(this2)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 2):
                if (_g1 == "to"):
                    t2 = c1.elements()
                    while t2.hasNext():
                        t3 = t2.next()
                        x5 = t3.firstElement()
                        if ((x5.nodeType != Xml.Document) and ((x5.nodeType != Xml.Element))):
                            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x5.nodeType is None)) else _Xml_XmlType_Impl_.toString(x5.nodeType))))))
                        this3 = x5
                        x6 = self.xtype(this3)
                        x7 = (haxe_xml__Access_AttribAccess_Impl_.resolve(t3,"field") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(t3,"field")) else None)
                        to.append(_hx_AnonObject({'t': x6, 'field': x7}))
                else:
                    self.xerror(c1)
            else:
                self.xerror(c1)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'platforms': self.defplat(), 'meta': meta, 'athis': athis, 'to': to, '_hx_from': _hx_from, 'impl': impl})

    def xtypedef(self,x):
        doc = None
        t = None
        meta = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            tmp = None
            if (c1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                tmp = c1.nodeName
            if (tmp == "haxe_doc"):
                doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
            else:
                tmp1 = None
                if (c1.nodeType == Xml.Document):
                    tmp1 = "Document"
                else:
                    if (c1.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                    tmp1 = c1.nodeName
                if (tmp1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    t = self.xtype(c1)
        types = haxe_ds_StringMap()
        if (self.curplatform is not None):
            types.h[self.curplatform] = t
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'type': t, 'types': types, 'platforms': self.defplat(), 'meta': meta})

    def xtype(self,x):
        _g = None
        if (x.nodeType == Xml.Document):
            _g = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            _g = x.nodeName
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 1):
            if (_g1 == "a"):
                fields = list()
                f = x.elements()
                while f.hasNext():
                    f1 = f.next()
                    f2 = self.xclassfield(f1,True)
                    f2.platforms = list()
                    fields.append(f2)
                return haxe_rtti_CType.CAnonymous(fields)
            elif (_g1 == "c"):
                return haxe_rtti_CType.CClass(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "d"):
                t = None
                tx = x.firstElement()
                if (tx is not None):
                    if ((tx.nodeType != Xml.Document) and ((tx.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((tx.nodeType is None)) else _Xml_XmlType_Impl_.toString(tx.nodeType))))))
                    this1 = tx
                    t = self.xtype(this1)
                return haxe_rtti_CType.CDynamic(t)
            elif (_g1 == "e"):
                return haxe_rtti_CType.CEnum(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "f"):
                args = list()
                _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"a")
                aname = _this.split(":")
                eargs_current = 0
                eargs_array = aname
                evalues = None
                if haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"v"):
                    _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"v")
                    evalues = haxe_iterators_ArrayIterator(_this.split(":"))
                else:
                    evalues = None
                e = x.elements()
                while e.hasNext():
                    e1 = e.next()
                    opt = False
                    a = None
                    if (eargs_current < len(eargs_array)):
                        a1 = eargs_current
                        eargs_current = (eargs_current + 1)
                        a = (eargs_array[a1] if a1 >= 0 and a1 < len(eargs_array) else None)
                    else:
                        a = None
                    if (a is None):
                        a = ""
                    if ((("" if ((0 >= len(a))) else a[0])) == "?"):
                        opt = True
                        a = HxString.substr(a,1,None)
                    v = None
                    if ((evalues is None) or ((evalues.current >= len(evalues.array)))):
                        v = None
                    else:
                        def _hx_local_2():
                            _hx_local_1 = evalues.current
                            evalues.current = (evalues.current + 1)
                            return _hx_local_1
                        v = python_internal_ArrayImpl._get(evalues.array, _hx_local_2())
                    x1 = self.xtype(e1)
                    args.append(_hx_AnonObject({'name': a, 'opt': opt, 't': x1, 'value': (None if ((v == "")) else v)}))
                ret = python_internal_ArrayImpl._get(args, (len(args) - 1))
                python_internal_ArrayImpl.remove(args,ret)
                return haxe_rtti_CType.CFunction(args,ret.t)
            elif (_g1 == "t"):
                return haxe_rtti_CType.CTypedef(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "x"):
                return haxe_rtti_CType.CAbstract(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            else:
                return self.xerror(x)
        elif (_hx_local_0 == 7):
            if (_g1 == "unknown"):
                return haxe_rtti_CType.CUnknown
            else:
                return self.xerror(x)
        else:
            return self.xerror(x)

    def xtypeparams(self,x):
        p = list()
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            x = self.xtype(c1)
            p.append(x)
        return p

    def defplat(self):
        l = list()
        if (self.curplatform is not None):
            x = self.curplatform
            l.append(x)
        return l

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
        _hx_o.curplatform = None
haxe_rtti_XmlParser._hx_class = haxe_rtti_XmlParser
_hx_classes["haxe.rtti.XmlParser"] = haxe_rtti_XmlParser


