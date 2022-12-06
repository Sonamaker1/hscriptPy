class hscript_CheckerTypes:
    _hx_class_name = "hscript.CheckerTypes"
    __slots__ = ("types", "t_string", "localParams")
    _hx_fields = ["types", "t_string", "localParams"]
    _hx_methods = ["addXmlApi", "addXmlType", "makeXmlType", "getType", "resolve"]

    def __init__(self):
        self.localParams = None
        self.t_string = None
        self.types = haxe_ds_StringMap()
        self.types = haxe_ds_StringMap()
        self.types.h["Void"] = hscript_CTypedecl.CTAlias(hscript_TType.TVoid)
        self.types.h["Int"] = hscript_CTypedecl.CTAlias(hscript_TType.TInt)
        self.types.h["Float"] = hscript_CTypedecl.CTAlias(hscript_TType.TFloat)
        self.types.h["Bool"] = hscript_CTypedecl.CTAlias(hscript_TType.TBool)
        self.types.h["Dynamic"] = hscript_CTypedecl.CTAlias(hscript_TType.TDynamic)

    def addXmlApi(self,api):
        types = haxe_rtti_XmlParser()
        types.process(api,"")
        todo = []
        _g = 0
        _g1 = types.root
        while (_g < len(_g1)):
            v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            self.addXmlType(v,todo)
        _g = 0
        while (_g < len(todo)):
            f = (todo[_g] if _g >= 0 and _g < len(todo) else None)
            _g = (_g + 1)
            f()
        self.t_string = self.getType("String")

    def addXmlType(self,x,todo):
        _gthis = self
        tmp = x.index
        if (tmp == 0):
            name = x.params[0]
            full = x.params[1]
            subs = x.params[2]
            _g = 0
            while (_g < len(subs)):
                s = (subs[_g] if _g >= 0 and _g < len(subs) else None)
                _g = (_g + 1)
                self.addXmlType(s,todo)
        elif (tmp == 1):
            c = x.params[0]
            if (c.path in self.types.h):
                return
            cl = _hx_AnonObject({'name': c.path, 'params': [], 'fields': haxe_ds_StringMap(), 'statics': haxe_ds_StringMap()})
            if c.isInterface:
                Reflect.setField(cl,"isInterface",True)
            _g = 0
            _g1 = c.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _this = cl.params
                _this.append(hscript_TType.TParam(p))
            def _hx_local_9():
                _g = haxe_ds_StringMap()
                _g1 = 0
                _g2 = cl.params
                while (_g1 < len(_g2)):
                    t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    key = ((HxOverrides.stringOrNull(c.path) + ".") + HxOverrides.stringOrNull(hscript_Checker.typeStr(t)))
                    _g.h[key] = t
                _gthis.localParams = _g
                if (c.superClass is not None):
                    _gthis1 = _gthis
                    c1 = c.superClass.path
                    _g = []
                    _g1 = 0
                    _g2 = c.superClass.params
                    while (_g1 < len(_g2)):
                        t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                        _g1 = (_g1 + 1)
                        x = _gthis.makeXmlType(t)
                        _g.append(x)
                    Reflect.setField(cl,"superClass",_gthis1.getType(c1,_g))
                if (c.interfaces is not None):
                    Reflect.setField(cl,"interfaces",[])
                    _g = 0
                    _g1 = c.interfaces
                    while (_g < len(_g1)):
                        i = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                        _g = (_g + 1)
                        _this = Reflect.field(cl,"interfaces")
                        _gthis1 = _gthis
                        i1 = i.path
                        _g2 = []
                        _g3 = 0
                        _g4 = i.params
                        while (_g3 < len(_g4)):
                            t = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                            _g3 = (_g3 + 1)
                            x = _gthis.makeXmlType(t)
                            _g2.append(x)
                        x1 = _gthis1.getType(i1,_g2)
                        _this.append(x1)
                pkeys = []
                _g = 0
                _g1 = c.fields
                while (_g < len(_g1)):
                    f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    if ((f.isOverride or ((HxString.substr(f.name,0,4) == "get_"))) or ((HxString.substr(f.name,0,4) == "set_"))):
                        continue
                    skip = False
                    complete = (not f.name.startswith("__"))
                    _g2 = 0
                    _g3 = f.meta
                    while (_g2 < len(_g3)):
                        m = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        if (m.name == ":noScript"):
                            skip = True
                            break
                        if (m.name == ":noCompletion"):
                            complete = False
                    if skip:
                        continue
                    _g4 = f.set
                    fl = None
                    fl1 = _g4.index
                    if ((fl1 == 4) or ((fl1 == 0))):
                        fl = True
                    elif (fl1 == 2):
                        _g5 = _g4.params[0]
                        fl = True
                    else:
                        fl = False
                    fl2 = _hx_AnonObject({'isPublic': f.isPublic, 'canWrite': fl, 'complete': complete, 'params': [], 'name': f.name, 't': None})
                    _g6 = 0
                    _g7 = f.params
                    while (_g6 < len(_g7)):
                        p = (_g7[_g6] if _g6 >= 0 and _g6 < len(_g7) else None)
                        _g6 = (_g6 + 1)
                        pt = hscript_TType.TParam(p)
                        key = ((HxOverrides.stringOrNull(f.name) + ".") + ("null" if p is None else p))
                        pkeys.append(key)
                        _this = fl2.params
                        _this.append(pt)
                        _gthis.localParams.h[key] = pt
                    fl2.t = _gthis.makeXmlType(f.type)
                    while (len(pkeys) > 0):
                        _gthis.localParams.remove((None if ((len(pkeys) == 0)) else pkeys.pop()))
                    if (fl2.name == "new"):
                        Reflect.setField(cl,"constructor",fl2)
                    else:
                        cl.fields.h[f.name] = fl2
                _gthis.localParams = None
            todo.append(_hx_local_9)
            self.types.h[cl.name] = hscript_CTypedecl.CTClass(cl)
        elif (tmp == 2):
            e = x.params[0]
            if (e.path in self.types.h):
                return
            en = _hx_AnonObject({'name': e.path, 'params': [], 'constructors': []})
            _g = 0
            _g1 = e.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _this = en.params
                _this.append(hscript_TType.TParam(p))
            def _hx_local_14():
                _g = haxe_ds_StringMap()
                _g1 = 0
                _g2 = en.params
                while (_g1 < len(_g2)):
                    t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    key = ((HxOverrides.stringOrNull(e.path) + ".") + HxOverrides.stringOrNull(hscript_Checker.typeStr(t)))
                    _g.h[key] = t
                _gthis.localParams = _g
                _g = 0
                _g1 = e.constructors
                while (_g < len(_g1)):
                    c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    _this = en.constructors
                    c1 = c.name
                    x = None
                    if (c.args is None):
                        x = None
                    else:
                        _g2 = []
                        _g3 = 0
                        _g4 = c.args
                        while (_g3 < len(_g4)):
                            a = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                            _g3 = (_g3 + 1)
                            x1 = _hx_AnonObject({'name': a.name, 'opt': a.opt, 't': _gthis.makeXmlType(a.t)})
                            _g2.append(x1)
                        x = _g2
                    _this.append(_hx_AnonObject({'name': c1, 'args': x}))
                _gthis.localParams = None
            todo.append(_hx_local_14)
            self.types.h[en.name] = hscript_CTypedecl.CTEnum(en)
        elif (tmp == 3):
            t = x.params[0]
            if (t.path in self.types.h):
                return
            td = _hx_AnonObject({'name': t.path, 'params': [], 't': None})
            _g = 0
            _g1 = t.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _this = td.params
                _this.append(hscript_TType.TParam(p))
            if (t.path == "hscript.TypeCheck"):
                td.params.reverse()
            def _hx_local_17():
                _g = haxe_ds_StringMap()
                _g1 = 0
                _g2 = td.params
                while (_g1 < len(_g2)):
                    pt = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    key = ((HxOverrides.stringOrNull(t.path) + ".") + HxOverrides.stringOrNull(hscript_Checker.typeStr(pt)))
                    _g.h[key] = pt
                _gthis.localParams = _g
                td.t = _gthis.makeXmlType(t.type)
                _gthis.localParams = None
            todo.append(_hx_local_17)
            self.types.h[t.path] = hscript_CTypedecl.CTTypedef(td)
        elif (tmp == 4):
            a = x.params[0]
            if (a.path in self.types.h):
                return
            ta = _hx_AnonObject({'name': a.path, 'params': [], 't': None})
            _g = 0
            _g1 = a.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _this = ta.params
                _this.append(hscript_TType.TParam(p))
            def _hx_local_20():
                _g = haxe_ds_StringMap()
                _g1 = 0
                _g2 = ta.params
                while (_g1 < len(_g2)):
                    t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    key = ((HxOverrides.stringOrNull(a.path) + ".") + HxOverrides.stringOrNull(hscript_Checker.typeStr(t)))
                    _g.h[key] = t
                _gthis.localParams = _g
                ta.t = _gthis.makeXmlType(a.athis)
                _gthis.localParams = None
            todo.append(_hx_local_20)
            self.types.h[a.path] = hscript_CTypedecl.CTAbstract(ta)
        else:
            pass

    def makeXmlType(self,t):
        tmp = t.index
        if (tmp == 0):
            return hscript_TType.TUnresolved("Unknown")
        elif (tmp == 1):
            name = t.params[0]
            params = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(params)):
                t1 = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                _g1 = (_g1 + 1)
                x = self.makeXmlType(t1)
                _g.append(x)
            return self.getType(name,_g)
        elif (tmp == 2):
            name = t.params[0]
            params = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(params)):
                t1 = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                _g1 = (_g1 + 1)
                x = self.makeXmlType(t1)
                _g.append(x)
            return self.getType(name,_g)
        elif (tmp == 3):
            name = t.params[0]
            params = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(params)):
                t1 = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                _g1 = (_g1 + 1)
                x = self.makeXmlType(t1)
                _g.append(x)
            return self.getType(name,_g)
        elif (tmp == 4):
            args = t.params[0]
            ret = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': a.name, 'opt': a.opt, 't': self.makeXmlType(a.t)})
                _g.append(x)
            return hscript_TType.TFun(_g,self.makeXmlType(ret))
        elif (tmp == 5):
            fields = t.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                f1 = f.name
                x = self.makeXmlType(f.type)
                m = f.meta
                x1 = None
                if (m is None):
                    x1 = False
                else:
                    b = False
                    _g2 = 0
                    while (_g2 < len(m)):
                        m1 = (m[_g2] if _g2 >= 0 and _g2 < len(m) else None)
                        _g2 = (_g2 + 1)
                        if (m1.name == ":optional"):
                            b = True
                            break
                    x1 = b
                _g.append(_hx_AnonObject({'name': f1, 't': x, 'opt': x1}))
            return hscript_TType.TAnon(_g)
        elif (tmp == 6):
            t1 = t.params[0]
            return hscript_TType.TDynamic
        elif (tmp == 7):
            name = t.params[0]
            params = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(params)):
                t = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                _g1 = (_g1 + 1)
                x = self.makeXmlType(t)
                _g.append(x)
            return self.getType(name,_g)
        else:
            pass

    def getType(self,name,args = None):
        if (self.localParams is not None):
            t = self.localParams.h.get(name,None)
            if (t is not None):
                return t
        t = self.resolve(name,args)
        if (t is None):
            pack = name.split(".")
            if (len(pack) > 1):
                priv = python_internal_ArrayImpl._get(pack, (len(pack) - 2))
                if (HxString.charCodeAt(priv,0) == 95):
                    python_internal_ArrayImpl.remove(pack,priv)
                    return self.getType(".".join([python_Boot.toString1(x1,'') for x1 in pack]),args)
            return hscript_TType.TUnresolved(name)
        return t

    def resolve(self,name,args = None):
        if (name == "Null"):
            if ((args is None) or ((len(args) != 1))):
                raise haxe_Exception.thrown("Missing Null<T> parameter")
            return hscript_TType.TNull((args[0] if 0 < len(args) else None))
        t = self.types.h.get(name,None)
        if (t is None):
            return None
        if (args is None):
            args = []
        tmp = t.index
        if (tmp == 0):
            c = t.params[0]
            return hscript_TType.TInst(c,args)
        elif (tmp == 1):
            e = t.params[0]
            return hscript_TType.TEnum(e,args)
        elif (tmp == 2):
            t1 = t.params[0]
            return hscript_TType.TType(t1,args)
        elif (tmp == 3):
            t1 = t.params[0]
            return t1
        elif (tmp == 4):
            a = t.params[0]
            return hscript_TType.TAbstract(a,args)
        else:
            pass

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.types = None
        _hx_o.t_string = None
        _hx_o.localParams = None
hscript_CheckerTypes._hx_class = hscript_CheckerTypes
_hx_classes["hscript.CheckerTypes"] = hscript_CheckerTypes


