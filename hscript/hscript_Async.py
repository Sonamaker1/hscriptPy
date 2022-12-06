class hscript_Async:
    _hx_class_name = "hscript.Async"
    _hx_fields = ["definedVars", "vars", "currentFun", "currentLoop", "currentBreak", "uid", "asyncIdents", "syncFlag"]
    _hx_methods = ["getTopLevelEnd", "build", "defineVar", "lookupFunctions", "buildSync", "ignore", "ident", "fun", "funs", "block", "field", "binop", "call", "retNull", "makeCall", "isSync", "isAsyncIdent", "checkSync", "saveVars", "restoreVars", "toCps"]
    _hx_statics = ["nullExpr", "nullId", "expr", "mk", "toAsync"]

    def __init__(self):
        self.syncFlag = None
        self.asyncIdents = None
        self.currentBreak = None
        self.currentLoop = None
        self.currentFun = None
        self.uid = 0
        self.vars = haxe_ds_StringMap()
        self.definedVars = []

    def getTopLevelEnd(self):
        return self.ignore()

    def build(self,e,topLevelSync = None):
        if (topLevelSync is None):
            topLevelSync = False
        if topLevelSync:
            return self.buildSync(e,None)
        else:
            end = self.getTopLevelEnd()
            return self.toCps(e,end,end)

    def defineVar(self,v,mode):
        _this = self.definedVars
        x = _hx_AnonObject({'n': v, 'prev': self.vars.h.get(v,None)})
        _this.append(x)
        self.vars.h[v] = mode

    def lookupFunctions(self,el):
        _g = 0
        while (_g < len(el)):
            e = (el[_g] if _g >= 0 and _g < len(el) else None)
            _g = (_g + 1)
            tmp = e.index
            if (tmp == 14):
                _g1 = e.params[0]
                _g2 = e.params[1]
                _g3 = e.params[3]
                name = e.params[2]
                if (name is not None):
                    self.defineVar(name,hscript_VarMode.Defined)
            elif (tmp == 25):
                _g4 = e.params[1]
                if (e.params[0] == "sync"):
                    _hx_tmp = e.params[2]
                    if (_hx_tmp.index == 14):
                        _g5 = _hx_tmp.params[0]
                        _g6 = _hx_tmp.params[1]
                        _g7 = _hx_tmp.params[3]
                        name1 = _hx_tmp.params[2]
                        if (name1 is not None):
                            self.defineVar(name1,hscript_VarMode.ForceSync)
            else:
                pass

    def buildSync(self,e,exit):
        tmp = e.index
        if (tmp == 4):
            el = e.params[0]
            v = self.saveVars()
            self.lookupFunctions(el)
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = self.buildSync(e1,exit)
                _g.append(x)
            arr = _g
            e1 = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    e1 = True
                else:
                    e1 = False
            else:
                e1 = False
            e2 = ((arr[0] if 0 < len(arr) else None) if e1 else hscript_Expr.EBlock(arr))
            self.restoreVars(v)
            return e2
        elif (tmp == 10):
            _g = e.params[0]
            _g = e.params[1]
            oldLoop = self.currentLoop
            oldBreak = self.currentBreak
            self.currentLoop = None
            self.currentBreak = None
            _g = self.buildSync
            exit1 = exit
            def _hx_local_1(e):
                return _g(e,exit1)
            e = hscript_Tools.map(e,_hx_local_1)
            self.currentLoop = oldLoop
            self.currentBreak = oldBreak
            return e
        elif (tmp == 11):
            _g1 = e.params[0]
            _g1 = e.params[1]
            _g1 = e.params[2]
            oldLoop = self.currentLoop
            oldBreak = self.currentBreak
            self.currentLoop = None
            self.currentBreak = None
            _g1 = self.buildSync
            exit2 = exit
            def _hx_local_2(e):
                return _g1(e,exit2)
            e = hscript_Tools.map(e,_hx_local_2)
            self.currentLoop = oldLoop
            self.currentBreak = oldBreak
            return e
        elif (tmp == 12):
            if (self.currentBreak is not None):
                return self.currentBreak(e)
            else:
                _g2 = self.buildSync
                exit3 = exit
                def _hx_local_4():
                    def _hx_local_3(e):
                        return _g2(e,exit3)
                    return hscript_Tools.map(e,_hx_local_3)
                return _hx_local_4()
        elif (tmp == 13):
            if (self.currentLoop is not None):
                arr = [self.retNull(self.currentLoop,e), hscript_Expr.EReturn()]
                tmp = None
                if (len(arr) == 1):
                    _g3 = (arr[0] if 0 < len(arr) else None)
                    if (_g3.index == 4):
                        _g4 = _g3.params[0]
                        tmp = True
                    else:
                        tmp = False
                else:
                    tmp = False
                if tmp:
                    return (arr[0] if 0 < len(arr) else None)
                else:
                    return hscript_Expr.EBlock(arr)
            else:
                _g3 = self.buildSync
                exit4 = exit
                def _hx_local_6():
                    def _hx_local_5(e):
                        return _g3(e,exit4)
                    return hscript_Tools.map(e,_hx_local_5)
                return _hx_local_6()
        elif (tmp == 14):
            _g4 = e.params[0]
            _g4 = e.params[1]
            _g4 = e.params[3]
            name = e.params[2]
            if (name is not None):
                return self.toCps(e,None,None)
            return e
        elif (tmp == 15):
            eret = e.params[0]
            if (exit is not None):
                arr = [(self.retNull(exit,e) if ((eret is None)) else hscript_Expr.ECall(exit,[eret])), hscript_Expr.EReturn()]
                tmp = None
                if (len(arr) == 1):
                    _g4 = (arr[0] if 0 < len(arr) else None)
                    if (_g4.index == 4):
                        _g5 = _g4.params[0]
                        tmp = True
                    else:
                        tmp = False
                else:
                    tmp = False
                if tmp:
                    return (arr[0] if 0 < len(arr) else None)
                else:
                    return hscript_Expr.EBlock(arr)
            else:
                _g4 = self.buildSync
                exit5 = exit
                def _hx_local_8():
                    def _hx_local_7(e):
                        return _g4(e,exit5)
                    return hscript_Tools.map(e,_hx_local_7)
                return _hx_local_8()
        elif (tmp == 25):
            _g5 = e.params[1]
            _g6 = e.params[2]
            _g7 = e.params[0]
            _hx_local_9 = len(_g7)
            if (_hx_local_9 == 5):
                if (_g7 == "async"):
                    e1 = _g6
                    return self.toCps(e1,self.ignore(),self.ignore())
                else:
                    _g6 = self.buildSync
                    exit7 = exit
                    def _hx_local_11():
                        def _hx_local_10(e):
                            return _g6(e,exit7)
                        return hscript_Tools.map(e,_hx_local_10)
                    return _hx_local_11()
            elif (_hx_local_9 == 4):
                if (_g7 == "sync"):
                    _hx_tmp = _g6
                    if (_hx_tmp.index == 14):
                        args = _g5
                        ef = _g6
                        fargs = _hx_tmp.params[0]
                        body = _hx_tmp.params[1]
                        name = _hx_tmp.params[2]
                        ret = _hx_tmp.params[3]
                        return hscript_Expr.EMeta("sync",args,hscript_Expr.EFunction(fargs,self.buildSync(body,None),name,ret))
                    else:
                        _g5 = self.buildSync
                        exit6 = exit
                        def _hx_local_13():
                            def _hx_local_12(e):
                                return _g5(e,exit6)
                            return hscript_Tools.map(e,_hx_local_12)
                        return _hx_local_13()
                else:
                    _g6 = self.buildSync
                    exit7 = exit
                    def _hx_local_15():
                        def _hx_local_14(e):
                            return _g6(e,exit7)
                        return hscript_Tools.map(e,_hx_local_14)
                    return _hx_local_15()
            else:
                _g6 = self.buildSync
                exit7 = exit
                def _hx_local_17():
                    def _hx_local_16(e):
                        return _g6(e,exit7)
                    return hscript_Tools.map(e,_hx_local_16)
                return _hx_local_17()
        else:
            _g7 = self.buildSync
            exit8 = exit
            def _hx_local_19():
                def _hx_local_18(e):
                    return _g7(e,exit8)
                return hscript_Tools.map(e,_hx_local_18)
            return _hx_local_19()

    def ignore(self,e = None):
        inf = (hscript_Async.nullExpr if ((e is None)) else e)
        arr = ([] if ((e is None)) else [e])
        e = None
        if (len(arr) == 1):
            _g = (arr[0] if 0 < len(arr) else None)
            if (_g.index == 4):
                _g1 = _g.params[0]
                e = True
            else:
                e = False
        else:
            e = False
        return hscript_Expr.EFunction([_hx_AnonObject({'name': "_", 't': None})],((arr[0] if 0 < len(arr) else None) if e else hscript_Expr.EBlock(arr)),None)

    def ident(self,_hx_str,e):
        return hscript_Expr.EIdent(_hx_str)

    def fun(self,arg,e,name = None):
        return hscript_Expr.EFunction([_hx_AnonObject({'name': arg, 't': None})],e,name)

    def funs(self,arg,e,name = None):
        _g = []
        _g1 = 0
        while (_g1 < len(arg)):
            a = (arg[_g1] if _g1 >= 0 and _g1 < len(arg) else None)
            _g1 = (_g1 + 1)
            _g.append(_hx_AnonObject({'name': a, 't': None}))
        return hscript_Expr.EFunction(_g,e,name)

    def block(self,arr,e):
        tmp = None
        if (len(arr) == 1):
            _g = (arr[0] if 0 < len(arr) else None)
            if (_g.index == 4):
                _g1 = _g.params[0]
                tmp = True
            else:
                tmp = False
        else:
            tmp = False
        if tmp:
            return (arr[0] if 0 < len(arr) else None)
        return hscript_Expr.EBlock(arr)

    def field(self,e,f,inf):
        return hscript_Expr.EField(e,f)

    def binop(self,op,e1,e2,inf):
        return hscript_Expr.EBinop(op,e1,e2)

    def call(self,e,args,inf):
        return hscript_Expr.ECall(e,args)

    def retNull(self,e,pos = None):
        if (e.index == 14):
            _g = e.params[0]
            _g1 = e.params[2]
            _g1 = e.params[3]
            if (len(_g) == 1):
                _g1 = (_g[0] if 0 < len(_g) else None)
                _g = Reflect.field(_g1,"opt")
                _g = Reflect.field(_g1,"t")
                _g = Reflect.field(_g1,"value")
                if (_g1.name == "_"):
                    e1 = e.params[1]
                    return e1
        return hscript_Expr.ECall(e,[hscript_Async.nullId])

    def makeCall(self,ecall,args,rest,exit,sync = None):
        if (sync is None):
            sync = False
        _g = []
        _g1 = 0
        _g2 = len(args)
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.uid
                _hx_local_0.uid = (_hx_local_1 + 1)
                return _hx_local_1
            x = ("_a" + Std.string(_hx_local_2()))
            _g.append(x)
        names = _g
        _g = []
        _g1 = 0
        _g2 = len(args)
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            x = hscript_Expr.EIdent((names[i] if i >= 0 and i < len(names) else None))
            _g.append(x)
        rargs = _g
        if (not sync):
            rargs.insert(0, rest)
        rest1 = (hscript_Expr.ECall(rest,[hscript_Expr.ECall(ecall,rargs)]) if sync else hscript_Expr.ECall(ecall,rargs))
        i = (len(args) - 1)
        while (i >= 0):
            rest1 = self.toCps((args[i] if i >= 0 and i < len(args) else None),hscript_Expr.EFunction([_hx_AnonObject({'name': (names[i] if i >= 0 and i < len(names) else None), 't': None})],rest1,None),exit)
            i = (i - 1)
        return rest1

    def isSync(self,e):
        self.syncFlag = True
        self.checkSync(e)
        return self.syncFlag

    def isAsyncIdent(self,id):
        if (self.asyncIdents is not None):
            return (id in self.asyncIdents.h)
        else:
            return True

    def checkSync(self,e):
        if (not self.syncFlag):
            return
        tmp = e.index
        if (tmp == 8):
            _g = e.params[1]
            _hx_tmp = e.params[0]
            tmp = _hx_tmp.index
            if (tmp == 1):
                i = _hx_tmp.params[0]
                if (((self.asyncIdents is None) or (i in self.asyncIdents.h)) or ((self.vars.h.get(i,None) == hscript_VarMode.Defined))):
                    self.syncFlag = False
                else:
                    hscript_Tools.iter(e,self.checkSync)
            elif (tmp == 5):
                _g = _hx_tmp.params[0]
                i = _hx_tmp.params[1]
                if ((self.asyncIdents is None) or (i in self.asyncIdents.h)):
                    self.syncFlag = False
                else:
                    hscript_Tools.iter(e,self.checkSync)
            else:
                hscript_Tools.iter(e,self.checkSync)
        elif (tmp == 14):
            _g = e.params[0]
            _g = e.params[1]
            _g = e.params[3]
            name = e.params[2]
            if (name is not None):
                self.syncFlag = False
            else:
                hscript_Tools.iter(e,self.checkSync)
        elif (tmp == 25):
            _g = e.params[1]
            _g = e.params[2]
            _g = e.params[0]
            _hx_local_0 = len(_g)
            if (_hx_local_0 == 5):
                if (_g == "async"):
                    pass
                else:
                    hscript_Tools.iter(e,self.checkSync)
            elif (_hx_local_0 == 4):
                if (_g == "sync"):
                    pass
                else:
                    hscript_Tools.iter(e,self.checkSync)
            else:
                hscript_Tools.iter(e,self.checkSync)
        else:
            hscript_Tools.iter(e,self.checkSync)

    def saveVars(self):
        return len(self.definedVars)

    def restoreVars(self,k):
        while (len(self.definedVars) > k):
            _this = self.definedVars
            v = (None if ((len(_this) == 0)) else _this.pop())
            if (v.prev is None):
                self.vars.remove(v.n)
            else:
                self.vars.h[v.n] = v.prev

    def toCps(self,e,rest,exit):
        _gthis = self
        if self.isSync(e):
            args = [self.buildSync(e,exit)]
            return hscript_Expr.ECall(rest,args)
        tmp = e.index
        if (tmp == 0):
            _g = e.params[0]
            return hscript_Expr.ECall(rest,[e])
        elif (tmp == 1):
            _g = e.params[0]
            return hscript_Expr.ECall(rest,[e])
        elif (tmp == 2):
            v = e.params[0]
            t = e.params[1]
            ev = e.params[2]
            if (ev is None):
                arr = [e, self.retNull(rest,e)]
                tmp = None
                if (len(arr) == 1):
                    _g = (arr[0] if 0 < len(arr) else None)
                    if (_g.index == 4):
                        _g1 = _g.params[0]
                        tmp = True
                    else:
                        tmp = False
                else:
                    tmp = False
                if tmp:
                    return (arr[0] if 0 < len(arr) else None)
                else:
                    return hscript_Expr.EBlock(arr)
            arr = [hscript_Expr.EBinop("=",hscript_Expr.EIdent(v),hscript_Expr.EIdent("_r")), self.retNull(rest,e)]
            e1 = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    e1 = True
                else:
                    e1 = False
            else:
                e1 = False
            arr1 = [hscript_Expr.EVar(v,t), self.toCps(ev,hscript_Expr.EFunction([_hx_AnonObject({'name': "_r", 't': None})],((arr[0] if 0 < len(arr) else None) if e1 else hscript_Expr.EBlock(arr)),None),exit)]
            tmp = None
            if (len(arr1) == 1):
                _g = (arr1[0] if 0 < len(arr1) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if tmp:
                return (arr1[0] if 0 < len(arr1) else None)
            else:
                return hscript_Expr.EBlock(arr1)
        elif (tmp == 3):
            e1 = e.params[0]
            return hscript_Expr.EParent(self.toCps(e1,rest,exit))
        elif (tmp == 4):
            el = e.params[0]
            el1 = list(el)
            vold = self.saveVars()
            self.lookupFunctions(el1)
            while (len(el1) > 0):
                e1 = self.toCps((None if ((len(el1) == 0)) else el1.pop()),rest,exit)
                rest = self.ignore(e1)
            self.restoreVars(vold)
            return self.retNull(rest)
        elif (tmp == 5):
            _g = e.params[0]
            _g = e.params[1]
            return hscript_Expr.ECall(rest,[e])
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            op1 = op
            _hx_local_0 = len(op1)
            if (_hx_local_0 == 1):
                if (op1 == "="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_3():
                            _hx_local_1 = self
                            _hx_local_2 = _hx_local_1.uid
                            _hx_local_1.uid = (_hx_local_2 + 1)
                            return _hx_local_2
                        id = ("_r" + Std.string(_hx_local_3()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_6():
                            _hx_local_4 = self
                            _hx_local_5 = _hx_local_4.uid
                            _hx_local_4.uid = (_hx_local_5 + 1)
                            return _hx_local_5
                        id1 = ("_r" + Std.string(_hx_local_6()))
                        def _hx_local_9():
                            _hx_local_7 = self
                            _hx_local_8 = _hx_local_7.uid
                            _hx_local_7.uid = (_hx_local_8 + 1)
                            return _hx_local_8
                        id2 = ("_r" + Std.string(_hx_local_9()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_12():
                            _hx_local_10 = self
                            _hx_local_11 = _hx_local_10.uid
                            _hx_local_10.uid = (_hx_local_11 + 1)
                            return _hx_local_11
                        idArr = ("_r" + Std.string(_hx_local_12()))
                        def _hx_local_15():
                            _hx_local_13 = self
                            _hx_local_14 = _hx_local_13.uid
                            _hx_local_13.uid = (_hx_local_14 + 1)
                            return _hx_local_14
                        idIndex = ("_r" + Std.string(_hx_local_15()))
                        def _hx_local_18():
                            _hx_local_16 = self
                            _hx_local_17 = _hx_local_16.uid
                            _hx_local_16.uid = (_hx_local_17 + 1)
                            return _hx_local_17
                        idVal = ("_r" + Std.string(_hx_local_18()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                else:
                    def _hx_local_21():
                        _hx_local_19 = self
                        _hx_local_20 = _hx_local_19.uid
                        _hx_local_19.uid = (_hx_local_20 + 1)
                        return _hx_local_20
                    id1 = ("_r" + Std.string(_hx_local_21()))
                    def _hx_local_24():
                        _hx_local_22 = self
                        _hx_local_23 = _hx_local_22.uid
                        _hx_local_22.uid = (_hx_local_23 + 1)
                        return _hx_local_23
                    id2 = ("_r" + Std.string(_hx_local_24()))
                    e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EIdent(id1),hscript_Expr.EIdent(id2))]),None),exit)
                    return self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
            elif (_hx_local_0 == 2):
                if (op1 == "&&"):
                    def _hx_local_27():
                        _hx_local_25 = self
                        _hx_local_26 = _hx_local_25.uid
                        _hx_local_25.uid = (_hx_local_26 + 1)
                        return _hx_local_26
                    id1 = ("_r" + Std.string(_hx_local_27()))
                    def _hx_local_30():
                        _hx_local_28 = self
                        _hx_local_29 = _hx_local_28.uid
                        _hx_local_28.uid = (_hx_local_29 + 1)
                        return _hx_local_29
                    id2 = ("_r" + Std.string(_hx_local_30()))
                    e3 = hscript_Expr.EIf(hscript_Expr.EBinop("!=",hscript_Expr.EIdent(id1),hscript_Expr.EIdent("true")),hscript_Expr.ECall(rest,[hscript_Expr.EIdent("false")]),self.toCps(e2,rest,exit))
                    return self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                elif (op1 == "%="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_33():
                            _hx_local_31 = self
                            _hx_local_32 = _hx_local_31.uid
                            _hx_local_31.uid = (_hx_local_32 + 1)
                            return _hx_local_32
                        id = ("_r" + Std.string(_hx_local_33()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_36():
                            _hx_local_34 = self
                            _hx_local_35 = _hx_local_34.uid
                            _hx_local_34.uid = (_hx_local_35 + 1)
                            return _hx_local_35
                        id1 = ("_r" + Std.string(_hx_local_36()))
                        def _hx_local_39():
                            _hx_local_37 = self
                            _hx_local_38 = _hx_local_37.uid
                            _hx_local_37.uid = (_hx_local_38 + 1)
                            return _hx_local_38
                        id2 = ("_r" + Std.string(_hx_local_39()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_42():
                            _hx_local_40 = self
                            _hx_local_41 = _hx_local_40.uid
                            _hx_local_40.uid = (_hx_local_41 + 1)
                            return _hx_local_41
                        idArr = ("_r" + Std.string(_hx_local_42()))
                        def _hx_local_45():
                            _hx_local_43 = self
                            _hx_local_44 = _hx_local_43.uid
                            _hx_local_43.uid = (_hx_local_44 + 1)
                            return _hx_local_44
                        idIndex = ("_r" + Std.string(_hx_local_45()))
                        def _hx_local_48():
                            _hx_local_46 = self
                            _hx_local_47 = _hx_local_46.uid
                            _hx_local_46.uid = (_hx_local_47 + 1)
                            return _hx_local_47
                        idVal = ("_r" + Std.string(_hx_local_48()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "&="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_51():
                            _hx_local_49 = self
                            _hx_local_50 = _hx_local_49.uid
                            _hx_local_49.uid = (_hx_local_50 + 1)
                            return _hx_local_50
                        id = ("_r" + Std.string(_hx_local_51()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_54():
                            _hx_local_52 = self
                            _hx_local_53 = _hx_local_52.uid
                            _hx_local_52.uid = (_hx_local_53 + 1)
                            return _hx_local_53
                        id1 = ("_r" + Std.string(_hx_local_54()))
                        def _hx_local_57():
                            _hx_local_55 = self
                            _hx_local_56 = _hx_local_55.uid
                            _hx_local_55.uid = (_hx_local_56 + 1)
                            return _hx_local_56
                        id2 = ("_r" + Std.string(_hx_local_57()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_60():
                            _hx_local_58 = self
                            _hx_local_59 = _hx_local_58.uid
                            _hx_local_58.uid = (_hx_local_59 + 1)
                            return _hx_local_59
                        idArr = ("_r" + Std.string(_hx_local_60()))
                        def _hx_local_63():
                            _hx_local_61 = self
                            _hx_local_62 = _hx_local_61.uid
                            _hx_local_61.uid = (_hx_local_62 + 1)
                            return _hx_local_62
                        idIndex = ("_r" + Std.string(_hx_local_63()))
                        def _hx_local_66():
                            _hx_local_64 = self
                            _hx_local_65 = _hx_local_64.uid
                            _hx_local_64.uid = (_hx_local_65 + 1)
                            return _hx_local_65
                        idVal = ("_r" + Std.string(_hx_local_66()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "*="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_69():
                            _hx_local_67 = self
                            _hx_local_68 = _hx_local_67.uid
                            _hx_local_67.uid = (_hx_local_68 + 1)
                            return _hx_local_68
                        id = ("_r" + Std.string(_hx_local_69()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_72():
                            _hx_local_70 = self
                            _hx_local_71 = _hx_local_70.uid
                            _hx_local_70.uid = (_hx_local_71 + 1)
                            return _hx_local_71
                        id1 = ("_r" + Std.string(_hx_local_72()))
                        def _hx_local_75():
                            _hx_local_73 = self
                            _hx_local_74 = _hx_local_73.uid
                            _hx_local_73.uid = (_hx_local_74 + 1)
                            return _hx_local_74
                        id2 = ("_r" + Std.string(_hx_local_75()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_78():
                            _hx_local_76 = self
                            _hx_local_77 = _hx_local_76.uid
                            _hx_local_76.uid = (_hx_local_77 + 1)
                            return _hx_local_77
                        idArr = ("_r" + Std.string(_hx_local_78()))
                        def _hx_local_81():
                            _hx_local_79 = self
                            _hx_local_80 = _hx_local_79.uid
                            _hx_local_79.uid = (_hx_local_80 + 1)
                            return _hx_local_80
                        idIndex = ("_r" + Std.string(_hx_local_81()))
                        def _hx_local_84():
                            _hx_local_82 = self
                            _hx_local_83 = _hx_local_82.uid
                            _hx_local_82.uid = (_hx_local_83 + 1)
                            return _hx_local_83
                        idVal = ("_r" + Std.string(_hx_local_84()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "+="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_87():
                            _hx_local_85 = self
                            _hx_local_86 = _hx_local_85.uid
                            _hx_local_85.uid = (_hx_local_86 + 1)
                            return _hx_local_86
                        id = ("_r" + Std.string(_hx_local_87()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_90():
                            _hx_local_88 = self
                            _hx_local_89 = _hx_local_88.uid
                            _hx_local_88.uid = (_hx_local_89 + 1)
                            return _hx_local_89
                        id1 = ("_r" + Std.string(_hx_local_90()))
                        def _hx_local_93():
                            _hx_local_91 = self
                            _hx_local_92 = _hx_local_91.uid
                            _hx_local_91.uid = (_hx_local_92 + 1)
                            return _hx_local_92
                        id2 = ("_r" + Std.string(_hx_local_93()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_96():
                            _hx_local_94 = self
                            _hx_local_95 = _hx_local_94.uid
                            _hx_local_94.uid = (_hx_local_95 + 1)
                            return _hx_local_95
                        idArr = ("_r" + Std.string(_hx_local_96()))
                        def _hx_local_99():
                            _hx_local_97 = self
                            _hx_local_98 = _hx_local_97.uid
                            _hx_local_97.uid = (_hx_local_98 + 1)
                            return _hx_local_98
                        idIndex = ("_r" + Std.string(_hx_local_99()))
                        def _hx_local_102():
                            _hx_local_100 = self
                            _hx_local_101 = _hx_local_100.uid
                            _hx_local_100.uid = (_hx_local_101 + 1)
                            return _hx_local_101
                        idVal = ("_r" + Std.string(_hx_local_102()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "-="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_105():
                            _hx_local_103 = self
                            _hx_local_104 = _hx_local_103.uid
                            _hx_local_103.uid = (_hx_local_104 + 1)
                            return _hx_local_104
                        id = ("_r" + Std.string(_hx_local_105()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_108():
                            _hx_local_106 = self
                            _hx_local_107 = _hx_local_106.uid
                            _hx_local_106.uid = (_hx_local_107 + 1)
                            return _hx_local_107
                        id1 = ("_r" + Std.string(_hx_local_108()))
                        def _hx_local_111():
                            _hx_local_109 = self
                            _hx_local_110 = _hx_local_109.uid
                            _hx_local_109.uid = (_hx_local_110 + 1)
                            return _hx_local_110
                        id2 = ("_r" + Std.string(_hx_local_111()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_114():
                            _hx_local_112 = self
                            _hx_local_113 = _hx_local_112.uid
                            _hx_local_112.uid = (_hx_local_113 + 1)
                            return _hx_local_113
                        idArr = ("_r" + Std.string(_hx_local_114()))
                        def _hx_local_117():
                            _hx_local_115 = self
                            _hx_local_116 = _hx_local_115.uid
                            _hx_local_115.uid = (_hx_local_116 + 1)
                            return _hx_local_116
                        idIndex = ("_r" + Std.string(_hx_local_117()))
                        def _hx_local_120():
                            _hx_local_118 = self
                            _hx_local_119 = _hx_local_118.uid
                            _hx_local_118.uid = (_hx_local_119 + 1)
                            return _hx_local_119
                        idVal = ("_r" + Std.string(_hx_local_120()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "/="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_123():
                            _hx_local_121 = self
                            _hx_local_122 = _hx_local_121.uid
                            _hx_local_121.uid = (_hx_local_122 + 1)
                            return _hx_local_122
                        id = ("_r" + Std.string(_hx_local_123()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_126():
                            _hx_local_124 = self
                            _hx_local_125 = _hx_local_124.uid
                            _hx_local_124.uid = (_hx_local_125 + 1)
                            return _hx_local_125
                        id1 = ("_r" + Std.string(_hx_local_126()))
                        def _hx_local_129():
                            _hx_local_127 = self
                            _hx_local_128 = _hx_local_127.uid
                            _hx_local_127.uid = (_hx_local_128 + 1)
                            return _hx_local_128
                        id2 = ("_r" + Std.string(_hx_local_129()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_132():
                            _hx_local_130 = self
                            _hx_local_131 = _hx_local_130.uid
                            _hx_local_130.uid = (_hx_local_131 + 1)
                            return _hx_local_131
                        idArr = ("_r" + Std.string(_hx_local_132()))
                        def _hx_local_135():
                            _hx_local_133 = self
                            _hx_local_134 = _hx_local_133.uid
                            _hx_local_133.uid = (_hx_local_134 + 1)
                            return _hx_local_134
                        idIndex = ("_r" + Std.string(_hx_local_135()))
                        def _hx_local_138():
                            _hx_local_136 = self
                            _hx_local_137 = _hx_local_136.uid
                            _hx_local_136.uid = (_hx_local_137 + 1)
                            return _hx_local_137
                        idVal = ("_r" + Std.string(_hx_local_138()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "^="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_141():
                            _hx_local_139 = self
                            _hx_local_140 = _hx_local_139.uid
                            _hx_local_139.uid = (_hx_local_140 + 1)
                            return _hx_local_140
                        id = ("_r" + Std.string(_hx_local_141()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_144():
                            _hx_local_142 = self
                            _hx_local_143 = _hx_local_142.uid
                            _hx_local_142.uid = (_hx_local_143 + 1)
                            return _hx_local_143
                        id1 = ("_r" + Std.string(_hx_local_144()))
                        def _hx_local_147():
                            _hx_local_145 = self
                            _hx_local_146 = _hx_local_145.uid
                            _hx_local_145.uid = (_hx_local_146 + 1)
                            return _hx_local_146
                        id2 = ("_r" + Std.string(_hx_local_147()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_150():
                            _hx_local_148 = self
                            _hx_local_149 = _hx_local_148.uid
                            _hx_local_148.uid = (_hx_local_149 + 1)
                            return _hx_local_149
                        idArr = ("_r" + Std.string(_hx_local_150()))
                        def _hx_local_153():
                            _hx_local_151 = self
                            _hx_local_152 = _hx_local_151.uid
                            _hx_local_151.uid = (_hx_local_152 + 1)
                            return _hx_local_152
                        idIndex = ("_r" + Std.string(_hx_local_153()))
                        def _hx_local_156():
                            _hx_local_154 = self
                            _hx_local_155 = _hx_local_154.uid
                            _hx_local_154.uid = (_hx_local_155 + 1)
                            return _hx_local_155
                        idVal = ("_r" + Std.string(_hx_local_156()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "|="):
                    tmp = e1.index
                    if (tmp == 1):
                        _g = e1.params[0]
                        def _hx_local_159():
                            _hx_local_157 = self
                            _hx_local_158 = _hx_local_157.uid
                            _hx_local_157.uid = (_hx_local_158 + 1)
                            return _hx_local_158
                        id = ("_r" + Std.string(_hx_local_159()))
                        return self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,e1,hscript_Expr.EIdent(id))]),None),exit)
                    elif (tmp == 5):
                        ef1 = e1.params[0]
                        f = e1.params[1]
                        def _hx_local_162():
                            _hx_local_160 = self
                            _hx_local_161 = _hx_local_160.uid
                            _hx_local_160.uid = (_hx_local_161 + 1)
                            return _hx_local_161
                        id1 = ("_r" + Std.string(_hx_local_162()))
                        def _hx_local_165():
                            _hx_local_163 = self
                            _hx_local_164 = _hx_local_163.uid
                            _hx_local_163.uid = (_hx_local_164 + 1)
                            return _hx_local_164
                        id2 = ("_r" + Std.string(_hx_local_165()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EField(hscript_Expr.EIdent(id1),f),hscript_Expr.EIdent(id2))]),None),exit)
                        return self.toCps(ef1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                    elif (tmp == 16):
                        earr = e1.params[0]
                        eindex = e1.params[1]
                        def _hx_local_168():
                            _hx_local_166 = self
                            _hx_local_167 = _hx_local_166.uid
                            _hx_local_166.uid = (_hx_local_167 + 1)
                            return _hx_local_167
                        idArr = ("_r" + Std.string(_hx_local_168()))
                        def _hx_local_171():
                            _hx_local_169 = self
                            _hx_local_170 = _hx_local_169.uid
                            _hx_local_169.uid = (_hx_local_170 + 1)
                            return _hx_local_170
                        idIndex = ("_r" + Std.string(_hx_local_171()))
                        def _hx_local_174():
                            _hx_local_172 = self
                            _hx_local_173 = _hx_local_172.uid
                            _hx_local_172.uid = (_hx_local_173 + 1)
                            return _hx_local_173
                        idVal = ("_r" + Std.string(_hx_local_174()))
                        e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': idVal, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EArray(hscript_Expr.EIdent(idArr),hscript_Expr.EIdent(idIndex)),hscript_Expr.EIdent(idVal))]),None),exit)
                        e4 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': idIndex, 't': None})],e3,None),exit)
                        return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': idArr, 't': None})],e4,None),exit)
                    else:
                        raise haxe_Exception.thrown(("assert " + Std.string(e1)))
                elif (op1 == "||"):
                    def _hx_local_177():
                        _hx_local_175 = self
                        _hx_local_176 = _hx_local_175.uid
                        _hx_local_175.uid = (_hx_local_176 + 1)
                        return _hx_local_176
                    id1 = ("_r" + Std.string(_hx_local_177()))
                    def _hx_local_180():
                        _hx_local_178 = self
                        _hx_local_179 = _hx_local_178.uid
                        _hx_local_178.uid = (_hx_local_179 + 1)
                        return _hx_local_179
                    id2 = ("_r" + Std.string(_hx_local_180()))
                    e3 = hscript_Expr.EIf(hscript_Expr.EBinop("==",hscript_Expr.EIdent(id1),hscript_Expr.EIdent("true")),hscript_Expr.ECall(rest,[hscript_Expr.EIdent("true")]),self.toCps(e2,rest,exit))
                    return self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
                else:
                    def _hx_local_183():
                        _hx_local_181 = self
                        _hx_local_182 = _hx_local_181.uid
                        _hx_local_181.uid = (_hx_local_182 + 1)
                        return _hx_local_182
                    id1 = ("_r" + Std.string(_hx_local_183()))
                    def _hx_local_186():
                        _hx_local_184 = self
                        _hx_local_185 = _hx_local_184.uid
                        _hx_local_184.uid = (_hx_local_185 + 1)
                        return _hx_local_185
                    id2 = ("_r" + Std.string(_hx_local_186()))
                    e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EIdent(id1),hscript_Expr.EIdent(id2))]),None),exit)
                    return self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
            else:
                def _hx_local_189():
                    _hx_local_187 = self
                    _hx_local_188 = _hx_local_187.uid
                    _hx_local_187.uid = (_hx_local_188 + 1)
                    return _hx_local_188
                id1 = ("_r" + Std.string(_hx_local_189()))
                def _hx_local_192():
                    _hx_local_190 = self
                    _hx_local_191 = _hx_local_190.uid
                    _hx_local_190.uid = (_hx_local_191 + 1)
                    return _hx_local_191
                id2 = ("_r" + Std.string(_hx_local_192()))
                e3 = self.toCps(e2,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EBinop(op,hscript_Expr.EIdent(id1),hscript_Expr.EIdent(id2))]),None),exit)
                return self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e3,None),exit)
        elif (tmp == 7):
            _g = e.params[0]
            if (_g == "!"):
                op = _g
                prefix = e.params[1]
                eop = e.params[2]
                return self.toCps(eop,hscript_Expr.EFunction([_hx_AnonObject({'name': "_r", 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EUnop(op,prefix,hscript_Expr.EIdent("_r"))]),None),exit)
            else:
                return hscript_Expr.ECall(rest,[e])
        elif (tmp == 8):
            _g = e.params[1]
            _hx_tmp = e.params[0]
            tmp = _hx_tmp.index
            if (tmp == 1):
                i = _hx_tmp.params[0]
                args = _g
                mode = self.vars.h.get(i,None)
                return self.makeCall(hscript_Expr.EIdent((i if ((mode is not None)) else ("a_" + ("null" if i is None else i)))),args,rest,exit,(mode == hscript_VarMode.ForceSync))
            elif (tmp == 5):
                e1 = _hx_tmp.params[0]
                f = _hx_tmp.params[1]
                args = _g
                return self.makeCall(hscript_Expr.EField(e1,("a_" + ("null" if f is None else f))),args,rest,exit)
            else:
                raise haxe_Exception.thrown(("Unsupported async expression " + HxOverrides.stringOrNull(hscript_Printer.toString(e))))
        elif (tmp == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            e3 = self.toCps(e1,rest,exit)
            e1 = (self.retNull(rest) if ((e2 is None)) else self.toCps(e2,rest,exit))
            return self.toCps(cond,hscript_Expr.EFunction([_hx_AnonObject({'name': "_c", 't': None})],hscript_Expr.EIf(hscript_Expr.EIdent("_c"),e3,e1),None),exit)
        elif (tmp == 10):
            cond = e.params[0]
            ewh = e.params[1]
            self.uid = (self.uid + 1)
            id = self.uid
            loop = hscript_Expr.EIdent(("_loop" + Std.string(id)))
            oldLoop = self.currentLoop
            oldBreak = self.currentBreak
            self.currentLoop = loop
            def _hx_local_193(e):
                arr = [_gthis.retNull(rest,e), hscript_Expr.EReturn()]
                tmp = None
                if (len(arr) == 1):
                    _g = (arr[0] if 0 < len(arr) else None)
                    if (_g.index == 4):
                        _g1 = _g.params[0]
                        tmp = True
                    else:
                        tmp = False
                else:
                    tmp = False
                if tmp:
                    return (arr[0] if 0 < len(arr) else None)
                else:
                    return hscript_Expr.EBlock(arr)
            self.currentBreak = _hx_local_193
            e1 = hscript_Expr.EIf(hscript_Expr.EIdent("_c"),self.toCps(ewh,loop,exit),self.retNull(rest,cond))
            e2 = self.toCps(cond,hscript_Expr.EFunction([_hx_AnonObject({'name': "_c", 't': None})],e1,None),exit)
            arr = self.retNull(loop,cond)
            arr1 = [hscript_Expr.EFunction([_hx_AnonObject({'name': "_r", 't': None})],e2,("_loop" + Std.string(id))), arr]
            ewhile = None
            if (len(arr1) == 1):
                _g = (arr1[0] if 0 < len(arr1) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    ewhile = True
                else:
                    ewhile = False
            else:
                ewhile = False
            ewhile1 = ((arr1[0] if 0 < len(arr1) else None) if ewhile else hscript_Expr.EBlock(arr1))
            self.currentLoop = oldLoop
            self.currentBreak = oldBreak
            return ewhile1
        elif (tmp == 11):
            v = e.params[0]
            eit = e.params[1]
            eloop = e.params[2]
            self.uid = (self.uid + 1)
            id = self.uid
            it = hscript_Expr.EIdent(("_i" + Std.string(id)))
            oldLoop = self.currentLoop
            oldBreak = self.currentBreak
            loop = hscript_Expr.EIdent(("_loop" + Std.string(id)))
            self.currentLoop = loop
            def _hx_local_194(inf):
                arr = [_gthis.retNull(rest,inf), hscript_Expr.EReturn()]
                tmp = None
                if (len(arr) == 1):
                    _g = (arr[0] if 0 < len(arr) else None)
                    if (_g.index == 4):
                        _g1 = _g.params[0]
                        tmp = True
                    else:
                        tmp = False
                else:
                    tmp = False
                if tmp:
                    return (arr[0] if 0 < len(arr) else None)
                else:
                    return hscript_Expr.EBlock(arr)
            self.currentBreak = _hx_local_194
            arr = [hscript_Expr.EIf(hscript_Expr.EUnop("!",True,hscript_Expr.ECall(hscript_Expr.EField(it,"hasNext"),[])),self.currentBreak(it)), hscript_Expr.EVar(v,None,hscript_Expr.ECall(hscript_Expr.EField(it,"next"),[])), self.toCps(eloop,loop,exit)]
            e1 = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    e1 = True
                else:
                    e1 = False
            else:
                e1 = False
            e2 = ((arr[0] if 0 < len(arr) else None) if e1 else hscript_Expr.EBlock(arr))
            arr = self.retNull(loop,e)
            arr1 = [hscript_Expr.EVar(("_i" + Std.string(id)),None,hscript_Expr.ECall(hscript_Expr.EIdent("makeIterator"),[eit])), hscript_Expr.EFunction([_hx_AnonObject({'name': "_", 't': None})],e2,("_loop" + Std.string(id))), arr]
            efor = None
            if (len(arr1) == 1):
                _g = (arr1[0] if 0 < len(arr1) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    efor = True
                else:
                    efor = False
            else:
                efor = False
            efor1 = ((arr1[0] if 0 < len(arr1) else None) if efor else hscript_Expr.EBlock(arr1))
            self.currentLoop = oldLoop
            self.currentBreak = oldBreak
            return efor1
        elif (tmp == 12):
            if (self.currentBreak is None):
                raise haxe_Exception.thrown("Break outside loop")
            return self.currentBreak(e)
        elif (tmp == 13):
            if (self.currentLoop is None):
                raise haxe_Exception.thrown("Continue outside loop")
            arr = [self.retNull(self.currentLoop,e), hscript_Expr.EReturn()]
            tmp = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if tmp:
                return (arr[0] if 0 < len(arr) else None)
            else:
                return hscript_Expr.EBlock(arr)
        elif (tmp == 14):
            args = e.params[0]
            body = e.params[1]
            name = e.params[2]
            t = e.params[3]
            vold = self.saveVars()
            if (name is not None):
                self.defineVar(name,hscript_VarMode.Defined)
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                self.defineVar(a.name,hscript_VarMode.Defined)
            args.insert(0, _hx_AnonObject({'name': "_onEnd", 't': None}))
            frest = hscript_Expr.EIdent("_onEnd")
            oldFun = self.currentFun
            self.currentFun = name
            body1 = self.toCps(body,frest,frest)
            f = hscript_Expr.EFunction(args,body1,name,t)
            self.restoreVars(vold)
            if (rest is None):
                return f
            else:
                return hscript_Expr.ECall(rest,[f])
        elif (tmp == 15):
            eret = e.params[0]
            if (eret is None):
                return self.retNull(exit,e)
            else:
                return self.toCps(eret,exit,exit)
        elif (tmp == 16):
            earr = e.params[0]
            eindex = e.params[1]
            def _hx_local_198():
                _hx_local_196 = self
                _hx_local_197 = _hx_local_196.uid
                _hx_local_196.uid = (_hx_local_197 + 1)
                return _hx_local_197
            id1 = ("_r" + Std.string(_hx_local_198()))
            def _hx_local_201():
                _hx_local_199 = self
                _hx_local_200 = _hx_local_199.uid
                _hx_local_199.uid = (_hx_local_200 + 1)
                return _hx_local_200
            id2 = ("_r" + Std.string(_hx_local_201()))
            e1 = self.toCps(eindex,hscript_Expr.EFunction([_hx_AnonObject({'name': id2, 't': None})],hscript_Expr.ECall(rest,[hscript_Expr.EArray(hscript_Expr.EIdent(id1),hscript_Expr.EIdent(id2))]),None),exit)
            return self.toCps(earr,hscript_Expr.EFunction([_hx_AnonObject({'name': id1, 't': None})],e1,None),exit)
        elif (tmp == 17):
            el = e.params[0]
            def _hx_local_204():
                _hx_local_202 = self
                _hx_local_203 = _hx_local_202.uid
                _hx_local_202.uid = (_hx_local_203 + 1)
                return _hx_local_203
            id = ("_a" + Std.string(_hx_local_204()))
            rest1 = hscript_Expr.ECall(rest,[hscript_Expr.EIdent(id)])
            i = (len(el) - 1)
            while (i >= 0):
                e1 = (el[i] if i >= 0 and i < len(el) else None)
                arr = [hscript_Expr.EBinop("=",hscript_Expr.EArray(hscript_Expr.EIdent(id),hscript_Expr.EConst(hscript_Const.CInt(i))),hscript_Expr.EIdent("_r")), rest1]
                e2 = None
                if (len(arr) == 1):
                    _g = (arr[0] if 0 < len(arr) else None)
                    if (_g.index == 4):
                        _g1 = _g.params[0]
                        e2 = True
                    else:
                        e2 = False
                else:
                    e2 = False
                rest1 = self.toCps(e1,hscript_Expr.EFunction([_hx_AnonObject({'name': "_r", 't': None})],((arr[0] if 0 < len(arr) else None) if e2 else hscript_Expr.EBlock(arr)),None),exit)
                i = (i - 1)
            arr = [hscript_Expr.EVar(id,None,hscript_Expr.EArrayDecl([])), rest1]
            tmp = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if tmp:
                return (arr[0] if 0 < len(arr) else None)
            else:
                return hscript_Expr.EBlock(arr)
        elif (tmp == 18):
            cl = e.params[0]
            args = e.params[1]
            _g = []
            _g1 = 0
            _g2 = len(args)
            while (_g1 < _g2):
                i = _g1
                _g1 = (_g1 + 1)
                def _hx_local_208():
                    _hx_local_206 = self
                    _hx_local_207 = _hx_local_206.uid
                    _hx_local_206.uid = (_hx_local_207 + 1)
                    return _hx_local_207
                x = ("_a" + Std.string(_hx_local_208()))
                _g.append(x)
            names = _g
            _g = []
            _g1 = 0
            _g2 = len(args)
            while (_g1 < _g2):
                i = _g1
                _g1 = (_g1 + 1)
                x = hscript_Expr.EIdent((names[i] if i >= 0 and i < len(names) else None))
                _g.append(x)
            rargs = _g
            rest1 = hscript_Expr.ECall(rest,[hscript_Expr.ENew(cl,rargs)])
            i = (len(args) - 1)
            while (i >= 0):
                rest1 = self.toCps((args[i] if i >= 0 and i < len(args) else None),hscript_Expr.EFunction([_hx_AnonObject({'name': (names[i] if i >= 0 and i < len(names) else None), 't': None})],rest1,None),exit)
                i = (i - 1)
            return rest1
        elif (tmp == 19):
            v = e.params[0]
            return self.toCps(v,hscript_Expr.EFunction([_hx_AnonObject({'name': "_v", 't': None})],hscript_Expr.EThrow(v)),exit)
        elif (tmp == 21):
            fields = e.params[0]
            def _hx_local_212():
                _hx_local_210 = self
                _hx_local_211 = _hx_local_210.uid
                _hx_local_210.uid = (_hx_local_211 + 1)
                return _hx_local_211
            id = ("_o" + Std.string(_hx_local_212()))
            rest1 = hscript_Expr.ECall(rest,[hscript_Expr.EIdent(id)])
            fields.reverse()
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                e1 = f.e
                e2 = f.e
                inf = f.e
                arr = [hscript_Expr.EBinop("=",hscript_Expr.EField(hscript_Expr.EIdent(id),f.name),hscript_Expr.EIdent("_r")), rest1]
                e3 = f.e
                e4 = None
                if (len(arr) == 1):
                    _g1 = (arr[0] if 0 < len(arr) else None)
                    if (_g1.index == 4):
                        _g2 = _g1.params[0]
                        e4 = True
                    else:
                        e4 = False
                else:
                    e4 = False
                rest1 = self.toCps(f.e,hscript_Expr.EFunction([_hx_AnonObject({'name': "_r", 't': None})],((arr[0] if 0 < len(arr) else None) if e4 else hscript_Expr.EBlock(arr)),None),exit)
            arr = [hscript_Expr.EVar(id,None,hscript_Expr.EObject([])), rest1]
            tmp = None
            if (len(arr) == 1):
                _g = (arr[0] if 0 < len(arr) else None)
                if (_g.index == 4):
                    _g1 = _g.params[0]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if tmp:
                return (arr[0] if 0 < len(arr) else None)
            else:
                return hscript_Expr.EBlock(arr)
        elif (tmp == 22):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            e3 = self.toCps(e1,rest,exit)
            e1 = (self.retNull(rest) if ((e2 is None)) else self.toCps(e2,rest,exit))
            return self.toCps(cond,hscript_Expr.EFunction([_hx_AnonObject({'name': "_c", 't': None})],hscript_Expr.EIf(hscript_Expr.EIdent("_c"),e3,e1),None),exit)
        elif (tmp == 23):
            v = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            _g = []
            _g1 = 0
            while (_g1 < len(cases)):
                c = (cases[_g1] if _g1 >= 0 and _g1 < len(cases) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'values': c.values, 'expr': self.toCps(c.expr,rest,exit)})
                _g.append(x)
            cases = _g
            e1 = (self.retNull(rest) if ((_hx_def is None)) else self.toCps(_hx_def,rest,exit))
            return self.toCps(v,hscript_Expr.EFunction([_hx_AnonObject({'name': "_c", 't': None})],hscript_Expr.ESwitch(hscript_Expr.EIdent("_c"),cases,e1)),exit)
        elif (tmp == 25):
            _g = e.params[0]
            _g1 = e.params[1]
            _g1 = e.params[2]
            _g2 = _g
            _hx_local_215 = len(_g2)
            if (_hx_local_215 == 5):
                if (_g2 == "async"):
                    e1 = _g1
                    nothing = self.ignore()
                    arr = [self.toCps(e1,nothing,nothing), self.retNull(rest)]
                    tmp = None
                    if (len(arr) == 1):
                        _g2 = (arr[0] if 0 < len(arr) else None)
                        if (_g2.index == 4):
                            _g3 = _g2.params[0]
                            tmp = True
                        else:
                            tmp = False
                    else:
                        tmp = False
                    if tmp:
                        return (arr[0] if 0 < len(arr) else None)
                    else:
                        return hscript_Expr.EBlock(arr)
                elif (_g2 == "split"):
                    e1 = _g1
                    args = None
                    if (e1.index == 17):
                        el = e1.params[0]
                        args = el
                    else:
                        raise haxe_Exception.thrown("@split expression should be an array")
                    _g2 = []
                    _g3 = 0
                    while (_g3 < len(args)):
                        a = (args[_g3] if _g3 >= 0 and _g3 < len(args) else None)
                        _g3 = (_g3 + 1)
                        arr = [a]
                        e1 = None
                        if (len(arr) == 1):
                            _g4 = (arr[0] if 0 < len(arr) else None)
                            if (_g4.index == 4):
                                _g5 = _g4.params[0]
                                e1 = True
                            else:
                                e1 = False
                        else:
                            e1 = False
                        e2 = self.toCps(((arr[0] if 0 < len(arr) else None) if e1 else hscript_Expr.EBlock(arr)),hscript_Expr.EIdent("_rest"),exit)
                        _g2.append(hscript_Expr.EFunction([_hx_AnonObject({'name': "_rest", 't': None})],e2,None))
                    args = _g2
                    return hscript_Expr.ECall(hscript_Expr.EIdent("split"),[rest, hscript_Expr.EArrayDecl(args)])
                else:
                    name = _g
                    e1 = _g1
                    if (HxString.charCodeAt(name,0) == 58):
                        return self.toCps(e1,rest,exit)
                    else:
                        raise haxe_Exception.thrown(("Unsupported async expression " + HxOverrides.stringOrNull(hscript_Printer.toString(e))))
            elif (_hx_local_215 == 4):
                if (_g2 == "sync"):
                    e1 = _g1
                    args = [self.buildSync(e1,exit)]
                    return hscript_Expr.ECall(rest,args)
                else:
                    name = _g
                    e1 = _g1
                    if (HxString.charCodeAt(name,0) == 58):
                        return self.toCps(e1,rest,exit)
                    else:
                        raise haxe_Exception.thrown(("Unsupported async expression " + HxOverrides.stringOrNull(hscript_Printer.toString(e))))
            else:
                name = _g
                e1 = _g1
                if (HxString.charCodeAt(name,0) == 58):
                    return self.toCps(e1,rest,exit)
                else:
                    raise haxe_Exception.thrown(("Unsupported async expression " + HxOverrides.stringOrNull(hscript_Printer.toString(e))))
        else:
            raise haxe_Exception.thrown(("Unsupported async expression " + HxOverrides.stringOrNull(hscript_Printer.toString(e))))

    @staticmethod
    def expr(e):
        return e

    @staticmethod
    def mk(e,inf):
        return e

    @staticmethod
    def toAsync(e,topLevelSync = None):
        if (topLevelSync is None):
            topLevelSync = False
        a = hscript_Async()
        return a.build(e,topLevelSync)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.definedVars = None
        _hx_o.vars = None
        _hx_o.currentFun = None
        _hx_o.currentLoop = None
        _hx_o.currentBreak = None
        _hx_o.uid = None
        _hx_o.asyncIdents = None
        _hx_o.syncFlag = None
hscript_Async._hx_class = hscript_Async
_hx_classes["hscript.Async"] = hscript_Async


