class hscript_Interp:
    _hx_class_name = "hscript.Interp"
    __slots__ = ("variables", "locals", "binops", "depth", "inTry", "declared", "returnValue")
    _hx_fields = ["variables", "locals", "binops", "depth", "inTry", "declared", "returnValue"]
    _hx_methods = ["resetVariables", "posInfos", "initOps", "setVar", "assign", "assignOp", "evalAssignOp", "increment", "execute", "exprReturn", "duplicate", "restore", "error", "rethrow", "resolve", "expr", "doWhileLoop", "whileLoop", "makeIterator", "forLoop", "isMap", "getMapValue", "setMapValue", "get", "set", "fcall", "call", "cnew"]

    def __init__(self):
        self.returnValue = None
        self.inTry = None
        self.depth = None
        self.binops = None
        self.variables = None
        self.locals = haxe_ds_StringMap()
        self.declared = list()
        self.resetVariables()
        self.initOps()

    def resetVariables(self):
        _gthis = self
        self.variables = haxe_ds_StringMap()
        self.variables.h["null"] = None
        self.variables.h["true"] = True
        self.variables.h["false"] = False
        this1 = self.variables
        def _hx_local_0(el):
            inf = _gthis.posInfos()
            v = (None if ((len(el) == 0)) else el.pop(0))
            if (len(el) > 0):
                Reflect.setField(inf,"customParams",el)
            haxe_Log.trace(Std.string(v),inf)
        value = Reflect.makeVarArgs(_hx_local_0)
        this1.h["trace"] = value

    def posInfos(self):
        return _hx_AnonObject({'fileName': "hscript", 'lineNumber': 0})

    def initOps(self):
        me = self
        self.binops = haxe_ds_StringMap()
        def _hx_local_0(e1,e2):
            return python_Boot._add_dynamic(me.expr(e1),me.expr(e2))
        self.binops.h["+"] = _hx_local_0
        def _hx_local_1(e1,e2):
            return (me.expr(e1) - me.expr(e2))
        self.binops.h["-"] = _hx_local_1
        def _hx_local_2(e1,e2):
            return (me.expr(e1) * me.expr(e2))
        self.binops.h["*"] = _hx_local_2
        def _hx_local_3(e1,e2):
            return (me.expr(e1) / me.expr(e2))
        self.binops.h["/"] = _hx_local_3
        def _hx_local_4(e1,e2):
            return HxOverrides.modf(me.expr(e1), me.expr(e2))
        self.binops.h["%"] = _hx_local_4
        def _hx_local_5(e1,e2):
            return (me.expr(e1) & me.expr(e2))
        self.binops.h["&"] = _hx_local_5
        def _hx_local_6(e1,e2):
            return (me.expr(e1) | me.expr(e2))
        self.binops.h["|"] = _hx_local_6
        def _hx_local_7(e1,e2):
            return (me.expr(e1) ^ me.expr(e2))
        self.binops.h["^"] = _hx_local_7
        def _hx_local_8(e1,e2):
            return (me.expr(e1) << me.expr(e2))
        self.binops.h["<<"] = _hx_local_8
        def _hx_local_9(e1,e2):
            return (me.expr(e1) >> me.expr(e2))
        self.binops.h[">>"] = _hx_local_9
        def _hx_local_10(e1,e2):
            return HxOverrides.rshift(me.expr(e1), me.expr(e2))
        self.binops.h[">>>"] = _hx_local_10
        def _hx_local_11(e1,e2):
            return HxOverrides.eq(me.expr(e1),me.expr(e2))
        self.binops.h["=="] = _hx_local_11
        def _hx_local_12(e1,e2):
            return not HxOverrides.eq(me.expr(e1),me.expr(e2))
        self.binops.h["!="] = _hx_local_12
        def _hx_local_13(e1,e2):
            return (me.expr(e1) >= me.expr(e2))
        self.binops.h[">="] = _hx_local_13
        def _hx_local_14(e1,e2):
            return (me.expr(e1) <= me.expr(e2))
        self.binops.h["<="] = _hx_local_14
        def _hx_local_15(e1,e2):
            return (me.expr(e1) > me.expr(e2))
        self.binops.h[">"] = _hx_local_15
        def _hx_local_16(e1,e2):
            return (me.expr(e1) < me.expr(e2))
        self.binops.h["<"] = _hx_local_16
        def _hx_local_17(e1,e2):
            if (me.expr(e1) != True):
                return (me.expr(e2) == True)
            else:
                return True
        self.binops.h["||"] = _hx_local_17
        def _hx_local_18(e1,e2):
            if (me.expr(e1) == True):
                return (me.expr(e2) == True)
            else:
                return False
        self.binops.h["&&"] = _hx_local_18
        self.binops.h["="] = self.assign
        def _hx_local_19(e1,e2):
            return IntIterator(me.expr(e1),me.expr(e2))
        self.binops.h["..."] = _hx_local_19
        def _hx_local_20(v1,v2):
            return python_Boot._add_dynamic(v1,v2)
        self.assignOp("+=",_hx_local_20)
        def _hx_local_21(v1,v2):
            return (v1 - v2)
        self.assignOp("-=",_hx_local_21)
        def _hx_local_22(v1,v2):
            return (v1 * v2)
        self.assignOp("*=",_hx_local_22)
        def _hx_local_23(v1,v2):
            return (v1 / v2)
        self.assignOp("/=",_hx_local_23)
        def _hx_local_24(v1,v2):
            return HxOverrides.modf(v1, v2)
        self.assignOp("%=",_hx_local_24)
        def _hx_local_25(v1,v2):
            return (v1 & v2)
        self.assignOp("&=",_hx_local_25)
        def _hx_local_26(v1,v2):
            return (v1 | v2)
        self.assignOp("|=",_hx_local_26)
        def _hx_local_27(v1,v2):
            return (v1 ^ v2)
        self.assignOp("^=",_hx_local_27)
        def _hx_local_28(v1,v2):
            return (v1 << v2)
        self.assignOp("<<=",_hx_local_28)
        def _hx_local_29(v1,v2):
            return (v1 >> v2)
        self.assignOp(">>=",_hx_local_29)
        def _hx_local_30(v1,v2):
            return HxOverrides.rshift(v1, v2)
        self.assignOp(">>>=",_hx_local_30)

    def setVar(self,name,v):
        self.variables.h[name] = v

    def assign(self,e1,e2):
        v = self.expr(e2)
        tmp = e1.index
        if (tmp == 1):
            id = e1.params[0]
            l = self.locals.h.get(id,None)
            if (l is None):
                self.setVar(id,v)
            else:
                l.r = v
        elif (tmp == 5):
            e = e1.params[0]
            f = e1.params[1]
            v = self.set(self.expr(e),f,v)
        elif (tmp == 16):
            e = e1.params[0]
            index = e1.params[1]
            arr = self.expr(e)
            index1 = self.expr(index)
            if Std.isOfType(arr,haxe_IMap):
                def _hx_local_1():
                    _hx_local_0 = arr
                    if (Std.isOfType(_hx_local_0,haxe_IMap) or ((_hx_local_0 is None))):
                        _hx_local_0
                    else:
                        raise "Class cast error"
                    return _hx_local_0
                (_hx_local_1()).set(index1,v)
            else:
                HxOverrides.arraySet(arr,index1,v)
        else:
            e = hscript_Error.EInvalidOp("=")
            raise haxe_Exception.thrown(e)
        return v

    def assignOp(self,op,fop):
        me = self
        def _hx_local_0(e1,e2):
            return me.evalAssignOp(op,fop,e1,e2)
        self.binops.h[op] = _hx_local_0

    def evalAssignOp(self,op,fop,e1,e2):
        v = None
        tmp = e1.index
        if (tmp == 1):
            id = e1.params[0]
            l = self.locals.h.get(id,None)
            v = fop(self.expr(e1),self.expr(e2))
            if (l is None):
                self.setVar(id,v)
            else:
                l.r = v
        elif (tmp == 5):
            e = e1.params[0]
            f = e1.params[1]
            obj = self.expr(e)
            v = fop(self.get(obj,f),self.expr(e2))
            v = self.set(obj,f,v)
        elif (tmp == 16):
            e = e1.params[0]
            index = e1.params[1]
            arr = self.expr(e)
            index1 = self.expr(index)
            if Std.isOfType(arr,haxe_IMap):
                def _hx_local_1():
                    _hx_local_0 = arr
                    if (Std.isOfType(_hx_local_0,haxe_IMap) or ((_hx_local_0 is None))):
                        _hx_local_0
                    else:
                        raise "Class cast error"
                    return _hx_local_0
                v = fop((_hx_local_1()).get(index1),self.expr(e2))
                def _hx_local_3():
                    _hx_local_2 = arr
                    if (Std.isOfType(_hx_local_2,haxe_IMap) or ((_hx_local_2 is None))):
                        _hx_local_2
                    else:
                        raise "Class cast error"
                    return _hx_local_2
                (_hx_local_3()).set(index1,v)
            else:
                v = fop(HxOverrides.arrayGet(arr, index1),self.expr(e2))
                HxOverrides.arraySet(arr,index1,v)
        else:
            e = hscript_Error.EInvalidOp(op)
            raise haxe_Exception.thrown(e)
        return v

    def increment(self,e,prefix,delta):
        tmp = e.index
        if (tmp == 1):
            id = e.params[0]
            l = self.locals.h.get(id,None)
            v = (self.resolve(id) if ((l is None)) else l.r)
            if prefix:
                v = python_Boot._add_dynamic(v,delta)
                if (l is None):
                    self.setVar(id,v)
                else:
                    l.r = v
            elif (l is None):
                self.setVar(id,python_Boot._add_dynamic(v,delta))
            else:
                l.r = python_Boot._add_dynamic(v,delta)
            return v
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            obj = self.expr(e1)
            v = self.get(obj,f)
            if prefix:
                v = python_Boot._add_dynamic(v,delta)
                self.set(obj,f,v)
            else:
                self.set(obj,f,python_Boot._add_dynamic(v,delta))
            return v
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            arr = self.expr(e1)
            index1 = self.expr(index)
            if Std.isOfType(arr,haxe_IMap):
                def _hx_local_3():
                    _hx_local_2 = arr
                    if (Std.isOfType(_hx_local_2,haxe_IMap) or ((_hx_local_2 is None))):
                        _hx_local_2
                    else:
                        raise "Class cast error"
                    return _hx_local_2
                v = (_hx_local_3()).get(index1)
                if prefix:
                    v = python_Boot._add_dynamic(v,delta)
                    def _hx_local_6():
                        _hx_local_5 = arr
                        if (Std.isOfType(_hx_local_5,haxe_IMap) or ((_hx_local_5 is None))):
                            _hx_local_5
                        else:
                            raise "Class cast error"
                        return _hx_local_5
                    (_hx_local_6()).set(index1,v)
                else:
                    def _hx_local_8():
                        _hx_local_7 = arr
                        if (Std.isOfType(_hx_local_7,haxe_IMap) or ((_hx_local_7 is None))):
                            _hx_local_7
                        else:
                            raise "Class cast error"
                        return _hx_local_7
                    (_hx_local_8()).set(index1,python_Boot._add_dynamic(v,delta))
                return v
            else:
                v = HxOverrides.arrayGet(arr, index1)
                if prefix:
                    v = (v + delta)
                    HxOverrides.arraySet(arr,index1,v)
                else:
                    HxOverrides.arraySet(arr,index1,(v + delta))
                return v
        else:
            e = hscript_Error.EInvalidOp(("++" if ((delta > 0)) else "--"))
            raise haxe_Exception.thrown(e)

    def execute(self,expr):
        self.depth = 0
        self.locals = haxe_ds_StringMap()
        self.declared = list()
        return self.exprReturn(expr)

    def exprReturn(self,e):
        try:
            return self.expr(e)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,hscript__Interp_Stop):
                e = _g1
                tmp = e.index
                if (tmp == 0):
                    raise haxe_Exception.thrown("Invalid break")
                elif (tmp == 1):
                    raise haxe_Exception.thrown("Invalid continue")
                elif (tmp == 2):
                    v = self.returnValue
                    self.returnValue = None
                    return v
                else:
                    pass
            else:
                raise _g

    def duplicate(self,h):
        h2 = haxe_ds_StringMap()
        k = h.keys()
        while k.hasNext():
            k1 = k.next()
            value = h.h.get(k1,None)
            h2.h[k1] = value
        return h2

    def restore(self,old):
        while (len(self.declared) > old):
            _this = self.declared
            d = (None if ((len(_this) == 0)) else _this.pop())
            self.locals.h[d.n] = d.old

    def error(self,e,rethrow = None):
        if (rethrow is None):
            rethrow = False
        if rethrow:
            raise haxe_Exception.thrown(e)
        else:
            raise haxe_Exception.thrown(e)

    def rethrow(self,e):
        raise haxe_Exception.thrown(e)

    def resolve(self,id):
        l = self.locals.h.get(id,None)
        if (l is not None):
            return l.r
        v = self.variables.h.get(id,None)
        if ((v is None) and (not (id in self.variables.h))):
            e = hscript_Error.EUnknownVariable(id)
            raise haxe_Exception.thrown(e)
        return v

    def expr(self,e):
        _gthis = self
        tmp = e.index
        if (tmp == 0):
            c = e.params[0]
            tmp = c.index
            if (tmp == 0):
                v = c.params[0]
                return v
            elif (tmp == 1):
                f = c.params[0]
                return f
            elif (tmp == 2):
                s = c.params[0]
                return s
            else:
                pass
        elif (tmp == 1):
            id = e.params[0]
            return self.resolve(id)
        elif (tmp == 2):
            _g = e.params[1]
            n = e.params[0]
            e1 = e.params[2]
            _this = self.declared
            x = _hx_AnonObject({'n': n, 'old': self.locals.h.get(n,None)})
            _this.append(x)
            this1 = self.locals
            value = (None if ((e1 is None)) else self.expr(e1))
            this1.h[n] = _hx_AnonObject({'r': value})
            return None
        elif (tmp == 3):
            e1 = e.params[0]
            return self.expr(e1)
        elif (tmp == 4):
            exprs = e.params[0]
            old = len(self.declared)
            v = None
            _g = 0
            while (_g < len(exprs)):
                e1 = (exprs[_g] if _g >= 0 and _g < len(exprs) else None)
                _g = (_g + 1)
                v = self.expr(e1)
            self.restore(old)
            return v
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            return self.get(self.expr(e1),f)
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            fop = self.binops.h.get(op,None)
            if (fop is None):
                e3 = hscript_Error.EInvalidOp(op)
                raise haxe_Exception.thrown(e3)
            return fop(e1,e2)
        elif (tmp == 7):
            op = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            op1 = op
            _hx_local_1 = len(op1)
            if (_hx_local_1 == 1):
                if (op1 == "!"):
                    return (self.expr(e1) != True)
                elif (op1 == "-"):
                    return -self.expr(e1)
                elif (op1 == "~"):
                    return ~self.expr(e1)
                else:
                    e1 = hscript_Error.EInvalidOp(op)
                    raise haxe_Exception.thrown(e1)
            elif (_hx_local_1 == 2):
                if (op1 == "++"):
                    return self.increment(e1,prefix,1)
                elif (op1 == "--"):
                    return self.increment(e1,prefix,-1)
                else:
                    e1 = hscript_Error.EInvalidOp(op)
                    raise haxe_Exception.thrown(e1)
            else:
                e1 = hscript_Error.EInvalidOp(op)
                raise haxe_Exception.thrown(e1)
        elif (tmp == 8):
            e1 = e.params[0]
            params = e.params[1]
            args = list()
            _g = 0
            while (_g < len(params)):
                p = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                x = self.expr(p)
                args.append(x)
            if (e1.index == 5):
                e2 = e1.params[0]
                f = e1.params[1]
                obj = self.expr(e2)
                if (obj is None):
                    e2 = hscript_Error.EInvalidAccess(f)
                    raise haxe_Exception.thrown(e2)
                return self.fcall(obj,f,args)
            else:
                return self.call(None,self.expr(e1),args)
        elif (tmp == 9):
            econd = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            if (self.expr(econd) == True):
                return self.expr(e1)
            elif (e2 is None):
                return None
            else:
                return self.expr(e2)
        elif (tmp == 10):
            econd = e.params[0]
            e1 = e.params[1]
            self.whileLoop(econd,e1)
            return None
        elif (tmp == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            self.forLoop(v,it,e1)
            return None
        elif (tmp == 12):
            raise haxe_Exception.thrown(hscript__Interp_Stop.SBreak)
        elif (tmp == 13):
            raise haxe_Exception.thrown(hscript__Interp_Stop.SContinue)
        elif (tmp == 14):
            _g = e.params[3]
            params = e.params[0]
            fexpr = e.params[1]
            name = e.params[2]
            capturedLocals = self.duplicate(self.locals)
            me = self
            hasOpt = False
            minParams = 0
            _g = 0
            while (_g < len(params)):
                p = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                if Reflect.field(p,"opt"):
                    hasOpt = True
                else:
                    minParams = (minParams + 1)
            def _hx_local_9(args):
                if (((0 if ((args is None)) else len(args))) != len(params)):
                    if (len(args) < minParams):
                        _hx_str = ((("Invalid number of parameters. Got " + Std.string(len(args))) + ", required ") + Std.string(minParams))
                        if (name is not None):
                            _hx_str = (("null" if _hx_str is None else _hx_str) + HxOverrides.stringOrNull((((" for function '" + ("null" if name is None else name)) + "'"))))
                        e = hscript_Error.ECustom(_hx_str)
                        raise haxe_Exception.thrown(e)
                    args2 = []
                    extraParams = (len(args) - minParams)
                    pos = 0
                    _g = 0
                    while (_g < len(params)):
                        p = (params[_g] if _g >= 0 and _g < len(params) else None)
                        _g = (_g + 1)
                        if Reflect.field(p,"opt"):
                            if (extraParams > 0):
                                x = pos
                                pos = (pos + 1)
                                x1 = (args[x] if x >= 0 and x < len(args) else None)
                                args2.append(x1)
                                extraParams = (extraParams - 1)
                            else:
                                args2.append(None)
                        else:
                            x2 = pos
                            pos = (pos + 1)
                            x3 = (args[x2] if x2 >= 0 and x2 < len(args) else None)
                            args2.append(x3)
                    args = args2
                old = me.locals
                depth = me.depth
                me.depth = (me.depth + 1)
                me.locals = me.duplicate(capturedLocals)
                _g = 0
                _g1 = len(params)
                while (_g < _g1):
                    i = _g
                    _g = (_g + 1)
                    me.locals.h[(params[i] if i >= 0 and i < len(params) else None).name] = _hx_AnonObject({'r': (args[i] if i >= 0 and i < len(args) else None)})
                r = None
                oldDecl = len(_gthis.declared)
                if _gthis.inTry:
                    try:
                        r = me.exprReturn(fexpr)
                    except BaseException as _g:
                        None
                        e = haxe_Exception.caught(_g).unwrap()
                        me.locals = old
                        me.depth = depth
                        raise haxe_Exception.thrown(e)
                else:
                    r = me.exprReturn(fexpr)
                _gthis.restore(oldDecl)
                me.locals = old
                me.depth = depth
                return r
            f = _hx_local_9
            f1 = Reflect.makeVarArgs(f)
            if (name is not None):
                if (self.depth == 0):
                    self.variables.h[name] = f1
                else:
                    _this = self.declared
                    x = _hx_AnonObject({'n': name, 'old': self.locals.h.get(name,None)})
                    _this.append(x)
                    ref = _hx_AnonObject({'r': f1})
                    self.locals.h[name] = ref
                    capturedLocals.h[name] = ref
            return f1
        elif (tmp == 15):
            e1 = e.params[0]
            self.returnValue = (None if ((e1 is None)) else self.expr(e1))
            raise haxe_Exception.thrown(hscript__Interp_Stop.SReturn)
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            arr = self.expr(e1)
            index1 = self.expr(index)
            if Std.isOfType(arr,haxe_IMap):
                def _hx_local_12():
                    def _hx_local_11():
                        _hx_local_10 = arr
                        if (Std.isOfType(_hx_local_10,haxe_IMap) or ((_hx_local_10 is None))):
                            _hx_local_10
                        else:
                            raise "Class cast error"
                        return _hx_local_10
                    return (_hx_local_11()).get(index1)
                return _hx_local_12()
            else:
                return HxOverrides.arrayGet(arr, index1)
        elif (tmp == 17):
            arr = e.params[0]
            tmp = None
            if (len(arr) > 0):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 6):
                    _g1 = _g.params[1]
                    _g1 = _g.params[2]
                    tmp = (_g.params[0] == "=>")
                else:
                    tmp = False
            else:
                tmp = False
            if tmp:
                isAllString = True
                isAllInt = True
                isAllObject = True
                isAllEnum = True
                keys = []
                values = []
                _g = 0
                while (_g < len(arr)):
                    e1 = (arr[_g] if _g >= 0 and _g < len(arr) else None)
                    _g = (_g + 1)
                    if (e1.index == 6):
                        if (e1.params[0] == "=>"):
                            eKey = e1.params[1]
                            eValue = e1.params[2]
                            key = self.expr(eKey)
                            value = self.expr(eValue)
                            isAllString = (isAllString and Std.isOfType(key,str))
                            isAllInt = (isAllInt and Std.isOfType(key,Int))
                            isAllObject = (isAllObject and Reflect.isObject(key))
                            isAllEnum = (isAllEnum and Reflect.isEnumValue(key))
                            keys.append(key)
                            values.append(value)
                        else:
                            raise haxe_Exception.thrown("=> expected")
                    else:
                        raise haxe_Exception.thrown("=> expected")
                _hx_map = None
                if isAllInt:
                    _hx_map = haxe_ds_IntMap()
                elif isAllString:
                    _hx_map = haxe_ds_StringMap()
                elif isAllEnum:
                    _hx_map = haxe_ds_EnumValueMap()
                elif isAllObject:
                    _hx_map = haxe_ds_ObjectMap()
                else:
                    raise haxe_Exception.thrown("Inconsistent key types")
                _g = 0
                _g1 = len(keys)
                while (_g < _g1):
                    n = _g
                    _g = (_g + 1)
                    def _hx_local_15():
                        _hx_local_14 = _hx_map
                        if (Std.isOfType(_hx_local_14,haxe_IMap) or ((_hx_local_14 is None))):
                            _hx_local_14
                        else:
                            raise "Class cast error"
                        return _hx_local_14
                    (_hx_local_15()).set((keys[n] if n >= 0 and n < len(keys) else None),(values[n] if n >= 0 and n < len(values) else None))
                return _hx_map
            else:
                a = list()
                _g = 0
                while (_g < len(arr)):
                    e1 = (arr[_g] if _g >= 0 and _g < len(arr) else None)
                    _g = (_g + 1)
                    x = self.expr(e1)
                    a.append(x)
                return a
        elif (tmp == 18):
            cl = e.params[0]
            params1 = e.params[1]
            a = list()
            _g = 0
            while (_g < len(params1)):
                e1 = (params1[_g] if _g >= 0 and _g < len(params1) else None)
                _g = (_g + 1)
                x = self.expr(e1)
                a.append(x)
            return self.cnew(cl,a)
        elif (tmp == 19):
            e1 = e.params[0]
            raise haxe_Exception.thrown(self.expr(e1))
        elif (tmp == 20):
            _g = e.params[2]
            e1 = e.params[0]
            n = e.params[1]
            ecatch = e.params[3]
            old = len(self.declared)
            oldTry = self.inTry
            try:
                self.inTry = True
                v = self.expr(e1)
                self.restore(old)
                self.inTry = oldTry
                return v
            except BaseException as _g:
                None
                _g1 = haxe_Exception.caught(_g).unwrap()
                if Std.isOfType(_g1,hscript__Interp_Stop):
                    err = _g1
                    self.inTry = oldTry
                    raise haxe_Exception.thrown(err)
                else:
                    err = _g1
                    self.restore(old)
                    self.inTry = oldTry
                    _this = self.declared
                    x = _hx_AnonObject({'n': n, 'old': self.locals.h.get(n,None)})
                    _this.append(x)
                    self.locals.h[n] = _hx_AnonObject({'r': err})
                    v = self.expr(ecatch)
                    self.restore(old)
                    return v
        elif (tmp == 21):
            fl = e.params[0]
            o = _hx_AnonObject({})
            _g = 0
            while (_g < len(fl)):
                f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                self.set(o,f.name,self.expr(f.e))
            return o
        elif (tmp == 22):
            econd = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            if (self.expr(econd) == True):
                return self.expr(e1)
            else:
                return self.expr(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            val = self.expr(e1)
            match = False
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    if HxOverrides.eq(self.expr(v),val):
                        match = True
                        break
                if match:
                    val = self.expr(c.expr)
                    break
            if (not match):
                val = (None if ((_hx_def is None)) else self.expr(_hx_def))
            return val
        elif (tmp == 24):
            econd = e.params[0]
            e1 = e.params[1]
            self.doWhileLoop(econd,e1)
            return None
        elif (tmp == 25):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.expr(e1)
        elif (tmp == 26):
            _g = e.params[1]
            e1 = e.params[0]
            return self.expr(e1)
        else:
            pass

    def doWhileLoop(self,econd,e):
        old = len(self.declared)
        while True:
            try:
                self.expr(e)
            except BaseException as _g:
                None
                _g1 = haxe_Exception.caught(_g).unwrap()
                if Std.isOfType(_g1,hscript__Interp_Stop):
                    err = _g1
                    tmp = err.index
                    if (tmp == 0):
                        break
                    elif (tmp == 1):
                        pass
                    elif (tmp == 2):
                        raise haxe_Exception.thrown(err)
                    else:
                        pass
                else:
                    raise _g
            if (not ((self.expr(econd) == True))):
                break
        self.restore(old)

    def whileLoop(self,econd,e):
        old = len(self.declared)
        while (self.expr(econd) == True):
            try:
                self.expr(e)
            except BaseException as _g:
                None
                _g1 = haxe_Exception.caught(_g).unwrap()
                if Std.isOfType(_g1,hscript__Interp_Stop):
                    err = _g1
                    tmp = err.index
                    if (tmp == 0):
                        break
                    elif (tmp == 1):
                        pass
                    elif (tmp == 2):
                        raise haxe_Exception.thrown(err)
                    else:
                        pass
                else:
                    raise _g
        self.restore(old)

    def makeIterator(self,v):
        try:
            v = Reflect.field(v,"iterator")()
        except BaseException as _g:
            None
        if ((Reflect.field(v,"hasNext") is None) or ((Reflect.field(v,"next") is None))):
            e = hscript_Error.EInvalidIterator(v)
            raise haxe_Exception.thrown(e)
        return v

    def forLoop(self,n,it,e):
        old = len(self.declared)
        _this = self.declared
        x = _hx_AnonObject({'n': n, 'old': self.locals.h.get(n,None)})
        _this.append(x)
        it1 = self.makeIterator(self.expr(it))
        while it1.hasNext():
            this1 = self.locals
            value = _hx_AnonObject({'r': it1.next()})
            this1.h[n] = value
            try:
                self.expr(e)
            except BaseException as _g:
                None
                _g1 = haxe_Exception.caught(_g).unwrap()
                if Std.isOfType(_g1,hscript__Interp_Stop):
                    err = _g1
                    tmp = err.index
                    if (tmp == 0):
                        break
                    elif (tmp == 1):
                        pass
                    elif (tmp == 2):
                        raise haxe_Exception.thrown(err)
                    else:
                        pass
                else:
                    raise _g
        self.restore(old)

    def isMap(self,o):
        return Std.isOfType(o,haxe_IMap)

    def getMapValue(self,_hx_map,key):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = _hx_map
                if (Std.isOfType(_hx_local_0,haxe_IMap) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return (_hx_local_1()).get(key)
        return _hx_local_2()

    def setMapValue(self,_hx_map,key,value):
        def _hx_local_1():
            _hx_local_0 = _hx_map
            if (Std.isOfType(_hx_local_0,haxe_IMap) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        (_hx_local_1()).set(key,value)

    def get(self,o,f):
        if (o is None):
            e = hscript_Error.EInvalidAccess(f)
            raise haxe_Exception.thrown(e)
        return Reflect.getProperty(o,f)

    def set(self,o,f,v):
        if (o is None):
            e = hscript_Error.EInvalidAccess(f)
            raise haxe_Exception.thrown(e)
        Reflect.setProperty(o,f,v)
        return v

    def fcall(self,o,f,args):
        return self.call(o,self.get(o,f),args)

    def call(self,o,f,args):
        return Reflect.callMethod(o,f,args)

    def cnew(self,cl,args):
        c = Type.resolveClass(cl)
        if (c is None):
            c = self.resolve(cl)
        return c(*args)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.variables = None
        _hx_o.locals = None
        _hx_o.binops = None
        _hx_o.depth = None
        _hx_o.inTry = None
        _hx_o.declared = None
        _hx_o.returnValue = None
hscript_Interp._hx_class = hscript_Interp
_hx_classes["hscript.Interp"] = hscript_Interp


