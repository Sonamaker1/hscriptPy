class hscript_Checker:
    _hx_class_name = "hscript.Checker"
    __slots__ = ("types", "locals", "globals", "events", "currentFunType", "isCompletion", "allowDefine", "allowAsync", "allowReturn", "allowGlobalsDefine", "allowUntypedMeta")
    _hx_fields = ["types", "locals", "globals", "events", "currentFunType", "isCompletion", "allowDefine", "allowAsync", "allowReturn", "allowGlobalsDefine", "allowUntypedMeta"]
    _hx_methods = ["setGlobals", "removeGlobal", "setGlobal", "setEvent", "getGlobals", "typeArgs", "check", "edef", "error", "saveLocals", "makeType", "linkLoop", "link", "typeEq", "tryUnify", "unify", "apply", "mapType", "follow", "getFields", "getField", "unasync", "typeExprWith", "makeMono", "makeIterator", "mk", "isString", "onCompletion", "typeField", "typeExpr"]
    _hx_statics = ["typeStr"]

    def __init__(self,types = None):
        self.allowUntypedMeta = None
        self.allowGlobalsDefine = None
        self.allowReturn = None
        self.allowAsync = None
        self.allowDefine = None
        self.isCompletion = None
        self.currentFunType = None
        self.locals = None
        self.events = haxe_ds_StringMap()
        self.globals = haxe_ds_StringMap()
        if (types is None):
            types = hscript_CheckerTypes()
        self.types = types

    def setGlobals(self,cl):
        _gthis = self
        while True:
            f = cl.fields.iterator()
            while f.hasNext():
                f1 = [f.next()]
                if (f1[0] if 0 < len(f1) else None).isPublic:
                    def _hx_local_3():
                        def _hx_local_1(f):
                            def _hx_local_0():
                                _gthis1 = _gthis
                                f1 = (f[0] if 0 < len(f) else None).t
                                f2 = (f[0] if 0 < len(f) else None).params
                                _g = []
                                _g1 = 0
                                _g2 = len((f[0] if 0 < len(f) else None).params)
                                while (_g1 < _g2):
                                    i = _g1
                                    _g1 = (_g1 + 1)
                                    x = _gthis.makeMono()
                                    _g.append(x)
                                return _gthis1.apply(f1,f2,_g)
                            return _hx_local_0
                        return (f1[0] if 0 < len(f1) else None).t if (len((f1[0] if 0 < len(f1) else None).params) == 0) else hscript_TType.TLazy(_hx_local_1(f1))
                    self.setGlobal((f1[0] if 0 < len(f1) else None).name,_hx_local_3())
            if (Reflect.field(cl,"superClass") is None):
                break
            _g = Reflect.field(cl,"superClass")
            if (_g is None):
                raise haxe_Exception.thrown("assert")
            elif (_g.index == 9):
                _g1 = _g.params[1]
                c = _g.params[0]
                cl = c
            else:
                raise haxe_Exception.thrown("assert")

    def removeGlobal(self,name):
        self.globals.remove(name)

    def setGlobal(self,name,_hx_type):
        self.globals.h[name] = _hx_type

    def setEvent(self,name,_hx_type):
        self.events.h[name] = _hx_type

    def getGlobals(self):
        return self.globals

    def typeArgs(self,args,pos):
        _g = []
        _g1 = 0
        _g2 = len(args)
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            a = (args[i] if i >= 0 and i < len(args) else None)
            at = (self.makeMono() if ((Reflect.field(a,"t") is None)) else self.makeType(Reflect.field(a,"t"),pos))
            x = _hx_AnonObject({'name': a.name, 'opt': Reflect.field(a,"opt"), 't': at})
            _g.append(x)
        return _g

    def check(self,expr,withType = None,isCompletion = None):
        if (isCompletion is None):
            isCompletion = False
        _gthis = self
        if (withType is None):
            withType = hscript__Checker_WithType.NoValue
        self.locals = haxe_ds_StringMap()
        self.allowDefine = self.allowGlobalsDefine
        self.isCompletion = isCompletion
        if (expr.index == 4):
            el = expr.params[0]
            delayed = []
            last = hscript_TType.TVoid
            _g = 0
            while (_g < len(el)):
                e = [(el[_g] if _g >= 0 and _g < len(el) else None)]
                _g = (_g + 1)
                while True:
                    if ((e[0] if 0 < len(e) else None).index == 25):
                        _g1 = (e[0] if 0 < len(e) else None).params[0]
                        _g2 = (e[0] if 0 < len(e) else None).params[1]
                        e2 = (e[0] if 0 < len(e) else None).params[2]
                        python_internal_ArrayImpl._set(e, 0, e2)
                    else:
                        break
                if ((e[0] if 0 < len(e) else None).index == 14):
                    _g3 = (e[0] if 0 < len(e) else None).params[1]
                    args = (e[0] if 0 < len(e) else None).params[0]
                    name = (e[0] if 0 < len(e) else None).params[2]
                    ret = (e[0] if 0 < len(e) else None).params[3]
                    if (name is not None):
                        tret = (self.makeMono() if ((ret is None)) else self.makeType(ret,(e[0] if 0 < len(e) else None)))
                        ft = [hscript_TType.TFun(self.typeArgs(args,(e[0] if 0 < len(e) else None)),tret)]
                        self.locals.h[name] = (ft[0] if 0 < len(ft) else None)
                        def _hx_local_2(ft,e):
                            def _hx_local_1():
                                _gthis.currentFunType = (ft[0] if 0 < len(ft) else None)
                                _gthis.typeExpr((e[0] if 0 < len(e) else None),hscript__Checker_WithType.NoValue)
                                return (ft[0] if 0 < len(ft) else None)
                            return _hx_local_1
                        delayed.append(_hx_local_2(ft,e))
                    else:
                        _g4 = 0
                        while (_g4 < len(delayed)):
                            f = (delayed[_g4] if _g4 >= 0 and _g4 < len(delayed) else None)
                            _g4 = (_g4 + 1)
                            f()
                        delayed = []
                        if (python_internal_ArrayImpl._get(el, (len(el) - 1)) == (e[0] if 0 < len(e) else None)):
                            last = self.typeExpr((e[0] if 0 < len(e) else None),withType)
                        else:
                            self.typeExpr((e[0] if 0 < len(e) else None),hscript__Checker_WithType.NoValue)
                else:
                    _g5 = 0
                    while (_g5 < len(delayed)):
                        f1 = (delayed[_g5] if _g5 >= 0 and _g5 < len(delayed) else None)
                        _g5 = (_g5 + 1)
                        f1()
                    delayed = []
                    if (python_internal_ArrayImpl._get(el, (len(el) - 1)) == (e[0] if 0 < len(e) else None)):
                        last = self.typeExpr((e[0] if 0 < len(e) else None),withType)
                    else:
                        self.typeExpr((e[0] if 0 < len(e) else None),hscript__Checker_WithType.NoValue)
            _g = 0
            while (_g < len(delayed)):
                f = (delayed[_g] if _g >= 0 and _g < len(delayed) else None)
                _g = (_g + 1)
                last = f()
            return last
        return self.typeExpr(expr,withType)

    def edef(self,e):
        return e

    def error(self,msg,curExpr):
        e = hscript_Error.ECustom(msg)
        if (not self.isCompletion):
            raise haxe_Exception.thrown(e)

    def saveLocals(self):
        _g = haxe_ds_StringMap()
        k = self.locals.keys()
        while k.hasNext():
            k1 = k.next()
            value = self.locals.h.get(k1,None)
            _g.h[k1] = value
        return _g

    def makeType(self,t,e):
        tmp = t.index
        if (tmp == 0):
            path = t.params[0]
            params = t.params[1]
            ct = self.types
            ct1 = ".".join([python_Boot.toString1(x1,'') for x1 in path])
            ct2 = None
            if (params is None):
                ct2 = []
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(params)):
                    p = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                    _g1 = (_g1 + 1)
                    x = self.makeType(p,e)
                    _g.append(x)
                ct2 = _g
            ct3 = ct.resolve(ct1,ct2)
            if (ct3 is None):
                e1 = hscript_Error.ECustom(("Unknown type " + Std.string(path)))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e1)
                ct3 = hscript_TType.TDynamic
            return ct3
        elif (tmp == 1):
            args = t.params[0]
            ret = t.params[1]
            i = 0
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = i
                i = (i + 1)
                x1 = _hx_AnonObject({'name': ("p" + Std.string(x)), 'opt': False, 't': self.makeType(a,e)})
                _g.append(x1)
            return hscript_TType.TFun(_g,self.makeType(ret,e))
        elif (tmp == 2):
            fields = t.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': f.name, 'opt': False, 't': self.makeType(f.t,e)})
                _g.append(x)
            return hscript_TType.TAnon(_g)
        elif (tmp == 3):
            t1 = t.params[0]
            return self.makeType(t1,e)
        elif (tmp == 4):
            t1 = t.params[0]
            return self.makeType(t1,e)
        elif (tmp == 5):
            n = t.params[0]
            t1 = t.params[1]
            return self.makeType(t1,e)
        else:
            pass

    def linkLoop(self,a,t):
        if (t == a):
            return True
        tmp = t.index
        if (tmp == 0):
            r = t.params[0]
            if (r.r is None):
                return False
            return self.linkLoop(a,r.r)
        elif (tmp == 5):
            if (t == hscript_TType.TDynamic):
                return False
            return self.linkLoop(a,hscript_TType.TDynamic)
        elif (tmp == 9):
            _g = t.params[0]
            tl = t.params[1]
            _g = 0
            while (_g < len(tl)):
                t1 = (tl[_g] if _g >= 0 and _g < len(tl) else None)
                _g = (_g + 1)
                if self.linkLoop(a,t1):
                    return True
            return False
        elif (tmp == 10):
            _g = t.params[0]
            tl = t.params[1]
            _g = 0
            while (_g < len(tl)):
                t1 = (tl[_g] if _g >= 0 and _g < len(tl) else None)
                _g = (_g + 1)
                if self.linkLoop(a,t1):
                    return True
            return False
        elif (tmp == 11):
            _g = t.params[0]
            tl = t.params[1]
            _g = 0
            while (_g < len(tl)):
                t1 = (tl[_g] if _g >= 0 and _g < len(tl) else None)
                _g = (_g + 1)
                if self.linkLoop(a,t1):
                    return True
            return False
        elif (tmp == 12):
            _g = t.params[0]
            tl = t.params[1]
            _g = 0
            while (_g < len(tl)):
                t1 = (tl[_g] if _g >= 0 and _g < len(tl) else None)
                _g = (_g + 1)
                if self.linkLoop(a,t1):
                    return True
            return False
        elif (tmp == 13):
            args = t.params[0]
            ret = t.params[1]
            _g = 0
            while (_g < len(args)):
                arg = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                if self.linkLoop(a,arg.t):
                    return True
            return self.linkLoop(a,ret)
        elif (tmp == 14):
            fl = t.params[0]
            _g = 0
            while (_g < len(fl)):
                f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                if self.linkLoop(a,f.t):
                    return True
            return False
        else:
            return False

    def link(self,a,b,r):
        if self.linkLoop(a,b):
            return (self.follow(b) == a)
        if (b == hscript_TType.TDynamic):
            return True
        r.r = b
        return True

    def typeEq(self,t1,t2):
        if (t1 == t2):
            return True
        tmp = t1.index
        if (tmp == 0):
            r = t1.params[0]
            if (r.r is None):
                if (not self.link(t1,t2,r)):
                    return False
                r.r = t2
                return True
            return self.typeEq(r.r,t2)
        elif (tmp == 8):
            _g = t1.params[0]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                t11 = _g
                return self.typeEq(t11,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            else:
                t11 = _g
                return self.typeEq(t11,t2)
        elif (tmp == 9):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 9):
                cl2 = t2.params[0]
                pl2 = t2.params[1]
                pl1 = _g1
                cl1 = _g
                if (cl1 == cl2):
                    _g = 0
                    _g1 = len(pl1)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if (not self.typeEq((pl1[i] if i >= 0 and i < len(pl1) else None),(pl2[i] if i >= 0 and i < len(pl2) else None))):
                            return False
                    return True
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            else:
                pass
        elif (tmp == 10):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 10):
                e2 = t2.params[0]
                pl2 = t2.params[1]
                pl1 = _g1
                e1 = _g
                if (e1 == e2):
                    _g = 0
                    _g1 = len(pl1)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if (not self.typeEq((pl1[i] if i >= 0 and i < len(pl1) else None),(pl2[i] if i >= 0 and i < len(pl2) else None))):
                            return False
                    return True
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            else:
                pass
        elif (tmp == 11):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                _g2 = t2.params[0]
                pl1 = _g1
                t11 = _g
                return self.typeEq(self.apply(t11.t,t11.params,pl1),t2)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                pl1 = _g1
                t11 = _g
                if (t11 == t21):
                    _g2 = 0
                    _g3 = len(pl1)
                    while (_g2 < _g3):
                        i = _g2
                        _g2 = (_g2 + 1)
                        if (not self.typeEq((pl1[i] if i >= 0 and i < len(pl1) else None),(pl2[i] if i >= 0 and i < len(pl2) else None))):
                            return False
                    return True
                else:
                    pl1 = _g1
                    t11 = _g
                    return self.typeEq(self.apply(t11.t,t11.params,pl1),t2)
            else:
                pl1 = _g1
                t11 = _g
                return self.typeEq(self.apply(t11.t,t11.params,pl1),t2)
        elif (tmp == 12):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 12):
                a2 = t2.params[0]
                pl2 = t2.params[1]
                pl1 = _g1
                a1 = _g
                if (a1 == a2):
                    _g = 0
                    _g1 = len(pl1)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if (not self.typeEq((pl1[i] if i >= 0 and i < len(pl1) else None),(pl2[i] if i >= 0 and i < len(pl2) else None))):
                            return False
                    return True
            else:
                pass
        elif (tmp == 13):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 13):
                args2 = t2.params[0]
                r2 = t2.params[1]
                r1 = _g1
                args1 = _g
                if (len(args1) == len(args2)):
                    _g = 0
                    _g1 = len(args1)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        if (not self.typeEq((args1[i] if i >= 0 and i < len(args1) else None).t,(args2[i] if i >= 0 and i < len(args2) else None).t)):
                            return False
                    return self.typeEq(r1,r2)
            else:
                pass
        elif (tmp == 14):
            _g = t1.params[0]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 14):
                a2 = t2.params[0]
                a1 = _g
                if (len(a1) == len(a2)):
                    m = haxe_ds_StringMap()
                    _g = 0
                    while (_g < len(a2)):
                        f = (a2[_g] if _g >= 0 and _g < len(a2) else None)
                        _g = (_g + 1)
                        m.h[f.name] = f
                    _g = 0
                    while (_g < len(a1)):
                        f1 = (a1[_g] if _g >= 0 and _g < len(a1) else None)
                        _g = (_g + 1)
                        f2 = m.h.get(f1.name,None)
                        if (f2 is None):
                            return False
                        if (not self.typeEq(f1.t,f2.t)):
                            return False
                    return True
            else:
                pass
        else:
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.typeEq(t1,r.r)
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.typeEq(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.typeEq(t1,self.apply(t21.t,t21.params,pl2))
            else:
                pass
        return False

    def tryUnify(self,t1,t2):
        if (t1 == t2):
            return True
        tmp = t1.index
        if (tmp == 0):
            r = t1.params[0]
            if (r.r is None):
                if (not self.link(t1,t2,r)):
                    return False
                r.r = t2
                return True
            return self.tryUnify(r.r,t2)
        elif (tmp == 2):
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 3):
                return True
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            else:
                pass
        elif (tmp == 5):
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            else:
                return True
        elif (tmp == 8):
            _g = t1.params[0]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                t11 = _g
                return self.tryUnify(t11,t2)
            elif (tmp == 8):
                _g1 = t2.params[0]
                t11 = _g
                return self.tryUnify(t11,t2)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            else:
                t11 = _g
                return self.tryUnify(t11,t2)
        elif (tmp == 9):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 9):
                cl2 = t2.params[0]
                pl2 = t2.params[1]
                pl1 = _g1
                cl1 = _g
                while (cl1 != cl2):
                    if (Reflect.field(cl1,"interfaces") is not None):
                        _g2 = 0
                        _g3 = Reflect.field(cl1,"interfaces")
                        while (_g2 < len(_g3)):
                            i = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                            _g2 = (_g2 + 1)
                            if (i.index == 9):
                                cli = i.params[0]
                                args = i.params[1]
                                _g4 = []
                                _g5 = 0
                                while (_g5 < len(args)):
                                    a = (args[_g5] if _g5 >= 0 and _g5 < len(args) else None)
                                    _g5 = (_g5 + 1)
                                    x = self.apply(a,cl1.params,pl1)
                                    _g4.append(x)
                                i1 = hscript_TType.TInst(cli,_g4)
                                if self.tryUnify(i1,t2):
                                    return True
                            else:
                                raise haxe_Exception.thrown("assert")
                    _g6 = Reflect.field(cl1,"superClass")
                    if (_g6 is None):
                        return False
                    elif (_g6.index == 9):
                        c = _g6.params[0]
                        args1 = _g6.params[1]
                        _g7 = []
                        _g8 = 0
                        while (_g8 < len(args1)):
                            a1 = (args1[_g8] if _g8 >= 0 and _g8 < len(args1) else None)
                            _g8 = (_g8 + 1)
                            x1 = self.apply(a1,cl1.params,pl1)
                            _g7.append(x1)
                        pl1 = _g7
                        cl1 = c
                    else:
                        raise haxe_Exception.thrown("assert")
                _g2 = 0
                _g3 = len(pl1)
                while (_g2 < _g3):
                    i = _g2
                    _g2 = (_g2 + 1)
                    if (not self.typeEq((pl1[i] if i >= 0 and i < len(pl1) else None),(pl2[i] if i >= 0 and i < len(pl2) else None))):
                        return False
                return True
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 14):
                fl = t2.params[0]
                pl1 = _g1
                cl1 = _g
                _g = 0
                _g1 = len(fl)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    f2 = (fl[i] if i >= 0 and i < len(fl) else None)
                    f1 = None
                    cl = cl1
                    while True:
                        f1 = cl.fields.h.get(f2.name,None)
                        if (f1 is not None):
                            break
                        if (Reflect.field(cl,"superClass") is None):
                            return False
                        _g2 = Reflect.field(cl,"superClass")
                        if (_g2 is None):
                            raise haxe_Exception.thrown("assert")
                        elif (_g2.index == 9):
                            _g3 = _g2.params[1]
                            c = _g2.params[0]
                            cl = c
                        else:
                            raise haxe_Exception.thrown("assert")
                    if (not self.typeEq(f1.t,f2.t)):
                        return False
                return True
            else:
                pass
        elif (tmp == 11):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                pl1 = _g1
                t11 = _g
                return self.tryUnify(self.apply(t11.t,t11.params,pl1),t2)
            elif (tmp == 8):
                _g2 = t2.params[0]
                pl1 = _g1
                t11 = _g
                return self.tryUnify(self.apply(t11.t,t11.params,pl1),t2)
            elif (tmp == 11):
                _g2 = t2.params[0]
                _g2 = t2.params[1]
                pl1 = _g1
                t11 = _g
                return self.tryUnify(self.apply(t11.t,t11.params,pl1),t2)
            else:
                pl1 = _g1
                t11 = _g
                return self.tryUnify(self.apply(t11.t,t11.params,pl1),t2)
        elif (tmp == 13):
            _g = t1.params[0]
            _g1 = t1.params[1]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 12):
                _g2 = t2.params[0]
                _g3 = t2.params[1]
                _g3 = _g2.params
                _g3 = _g2.t
                if (_g2.name == "haxe.Function"):
                    return True
            elif (tmp == 13):
                args2 = t2.params[0]
                r2 = t2.params[1]
                r1 = _g1
                args1 = _g
                if (len(args1) == len(args2)):
                    _g = 0
                    _g1 = len(args1)
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        a1 = (args1[i] if i >= 0 and i < len(args1) else None)
                        a2 = (args2[i] if i >= 0 and i < len(args2) else None)
                        if (a2.opt and (not a1.opt)):
                            return False
                        if (not self.tryUnify(a2.t,a1.t)):
                            return False
                    return self.tryUnify(r1,r2)
            else:
                pass
        elif (tmp == 14):
            _g = t1.params[0]
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            elif (tmp == 14):
                a2 = t2.params[0]
                a1 = _g
                if (len(a2) == 0):
                    return True
                m = haxe_ds_StringMap()
                _g = 0
                while (_g < len(a1)):
                    f = (a1[_g] if _g >= 0 and _g < len(a1) else None)
                    _g = (_g + 1)
                    m.h[f.name] = f
                _g = 0
                while (_g < len(a2)):
                    f2 = (a2[_g] if _g >= 0 and _g < len(a2) else None)
                    _g = (_g + 1)
                    f1 = m.h.get(f2.name,None)
                    if (f1 is None):
                        if f2.opt:
                            continue
                        return False
                    if (not self.typeEq(f1.t,f2.t)):
                        return False
                return True
            else:
                pass
        else:
            tmp = t2.index
            if (tmp == 0):
                r = t2.params[0]
                if (r.r is None):
                    if (not self.link(t2,t1,r)):
                        return False
                    r.r = t1
                    return True
                return self.tryUnify(t1,r.r)
            elif (tmp == 5):
                return True
            elif (tmp == 8):
                t21 = t2.params[0]
                return self.tryUnify(t1,t21)
            elif (tmp == 11):
                t21 = t2.params[0]
                pl2 = t2.params[1]
                return self.tryUnify(t1,self.apply(t21.t,t21.params,pl2))
            else:
                pass
        return self.typeEq(t1,t2)

    def unify(self,t1,t2,e):
        if (not self.tryUnify(t1,t2)):
            e = hscript_Error.ECustom(((HxOverrides.stringOrNull(hscript_Checker.typeStr(t1)) + " should be ") + HxOverrides.stringOrNull(hscript_Checker.typeStr(t2))))
            if (not self.isCompletion):
                raise haxe_Exception.thrown(e)

    def apply(self,t,params,args):
        _gthis = self
        if (len(args) != len(params)):
            raise haxe_Exception.thrown("Invalid number of type parameters")
        if (len(args) == 0):
            return t
        subst = haxe_ds_EnumValueMap()
        _g = 0
        _g1 = len(params)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            subst.set((params[i] if i >= 0 and i < len(params) else None),(args[i] if i >= 0 and i < len(args) else None))
        _hx_map = None
        def _hx_local_0(t):
            st = subst.get(t)
            if (st is not None):
                return st
            return _gthis.mapType(t,_hx_map)
        _hx_map = _hx_local_0
        return _hx_map(t)

    def mapType(self,t,f):
        tmp = t.index
        if (tmp == 0):
            r = t.params[0]
            if (r.r is None):
                return t
            return f(t)
        elif (((((tmp == 5) or ((tmp == 4))) or ((tmp == 3))) or ((tmp == 2))) or ((tmp == 1))):
            return t
        elif (tmp == 6):
            _g = t.params[0]
            return t
        elif (tmp == 7):
            _g = t.params[0]
            return t
        elif (tmp == 8):
            t1 = t.params[0]
            return hscript_TType.TNull(f(t1))
        elif (tmp == 9):
            _g = t.params[1]
            if (len(_g) == 0):
                return t
            else:
                args = _g
                c = t.params[0]
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(t1)
                    _g.append(x)
                return hscript_TType.TInst(c,_g)
        elif (tmp == 10):
            _g = t.params[1]
            if (len(_g) == 0):
                return t
            else:
                args = _g
                e = t.params[0]
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(t1)
                    _g.append(x)
                return hscript_TType.TEnum(e,_g)
        elif (tmp == 11):
            _g = t.params[1]
            if (len(_g) == 0):
                return t
            else:
                args = _g
                t1 = t.params[0]
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t2 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(t2)
                    _g.append(x)
                return hscript_TType.TType(t1,_g)
        elif (tmp == 12):
            _g = t.params[1]
            if (len(_g) == 0):
                return t
            else:
                args = _g
                a = t.params[0]
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(t1)
                    _g.append(x)
                return hscript_TType.TAbstract(a,_g)
        elif (tmp == 13):
            args = t.params[0]
            ret = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': a.name, 'opt': a.opt, 't': f(a.t)})
                _g.append(x)
            return hscript_TType.TFun(_g,f(ret))
        elif (tmp == 14):
            fields = t.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                af = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': af.name, 'opt': af.opt, 't': f(af.t)})
                _g.append(x)
            return hscript_TType.TAnon(_g)
        elif (tmp == 15):
            l = t.params[0]
            return f(l())
        else:
            pass

    def follow(self,t):
        tmp = t.index
        if (tmp == 0):
            r = t.params[0]
            if (r.r is not None):
                return self.follow(r.r)
            else:
                return t
        elif (tmp == 8):
            t1 = t.params[0]
            return self.follow(t1)
        elif (tmp == 11):
            t1 = t.params[0]
            args = t.params[1]
            return self.follow(self.apply(t1.t,t1.params,args))
        elif (tmp == 15):
            f = t.params[0]
            return self.follow(f())
        else:
            return t

    def getFields(self,t):
        _gthis = self
        fields = []
        _g = self.follow(t)
        tmp = _g.index
        if (tmp == 9):
            c = _g.params[0]
            args = _g.params[1]
            def _hx_local_0(t):
                return _gthis.apply(t,c.params,args)
            _hx_map = _hx_local_0
            while (c is not None):
                fname = c.fields.keys()
                while fname.hasNext():
                    fname1 = fname.next()
                    f = c.fields.h.get(fname1,None)
                    if ((not f.isPublic) or (not f.complete)):
                        continue
                    name = f.name
                    t = _hx_map(f.t)
                    if (self.allowAsync and name.startswith("a_")):
                        t = self.unasync(t)
                        name = HxString.substr(name,2,None)
                    fields.append(_hx_AnonObject({'name': name, 't': t}))
                if (Reflect.field(c,"isInterface") and ((Reflect.field(c,"interfaces") is not None))):
                    _g1 = 0
                    _g2 = Reflect.field(c,"interfaces")
                    while (_g1 < len(_g2)):
                        i = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                        _g1 = (_g1 + 1)
                        _g3 = 0
                        _g4 = self.getFields(i)
                        while (_g3 < len(_g4)):
                            f1 = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                            _g3 = (_g3 + 1)
                            x = _hx_AnonObject({'name': f1.name, 't': _hx_map(f1.t)})
                            fields.append(x)
                if (Reflect.field(c,"superClass") is None):
                    break
                _g5 = Reflect.field(c,"superClass")
                if (_g5 is None):
                    break
                elif (_g5.index == 9):
                    csup = [_g5.params[0]]
                    args1 = [_g5.params[1]]
                    curMap = [_hx_map]
                    def _hx_local_4(curMap,args,csup):
                        def _hx_local_3(t):
                            return (curMap[0] if 0 < len(curMap) else None)(_gthis.apply(t,(csup[0] if 0 < len(csup) else None).params,(args[0] if 0 < len(args) else None)))
                        return _hx_local_3
                    _hx_map = _hx_local_4(curMap,args1,csup)
                    c = (csup[0] if 0 < len(csup) else None)
                else:
                    break
        elif (tmp == 14):
            fl = _g.params[0]
            _g = 0
            while (_g < len(fl)):
                f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                x = _hx_AnonObject({'name': f.name, 't': f.t})
                fields.append(x)
        else:
            pass
        return fields

    def getField(self,t,f,e,forWrite = None):
        if (forWrite is None):
            forWrite = False
        _g = self.follow(t)
        tmp = _g.index
        if (tmp == 5):
            return self.makeMono()
        elif (tmp == 9):
            c = _g.params[0]
            args = _g.params[1]
            cf = c.fields.h.get(f,None)
            if ((cf is None) and self.allowAsync):
                cf = c.fields.h.get(("a_" + ("null" if f is None else f)),None)
                if (cf is not None):
                    isPublic = True
                    cf = _hx_AnonObject({'isPublic': isPublic, 'canWrite': False, 'params': cf.params, 'name': cf.name, 't': self.unasync(cf.t), 'complete': cf.complete})
                    if (cf.t is None):
                        cf = None
            if (((cf is None) and Reflect.field(c,"isInterface")) and ((Reflect.field(c,"interfaces") is not None))):
                _g1 = 0
                _g2 = Reflect.field(c,"interfaces")
                while (_g1 < len(_g2)):
                    i = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    ft = self.getField(i,f,e,forWrite)
                    if (ft is not None):
                        return self.apply(ft,c.params,args)
            if (cf is None):
                if (Reflect.field(c,"superClass") is None):
                    return None
                ft = self.getField(Reflect.field(c,"superClass"),f,e,forWrite)
                if (ft is not None):
                    ft = self.apply(ft,c.params,args)
                return ft
            if (not cf.isPublic):
                e = hscript_Error.ECustom(((("Can't access private field " + ("null" if f is None else f)) + " on ") + HxOverrides.stringOrNull(c.name)))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
            if (forWrite and (not cf.canWrite)):
                e = hscript_Error.ECustom(((("Can't write readonly field " + ("null" if f is None else f)) + " on ") + HxOverrides.stringOrNull(c.name)))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
            t = cf.t
            if (cf.params is not None):
                cf1 = cf.params
                _g1 = []
                _g2 = 0
                _g3 = len(cf.params)
                while (_g2 < _g3):
                    i = _g2
                    _g2 = (_g2 + 1)
                    x = self.makeMono()
                    _g1.append(x)
                t = self.apply(t,cf1,_g1)
            return self.apply(t,c.params,args)
        elif (tmp == 14):
            fields = _g.params[0]
            _g = 0
            while (_g < len(fields)):
                af = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                if (af.name == f):
                    return af.t
            return None
        else:
            return None

    def unasync(self,t):
        _g = self.follow(t)
        if (_g.index == 13):
            args = _g.params[0]
            ret = _g.params[1]
            if (len(args) > 0):
                rargs = list(args)
                _g = self.follow(((None if ((len(rargs) == 0)) else rargs.pop(0))).t)
                if (_g.index == 13):
                    _g1 = _g.params[0]
                    _g2 = _g.params[1]
                    if (len(_g1) == 1):
                        r = (_g1[0] if 0 < len(_g1) else None)
                        return hscript_TType.TFun(rargs,r.t)
        return None

    def typeExprWith(self,expr,t):
        et = self.typeExpr(expr,hscript__Checker_WithType.WithType(t))
        self.unify(et,t,expr)
        return t

    def makeMono(self):
        return hscript_TType.TMono(_hx_AnonObject({'r': None}))

    def makeIterator(self,t):
        return hscript_TType.TAnon([_hx_AnonObject({'name': "next", 'opt': False, 't': hscript_TType.TFun([],t)}), _hx_AnonObject({'name': "hasNext", 'opt': False, 't': hscript_TType.TFun([],hscript_TType.TBool)})])

    def mk(self,e,p):
        return e

    def isString(self,t):
        t = self.follow(t)
        if (t.index == 9):
            _g = t.params[0]
            _g1 = t.params[1]
            _g1 = Reflect.field(_g,"constructor")
            _g1 = _g.fields
            _g1 = Reflect.field(_g,"interfaces")
            _g1 = Reflect.field(_g,"isInterface")
            _g1 = _g.params
            _g1 = _g.statics
            _g1 = Reflect.field(_g,"superClass")
            if (_g.name == "String"):
                return True
            else:
                return False
        else:
            return False

    def onCompletion(self,expr,t):
        if self.isCompletion:
            raise haxe_Exception.thrown(hscript_Completion(expr,t))

    def typeField(self,o,f,expr,forWrite):
        ot = self.typeExpr(o,hscript__Checker_WithType.Value)
        if (f is None):
            self.onCompletion(expr,ot)
        ft = self.getField(ot,f,expr,forWrite)
        if (ft is None):
            e = hscript_Error.ECustom(((HxOverrides.stringOrNull(hscript_Checker.typeStr(ot)) + " has no field ") + ("null" if f is None else f)))
            if (not self.isCompletion):
                raise haxe_Exception.thrown(e)
            ft = hscript_TType.TDynamic
        return ft

    def typeExpr(self,expr,withType):
        _gthis = self
        if ((expr is None) and self.isCompletion):
            if (withType.index == 2):
                t = withType.params[0]
                return t
            else:
                return hscript_TType.TDynamic
        tmp = expr.index
        if (tmp == 0):
            c = expr.params[0]
            tmp = c.index
            if (tmp == 0):
                _g = c.params[0]
                return hscript_TType.TInt
            elif (tmp == 1):
                _g = c.params[0]
                return hscript_TType.TFloat
            elif (tmp == 2):
                _g = c.params[0]
                return self.types.t_string
            else:
                pass
        elif (tmp == 1):
            v = expr.params[0]
            l = self.locals.h.get(v,None)
            if (l is not None):
                return l
            g = self.globals.h.get(v,None)
            if (g is not None):
                if (g is None):
                    return g
                elif (g.index == 15):
                    f = g.params[0]
                    return f()
                else:
                    return g
            if self.allowAsync:
                g = self.globals.h.get(("a_" + ("null" if v is None else v)),None)
                if (g is not None):
                    g = self.unasync(g)
                if (g is not None):
                    return g
            v1 = v
            _hx_local_0 = len(v1)
            if (_hx_local_0 == 4):
                if (v1 == "null"):
                    return self.makeMono()
                elif (v1 == "true"):
                    return hscript_TType.TBool
                else:
                    if self.isCompletion:
                        return hscript_TType.TDynamic
                    e = hscript_Error.ECustom(("Unknown identifier " + ("null" if v is None else v)))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            elif (_hx_local_0 == 5):
                if (v1 == "trace"):
                    return hscript_TType.TDynamic
                elif (v1 == "false"):
                    return hscript_TType.TBool
                else:
                    if self.isCompletion:
                        return hscript_TType.TDynamic
                    e = hscript_Error.ECustom(("Unknown identifier " + ("null" if v is None else v)))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            else:
                if self.isCompletion:
                    return hscript_TType.TDynamic
                e = hscript_Error.ECustom(("Unknown identifier " + ("null" if v is None else v)))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
        elif (tmp == 2):
            n = expr.params[0]
            t = expr.params[1]
            init = expr.params[2]
            vt = (self.makeMono() if ((t is None)) else self.makeType(t,expr))
            if (init is not None):
                et = self.typeExpr(init,(hscript__Checker_WithType.Value if ((t is None)) else hscript__Checker_WithType.WithType(vt)))
                if (t is None):
                    vt = et
                else:
                    self.unify(et,vt,init)
            self.locals.h[n] = vt
            return hscript_TType.TVoid
        elif (tmp == 3):
            e = expr.params[0]
            return self.typeExpr(e,withType)
        elif (tmp == 4):
            el = expr.params[0]
            t = hscript_TType.TVoid
            locals = self.saveLocals()
            _g = 0
            while (_g < len(el)):
                e = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                t = self.typeExpr(e,(withType if ((e == python_internal_ArrayImpl._get(el, (len(el) - 1)))) else hscript__Checker_WithType.NoValue))
            self.locals = locals
            return t
        elif (tmp == 5):
            o = expr.params[0]
            f = expr.params[1]
            return self.typeField(o,f,expr,False)
        elif (tmp == 6):
            op = expr.params[0]
            e1 = expr.params[1]
            e2 = expr.params[2]
            op1 = op
            _hx_local_2 = len(op1)
            if (_hx_local_2 == 1):
                if (op1 == "%"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.WithType(hscript_TType.TInt))
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    _g1 = self.follow(t2)
                    tmp = _g.index
                    if (tmp == 2):
                        tmp = _g1.index
                        if (tmp == 2):
                            if (op == "/"):
                                return hscript_TType.TFloat
                            return hscript_TType.TInt
                        elif ((tmp == 5) or ((tmp == 3))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif ((tmp == 5) or ((tmp == 3))):
                        tmp = _g1.index
                        if (((tmp == 5) or ((tmp == 3))) or ((tmp == 2))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    else:
                        self.unify(t1,hscript_TType.TFloat,e1)
                        self.unify(t2,hscript_TType.TFloat,e2)
                elif (op1 == "*"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.WithType(hscript_TType.TInt))
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    _g1 = self.follow(t2)
                    tmp = _g.index
                    if (tmp == 2):
                        tmp = _g1.index
                        if (tmp == 2):
                            if (op == "/"):
                                return hscript_TType.TFloat
                            return hscript_TType.TInt
                        elif ((tmp == 5) or ((tmp == 3))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif ((tmp == 5) or ((tmp == 3))):
                        tmp = _g1.index
                        if (((tmp == 5) or ((tmp == 3))) or ((tmp == 2))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    else:
                        self.unify(t1,hscript_TType.TFloat,e1)
                        self.unify(t2,hscript_TType.TFloat,e2)
                elif (op1 == "-"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.WithType(hscript_TType.TInt))
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    _g1 = self.follow(t2)
                    tmp = _g.index
                    if (tmp == 2):
                        tmp = _g1.index
                        if (tmp == 2):
                            if (op == "/"):
                                return hscript_TType.TFloat
                            return hscript_TType.TInt
                        elif ((tmp == 5) or ((tmp == 3))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif ((tmp == 5) or ((tmp == 3))):
                        tmp = _g1.index
                        if (((tmp == 5) or ((tmp == 3))) or ((tmp == 2))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    else:
                        self.unify(t1,hscript_TType.TFloat,e1)
                        self.unify(t2,hscript_TType.TFloat,e2)
                elif (op1 == "/"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.WithType(hscript_TType.TInt))
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    _g1 = self.follow(t2)
                    tmp = _g.index
                    if (tmp == 2):
                        tmp = _g1.index
                        if (tmp == 2):
                            if (op == "/"):
                                return hscript_TType.TFloat
                            return hscript_TType.TInt
                        elif ((tmp == 5) or ((tmp == 3))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif ((tmp == 5) or ((tmp == 3))):
                        tmp = _g1.index
                        if (((tmp == 5) or ((tmp == 3))) or ((tmp == 2))):
                            return hscript_TType.TFloat
                        else:
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    else:
                        self.unify(t1,hscript_TType.TFloat,e1)
                        self.unify(t2,hscript_TType.TFloat,e2)
                elif (op1 == "+"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.WithType(hscript_TType.TInt))
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    self.tryUnify(t1,t2)
                    _g = self.follow(t1)
                    _g1 = self.follow(t2)
                    tmp = _g.index
                    if (tmp == 2):
                        tmp = _g1.index
                        if (tmp == 2):
                            return hscript_TType.TInt
                        elif (tmp == 3):
                            return hscript_TType.TFloat
                        elif (tmp == 5):
                            return hscript_TType.TDynamic
                        else:
                            t1 = _g
                            t2 = _g1
                            if (self.isString(t1) or self.isString(t2)):
                                return self.types.t_string
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif (tmp == 3):
                        tmp = _g1.index
                        if ((tmp == 3) or ((tmp == 2))):
                            return hscript_TType.TFloat
                        elif (tmp == 5):
                            return hscript_TType.TDynamic
                        else:
                            t1 = _g
                            t2 = _g1
                            if (self.isString(t1) or self.isString(t2)):
                                return self.types.t_string
                            self.unify(t1,hscript_TType.TFloat,e1)
                            self.unify(t2,hscript_TType.TFloat,e2)
                    elif (tmp == 5):
                        return hscript_TType.TDynamic
                    elif (_g1.index == 5):
                        return hscript_TType.TDynamic
                    else:
                        t1 = _g
                        t2 = _g1
                        if (self.isString(t1) or self.isString(t2)):
                            return self.types.t_string
                        self.unify(t1,hscript_TType.TFloat,e1)
                        self.unify(t2,hscript_TType.TFloat,e2)
                elif (op1 == "&"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                elif (op1 == "^"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                elif (op1 == "|"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                elif (op1 == "="):
                    if self.allowDefine:
                        if (e1.index == 1):
                            i = e1.params[0]
                            if ((not (i in self.locals.h)) and (not (i in self.globals.h))):
                                vt = self.typeExpr(e2,hscript__Checker_WithType.Value)
                                self.locals.h[i] = vt
                                return vt
                    vt = None
                    if (e1.index == 5):
                        o = e1.params[0]
                        f = e1.params[1]
                        vt = self.typeField(o,f,e1,True)
                    else:
                        vt = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    self.typeExprWith(e2,vt)
                    return vt
                elif (op1 == "<"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    tmp = _g.index
                    if (((tmp == 4) or ((tmp == 3))) or ((tmp == 2))):
                        pass
                    elif (tmp == 9):
                        _g1 = _g.params[0]
                        _g2 = _g.params[1]
                        _g = Reflect.field(_g1,"constructor")
                        _g = _g1.fields
                        _g = Reflect.field(_g1,"interfaces")
                        _g = Reflect.field(_g1,"isInterface")
                        _g = _g1.params
                        _g = _g1.statics
                        _g = Reflect.field(_g1,"superClass")
                        if (_g1.name != "String"):
                            e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                            if (not self.isCompletion):
                                raise haxe_Exception.thrown(e)
                    else:
                        e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                    return hscript_TType.TBool
                elif (op1 == ">"):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    tmp = _g.index
                    if (((tmp == 4) or ((tmp == 3))) or ((tmp == 2))):
                        pass
                    elif (tmp == 9):
                        _g1 = _g.params[0]
                        _g2 = _g.params[1]
                        _g = Reflect.field(_g1,"constructor")
                        _g = _g1.fields
                        _g = Reflect.field(_g1,"interfaces")
                        _g = Reflect.field(_g1,"isInterface")
                        _g = _g1.params
                        _g = _g1.statics
                        _g = Reflect.field(_g1,"superClass")
                        if (_g1.name != "String"):
                            e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                            if (not self.isCompletion):
                                raise haxe_Exception.thrown(e)
                    else:
                        e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                    return hscript_TType.TBool
                else:
                    if (HxString.charCodeAt(op,(len(op) - 1)) == 61):
                        t = self.typeExpr(self.mk(hscript_Expr.EBinop(HxString.substr(op,0,(len(op) - 1)),e1,e2),expr),withType)
                        return self.typeExpr(self.mk(hscript_Expr.EBinop("=",e1,e2),expr),withType)
                    e = hscript_Error.ECustom(("Unsupported operation " + ("null" if op is None else op)))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            elif (_hx_local_2 == 3):
                if (op1 == "..."):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return self.makeIterator(hscript_TType.TInt)
                elif (op1 == ">>>"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                else:
                    if (HxString.charCodeAt(op,(len(op) - 1)) == 61):
                        t = self.typeExpr(self.mk(hscript_Expr.EBinop(HxString.substr(op,0,(len(op) - 1)),e1,e2),expr),withType)
                        return self.typeExpr(self.mk(hscript_Expr.EBinop("=",e1,e2),expr),withType)
                    e = hscript_Error.ECustom(("Unsupported operation " + ("null" if op is None else op)))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            elif (_hx_local_2 == 2):
                if (op1 == "<<"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                elif (op1 == ">>"):
                    self.typeExprWith(e1,hscript_TType.TInt)
                    self.typeExprWith(e2,hscript_TType.TInt)
                    return hscript_TType.TInt
                elif (op1 == "!="):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    return hscript_TType.TBool
                elif (op1 == "=="):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    return hscript_TType.TBool
                elif (op1 == "<="):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    tmp = _g.index
                    if (((tmp == 4) or ((tmp == 3))) or ((tmp == 2))):
                        pass
                    elif (tmp == 9):
                        _g1 = _g.params[0]
                        _g2 = _g.params[1]
                        _g = Reflect.field(_g1,"constructor")
                        _g = _g1.fields
                        _g = Reflect.field(_g1,"interfaces")
                        _g = Reflect.field(_g1,"isInterface")
                        _g = _g1.params
                        _g = _g1.statics
                        _g = Reflect.field(_g1,"superClass")
                        if (_g1.name != "String"):
                            e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                            if (not self.isCompletion):
                                raise haxe_Exception.thrown(e)
                    else:
                        e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                    return hscript_TType.TBool
                elif (op1 == ">="):
                    t1 = self.typeExpr(e1,hscript__Checker_WithType.Value)
                    t2 = self.typeExpr(e2,hscript__Checker_WithType.WithType(t1))
                    if (not self.tryUnify(t1,t2)):
                        self.unify(t2,t1,e2)
                    _g = self.follow(t1)
                    tmp = _g.index
                    if (((tmp == 4) or ((tmp == 3))) or ((tmp == 2))):
                        pass
                    elif (tmp == 9):
                        _g1 = _g.params[0]
                        _g2 = _g.params[1]
                        _g = Reflect.field(_g1,"constructor")
                        _g = _g1.fields
                        _g = Reflect.field(_g1,"interfaces")
                        _g = Reflect.field(_g1,"isInterface")
                        _g = _g1.params
                        _g = _g1.statics
                        _g = Reflect.field(_g1,"superClass")
                        if (_g1.name != "String"):
                            e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                            if (not self.isCompletion):
                                raise haxe_Exception.thrown(e)
                    else:
                        e = hscript_Error.ECustom(("Cannot compare " + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                    return hscript_TType.TBool
                elif (op1 == "&&"):
                    self.typeExprWith(e1,hscript_TType.TBool)
                    self.typeExprWith(e2,hscript_TType.TBool)
                    return hscript_TType.TBool
                elif (op1 == "||"):
                    self.typeExprWith(e1,hscript_TType.TBool)
                    self.typeExprWith(e2,hscript_TType.TBool)
                    return hscript_TType.TBool
                else:
                    if (HxString.charCodeAt(op,(len(op) - 1)) == 61):
                        t = self.typeExpr(self.mk(hscript_Expr.EBinop(HxString.substr(op,0,(len(op) - 1)),e1,e2),expr),withType)
                        return self.typeExpr(self.mk(hscript_Expr.EBinop("=",e1,e2),expr),withType)
                    e = hscript_Error.ECustom(("Unsupported operation " + ("null" if op is None else op)))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            else:
                if (HxString.charCodeAt(op,(len(op) - 1)) == 61):
                    t = self.typeExpr(self.mk(hscript_Expr.EBinop(HxString.substr(op,0,(len(op) - 1)),e1,e2),expr),withType)
                    return self.typeExpr(self.mk(hscript_Expr.EBinop("=",e1,e2),expr),withType)
                e = hscript_Error.ECustom(("Unsupported operation " + ("null" if op is None else op)))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
        elif (tmp == 7):
            _g = expr.params[1]
            op = expr.params[0]
            e = expr.params[2]
            et = self.typeExpr(e,hscript__Checker_WithType.Value)
            op1 = op
            _hx_local_3 = len(op1)
            if (_hx_local_3 == 1):
                if (op1 == "!"):
                    self.unify(et,hscript_TType.TBool,e)
                    return et
                elif (op1 == "-"):
                    self.unify(et,hscript_TType.TInt,e)
                    return et
                else:
                    pass
            elif (_hx_local_3 == 2):
                if (op1 == "++"):
                    self.unify(et,hscript_TType.TInt,e)
                    return et
                elif (op1 == "--"):
                    self.unify(et,hscript_TType.TInt,e)
                    return et
                else:
                    pass
            else:
                pass
        elif (tmp == 8):
            e = expr.params[0]
            params = expr.params[1]
            ft = self.typeExpr(e,hscript__Checker_WithType.Value)
            _g = self.follow(ft)
            tmp = _g.index
            if (tmp == 5):
                _g1 = 0
                while (_g1 < len(params)):
                    p = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                    _g1 = (_g1 + 1)
                    self.typeExpr(p,hscript__Checker_WithType.Value)
                return self.makeMono()
            elif (tmp == 13):
                args = _g.params[0]
                ret = _g.params[1]
                _g = 0
                _g1 = len(params)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    a = (args[i] if i >= 0 and i < len(args) else None)
                    if (a is None):
                        e = hscript_Error.ECustom("Too many arguments")
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                        break
                    t = self.typeExpr((params[i] if i >= 0 and i < len(params) else None),(hscript__Checker_WithType.Value if ((a is None)) else hscript__Checker_WithType.WithType(a.t)))
                    self.unify(t,a.t,(params[i] if i >= 0 and i < len(params) else None))
                _g = len(params)
                _g1 = len(args)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    if (not (args[i] if i >= 0 and i < len(args) else None).opt):
                        e = hscript_Error.ECustom(((("Missing argument " + HxOverrides.stringOrNull((args[i] if i >= 0 and i < len(args) else None).name)) + ":") + HxOverrides.stringOrNull(hscript_Checker.typeStr((args[i] if i >= 0 and i < len(args) else None).t))))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                return ret
            else:
                e = hscript_Error.ECustom((HxOverrides.stringOrNull(hscript_Checker.typeStr(ft)) + " cannot be called"))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
                return self.makeMono()
        elif (tmp == 9):
            cond = expr.params[0]
            e1 = expr.params[1]
            e2 = expr.params[2]
            self.typeExprWith(cond,hscript_TType.TBool)
            t1 = self.typeExpr(e1,withType)
            if (e2 is None):
                return t1
            t2 = self.typeExpr(e2,withType)
            if (withType == hscript__Checker_WithType.NoValue):
                return hscript_TType.TVoid
            if self.tryUnify(t2,t1):
                return t1
            if self.tryUnify(t1,t2):
                return t2
            self.unify(t2,t1,e2)
        elif (tmp == 10):
            cond = expr.params[0]
            e = expr.params[1]
            self.typeExprWith(cond,hscript_TType.TBool)
            self.typeExpr(e,hscript__Checker_WithType.NoValue)
            return hscript_TType.TVoid
        elif (tmp == 11):
            v = expr.params[0]
            it = expr.params[1]
            e = expr.params[2]
            locals = self.saveLocals()
            itt = self.typeExpr(it,hscript__Checker_WithType.Value)
            vt = None
            _g = self.follow(itt)
            if (_g.index == 9):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                _g = Reflect.field(_g1,"constructor")
                _g = _g1.fields
                _g = Reflect.field(_g1,"interfaces")
                _g = Reflect.field(_g1,"isInterface")
                _g = _g1.params
                _g = _g1.statics
                _g = Reflect.field(_g1,"superClass")
                if (_g1.name == "Array"):
                    if (len(_g2) == 1):
                        t = (_g2[0] if 0 < len(_g2) else None)
                        vt = t
                    else:
                        ft = self.getField(itt,"iterator",it)
                        if (ft is None):
                            if (itt.index == 12):
                                a = itt.params[0]
                                args = itt.params[1]
                                ft = self.getField(self.apply(a.t,a.params,args),"iterator",it)
                        if (ft is not None):
                            if (ft.index == 13):
                                if (len(ft.params[0]) == 0):
                                    ret = ft.params[1]
                                    ft = ret
                                else:
                                    ft = None
                            else:
                                ft = None
                        t = self.makeMono()
                        _hx_iter = self.makeIterator(t)
                        self.unify((ft if ((ft is not None)) else itt),_hx_iter,it)
                        vt = t
                else:
                    ft = self.getField(itt,"iterator",it)
                    if (ft is None):
                        if (itt.index == 12):
                            a = itt.params[0]
                            args = itt.params[1]
                            ft = self.getField(self.apply(a.t,a.params,args),"iterator",it)
                    if (ft is not None):
                        if (ft.index == 13):
                            if (len(ft.params[0]) == 0):
                                ret = ft.params[1]
                                ft = ret
                            else:
                                ft = None
                        else:
                            ft = None
                    t = self.makeMono()
                    _hx_iter = self.makeIterator(t)
                    self.unify((ft if ((ft is not None)) else itt),_hx_iter,it)
                    vt = t
            else:
                ft = self.getField(itt,"iterator",it)
                if (ft is None):
                    if (itt.index == 12):
                        a = itt.params[0]
                        args = itt.params[1]
                        ft = self.getField(self.apply(a.t,a.params,args),"iterator",it)
                if (ft is not None):
                    if (ft.index == 13):
                        if (len(ft.params[0]) == 0):
                            ret = ft.params[1]
                            ft = ret
                        else:
                            ft = None
                    else:
                        ft = None
                t = self.makeMono()
                _hx_iter = self.makeIterator(t)
                self.unify((ft if ((ft is not None)) else itt),_hx_iter,it)
                vt = t
            self.locals.h[v] = vt
            self.typeExpr(e,hscript__Checker_WithType.NoValue)
            self.locals = locals
            return hscript_TType.TVoid
        elif ((tmp == 13) or ((tmp == 12))):
            return hscript_TType.TVoid
        elif (tmp == 14):
            args = expr.params[0]
            body = expr.params[1]
            name = expr.params[2]
            ret = expr.params[3]
            ft = None
            tret = None
            targs = None
            if (self.currentFunType is not None):
                _g = self.currentFunType
                if (_g.index == 13):
                    args1 = _g.params[0]
                    ret1 = _g.params[1]
                    ft = self.currentFunType
                    tret = ret1
                    targs = args1
                else:
                    raise haxe_Exception.thrown("assert")
                self.currentFunType = None
            else:
                tret = (self.makeMono() if ((ret is None)) else self.makeType(ret,expr))
            locals = self.saveLocals()
            oldRet = self.allowReturn
            oldGDef = self.allowDefine
            self.allowReturn = tret
            self.allowDefine = False
            withArgs = None
            tmp = None
            if (name is not None):
                tmp1 = None
                if (withType.index == 2):
                    _hx_tmp = self.follow(withType.params[0])
                    if (_hx_tmp.index == 13):
                        _g = _hx_tmp.params[0]
                        _g = _hx_tmp.params[1]
                        tmp1 = True
                    else:
                        tmp1 = False
                else:
                    tmp1 = False
                tmp = (not tmp1)
            else:
                tmp = False
            if tmp:
                ev = self.events.h.get(name,None)
                if (ev is not None):
                    withType = hscript__Checker_WithType.WithType(ev)
            if (withType.index == 2):
                _hx_tmp = self.follow(withType.params[0])
                if (_hx_tmp.index == 13):
                    args1 = _hx_tmp.params[0]
                    ret = _hx_tmp.params[1]
                    withArgs = args1
                    self.unify(tret,ret,expr)
            if (targs is None):
                targs = self.typeArgs(args,expr)
            _g = 0
            _g1 = len(targs)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                a = (targs[i] if i >= 0 and i < len(targs) else None)
                if (withArgs is not None):
                    if (i < len(withArgs)):
                        self.unify((withArgs[i] if i >= 0 and i < len(withArgs) else None).t,a.t,expr)
                    else:
                        e = hscript_Error.ECustom(("Extra argument " + HxOverrides.stringOrNull(a.name)))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                self.locals.h[a.name] = a.t
            if ((withArgs is not None) and ((len(targs) < len(withArgs)))):
                msg = (("Missing " + Std.string(((len(withArgs) - len(targs))))) + " arguments (")
                _g = []
                _g1 = len(targs)
                _g2 = len(withArgs)
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    x = hscript_Checker.typeStr((withArgs[i] if i >= 0 and i < len(withArgs) else None).t)
                    _g.append(x)
                e = hscript_Error.ECustom(((("null" if msg is None else msg) + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ")"))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
            self.typeExpr(body,hscript__Checker_WithType.NoValue)
            self.allowDefine = oldGDef
            self.allowReturn = oldRet
            self.locals = locals
            if (ft is None):
                ft = hscript_TType.TFun(targs,tret)
                locals.h[name] = ft
            return ft
        elif (tmp == 15):
            v = expr.params[0]
            et = (hscript_TType.TVoid if ((v is None)) else self.typeExpr(v,(hscript__Checker_WithType.Value if ((self.allowReturn is None)) else hscript__Checker_WithType.WithType(self.allowReturn))))
            if (self.allowReturn is None):
                e = hscript_Error.ECustom("Return not allowed here")
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
            else:
                self.unify(et,self.allowReturn,(expr if ((v is None)) else v))
            return self.makeMono()
        elif (tmp == 16):
            a = expr.params[0]
            index = expr.params[1]
            self.typeExprWith(index,hscript_TType.TInt)
            at = self.typeExpr(a,hscript__Checker_WithType.Value)
            _g = self.follow(at)
            if (_g.index == 9):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                _g = Reflect.field(_g1,"constructor")
                _g = _g1.fields
                _g = Reflect.field(_g1,"interfaces")
                _g = Reflect.field(_g1,"isInterface")
                _g = _g1.params
                _g = _g1.statics
                _g = Reflect.field(_g1,"superClass")
                if (_g1.name == "Array"):
                    if (len(_g2) == 1):
                        et = (_g2[0] if 0 < len(_g2) else None)
                        return et
                    else:
                        e = hscript_Error.ECustom((HxOverrides.stringOrNull(hscript_Checker.typeStr(at)) + " is not an Array"))
                        if (not self.isCompletion):
                            raise haxe_Exception.thrown(e)
                else:
                    e = hscript_Error.ECustom((HxOverrides.stringOrNull(hscript_Checker.typeStr(at)) + " is not an Array"))
                    if (not self.isCompletion):
                        raise haxe_Exception.thrown(e)
            else:
                e = hscript_Error.ECustom((HxOverrides.stringOrNull(hscript_Checker.typeStr(at)) + " is not an Array"))
                if (not self.isCompletion):
                    raise haxe_Exception.thrown(e)
        elif (tmp == 17):
            el = expr.params[0]
            et = None
            _g = 0
            while (_g < len(el)):
                v = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                t = self.typeExpr(v,(hscript__Checker_WithType.Value if ((et is None)) else hscript__Checker_WithType.WithType(et)))
                if (et is None):
                    et = t
                elif (not self.tryUnify(t,et)):
                    if self.tryUnify(et,t):
                        et = t
                    else:
                        self.unify(t,et,v)
            if (et is None):
                et = self.makeMono()
            return self.types.getType("Array",[et])
        elif (tmp == 18):
            cl = expr.params[0]
            params = expr.params[1]
        elif (tmp == 19):
            e = expr.params[0]
            self.typeExpr(e,hscript__Checker_WithType.Value)
            return self.makeMono()
        elif (tmp == 20):
            etry = expr.params[0]
            v = expr.params[1]
            et = expr.params[2]
            ecatch = expr.params[3]
            vt = self.typeExpr(etry,withType)
            old = self.locals.h.get(v,None)
            this1 = self.locals
            value = self.makeType(et,ecatch)
            this1.h[v] = value
            ct = self.typeExpr(ecatch,withType)
            if (old is not None):
                self.locals.h[v] = old
            else:
                self.locals.remove(v)
            if (withType == hscript__Checker_WithType.NoValue):
                return hscript_TType.TVoid
            if self.tryUnify(vt,ct):
                return ct
            self.unify(ct,vt,ecatch)
            return vt
        elif (tmp == 21):
            fl = expr.params[0]
            if (withType.index == 2):
                _hx_tmp = self.follow(withType.params[0])
                if (_hx_tmp.index == 14):
                    tfields = _hx_tmp.params[0]
                    if (len(tfields) > 0):
                        _g = haxe_ds_StringMap()
                        _g1 = 0
                        while (_g1 < len(tfields)):
                            f = (tfields[_g1] if _g1 >= 0 and _g1 < len(tfields) else None)
                            _g1 = (_g1 + 1)
                            _g.h[f.name] = f
                        _hx_map = _g
                        _g = []
                        _g1 = 0
                        while (_g1 < len(fl)):
                            f = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                            _g1 = (_g1 + 1)
                            ft = _hx_map.h.get(f.name,None)
                            ft1 = None
                            if (ft is None):
                                curExpr = f.e
                                e = hscript_Error.ECustom(("Extra field " + HxOverrides.stringOrNull(f.name)))
                                if (not self.isCompletion):
                                    raise haxe_Exception.thrown(e)
                                ft1 = hscript_TType.TDynamic
                            else:
                                ft1 = ft.t
                            x = _hx_AnonObject({'t': self.typeExprWith(f.e,ft1), 'opt': False, 'name': f.name})
                            _g.append(x)
                        return hscript_TType.TAnon(_g)
                    else:
                        _g = []
                        _g1 = 0
                        while (_g1 < len(fl)):
                            f = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                            _g1 = (_g1 + 1)
                            x = _hx_AnonObject({'t': self.typeExpr(f.e,hscript__Checker_WithType.Value), 'opt': False, 'name': f.name})
                            _g.append(x)
                        return hscript_TType.TAnon(_g)
                else:
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fl)):
                        f = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                        _g1 = (_g1 + 1)
                        x = _hx_AnonObject({'t': self.typeExpr(f.e,hscript__Checker_WithType.Value), 'opt': False, 'name': f.name})
                        _g.append(x)
                    return hscript_TType.TAnon(_g)
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(fl)):
                    f = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                    _g1 = (_g1 + 1)
                    x = _hx_AnonObject({'t': self.typeExpr(f.e,hscript__Checker_WithType.Value), 'opt': False, 'name': f.name})
                    _g.append(x)
                return hscript_TType.TAnon(_g)
        elif (tmp == 22):
            cond = expr.params[0]
            e1 = expr.params[1]
            e2 = expr.params[2]
            self.typeExprWith(cond,hscript_TType.TBool)
            t1 = self.typeExpr(e1,withType)
            if (e2 is None):
                return t1
            t2 = self.typeExpr(e2,withType)
            if (withType == hscript__Checker_WithType.NoValue):
                return hscript_TType.TVoid
            if self.tryUnify(t2,t1):
                return t1
            if self.tryUnify(t1,t2):
                return t2
            self.unify(t2,t1,e2)
        elif (tmp == 23):
            value = expr.params[0]
            cases = expr.params[1]
            defaultExpr = expr.params[2]
            tmin = None
            vt = self.typeExpr(value,hscript__Checker_WithType.Value)
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    ct = self.typeExpr(v,hscript__Checker_WithType.WithType(vt))
                    self.unify(ct,vt,v)
                et = self.typeExpr(c.expr,withType)
                p = c.expr
                if (withType != hscript__Checker_WithType.NoValue):
                    if (tmin is None):
                        tmin = et
                    elif (not _gthis.tryUnify(et,tmin)):
                        _gthis.unify(tmin,et,p)
                        tmin = et
            if (defaultExpr is not None):
                t = self.typeExpr(defaultExpr,withType)
                if (withType != hscript__Checker_WithType.NoValue):
                    if (tmin is None):
                        tmin = t
                    elif (not _gthis.tryUnify(t,tmin)):
                        _gthis.unify(tmin,t,defaultExpr)
                        tmin = t
            if (withType == hscript__Checker_WithType.NoValue):
                return hscript_TType.TVoid
            elif (tmin is None):
                return self.makeMono()
            else:
                return tmin
        elif (tmp == 24):
            cond = expr.params[0]
            e = expr.params[1]
            self.typeExprWith(cond,hscript_TType.TBool)
            self.typeExpr(e,hscript__Checker_WithType.NoValue)
            return hscript_TType.TVoid
        elif (tmp == 25):
            _g = expr.params[1]
            m = expr.params[0]
            e = expr.params[2]
            if ((m == ":untyped") and self.allowUntypedMeta):
                return self.makeMono()
            return self.typeExpr(e,withType)
        elif (tmp == 26):
            v = expr.params[0]
            t = expr.params[1]
            ct = self.makeType(t,expr)
            vt = self.typeExpr(v,hscript__Checker_WithType.WithType(ct))
            self.unify(vt,ct,v)
            return ct
        else:
            pass
        e = hscript_Error.ECustom(("Don't know how to type " + HxOverrides.stringOrNull(expr.tag)))
        if (not self.isCompletion):
            raise haxe_Exception.thrown(e)
        return hscript_TType.TDynamic

    @staticmethod
    def typeStr(t):
        tmp = t.index
        if (tmp == 0):
            r = t.params[0]
            if (r.r is None):
                return "Unknown"
            else:
                return hscript_Checker.typeStr(r.r)
        elif (tmp == 6):
            name = t.params[0]
            return name
        elif (tmp == 7):
            name = t.params[0]
            return ("?" + ("null" if name is None else name))
        elif (tmp == 8):
            t1 = t.params[0]
            return (("Null<" + HxOverrides.stringOrNull(hscript_Checker.typeStr(t1))) + ">")
        elif (tmp == 9):
            c = t.params[0]
            args = t.params[1]
            c1 = c.name
            tmp = None
            if (len(args) == 0):
                tmp = ""
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = hscript_Checker.typeStr(t1)
                    _g.append(x)
                tmp = (("<" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ">")
            return (("null" if c1 is None else c1) + ("null" if tmp is None else tmp))
        elif (tmp == 10):
            e = t.params[0]
            args = t.params[1]
            e1 = e.name
            tmp = None
            if (len(args) == 0):
                tmp = ""
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = hscript_Checker.typeStr(t1)
                    _g.append(x)
                tmp = (("<" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ">")
            return (("null" if e1 is None else e1) + ("null" if tmp is None else tmp))
        elif (tmp == 11):
            t1 = t.params[0]
            args = t.params[1]
            if (t1.name == "hscript.TypeCheck"):
                return hscript_Checker.typeStr((args[1] if 1 < len(args) else None))
            else:
                t2 = t1.name
                tmp = None
                if (len(args) == 0):
                    tmp = ""
                else:
                    _g = []
                    _g1 = 0
                    while (_g1 < len(args)):
                        t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                        _g1 = (_g1 + 1)
                        x = hscript_Checker.typeStr(t1)
                        _g.append(x)
                    tmp = (("<" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ">")
                return (("null" if t2 is None else t2) + ("null" if tmp is None else tmp))
        elif (tmp == 12):
            a = t.params[0]
            args = t.params[1]
            a1 = a.name
            tmp = None
            if (len(args) == 0):
                tmp = ""
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    t1 = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = hscript_Checker.typeStr(t1)
                    _g.append(x)
                tmp = (("<" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ">")
            return (("null" if a1 is None else a1) + ("null" if tmp is None else tmp))
        elif (tmp == 13):
            args = t.params[0]
            ret = t.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = ((HxOverrides.stringOrNull((("?" if (a.opt) else ""))) + HxOverrides.stringOrNull((("" if ((a.name == "")) else (HxOverrides.stringOrNull(a.name) + ":"))))) + HxOverrides.stringOrNull(hscript_Checker.typeStr(a.t)))
                _g.append(x)
            return ((("(" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _g]))) + ") -> ") + HxOverrides.stringOrNull(hscript_Checker.typeStr(ret)))
        elif (tmp == 14):
            fields = t.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                x = (((HxOverrides.stringOrNull((("?" if (f.opt) else ""))) + HxOverrides.stringOrNull(f.name)) + ":") + HxOverrides.stringOrNull(hscript_Checker.typeStr(f.t)))
                _g.append(x)
            return (("{" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _g]))) + "}")
        else:
            return HxString.substr(t.tag,1,None)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.types = None
        _hx_o.locals = None
        _hx_o.globals = None
        _hx_o.events = None
        _hx_o.currentFunType = None
        _hx_o.isCompletion = None
        _hx_o.allowDefine = None
        _hx_o.allowAsync = None
        _hx_o.allowReturn = None
        _hx_o.allowGlobalsDefine = None
        _hx_o.allowUntypedMeta = None
hscript_Checker._hx_class = hscript_Checker
_hx_classes["hscript.Checker"] = hscript_Checker

