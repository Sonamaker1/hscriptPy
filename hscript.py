from _hx_AnonObject import _hx_AnonObject
import globalClasses
import sys
import _hx_AnonObject as anon
from classes_hscript import Enum, HxOverrides, HxString, Int, IntIterator, Lambda, Reflect, Std, StringBuf, Type 
import math as Math


from haxe import haxe_ds_EnumValueMap, haxe_ds_GenericCell, haxe_ds_GenericStack, haxe_ds_IntMap, haxe_ds_ObjectMap, haxe_ds_StringMap, haxe_Exception, haxe_IMap, haxe_io_Bytes, haxe_io_BytesBuffer, haxe_Log, haxe_macro_Binop, haxe_macro_ComplexType, haxe_macro_Constant, haxe_macro_ExprDef, haxe_macro_FieldType, haxe_macro_FunctionKind, haxe_macro_TypeParam, haxe_macro_Unop, haxe_rtti_XmlParser
import math as Math

from classes_hscript import Enum

from python import python_Boot, python_internal_ArrayImpl
from io import StringIO as python_lib_io_StringIO
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
globalClasses._hx_classes["hscript.Async"] = hscript_Async

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
globalClasses._hx_classes["hscript.Interp"] = hscript_Interp

class hscript_AsyncInterp(hscript_Interp):
    _hx_class_name = "hscript.AsyncInterp"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["setContext", "hasMethod", "callValue", "callAsync", "split", "fcall"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hscript_Interp


    def __init__(self):
        super().__init__()

    def setContext(self,api):
        funs = list()
        v = self.variables.keys()
        while v.hasNext():
            v1 = v.next()
            if Reflect.isFunction(self.variables.h.get(v1,None)):
                funs.append(_hx_AnonObject({'v': v1, 'obj': None}))
        self.variables.h["split"] = self.split
        self.variables.h["makeIterator"] = self.makeIterator
        c = Type.getClass(api)
        _g = 0
        _g1 = (python_Boot.fields(api) if ((c is None)) else python_Boot.getInstanceFields(c))
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            fv = Reflect.field(api,f)
            if (not Reflect.isFunction(fv)):
                continue
            if (HxString.charCodeAt(f,0) == 95):
                f = HxString.substr(f,1,None)
            self.variables.h[f] = fv
            if (HxString.substr(f,0,2) != "a_"):
                funs.append(_hx_AnonObject({'v': f, 'obj': api}))
        _g = 0
        while (_g < len(funs)):
            v = (funs[_g] if _g >= 0 and _g < len(funs) else None)
            _g = (_g + 1)
            if (("a_" + HxOverrides.stringOrNull(v.v)) in self.variables.h):
                continue
            fv = [self.variables.h.get(v.v,None)]
            obj = [v.obj]
            this1 = self.variables
            key = ("a_" + HxOverrides.stringOrNull(v.v))
            def _hx_local_3(obj,fv):
                def _hx_local_2(args):
                    onEnd = (None if ((len(args) == 0)) else args.pop(0))
                    onEnd(Reflect.callMethod((obj[0] if 0 < len(obj) else None),(fv[0] if 0 < len(fv) else None),args))
                return _hx_local_2
            value = Reflect.makeVarArgs(_hx_local_3(obj,fv))
            this1.h[key] = value

    def hasMethod(self,name):
        v = self.variables.h.get(name,None)
        if (v is not None):
            return Reflect.isFunction(v)
        else:
            return False

    def callValue(self,value,args,onResult = None,vthis = None):
        oldThis = self.variables.h.get("this",None)
        if (vthis is not None):
            self.variables.h["this"] = vthis
        if (onResult is None):
            def _hx_local_0(_):
                pass
            onResult = _hx_local_0
        args.insert(0, onResult)
        Reflect.callMethod(None,value,args)
        self.variables.h["this"] = oldThis

    def callAsync(self,id,args,onResult = None,vthis = None):
        v = self.variables.h.get(id,None)
        if (v is None):
            raise haxe_Exception.thrown((("Missing function " + ("null" if id is None else id)) + "()"))
        self.callValue(v,args,onResult,vthis)

    def split(self,rest,args):
        if (len(args) == 0):
            rest(None)
        else:
            count = len(args)
            def _hx_local_2(_):
                def _hx_local_1():
                    nonlocal count
                    count = (count - 1)
                    return count
                if ((_hx_local_1()) == 0):
                    rest(None)
            next = _hx_local_2
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                a(next)

    def fcall(self,o,f,args):
        m = Reflect.field(o,f)
        if (m is None):
            if (HxString.substr(f,0,2) == "a_"):
                m = Reflect.field(o,HxString.substr(f,2,None))
                if (m is not None):
                    onEnd = (None if ((len(args) == 0)) else args.pop(0))
                    onEnd(self.call(o,m,args))
                    return None
                m = Reflect.field(o,"scriptCall")
                if (m is not None):
                    self.call(o,m,[(None if ((len(args) == 0)) else args.pop(0)), HxString.substr(f,2,None), args])
                    return None
            else:
                m = Reflect.field(o,"scriptCall")
                if (m is not None):
                    result = None
                    def _hx_local_0(r):
                        nonlocal result
                        result = r
                    self.call(o,m,[_hx_local_0, f, args])
                    return result
            e = hscript_Error.ECustom(((Std.string(o) + " has no method ") + ("null" if f is None else f)))
            raise haxe_Exception.thrown(e)
        return self.call(o,m,args)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
hscript_AsyncInterp._hx_class = hscript_AsyncInterp
globalClasses._hx_classes["hscript.AsyncInterp"] = hscript_AsyncInterp


class hscript_Bytes:
    _hx_class_name = "hscript.Bytes"
    __slots__ = ("bin", "bout", "pin", "hstrings", "strings", "nstrings")
    _hx_fields = ["bin", "bout", "pin", "hstrings", "strings", "nstrings"]
    _hx_methods = ["doEncodeString", "doDecodeString", "doEncodeInt", "doEncodeConst", "doDecodeInt", "doDecodeConst", "doEncode", "doDecode"]
    _hx_statics = ["encode", "decode"]

    def __init__(self,bin = None):
        self.bin = bin
        self.pin = 0
        self.bout = haxe_io_BytesBuffer()
        self.hstrings = haxe_ds_StringMap()
        self.strings = [None]
        self.nstrings = 1

    def doEncodeString(self,v):
        vid = self.hstrings.h.get(v,None)
        if (vid is None):
            if (self.nstrings == 256):
                self.hstrings = haxe_ds_StringMap()
                self.nstrings = 1
            self.hstrings.h[v] = self.nstrings
            self.bout.b.append(0)
            vb = haxe_io_Bytes.ofString(v)
            self.bout.b.append(vb.length)
            self.bout.b.extend(vb.b)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.nstrings
            _hx_local_0.nstrings = (_hx_local_1 + 1)
            _hx_local_1
        else:
            self.bout.b.append(vid)

    def doDecodeString(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        id = self.bin.b[pos]
        if (id == 0):
            _hx_len = self.bin.b[self.pin]
            _hx_str = self.bin.getString((self.pin + 1),_hx_len)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.pin
            _hx_local_0.pin = (_hx_local_1 + ((_hx_len + 1)))
            _hx_local_0.pin
            if (len(self.strings) == 255):
                self.strings = [None]
            _this = self.strings
            _this.append(_hx_str)
            return _hx_str
        return (self.strings[id] if id >= 0 and id < len(self.strings) else None)

    def doEncodeInt(self,v):
        self.bout.addInt32(v)

    def doEncodeConst(self,c):
        tmp = c.index
        if (tmp == 0):
            v = c.params[0]
            if ((v >= 0) and ((v <= 255))):
                self.bout.b.append(0)
                self.bout.b.append(v)
            else:
                self.bout.b.append(1)
                self.doEncodeInt(v)
        elif (tmp == 1):
            f = c.params[0]
            self.bout.b.append(2)
            self.doEncodeString(Std.string(f))
        elif (tmp == 2):
            s = c.params[0]
            self.bout.b.append(3)
            self.doEncodeString(s)
        else:
            pass

    def doDecodeInt(self):
        _this = self.bin
        pos = self.pin
        v = (((_this.b[pos] | ((_this.b[(pos + 1)] << 8))) | ((_this.b[(pos + 2)] << 16))) | ((_this.b[(pos + 3)] << 24)))
        i = ((v | -2147483648) if ((((v & -2147483648)) != 0)) else v)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.pin
        _hx_local_0.pin = (_hx_local_1 + 4)
        _hx_local_0.pin
        return i

    def doDecodeConst(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        _g = self.bin.b[pos]
        if (_g == 0):
            pos = self.pin
            self.pin = (self.pin + 1)
            return hscript_Const.CInt(self.bin.b[pos])
        elif (_g == 1):
            i = self.doDecodeInt()
            return hscript_Const.CInt(i)
        elif (_g == 2):
            return hscript_Const.CFloat(Std.parseFloat(self.doDecodeString()))
        elif (_g == 3):
            return hscript_Const.CString(self.doDecodeString())
        else:
            raise haxe_Exception.thrown(("Invalid code " + Std.string(self.bin.b[(self.pin - 1)])))

    def doEncode(self,e):
        self.bout.b.append(e.index)
        tmp = e.index
        if (tmp == 0):
            c = e.params[0]
            self.doEncodeConst(c)
        elif (tmp == 1):
            v = e.params[0]
            self.doEncodeString(v)
        elif (tmp == 2):
            _g = e.params[1]
            n = e.params[0]
            e1 = e.params[2]
            self.doEncodeString(n)
            if (e1 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            self.doEncode(e1)
        elif (tmp == 4):
            el = e.params[0]
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            self.doEncode(e1)
            self.doEncodeString(f)
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncodeString(op)
            self.doEncode(e1)
            self.doEncode(e2)
        elif (tmp == 7):
            op = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(op)
            self.bout.b.append((1 if prefix else 0))
            self.doEncode(e1)
        elif (tmp == 8):
            e1 = e.params[0]
            el = e.params[1]
            self.doEncode(e1)
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncode(cond)
            self.doEncode(e1)
            if (e2 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e2)
        elif (tmp == 10):
            cond = e.params[0]
            e1 = e.params[1]
            self.doEncode(cond)
            self.doEncode(e1)
        elif (tmp == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(v)
            self.doEncode(it)
            self.doEncode(e1)
        elif ((tmp == 13) or ((tmp == 12))):
            pass
        elif (tmp == 14):
            _g = e.params[3]
            params = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            self.bout.b.append(len(params))
            _g = 0
            while (_g < len(params)):
                p = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                self.doEncodeString(p.name)
            self.doEncode(e1)
            self.doEncodeString(("" if ((name is None)) else name))
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            self.doEncode(e1)
            self.doEncode(index)
        elif (tmp == 17):
            el = e.params[0]
            if (len(el) >= 255):
                raise haxe_Exception.thrown("assert")
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 18):
            cl = e.params[0]
            params = e.params[1]
            self.doEncodeString(cl)
            self.bout.b.append(len(params))
            _g = 0
            while (_g < len(params)):
                e1 = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 19):
            e1 = e.params[0]
            self.doEncode(e1)
        elif (tmp == 20):
            _g = e.params[2]
            e1 = e.params[0]
            v = e.params[1]
            ecatch = e.params[3]
            self.doEncode(e1)
            self.doEncodeString(v)
            self.doEncode(ecatch)
        elif (tmp == 21):
            fl = e.params[0]
            self.bout.b.append(len(fl))
            _g = 0
            while (_g < len(fl)):
                f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                self.doEncodeString(f.name)
                self.doEncode(f.e)
        elif (tmp == 22):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncode(cond)
            self.doEncode(e1)
            self.doEncode(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            self.doEncode(e1)
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                if (len(c.values) == 0):
                    raise haxe_Exception.thrown("assert")
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    self.doEncode(v)
                self.bout.b.append(255)
                self.doEncode(c.expr)
            self.bout.b.append(255)
            if (_hx_def is None):
                self.bout.b.append(255)
            else:
                self.doEncode(_hx_def)
        elif (tmp == 24):
            cond = e.params[0]
            e1 = e.params[1]
            self.doEncode(cond)
            self.doEncode(e1)
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(name)
            self.bout.b.append((0 if ((args is None)) else (len(args) + 1)))
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    e2 = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    self.doEncode(e2)
            self.doEncode(e1)
        elif (tmp == 26):
            _g = e.params[1]
            e1 = e.params[0]
            self.doEncode(e1)
        else:
            pass

    def doDecode(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        _g = self.bin.b[pos]
        if (_g == 0):
            return hscript_Expr.EConst(self.doDecodeConst())
        elif (_g == 1):
            return hscript_Expr.EIdent(self.doDecodeString())
        elif (_g == 2):
            v = self.doDecodeString()
            return hscript_Expr.EVar(v,None,self.doDecode())
        elif (_g == 3):
            return hscript_Expr.EParent(self.doDecode())
        elif (_g == 4):
            a = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                a.append(x)
            return hscript_Expr.EBlock(a)
        elif (_g == 5):
            e = self.doDecode()
            return hscript_Expr.EField(e,self.doDecodeString())
        elif (_g == 6):
            op = self.doDecodeString()
            e1 = self.doDecode()
            return hscript_Expr.EBinop(op,e1,self.doDecode())
        elif (_g == 7):
            op = self.doDecodeString()
            pos = self.pin
            self.pin = (self.pin + 1)
            prefix = (self.bin.b[pos] != 0)
            return hscript_Expr.EUnop(op,prefix,self.doDecode())
        elif (_g == 8):
            e = self.doDecode()
            params = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                params.append(x)
            return hscript_Expr.ECall(e,params)
        elif (_g == 9):
            cond = self.doDecode()
            e1 = self.doDecode()
            return hscript_Expr.EIf(cond,e1,self.doDecode())
        elif (_g == 10):
            cond = self.doDecode()
            return hscript_Expr.EWhile(cond,self.doDecode())
        elif (_g == 11):
            v = self.doDecodeString()
            it = self.doDecode()
            return hscript_Expr.EFor(v,it,self.doDecode())
        elif (_g == 12):
            return hscript_Expr.EBreak
        elif (_g == 13):
            return hscript_Expr.EContinue
        elif (_g == 14):
            params = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = _hx_AnonObject({'name': self.doDecodeString()})
                params.append(x)
            e = self.doDecode()
            name = self.doDecodeString()
            return hscript_Expr.EFunction(params,e,(None if ((name == "")) else name))
        elif (_g == 15):
            return hscript_Expr.EReturn(self.doDecode())
        elif (_g == 16):
            e = self.doDecode()
            return hscript_Expr.EArray(e,self.doDecode())
        elif (_g == 17):
            el = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                el.append(x)
            return hscript_Expr.EArrayDecl(el)
        elif (_g == 18):
            cl = self.doDecodeString()
            el = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                el.append(x)
            return hscript_Expr.ENew(cl,el)
        elif (_g == 19):
            return hscript_Expr.EThrow(self.doDecode())
        elif (_g == 20):
            e = self.doDecode()
            v = self.doDecodeString()
            return hscript_Expr.ETry(e,v,None,self.doDecode())
        elif (_g == 21):
            fl = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                name = self.doDecodeString()
                e = self.doDecode()
                fl.append(_hx_AnonObject({'name': name, 'e': e}))
            return hscript_Expr.EObject(fl)
        elif (_g == 22):
            cond = self.doDecode()
            e1 = self.doDecode()
            e2 = self.doDecode()
            return hscript_Expr.ETernary(cond,e1,e2)
        elif (_g == 23):
            e = self.doDecode()
            cases = []
            while True:
                v = self.doDecode()
                if (v is None):
                    break
                values = [v]
                while True:
                    v = self.doDecode()
                    if (v is None):
                        break
                    values.append(v)
                x = _hx_AnonObject({'values': values, 'expr': self.doDecode()})
                cases.append(x)
            _hx_def = self.doDecode()
            return hscript_Expr.ESwitch(e,cases,_hx_def)
        elif (_g == 24):
            cond = self.doDecode()
            return hscript_Expr.EDoWhile(cond,self.doDecode())
        elif (_g == 25):
            name = self.doDecodeString()
            pos = self.pin
            self.pin = (self.pin + 1)
            count = self.bin.b[pos]
            args = None
            if (count == 0):
                args = None
            else:
                _g = []
                _g1 = 0
                _g2 = (count - 1)
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    x = self.doDecode()
                    _g.append(x)
                args = _g
            return hscript_Expr.EMeta(name,args,self.doDecode())
        elif (_g == 26):
            return hscript_Expr.ECheckType(self.doDecode(),hscript_CType.CTPath(["Void"]))
        elif (_g == 255):
            return None
        else:
            raise haxe_Exception.thrown(("Invalid code " + Std.string(self.bin.b[(self.pin - 1)])))

    @staticmethod
    def encode(e):
        b = hscript_Bytes()
        b.doEncode(e)
        return b.bout.getBytes()

    @staticmethod
    def decode(_hx_bytes):
        b = hscript_Bytes(_hx_bytes)
        return b.doDecode()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bin = None
        _hx_o.bout = None
        _hx_o.pin = None
        _hx_o.hstrings = None
        _hx_o.strings = None
        _hx_o.nstrings = None
hscript_Bytes._hx_class = hscript_Bytes
globalClasses._hx_classes["hscript.Bytes"] = hscript_Bytes

class hscript_CType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.CType"
    _hx_constructs = ["CTPath", "CTFun", "CTAnon", "CTParent", "CTOpt", "CTNamed"]

    @staticmethod
    def CTPath(path,params = None):
        return hscript_CType("CTPath", 0, (path,params))

    @staticmethod
    def CTFun(args,ret):
        return hscript_CType("CTFun", 1, (args,ret))

    @staticmethod
    def CTAnon(fields):
        return hscript_CType("CTAnon", 2, (fields,))

    @staticmethod
    def CTParent(t):
        return hscript_CType("CTParent", 3, (t,))

    @staticmethod
    def CTOpt(t):
        return hscript_CType("CTOpt", 4, (t,))

    @staticmethod
    def CTNamed(n,t):
        return hscript_CType("CTNamed", 5, (n,t))
hscript_CType._hx_class = hscript_CType
globalClasses._hx_classes["hscript.CType"] = hscript_CType

class hscript_CTypedecl(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.CTypedecl"
    _hx_constructs = ["CTClass", "CTEnum", "CTTypedef", "CTAlias", "CTAbstract"]

    @staticmethod
    def CTClass(c):
        return hscript_CTypedecl("CTClass", 0, (c,))

    @staticmethod
    def CTEnum(e):
        return hscript_CTypedecl("CTEnum", 1, (e,))

    @staticmethod
    def CTTypedef(t):
        return hscript_CTypedecl("CTTypedef", 2, (t,))

    @staticmethod
    def CTAlias(t):
        return hscript_CTypedecl("CTAlias", 3, (t,))

    @staticmethod
    def CTAbstract(a):
        return hscript_CTypedecl("CTAbstract", 4, (a,))
hscript_CTypedecl._hx_class = hscript_CTypedecl
globalClasses._hx_classes["hscript.CTypedecl"] = hscript_CTypedecl


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
globalClasses._hx_classes["hscript.Checker"] = hscript_Checker

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
globalClasses._hx_classes["hscript.CheckerTypes"] = hscript_CheckerTypes


class hscript_Completion:
    _hx_class_name = "hscript.Completion"
    __slots__ = ("expr", "t")
    _hx_fields = ["expr", "t"]

    def __init__(self,expr,t):
        self.expr = expr
        self.t = t

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.expr = None
        _hx_o.t = None
hscript_Completion._hx_class = hscript_Completion
globalClasses._hx_classes["hscript.Completion"] = hscript_Completion


class hscript_Const(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Const"
    _hx_constructs = ["CInt", "CFloat", "CString"]

    @staticmethod
    def CInt(v):
        return hscript_Const("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return hscript_Const("CFloat", 1, (f,))

    @staticmethod
    def CString(s):
        return hscript_Const("CString", 2, (s,))
hscript_Const._hx_class = hscript_Const
globalClasses._hx_classes["hscript.Const"] = hscript_Const

class hscript_Error(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Error"
    _hx_constructs = ["EInvalidChar", "EUnexpected", "EUnterminatedString", "EUnterminatedComment", "EInvalidPreprocessor", "EUnknownVariable", "EInvalidIterator", "EInvalidOp", "EInvalidAccess", "ECustom"]

    @staticmethod
    def EInvalidChar(c):
        return hscript_Error("EInvalidChar", 0, (c,))

    @staticmethod
    def EUnexpected(s):
        return hscript_Error("EUnexpected", 1, (s,))

    @staticmethod
    def EInvalidPreprocessor(msg):
        return hscript_Error("EInvalidPreprocessor", 4, (msg,))

    @staticmethod
    def EUnknownVariable(v):
        return hscript_Error("EUnknownVariable", 5, (v,))

    @staticmethod
    def EInvalidIterator(v):
        return hscript_Error("EInvalidIterator", 6, (v,))

    @staticmethod
    def EInvalidOp(op):
        return hscript_Error("EInvalidOp", 7, (op,))

    @staticmethod
    def EInvalidAccess(f):
        return hscript_Error("EInvalidAccess", 8, (f,))

    @staticmethod
    def ECustom(msg):
        return hscript_Error("ECustom", 9, (msg,))
hscript_Error.EUnterminatedString = hscript_Error("EUnterminatedString", 2, ())
hscript_Error.EUnterminatedComment = hscript_Error("EUnterminatedComment", 3, ())
hscript_Error._hx_class = hscript_Error
globalClasses._hx_classes["hscript.Error"] = hscript_Error

class hscript_Expr(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Expr"
    _hx_constructs = ["EConst", "EIdent", "EVar", "EParent", "EBlock", "EField", "EBinop", "EUnop", "ECall", "EIf", "EWhile", "EFor", "EBreak", "EContinue", "EFunction", "EReturn", "EArray", "EArrayDecl", "ENew", "EThrow", "ETry", "EObject", "ETernary", "ESwitch", "EDoWhile", "EMeta", "ECheckType"]

    @staticmethod
    def EConst(c):
        return hscript_Expr("EConst", 0, (c,))

    @staticmethod
    def EIdent(v):
        return hscript_Expr("EIdent", 1, (v,))

    @staticmethod
    def EVar(n,t = None,e= None):
        return hscript_Expr("EVar", 2, (n,t,e))

    @staticmethod
    def EParent(e):
        return hscript_Expr("EParent", 3, (e,))

    @staticmethod
    def EBlock(e):
        return hscript_Expr("EBlock", 4, (e,))

    @staticmethod
    def EField(e,f):
        return hscript_Expr("EField", 5, (e,f))

    @staticmethod
    def EBinop(op,e1,e2):
        return hscript_Expr("EBinop", 6, (op,e1,e2))

    @staticmethod
    def EUnop(op,prefix,e):
        return hscript_Expr("EUnop", 7, (op,prefix,e))

    @staticmethod
    def ECall(e,params):
        return hscript_Expr("ECall", 8, (e,params))

    @staticmethod
    def EIf(cond,e1,e2 = None):
        return hscript_Expr("EIf", 9, (cond,e1,e2))

    @staticmethod
    def EWhile(cond,e):
        return hscript_Expr("EWhile", 10, (cond,e))

    @staticmethod
    def EFor(v,it,e):
        return hscript_Expr("EFor", 11, (v,it,e))

    @staticmethod
    def EFunction(args,e,name = None,ret= None):
        return hscript_Expr("EFunction", 14, (args,e,name,ret))

    @staticmethod
    def EReturn(e = None):
        return hscript_Expr("EReturn", 15, (e,))

    @staticmethod
    def EArray(e,index):
        return hscript_Expr("EArray", 16, (e,index))

    @staticmethod
    def EArrayDecl(e):
        return hscript_Expr("EArrayDecl", 17, (e,))

    @staticmethod
    def ENew(cl,params):
        return hscript_Expr("ENew", 18, (cl,params))

    @staticmethod
    def EThrow(e):
        return hscript_Expr("EThrow", 19, (e,))

    @staticmethod
    def ETry(e,v,t,ecatch):
        return hscript_Expr("ETry", 20, (e,v,t,ecatch))

    @staticmethod
    def EObject(fl):
        return hscript_Expr("EObject", 21, (fl,))

    @staticmethod
    def ETernary(cond,e1,e2):
        return hscript_Expr("ETernary", 22, (cond,e1,e2))

    @staticmethod
    def ESwitch(e,cases,defaultExpr = None):
        return hscript_Expr("ESwitch", 23, (e,cases,defaultExpr))

    @staticmethod
    def EDoWhile(cond,e):
        return hscript_Expr("EDoWhile", 24, (cond,e))

    @staticmethod
    def EMeta(name,args,e):
        return hscript_Expr("EMeta", 25, (name,args,e))

    @staticmethod
    def ECheckType(e,t):
        return hscript_Expr("ECheckType", 26, (e,t))
hscript_Expr.EBreak = hscript_Expr("EBreak", 12, ())
hscript_Expr.EContinue = hscript_Expr("EContinue", 13, ())
hscript_Expr._hx_class = hscript_Expr
globalClasses._hx_classes["hscript.Expr"] = hscript_Expr


class hscript_FieldAccess(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.FieldAccess"
    _hx_constructs = ["APublic", "APrivate", "AInline", "AOverride", "AStatic", "AMacro"]
hscript_FieldAccess.APublic = hscript_FieldAccess("APublic", 0, ())
hscript_FieldAccess.APrivate = hscript_FieldAccess("APrivate", 1, ())
hscript_FieldAccess.AInline = hscript_FieldAccess("AInline", 2, ())
hscript_FieldAccess.AOverride = hscript_FieldAccess("AOverride", 3, ())
hscript_FieldAccess.AStatic = hscript_FieldAccess("AStatic", 4, ())
hscript_FieldAccess.AMacro = hscript_FieldAccess("AMacro", 5, ())
hscript_FieldAccess._hx_class = hscript_FieldAccess
globalClasses._hx_classes["hscript.FieldAccess"] = hscript_FieldAccess

class hscript_FieldKind(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.FieldKind"
    _hx_constructs = ["KFunction", "KVar"]

    @staticmethod
    def KFunction(f):
        return hscript_FieldKind("KFunction", 0, (f,))

    @staticmethod
    def KVar(v):
        return hscript_FieldKind("KVar", 1, (v,))
hscript_FieldKind._hx_class = hscript_FieldKind
globalClasses._hx_classes["hscript.FieldKind"] = hscript_FieldKind



class hscript_Macro:
    _hx_class_name = "hscript.Macro"
    __slots__ = ("p", "binops", "unops")
    _hx_fields = ["p", "binops", "unops"]
    _hx_methods = ["map", "convertType", "convert"]

    def __init__(self,pos):
        self.p = pos
        self.binops = haxe_ds_StringMap()
        self.unops = haxe_ds_StringMap()
        _g = 0
        _g1 = Type.getEnumConstructs(haxe_macro_Binop)
        while (_g < len(_g1)):
            c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (c == "OpAssignOp"):
                continue
            op = Type.createEnum(haxe_macro_Binop,c)
            assign = False
            _hx_str = None
            str1 = op.index
            if (str1 == 0):
                assign = True
                _hx_str = "+"
            elif (str1 == 1):
                assign = True
                _hx_str = "*"
            elif (str1 == 2):
                assign = True
                _hx_str = "/"
            elif (str1 == 3):
                assign = True
                _hx_str = "-"
            elif (str1 == 4):
                _hx_str = "="
            elif (str1 == 5):
                _hx_str = "=="
            elif (str1 == 6):
                _hx_str = "!="
            elif (str1 == 7):
                _hx_str = ">"
            elif (str1 == 8):
                _hx_str = ">="
            elif (str1 == 9):
                _hx_str = "<"
            elif (str1 == 10):
                _hx_str = "<="
            elif (str1 == 11):
                assign = True
                _hx_str = "&"
            elif (str1 == 12):
                assign = True
                _hx_str = "|"
            elif (str1 == 13):
                assign = True
                _hx_str = "^"
            elif (str1 == 14):
                _hx_str = "&&"
            elif (str1 == 15):
                _hx_str = "||"
            elif (str1 == 16):
                assign = True
                _hx_str = "<<"
            elif (str1 == 17):
                assign = True
                _hx_str = ">>"
            elif (str1 == 18):
                assign = True
                _hx_str = ">>>"
            elif (str1 == 19):
                assign = True
                _hx_str = "%"
            elif (str1 == 20):
                _g2 = op.params[0]
                _hx_str = ""
            elif (str1 == 21):
                _hx_str = "..."
            elif (str1 == 22):
                _hx_str = "=>"
            elif (str1 == 23):
                _hx_str = "in"
            else:
                pass
            self.binops.h[_hx_str] = op
            if assign:
                self.binops.h[(("null" if _hx_str is None else _hx_str) + "=")] = haxe_macro_Binop.OpAssignOp(op)
        _g = 0
        _g1 = Type.getEnumConstructs(haxe_macro_Unop)
        while (_g < len(_g1)):
            c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            op = Type.createEnum(haxe_macro_Unop,c)
            _hx_str = None
            str1 = op.index
            if (str1 == 0):
                _hx_str = "++"
            elif (str1 == 1):
                _hx_str = "--"
            elif (str1 == 2):
                _hx_str = "!"
            elif (str1 == 3):
                _hx_str = "-"
            elif (str1 == 4):
                _hx_str = "~"
            elif (str1 == 5):
                continue
            else:
                pass
            self.unops.h[_hx_str] = op

    def map(self,a,f):
        b = list()
        _g = 0
        while (_g < len(a)):
            x = (a[_g] if _g >= 0 and _g < len(a) else None)
            _g = (_g + 1)
            x1 = f(x)
            b.append(x1)
        return b

    def convertType(self,t):
        tmp = t.index
        if (tmp == 0):
            pack = t.params[0]
            args = t.params[1]
            params = []
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    t1 = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    x = haxe_macro_TypeParam.TPType(self.convertType(t1))
                    params.append(x)
            return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': pack, 'name': (None if ((len(pack) == 0)) else pack.pop()), 'params': params, 'sub': None}))
        elif (tmp == 1):
            args = t.params[0]
            ret = t.params[1]
            return haxe_macro_ComplexType.TFunction(self.map(args,self.convertType),self.convertType(ret))
        elif (tmp == 2):
            fields = t.params[0]
            tf = []
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                meta = None
                if (Reflect.field(f,"meta") is None):
                    meta = []
                else:
                    _g1 = []
                    _g2 = 0
                    _g3 = Reflect.field(f,"meta")
                    while (_g2 < len(_g3)):
                        m = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        m1 = m.name
                        x = None
                        if (m.params is None):
                            x = []
                        else:
                            _g4 = []
                            _g5 = 0
                            _g6 = m.params
                            while (_g5 < len(_g6)):
                                e = (_g6[_g5] if _g5 >= 0 and _g5 < len(_g6) else None)
                                _g5 = (_g5 + 1)
                                x1 = self.convert(e)
                                _g4.append(x1)
                            x = _g4
                        x2 = _hx_AnonObject({'name': m1, 'params': x, 'pos': self.p})
                        _g1.append(x2)
                    meta = _g1
                x3 = _hx_AnonObject({'name': f.name, 'meta': meta, 'doc': None, 'access': [], 'kind': haxe_macro_FieldType.FVar(self.convertType(f.t),None), 'pos': self.p})
                tf.append(x3)
            return haxe_macro_ComplexType.TAnonymous(tf)
        elif (tmp == 3):
            t1 = t.params[0]
            return haxe_macro_ComplexType.TParent(self.convertType(t1))
        elif (tmp == 4):
            t1 = t.params[0]
            return haxe_macro_ComplexType.TOptional(self.convertType(t1))
        elif (tmp == 5):
            name = t.params[0]
            ct = self.convertType(t.params[1])
            return haxe_macro_ComplexType.TNamed(name,ct)
        else:
            pass

    def convert(self,e):
        tmp = None
        tmp1 = e.index
        if (tmp1 == 0):
            c = e.params[0]
            tmp1 = None
            tmp2 = c.index
            if (tmp2 == 0):
                v = c.params[0]
                tmp1 = haxe_macro_Constant.CInt(Std.string(v))
            elif (tmp2 == 1):
                f = c.params[0]
                tmp1 = haxe_macro_Constant.CFloat(Std.string(f))
            elif (tmp2 == 2):
                s = c.params[0]
                tmp1 = haxe_macro_Constant.CString(s)
            else:
                pass
            tmp = haxe_macro_ExprDef.EConst(tmp1)
        elif (tmp1 == 1):
            v = e.params[0]
            tmp = haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent(v))
        elif (tmp1 == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            tmp = haxe_macro_ExprDef.EVars([_hx_AnonObject({'name': n, 'expr': (None if ((e1 is None)) else self.convert(e1)), 'type': (None if ((t is None)) else self.convertType(t))})])
        elif (tmp1 == 3):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EParenthesis(self.convert(e1))
        elif (tmp1 == 4):
            el = e.params[0]
            tmp = haxe_macro_ExprDef.EBlock(self.map(el,self.convert))
        elif (tmp1 == 5):
            e1 = e.params[0]
            f = e.params[1]
            tmp = haxe_macro_ExprDef.EField(self.convert(e1),f)
        elif (tmp1 == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            b = self.binops.h.get(op,None)
            if (b is None):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp(op))
            tmp = haxe_macro_ExprDef.EBinop(b,self.convert(e1),self.convert(e2))
        elif (tmp1 == 7):
            op = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            u = self.unops.h.get(op,None)
            if (u is None):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp(op))
            tmp = haxe_macro_ExprDef.EUnop(u,(not prefix),self.convert(e1))
        elif (tmp1 == 8):
            e1 = e.params[0]
            params = e.params[1]
            tmp = haxe_macro_ExprDef.ECall(self.convert(e1),self.map(params,self.convert))
        elif (tmp1 == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            tmp = haxe_macro_ExprDef.EIf(self.convert(c),self.convert(e1),(None if ((e2 is None)) else self.convert(e2)))
        elif (tmp1 == 10):
            c = e.params[0]
            e1 = e.params[1]
            tmp = haxe_macro_ExprDef.EWhile(self.convert(c),self.convert(e1),True)
        elif (tmp1 == 11):
            v = e.params[0]
            it = e.params[1]
            efor = e.params[2]
            p = self.p
            tmp1 = self.convert(it)
            tmp2 = self.convert(efor)
            tmp = haxe_macro_ExprDef.EFor(_hx_AnonObject({'expr': haxe_macro_ExprDef.EBinop(haxe_macro_Binop.OpIn,_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent(v)), 'pos': p}),tmp1), 'pos': p}),tmp2)
        elif (tmp1 == 12):
            tmp = haxe_macro_ExprDef.EBreak
        elif (tmp1 == 13):
            tmp = haxe_macro_ExprDef.EContinue
        elif (tmp1 == 14):
            args = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            ret = e.params[3]
            targs = []
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                a1 = a.name
                x = (None if ((Reflect.field(a,"t") is None)) else self.convertType(Reflect.field(a,"t")))
                targs.append(_hx_AnonObject({'name': a1, 'type': x, 'opt': False, 'value': None}))
            tmp = haxe_macro_ExprDef.EFunction(haxe_macro_FunctionKind.FNamed(name,False),_hx_AnonObject({'params': [], 'args': targs, 'expr': self.convert(e1), 'ret': (None if ((ret is None)) else self.convertType(ret))}))
        elif (tmp1 == 15):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EReturn((None if ((e1 is None)) else self.convert(e1)))
        elif (tmp1 == 16):
            e1 = e.params[0]
            index = e.params[1]
            tmp = haxe_macro_ExprDef.EArray(self.convert(e1),self.convert(index))
        elif (tmp1 == 17):
            el = e.params[0]
            tmp = haxe_macro_ExprDef.EArrayDecl(self.map(el,self.convert))
        elif (tmp1 == 18):
            cl = e.params[0]
            params = e.params[1]
            pack = cl.split(".")
            tmp1 = (None if ((len(pack) == 0)) else pack.pop())
            tmp2 = self.map(params,self.convert)
            tmp = haxe_macro_ExprDef.ENew(_hx_AnonObject({'pack': pack, 'name': tmp1, 'params': [], 'sub': None}),tmp2)
        elif (tmp1 == 19):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EThrow(self.convert(e1))
        elif (tmp1 == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            ec = e.params[3]
            tmp = haxe_macro_ExprDef.ETry(self.convert(e1),[_hx_AnonObject({'type': self.convertType(t), 'name': v, 'expr': self.convert(ec)})])
        elif (tmp1 == 21):
            fields = e.params[0]
            tf = []
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                x = _hx_AnonObject({'field': f.name, 'expr': self.convert(f.e)})
                tf.append(x)
            tmp = haxe_macro_ExprDef.EObjectDecl(tf)
        elif (tmp1 == 22):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            tmp = haxe_macro_ExprDef.ETernary(self.convert(cond),self.convert(e1),self.convert(e2))
        elif (tmp1 == 23):
            e1 = e.params[0]
            cases = e.params[1]
            edef = e.params[2]
            tmp1 = self.convert(e1)
            _g = []
            _g1 = 0
            while (_g1 < len(cases)):
                c = (cases[_g1] if _g1 >= 0 and _g1 < len(cases) else None)
                _g1 = (_g1 + 1)
                _g2 = []
                _g3 = 0
                _g4 = c.values
                while (_g3 < len(_g4)):
                    v = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                    _g3 = (_g3 + 1)
                    x = self.convert(v)
                    _g2.append(x)
                x1 = _hx_AnonObject({'values': _g2, 'expr': self.convert(c.expr)})
                _g.append(x1)
            tmp = haxe_macro_ExprDef.ESwitch(tmp1,_g,(None if ((edef is None)) else self.convert(edef)))
        elif (tmp1 == 24):
            c = e.params[0]
            e1 = e.params[1]
            tmp = haxe_macro_ExprDef.EWhile(self.convert(c),self.convert(e1),False)
        elif (tmp1 == 25):
            m = e.params[0]
            params = e.params[1]
            esub = e.params[2]
            mpos = self.p
            tmp1 = None
            if (params is None):
                tmp1 = []
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(params)):
                    p = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                    _g1 = (_g1 + 1)
                    x = self.convert(p)
                    _g.append(x)
                tmp1 = _g
            tmp2 = self.convert(esub)
            tmp = haxe_macro_ExprDef.EMeta(_hx_AnonObject({'name': m, 'params': tmp1, 'pos': mpos}),tmp2)
        elif (tmp1 == 26):
            e1 = e.params[0]
            t = e.params[1]
            tmp = haxe_macro_ExprDef.ECheckType(self.convert(e1),self.convertType(t))
        else:
            pass
        return _hx_AnonObject({'expr': tmp, 'pos': self.p})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.p = None
        _hx_o.binops = None
        _hx_o.unops = None
hscript_Macro._hx_class = hscript_Macro
globalClasses._hx_classes["hscript.Macro"] = hscript_Macro

class hscript_ModuleDecl(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.ModuleDecl"
    _hx_constructs = ["DPackage", "DImport", "DClass", "DTypedef"]

    @staticmethod
    def DPackage(path):
        return hscript_ModuleDecl("DPackage", 0, (path,))

    @staticmethod
    def DImport(path,everything = None):
        return hscript_ModuleDecl("DImport", 1, (path,everything))

    @staticmethod
    def DClass(c):
        return hscript_ModuleDecl("DClass", 2, (c,))

    @staticmethod
    def DTypedef(c):
        return hscript_ModuleDecl("DTypedef", 3, (c,))
hscript_ModuleDecl._hx_class = hscript_ModuleDecl
globalClasses._hx_classes["hscript.ModuleDecl"] = hscript_ModuleDecl

class hscript_Parser:
    _hx_class_name = "hscript.Parser"
    __slots__ = ("line", "opChars", "identChars", "opPriority", "opRightAssoc", "preprocesorValues", "allowJSON", "allowTypes", "allowMetadata", "resumeErrors", "input", "readPos", "char", "ops", "idents", "uid", "tokens", "preprocStack")
    _hx_fields = ["line", "opChars", "identChars", "opPriority", "opRightAssoc", "preprocesorValues", "allowJSON", "allowTypes", "allowMetadata", "resumeErrors", "input", "readPos", "char", "ops", "idents", "uid", "tokens", "preprocStack"]
    _hx_methods = ["error", "invalidChar", "initParser", "parseString", "unexpected", "push", "ensure", "ensureToken", "maybe", "getIdent", "expr", "pmin", "pmax", "mk", "isBlock", "parseFullExpr", "parseObject", "parseExpr", "parseLambda", "parseMetaArgs", "mapCompr", "makeUnop", "makeBinop", "parseStructure", "parseExprNext", "parseFunctionArgs", "parseFunctionDecl", "parsePath", "parseType", "parseTypeNext", "parseExprList", "parseModule", "parseMetadata", "parseParams", "parseModuleDecl", "parseField", "readChar", "readString", "token", "preprocValue", "parsePreproCond", "evalPreproCond", "preprocess", "skipTokens", "tokenComment", "constString", "tokenString"]
    _hx_statics = ["p1", "tokenMin", "tokenMax"]

    def __init__(self):
        self.preprocStack = None
        self.tokens = None
        self.idents = None
        self.ops = None
        self.char = None
        self.readPos = None
        self.input = None
        self.resumeErrors = None
        self.allowMetadata = None
        self.allowTypes = None
        self.allowJSON = None
        self.uid = 0
        self.preprocesorValues = haxe_ds_StringMap()
        self.line = 1
        self.opChars = "+*/-=!><&|^%~"
        self.identChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
        priorities = [["%"], ["*", "/"], ["+", "-"], ["<<", ">>", ">>>"], ["|", "&", "^"], ["==", "!=", ">", "<", ">=", "<="], ["..."], ["&&"], ["||"], ["=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", ">>>=", "|=", "&=", "^=", "=>"], ["->"]]
        self.opPriority = haxe_ds_StringMap()
        self.opRightAssoc = haxe_ds_StringMap()
        _g = 0
        _g1 = len(priorities)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = (priorities[i] if i >= 0 and i < len(priorities) else None)
            while (_g2 < len(_g3)):
                x = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                self.opPriority.h[x] = i
                if (i == 9):
                    self.opRightAssoc.h[x] = True
        x = "!"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "++"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "--"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "~"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)

    def error(self,err,pmin,pmax):
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(err)

    def invalidChar(self,c):
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(hscript_Error.EInvalidChar(c))

    def initParser(self,origin):
        self.preprocStack = []
        self.tokens = haxe_ds_GenericStack()
        self.char = -1
        self.ops = list()
        self.idents = list()
        self.uid = 0
        _g = 0
        _g1 = len(self.opChars)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(self.ops, HxString.charCodeAt(self.opChars,i), True)
        _g = 0
        _g1 = len(self.identChars)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(self.idents, HxString.charCodeAt(self.identChars,i), True)

    def parseString(self,s,origin = None):
        if (origin is None):
            origin = "hscript"
        self.initParser(origin)
        self.input = s
        self.readPos = 0
        a = list()
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                break
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            self.parseFullExpr(a)
        if (len(a) == 1):
            return (a[0] if 0 < len(a) else None)
        else:
            return hscript_Expr.EBlock(a)

    def unexpected(self,tk):
        err = hscript_Error.EUnexpected(self.tokenString(tk))
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(err)
        return None

    def push(self,tk):
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(tk,_this.head)

    def ensure(self,tk):
        t = self.token()
        if (t != tk):
            self.unexpected(t)

    def ensureToken(self,tk):
        t = self.token()
        if (not Type.enumEq(t,tk)):
            self.unexpected(t)

    def maybe(self,tk):
        t = self.token()
        if Type.enumEq(t,tk):
            return True
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(t,_this.head)
        return False

    def getIdent(self):
        tk = self.token()
        if (tk is None):
            self.unexpected(tk)
            return None
        elif (tk.index == 2):
            id = tk.params[0]
            return id
        else:
            self.unexpected(tk)
            return None

    def expr(self,e):
        return e

    def pmin(self,e):
        return 0

    def pmax(self,e):
        return 0

    def mk(self,e,pmin = None,pmax = None):
        return e

    def isBlock(self,e):
        if (e is None):
            return False
        tmp = e.index
        if (tmp == 2):
            _g = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            if (e1 is not None):
                return self.isBlock(e1)
            elif (t is not None):
                if (t is None):
                    return False
                elif (t.index == 2):
                    _g = t.params[0]
                    return True
                else:
                    return False
            else:
                return False
        elif (tmp == 4):
            _g = e.params[0]
            return True
        elif (tmp == 6):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        elif (tmp == 7):
            _g = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            if (not prefix):
                return self.isBlock(e1)
            else:
                return False
        elif (tmp == 9):
            _g = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            if (e2 is not None):
                return self.isBlock(e2)
            else:
                return self.isBlock(e1)
        elif (tmp == 10):
            _g = e.params[0]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 11):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        elif (tmp == 14):
            _g = e.params[0]
            _g = e.params[2]
            _g = e.params[3]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is not None):
                return self.isBlock(e1)
            else:
                return False
        elif (tmp == 20):
            _g = e.params[0]
            _g = e.params[1]
            _g = e.params[2]
            e1 = e.params[3]
            return self.isBlock(e1)
        elif (tmp == 21):
            _g = e.params[0]
            return True
        elif (tmp == 23):
            _g = e.params[0]
            _g = e.params[1]
            _g = e.params[2]
            return True
        elif (tmp == 24):
            _g = e.params[0]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 25):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        else:
            return False

    def parseFullExpr(self,exprs):
        e = self.parseExpr()
        exprs.append(e)
        tk = self.token()
        while True:
            tmp = None
            if ((tk == hscript_Token.TComma) and ((e is not None))):
                if (e.index == 2):
                    _g = e.params[0]
                    _g1 = e.params[1]
                    _g2 = e.params[2]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if (not tmp):
                break
            e = self.parseStructure("var")
            exprs.append(e)
            tk = self.token()
        if ((tk != hscript_Token.TSemicolon) and ((tk != hscript_Token.TEof))):
            if self.isBlock(e):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
            else:
                self.unexpected(tk)

    def parseObject(self,p1):
        fl = list()
        while True:
            tk = self.token()
            id = None
            if (tk is None):
                self.unexpected(tk)
                break
            else:
                tmp = tk.index
                if (tmp == 1):
                    c = tk.params[0]
                    if (not self.allowJSON):
                        self.unexpected(tk)
                    if (c.index == 2):
                        s = c.params[0]
                        id = s
                    else:
                        self.unexpected(tk)
                elif (tmp == 2):
                    i = tk.params[0]
                    id = i
                elif (tmp == 7):
                    break
                else:
                    self.unexpected(tk)
                    break
            t = self.token()
            if (t != hscript_Token.TDoubleDot):
                self.unexpected(t)
            x = _hx_AnonObject({'name': id, 'e': self.parseExpr()})
            fl.append(x)
            tk = self.token()
            if (tk is None):
                self.unexpected(tk)
            else:
                tmp1 = tk.index
                if (tmp1 == 7):
                    break
                elif (tmp1 == 9):
                    pass
                else:
                    self.unexpected(tk)
        return self.parseExprNext(hscript_Expr.EObject(fl))

    def parseExpr(self):
        tk = self.token()
        if (tk is None):
            return self.unexpected(tk)
        else:
            tmp = tk.index
            if (tmp == 1):
                c = tk.params[0]
                return self.parseExprNext(hscript_Expr.EConst(c))
            elif (tmp == 2):
                id = tk.params[0]
                e = self.parseStructure(id)
                if (e is None):
                    e = hscript_Expr.EIdent(id)
                return self.parseExprNext(e)
            elif (tmp == 3):
                op = tk.params[0]
                if (op == "-"):
                    start = 0
                    e = self.parseExpr()
                    if (e is None):
                        return self.makeUnop(op,e)
                    if (e.index == 0):
                        _g = e.params[0]
                        tmp = _g.index
                        if (tmp == 0):
                            i = _g.params[0]
                            return hscript_Expr.EConst(hscript_Const.CInt(-i))
                        elif (tmp == 1):
                            f = _g.params[0]
                            return hscript_Expr.EConst(hscript_Const.CFloat(-f))
                        else:
                            return self.makeUnop(op,e)
                    else:
                        return self.makeUnop(op,e)
                if (self.opPriority.h.get(op,None) < 0):
                    return self.makeUnop(op,self.parseExpr())
                return self.unexpected(tk)
            elif (tmp == 4):
                tk = self.token()
                if (tk == hscript_Token.TPClose):
                    t = self.token()
                    if (not Type.enumEq(t,hscript_Token.TOp("->"))):
                        self.unexpected(t)
                    eret = self.parseExpr()
                    return hscript_Expr.EFunction([],hscript_Expr.EReturn(eret))
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                e = self.parseExpr()
                tk = self.token()
                if (tk is not None):
                    tmp = tk.index
                    if (tmp == 5):
                        return self.parseExprNext(hscript_Expr.EParent(e))
                    elif (tmp == 9):
                        if (e.index == 1):
                            v = e.params[0]
                            return self.parseLambda([_hx_AnonObject({'name': v})],0)
                    elif (tmp == 14):
                        t = self.parseType()
                        tk = self.token()
                        if (tk is not None):
                            tmp = tk.index
                            if (tmp == 5):
                                return self.parseExprNext(hscript_Expr.ECheckType(e,t))
                            elif (tmp == 9):
                                if (e.index == 1):
                                    v = e.params[0]
                                    return self.parseLambda([_hx_AnonObject({'name': v, 't': t})],0)
                            else:
                                pass
                    else:
                        pass
                return self.unexpected(tk)
            elif (tmp == 6):
                tk = self.token()
                if (tk is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                else:
                    tmp = tk.index
                    if (tmp == 1):
                        c = tk.params[0]
                        if self.allowJSON:
                            if (c.index == 2):
                                _g = c.params[0]
                                tk2 = self.token()
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk2,_this.head)
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk,_this.head)
                                if (tk2 is not None):
                                    if (tk2.index == 14):
                                        return self.parseExprNext(self.parseObject(0))
                            else:
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk,_this.head)
                        else:
                            _this = self.tokens
                            _this.head = haxe_ds_GenericCell(tk,_this.head)
                    elif (tmp == 2):
                        _g = tk.params[0]
                        tk2 = self.token()
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk2,_this.head)
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                        if (tk2 is not None):
                            if (tk2.index == 14):
                                return self.parseExprNext(self.parseObject(0))
                    elif (tmp == 7):
                        return self.parseExprNext(hscript_Expr.EObject([]))
                    else:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                a = list()
                while True:
                    self.parseFullExpr(a)
                    tk = self.token()
                    if ((tk == hscript_Token.TBrClose) or ((self.resumeErrors and ((tk == hscript_Token.TEof))))):
                        break
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                return hscript_Expr.EBlock(a)
            elif (tmp == 11):
                a = list()
                tk = self.token()
                while ((tk != hscript_Token.TBkClose) and (((not self.resumeErrors) or ((tk != hscript_Token.TEof))))):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                    x = self.parseExpr()
                    a.append(x)
                    tk = self.token()
                    if (tk == hscript_Token.TComma):
                        tk = self.token()
                if ((len(a) == 1) and (((a[0] if 0 < len(a) else None) is not None))):
                    _g = (a[0] if 0 < len(a) else None)
                    tmp = _g.index
                    if (tmp == 10):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        def _hx_local_2():
                            _hx_local_0 = self
                            _hx_local_1 = _hx_local_0.uid
                            _hx_local_0.uid = (_hx_local_1 + 1)
                            return _hx_local_1
                        tmp = ("__a_" + Std.string(_hx_local_2()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    elif (tmp == 11):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        _g1 = _g.params[2]
                        def _hx_local_5():
                            _hx_local_3 = self
                            _hx_local_4 = _hx_local_3.uid
                            _hx_local_3.uid = (_hx_local_4 + 1)
                            return _hx_local_4
                        tmp = ("__a_" + Std.string(_hx_local_5()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    elif (tmp == 24):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        def _hx_local_8():
                            _hx_local_6 = self
                            _hx_local_7 = _hx_local_6.uid
                            _hx_local_6.uid = (_hx_local_7 + 1)
                            return _hx_local_7
                        tmp = ("__a_" + Std.string(_hx_local_8()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    else:
                        pass
                return self.parseExprNext(hscript_Expr.EArrayDecl(a))
            elif (tmp == 15):
                id = tk.params[0]
                if self.allowMetadata:
                    args = self.parseMetaArgs()
                    return hscript_Expr.EMeta(id,args,self.parseExpr())
                else:
                    return self.unexpected(tk)
            else:
                return self.unexpected(tk)

    def parseLambda(self,args,pmin):
        while True:
            id = self.getIdent()
            t = (self.parseType() if (self.maybe(hscript_Token.TDoubleDot)) else None)
            args.append(_hx_AnonObject({'name': id, 't': t}))
            tk = self.token()
            if (tk is None):
                self.unexpected(tk)
                break
            else:
                tmp = tk.index
                if (tmp == 5):
                    break
                elif (tmp == 9):
                    pass
                else:
                    self.unexpected(tk)
                    break
        t = self.token()
        if (not Type.enumEq(t,hscript_Token.TOp("->"))):
            self.unexpected(t)
        eret = self.parseExpr()
        return hscript_Expr.EFunction(args,hscript_Expr.EReturn(eret))

    def parseMetaArgs(self):
        tk = self.token()
        if (tk != hscript_Token.TPOpen):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return None
        args = []
        tk = self.token()
        if (tk != hscript_Token.TPClose):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            while True:
                x = self.parseExpr()
                args.append(x)
                _g = self.token()
                if (_g is None):
                    tk = _g
                    self.unexpected(tk)
                else:
                    tmp = _g.index
                    if (tmp == 5):
                        break
                    elif (tmp == 9):
                        pass
                    else:
                        tk1 = _g
                        self.unexpected(tk1)
        return args

    def mapCompr(self,tmp,e):
        if (e is None):
            return None
        edef = None
        edef1 = e.index
        if (edef1 == 3):
            e2 = e.params[0]
            edef = hscript_Expr.EParent(self.mapCompr(tmp,e2))
        elif (edef1 == 4):
            _g = e.params[0]
            if (len(_g) == 1):
                e1 = (_g[0] if 0 < len(_g) else None)
                edef = hscript_Expr.EBlock([self.mapCompr(tmp,e1)])
            else:
                edef = hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e])
        elif (edef1 == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = (hscript_Expr.EIf(cond,self.mapCompr(tmp,e1),None) if ((e2 is None)) else hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e]))
        elif (edef1 == 10):
            cond = e.params[0]
            e2 = e.params[1]
            edef = hscript_Expr.EWhile(cond,self.mapCompr(tmp,e2))
        elif (edef1 == 11):
            v = e.params[0]
            it = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EFor(v,it,self.mapCompr(tmp,e2))
        elif (edef1 == 24):
            cond = e.params[0]
            e2 = e.params[1]
            edef = hscript_Expr.EDoWhile(cond,self.mapCompr(tmp,e2))
        else:
            edef = hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e])
        return edef

    def makeUnop(self,op,e):
        if ((e is None) and self.resumeErrors):
            return None
        tmp = e.index
        if (tmp == 6):
            bop = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            return hscript_Expr.EBinop(bop,self.makeUnop(op,e1),e2)
        elif (tmp == 22):
            e1 = e.params[0]
            e2 = e.params[1]
            e3 = e.params[2]
            return hscript_Expr.ETernary(self.makeUnop(op,e1),e2,e3)
        else:
            return hscript_Expr.EUnop(op,True,e)

    def makeBinop(self,op,e1,e):
        if ((e is None) and self.resumeErrors):
            return hscript_Expr.EBinop(op,e1,e)
        tmp = e.index
        if (tmp == 6):
            op2 = e.params[0]
            e2 = e.params[1]
            e3 = e.params[2]
            if ((self.opPriority.h.get(op,None) <= self.opPriority.h.get(op2,None)) and (not (op in self.opRightAssoc.h))):
                return hscript_Expr.EBinop(op2,self.makeBinop(op,e1,e2),e3)
            else:
                return hscript_Expr.EBinop(op,e1,e)
        elif (tmp == 22):
            e2 = e.params[0]
            e3 = e.params[1]
            e4 = e.params[2]
            if (op in self.opRightAssoc.h):
                return hscript_Expr.EBinop(op,e1,e)
            else:
                return hscript_Expr.ETernary(self.makeBinop(op,e1,e2),e3,e4)
        else:
            return hscript_Expr.EBinop(op,e1,e)

    def parseStructure(self,id):
        id1 = id
        _hx_local_0 = len(id1)
        if (_hx_local_0 == 5):
            if (id1 == "break"):
                return hscript_Expr.EBreak
            elif (id1 == "throw"):
                e = self.parseExpr()
                return hscript_Expr.EThrow(e)
            elif (id1 == "while"):
                econd = self.parseExpr()
                e = self.parseExpr()
                return hscript_Expr.EWhile(econd,e)
            else:
                return None
        elif (_hx_local_0 == 4):
            if (id1 == "else"):
                return self.unexpected(hscript_Token.TId(id))
            else:
                return None
        elif (_hx_local_0 == 3):
            if (id1 == "for"):
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                vname = self.getIdent()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TId("in"))):
                    self.unexpected(t)
                eiter = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TPClose):
                    self.unexpected(t)
                e = self.parseExpr()
                return hscript_Expr.EFor(vname,eiter,e)
            elif (id1 == "new"):
                a = list()
                x = self.getIdent()
                a.append(x)
                while True:
                    tk = self.token()
                    if (tk is None):
                        self.unexpected(tk)
                        break
                    else:
                        tmp = tk.index
                        if (tmp == 4):
                            break
                        elif (tmp == 8):
                            x = self.getIdent()
                            a.append(x)
                        else:
                            self.unexpected(tk)
                            break
                args = self.parseExprList(hscript_Token.TPClose)
                return hscript_Expr.ENew(".".join([python_Boot.toString1(x1,'') for x1 in a]),args)
            elif (id1 == "try"):
                e = self.parseExpr()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TId("catch"))):
                    self.unexpected(t)
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                vname = self.getIdent()
                t = self.token()
                if (t != hscript_Token.TDoubleDot):
                    self.unexpected(t)
                t = None
                if self.allowTypes:
                    t = self.parseType()
                else:
                    t1 = self.token()
                    if (not Type.enumEq(t1,hscript_Token.TId("Dynamic"))):
                        self.unexpected(t1)
                t1 = self.token()
                if (t1 != hscript_Token.TPClose):
                    self.unexpected(t1)
                ec = self.parseExpr()
                return hscript_Expr.ETry(e,vname,t,ec)
            elif (id1 == "var"):
                ident = self.getIdent()
                tk = self.token()
                t = None
                if ((tk == hscript_Token.TDoubleDot) and self.allowTypes):
                    t = self.parseType()
                    tk = self.token()
                e = None
                if Type.enumEq(tk,hscript_Token.TOp("=")):
                    e = self.parseExpr()
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                return hscript_Expr.EVar(ident,t,e)
            else:
                return None
        elif (_hx_local_0 == 8):
            if (id1 == "continue"):
                return hscript_Expr.EContinue
            elif (id1 == "function"):
                tk = self.token()
                name = None
                if (tk is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                elif (tk.index == 2):
                    id = tk.params[0]
                    name = id
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                inf = self.parseFunctionDecl()
                return hscript_Expr.EFunction(inf.args,inf.body,name,inf.ret)
            else:
                return None
        elif (_hx_local_0 == 2):
            if (id1 == "do"):
                e = self.parseExpr()
                tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                elif (tk.index == 2):
                    if (tk.params[0] != "while"):
                        self.unexpected(tk)
                else:
                    self.unexpected(tk)
                econd = self.parseExpr()
                return hscript_Expr.EDoWhile(econd,e)
            elif (id1 == "if"):
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                cond = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TPClose):
                    self.unexpected(t)
                e1 = self.parseExpr()
                e2 = None
                semic = False
                tk = self.token()
                if (tk == hscript_Token.TSemicolon):
                    semic = True
                    tk = self.token()
                if Type.enumEq(tk,hscript_Token.TId("else")):
                    e2 = self.parseExpr()
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                    if semic:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(hscript_Token.TSemicolon,_this.head)
                return hscript_Expr.EIf(cond,e1,e2)
            else:
                return None
        elif (_hx_local_0 == 6):
            if (id1 == "inline"):
                if (not self.maybe(hscript_Token.TId("function"))):
                    self.unexpected(hscript_Token.TId("inline"))
                return self.parseStructure("function")
            elif (id1 == "return"):
                tk = self.token()
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                e = (None if ((tk == hscript_Token.TSemicolon)) else self.parseExpr())
                return hscript_Expr.EReturn(e)
            elif (id1 == "switch"):
                e = self.parseExpr()
                _hx_def = None
                cases = []
                t = self.token()
                if (t != hscript_Token.TBrOpen):
                    self.unexpected(t)
                while True:
                    tk = self.token()
                    if (tk is None):
                        self.unexpected(tk)
                        break
                    else:
                        tmp = tk.index
                        if (tmp == 2):
                            _g = tk.params[0]
                            _hx_local_1 = len(_g)
                            if (_hx_local_1 == 4):
                                if (_g == "case"):
                                    c = _hx_AnonObject({'values': [], 'expr': None})
                                    cases.append(c)
                                    while True:
                                        e1 = self.parseExpr()
                                        _this = c.values
                                        _this.append(e1)
                                        tk = self.token()
                                        if (tk is None):
                                            self.unexpected(tk)
                                            break
                                        else:
                                            tmp1 = tk.index
                                            if (tmp1 == 9):
                                                pass
                                            elif (tmp1 == 14):
                                                break
                                            else:
                                                self.unexpected(tk)
                                                break
                                    exprs = []
                                    while True:
                                        tk = self.token()
                                        _this1 = self.tokens
                                        _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                                        if (tk is None):
                                            self.parseFullExpr(exprs)
                                        else:
                                            tmp2 = tk.index
                                            if (tmp2 == 0):
                                                if self.resumeErrors:
                                                    break
                                                else:
                                                    self.parseFullExpr(exprs)
                                            elif (tmp2 == 2):
                                                _g1 = tk.params[0]
                                                _hx_local_2 = len(_g1)
                                                if (_hx_local_2 == 4):
                                                    if (_g1 == "case"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs)
                                                elif (_hx_local_2 == 7):
                                                    if (_g1 == "default"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs)
                                                else:
                                                    self.parseFullExpr(exprs)
                                            elif (tmp2 == 7):
                                                break
                                            else:
                                                self.parseFullExpr(exprs)
                                    c.expr = ((exprs[0] if 0 < len(exprs) else None) if ((len(exprs) == 1)) else (hscript_Expr.EBlock([]) if ((len(exprs) == 0)) else hscript_Expr.EBlock(exprs)))
                                else:
                                    self.unexpected(tk)
                                    break
                            elif (_hx_local_1 == 7):
                                if (_g == "default"):
                                    if (_hx_def is not None):
                                        self.unexpected(tk)
                                    t = self.token()
                                    if (t != hscript_Token.TDoubleDot):
                                        self.unexpected(t)
                                    exprs1 = []
                                    while True:
                                        tk = self.token()
                                        _this2 = self.tokens
                                        _this2.head = haxe_ds_GenericCell(tk,_this2.head)
                                        if (tk is None):
                                            self.parseFullExpr(exprs1)
                                        else:
                                            tmp3 = tk.index
                                            if (tmp3 == 0):
                                                if self.resumeErrors:
                                                    break
                                                else:
                                                    self.parseFullExpr(exprs1)
                                            elif (tmp3 == 2):
                                                _g2 = tk.params[0]
                                                _hx_local_3 = len(_g2)
                                                if (_hx_local_3 == 4):
                                                    if (_g2 == "case"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs1)
                                                elif (_hx_local_3 == 7):
                                                    if (_g2 == "default"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs1)
                                                else:
                                                    self.parseFullExpr(exprs1)
                                            elif (tmp3 == 7):
                                                break
                                            else:
                                                self.parseFullExpr(exprs1)
                                    _hx_def = ((exprs1[0] if 0 < len(exprs1) else None) if ((len(exprs1) == 1)) else (hscript_Expr.EBlock([]) if ((len(exprs1) == 0)) else hscript_Expr.EBlock(exprs1)))
                                else:
                                    self.unexpected(tk)
                                    break
                            else:
                                self.unexpected(tk)
                                break
                        elif (tmp == 7):
                            break
                        else:
                            self.unexpected(tk)
                            break
                return hscript_Expr.ESwitch(e,cases,_hx_def)
            else:
                return None
        else:
            return None

    def parseExprNext(self,e1):
        tk = self.token()
        if (tk is None):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return e1
        else:
            tmp = tk.index
            if (tmp == 3):
                op = tk.params[0]
                if (op == "->"):
                    tmp = e1.index
                    if (tmp == 1):
                        i = e1.params[0]
                        eret = self.parseExpr()
                        return hscript_Expr.EFunction([_hx_AnonObject({'name': i})],hscript_Expr.EReturn(eret))
                    elif (tmp == 3):
                        _hx_tmp = e1.params[0]
                        if (_hx_tmp.index == 1):
                            i = _hx_tmp.params[0]
                            eret = self.parseExpr()
                            return hscript_Expr.EFunction([_hx_AnonObject({'name': i})],hscript_Expr.EReturn(eret))
                    elif (tmp == 26):
                        _hx_tmp = e1.params[0]
                        if (_hx_tmp.index == 1):
                            i = _hx_tmp.params[0]
                            t = e1.params[1]
                            eret = self.parseExpr()
                            return hscript_Expr.EFunction([_hx_AnonObject({'name': i, 't': t})],hscript_Expr.EReturn(eret))
                    else:
                        pass
                    self.unexpected(tk)
                if (self.opPriority.h.get(op,None) == -1):
                    tmp = None
                    if (not self.isBlock(e1)):
                        if (e1.index == 3):
                            _g = e1.params[0]
                            tmp = True
                        else:
                            tmp = False
                    else:
                        tmp = True
                    if tmp:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                        return e1
                    return self.parseExprNext(hscript_Expr.EUnop(op,False,e1))
                return self.makeBinop(op,e1,self.parseExpr())
            elif (tmp == 4):
                return self.parseExprNext(hscript_Expr.ECall(e1,self.parseExprList(hscript_Token.TPClose)))
            elif (tmp == 8):
                field = self.getIdent()
                return self.parseExprNext(hscript_Expr.EField(e1,field))
            elif (tmp == 11):
                e2 = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TBkClose):
                    self.unexpected(t)
                return self.parseExprNext(hscript_Expr.EArray(e1,e2))
            elif (tmp == 13):
                e2 = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TDoubleDot):
                    self.unexpected(t)
                e3 = self.parseExpr()
                return hscript_Expr.ETernary(e1,e2,e3)
            else:
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                return e1

    def parseFunctionArgs(self):
        args = list()
        tk = self.token()
        if (tk != hscript_Token.TPClose):
            done = False
            while (not done):
                name = None
                opt = False
                if (tk is not None):
                    if (tk.index == 13):
                        opt = True
                        tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                    break
                elif (tk.index == 2):
                    id = tk.params[0]
                    name = id
                else:
                    self.unexpected(tk)
                    break
                arg = _hx_AnonObject({'name': name})
                args.append(arg)
                if opt:
                    Reflect.setField(arg,"opt",True)
                if self.allowTypes:
                    if self.maybe(hscript_Token.TDoubleDot):
                        Reflect.setField(arg,"t",self.parseType())
                    if self.maybe(hscript_Token.TOp("=")):
                        Reflect.setField(arg,"value",self.parseExpr())
                tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                else:
                    tmp = tk.index
                    if (tmp == 5):
                        done = True
                    elif (tmp == 9):
                        tk = self.token()
                    else:
                        self.unexpected(tk)
        return args

    def parseFunctionDecl(self):
        t = self.token()
        if (t != hscript_Token.TPOpen):
            self.unexpected(t)
        args = self.parseFunctionArgs()
        ret = None
        if self.allowTypes:
            tk = self.token()
            if (tk != hscript_Token.TDoubleDot):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
            else:
                ret = self.parseType()
        return _hx_AnonObject({'args': args, 'ret': ret, 'body': self.parseExpr()})

    def parsePath(self):
        path = [self.getIdent()]
        while True:
            t = self.token()
            if (t != hscript_Token.TDot):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(t,_this.head)
                break
            x = self.getIdent()
            path.append(x)
        return path

    def parseType(self):
        _gthis = self
        t = self.token()
        if (t is None):
            return self.unexpected(t)
        else:
            tmp = t.index
            if (tmp == 2):
                v = t.params[0]
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(t,_this.head)
                path = self.parsePath()
                params = None
                t = self.token()
                if (t is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(t,_this.head)
                elif (t.index == 3):
                    op = t.params[0]
                    if (op == "<"):
                        params = []
                        while True:
                            x = self.parseType()
                            params.append(x)
                            t = self.token()
                            if (t is not None):
                                tmp = t.index
                                if (tmp == 3):
                                    op = t.params[0]
                                    if (op == ">"):
                                        break
                                    if (HxString.charCodeAt(op,0) == 62):
                                        _this = self.tokens
                                        _this.head = haxe_ds_GenericCell(hscript_Token.TOp(HxString.substr(op,1,None)),_this.head)
                                        break
                                elif (tmp == 9):
                                    continue
                                else:
                                    pass
                            self.unexpected(t)
                            break
                    else:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(t,_this.head)
                return self.parseTypeNext(hscript_CType.CTPath(path,params))
            elif (tmp == 4):
                a = self.token()
                b = self.token()
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(b,_this.head)
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(a,_this.head)
                def _hx_local_0(args):
                    _g = _gthis.token()
                    if (_g is None):
                        t = _g
                        _gthis.unexpected(t)
                    elif (_g.index == 3):
                        if (_g.params[0] != "->"):
                            t = _g
                            _gthis.unexpected(t)
                    else:
                        t = _g
                        _gthis.unexpected(t)
                    return hscript_CType.CTFun(args,_gthis.parseType())
                withReturn = _hx_local_0
                if (a is None):
                    t1 = self.parseType()
                    _g = self.token()
                    if (_g is None):
                        t2 = _g
                        return self.unexpected(t2)
                    else:
                        tmp = _g.index
                        if (tmp == 5):
                            return self.parseTypeNext(hscript_CType.CTParent(t1))
                        elif (tmp == 9):
                            args = [t1]
                            while True:
                                x = self.parseType()
                                args.append(x)
                                if (not self.maybe(hscript_Token.TComma)):
                                    break
                            t1 = self.token()
                            if (t1 != hscript_Token.TPClose):
                                self.unexpected(t1)
                            return withReturn(args)
                        else:
                            t1 = _g
                            return self.unexpected(t1)
                else:
                    tmp = a.index
                    if (tmp == 2):
                        _g = a.params[0]
                        if (b is None):
                            t1 = self.parseType()
                            _g = self.token()
                            if (_g is None):
                                t2 = _g
                                return self.unexpected(t2)
                            else:
                                tmp = _g.index
                                if (tmp == 5):
                                    return self.parseTypeNext(hscript_CType.CTParent(t1))
                                elif (tmp == 9):
                                    args = [t1]
                                    while True:
                                        x = self.parseType()
                                        args.append(x)
                                        if (not self.maybe(hscript_Token.TComma)):
                                            break
                                    t1 = self.token()
                                    if (t1 != hscript_Token.TPClose):
                                        self.unexpected(t1)
                                    return withReturn(args)
                                else:
                                    t1 = _g
                                    return self.unexpected(t1)
                        elif (b.index == 14):
                            _g = []
                            _g1 = 0
                            _g2 = self.parseFunctionArgs()
                            while (_g1 < len(_g2)):
                                arg = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                                _g1 = (_g1 + 1)
                                _g3 = Reflect.field(arg,"value")
                                if (_g3 is not None):
                                    v = _g3
                                    if (not self.resumeErrors):
                                        raise haxe_Exception.thrown(hscript_Error.ECustom("Default values not allowed in function types"))
                                x = hscript_CType.CTNamed(arg.name,(hscript_CType.CTOpt(Reflect.field(arg,"t")) if (Reflect.field(arg,"opt")) else Reflect.field(arg,"t")))
                                _g.append(x)
                            args = _g
                            return withReturn(args)
                        else:
                            t1 = self.parseType()
                            _g = self.token()
                            if (_g is None):
                                t2 = _g
                                return self.unexpected(t2)
                            else:
                                tmp = _g.index
                                if (tmp == 5):
                                    return self.parseTypeNext(hscript_CType.CTParent(t1))
                                elif (tmp == 9):
                                    args = [t1]
                                    while True:
                                        x = self.parseType()
                                        args.append(x)
                                        if (not self.maybe(hscript_Token.TComma)):
                                            break
                                    t1 = self.token()
                                    if (t1 != hscript_Token.TPClose):
                                        self.unexpected(t1)
                                    return withReturn(args)
                                else:
                                    t1 = _g
                                    return self.unexpected(t1)
                    elif (tmp == 5):
                        _g = []
                        _g1 = 0
                        _g2 = self.parseFunctionArgs()
                        while (_g1 < len(_g2)):
                            arg = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                            _g1 = (_g1 + 1)
                            _g3 = Reflect.field(arg,"value")
                            if (_g3 is not None):
                                v = _g3
                                if (not self.resumeErrors):
                                    raise haxe_Exception.thrown(hscript_Error.ECustom("Default values not allowed in function types"))
                            x = hscript_CType.CTNamed(arg.name,(hscript_CType.CTOpt(Reflect.field(arg,"t")) if (Reflect.field(arg,"opt")) else Reflect.field(arg,"t")))
                            _g.append(x)
                        args = _g
                        return withReturn(args)
                    else:
                        t1 = self.parseType()
                        _g = self.token()
                        if (_g is None):
                            t2 = _g
                            return self.unexpected(t2)
                        else:
                            tmp = _g.index
                            if (tmp == 5):
                                return self.parseTypeNext(hscript_CType.CTParent(t1))
                            elif (tmp == 9):
                                args = [t1]
                                while True:
                                    x = self.parseType()
                                    args.append(x)
                                    if (not self.maybe(hscript_Token.TComma)):
                                        break
                                t1 = self.token()
                                if (t1 != hscript_Token.TPClose):
                                    self.unexpected(t1)
                                return withReturn(args)
                            else:
                                t1 = _g
                                return self.unexpected(t1)
            elif (tmp == 6):
                fields = []
                meta = None
                while True:
                    t = self.token()
                    if (t is None):
                        self.unexpected(t)
                        break
                    else:
                        tmp = t.index
                        if (tmp == 2):
                            _g = t.params[0]
                            if (_g == "var"):
                                name = self.getIdent()
                                t1 = self.token()
                                if (t1 != hscript_Token.TDoubleDot):
                                    self.unexpected(t1)
                                x = _hx_AnonObject({'name': name, 't': self.parseType(), 'meta': meta})
                                fields.append(x)
                                meta = None
                                t2 = self.token()
                                if (t2 != hscript_Token.TSemicolon):
                                    self.unexpected(t2)
                            else:
                                name1 = _g
                                t3 = self.token()
                                if (t3 != hscript_Token.TDoubleDot):
                                    self.unexpected(t3)
                                x1 = _hx_AnonObject({'name': name1, 't': self.parseType(), 'meta': meta})
                                fields.append(x1)
                                t = self.token()
                                if (t is None):
                                    self.unexpected(t)
                                else:
                                    tmp1 = t.index
                                    if (tmp1 == 7):
                                        break
                                    elif (tmp1 == 9):
                                        pass
                                    else:
                                        self.unexpected(t)
                        elif (tmp == 7):
                            break
                        elif (tmp == 15):
                            name2 = t.params[0]
                            if (meta is None):
                                meta = []
                            x2 = _hx_AnonObject({'name': name2, 'params': self.parseMetaArgs()})
                            meta.append(x2)
                        else:
                            self.unexpected(t)
                            break
                return self.parseTypeNext(hscript_CType.CTAnon(fields))
            else:
                return self.unexpected(t)

    def parseTypeNext(self,t):
        tk = self.token()
        if (tk is None):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return t
        elif (tk.index == 3):
            op = tk.params[0]
            if (op != "->"):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                return t
        else:
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return t
        t2 = self.parseType()
        if (t2.index == 1):
            _g = t2.params[1]
            args = t2.params[0]
            args.insert(0, t)
            return t2
        else:
            return hscript_CType.CTFun([t],t2)

    def parseExprList(self,etk):
        args = list()
        tk = self.token()
        if (tk == etk):
            return args
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(tk,_this.head)
        while True:
            x = self.parseExpr()
            args.append(x)
            tk = self.token()
            if (tk is None):
                if (tk == etk):
                    break
                self.unexpected(tk)
                break
            elif (tk.index != 9):
                if (tk == etk):
                    break
                self.unexpected(tk)
                break
        return args

    def parseModule(self,content,origin = None):
        if (origin is None):
            origin = "hscript"
        self.initParser(origin)
        self.input = content
        self.readPos = 0
        self.allowTypes = True
        self.allowMetadata = True
        decls = []
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                break
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            x = self.parseModuleDecl()
            decls.append(x)
        return decls

    def parseMetadata(self):
        meta = []
        while True:
            tk = self.token()
            if (tk is None):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                break
            elif (tk.index == 15):
                name = tk.params[0]
                x = _hx_AnonObject({'name': name, 'params': self.parseMetaArgs()})
                meta.append(x)
            else:
                _this1 = self.tokens
                _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                break
        return meta

    def parseParams(self):
        if self.maybe(hscript_Token.TOp("<")):
            if (not self.resumeErrors):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp("Unsupported class type parameters"))
        return _hx_AnonObject({})

    def parseModuleDecl(self):
        meta = self.parseMetadata()
        ident = self.getIdent()
        isPrivate = False
        isExtern = False
        while True:
            ident1 = ident
            _hx_local_0 = len(ident1)
            if (_hx_local_0 == 7):
                if (ident1 == "private"):
                    isPrivate = True
                else:
                    break
            elif (_hx_local_0 == 6):
                if (ident1 == "extern"):
                    isExtern = True
                else:
                    break
            else:
                break
            ident = self.getIdent()
        ident1 = ident
        _hx_local_1 = len(ident1)
        if (_hx_local_1 == 5):
            if (ident1 == "class"):
                name = self.getIdent()
                params = self.parseParams()
                extend = None
                implement = []
                while True:
                    t = self.token()
                    if (t is None):
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                        break
                    elif (t.index == 2):
                        _g = t.params[0]
                        _hx_local_2 = len(_g)
                        if (_hx_local_2 == 10):
                            if (_g == "implements"):
                                x = self.parseType()
                                implement.append(x)
                            else:
                                _this1 = self.tokens
                                _this1.head = haxe_ds_GenericCell(t,_this1.head)
                                break
                        elif (_hx_local_2 == 7):
                            if (_g == "extends"):
                                extend = self.parseType()
                            else:
                                _this1 = self.tokens
                                _this1.head = haxe_ds_GenericCell(t,_this1.head)
                                break
                        else:
                            _this1 = self.tokens
                            _this1.head = haxe_ds_GenericCell(t,_this1.head)
                            break
                    else:
                        _this2 = self.tokens
                        _this2.head = haxe_ds_GenericCell(t,_this2.head)
                        break
                fields = []
                t = self.token()
                if (t != hscript_Token.TBrOpen):
                    self.unexpected(t)
                while (not self.maybe(hscript_Token.TBrClose)):
                    x = self.parseField()
                    fields.append(x)
                return hscript_ModuleDecl.DClass(_hx_AnonObject({'name': name, 'meta': meta, 'params': params, 'extend': extend, 'implement': implement, 'fields': fields, 'isPrivate': isPrivate, 'isExtern': isExtern}))
            else:
                self.unexpected(hscript_Token.TId(ident))
        elif (_hx_local_1 == 7):
            if (ident1 == "package"):
                path = self.parsePath()
                t = self.token()
                if (t != hscript_Token.TSemicolon):
                    self.unexpected(t)
                return hscript_ModuleDecl.DPackage(path)
            elif (ident1 == "typedef"):
                name = self.getIdent()
                params = self.parseParams()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TOp("="))):
                    self.unexpected(t)
                t = self.parseType()
                return hscript_ModuleDecl.DTypedef(_hx_AnonObject({'name': name, 'meta': meta, 'params': params, 'isPrivate': isPrivate, 't': t}))
            else:
                self.unexpected(hscript_Token.TId(ident))
        elif (_hx_local_1 == 6):
            if (ident1 == "import"):
                path = [self.getIdent()]
                star = False
                while True:
                    t = self.token()
                    if (t != hscript_Token.TDot):
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                        break
                    t = self.token()
                    if (t is None):
                        self.unexpected(t)
                    else:
                        tmp = t.index
                        if (tmp == 2):
                            id = t.params[0]
                            path.append(id)
                        elif (tmp == 3):
                            if (t.params[0] == "*"):
                                star = True
                            else:
                                self.unexpected(t)
                        else:
                            self.unexpected(t)
                t = self.token()
                if (t != hscript_Token.TSemicolon):
                    self.unexpected(t)
                return hscript_ModuleDecl.DImport(path,star)
            else:
                self.unexpected(hscript_Token.TId(ident))
        else:
            self.unexpected(hscript_Token.TId(ident))
        return None

    def parseField(self):
        meta = self.parseMetadata()
        access = []
        while True:
            id = self.getIdent()
            id1 = id
            _hx_local_0 = len(id1)
            if (_hx_local_0 == 5):
                if (id1 == "macro"):
                    access.append(hscript_FieldAccess.AMacro)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 7):
                if (id1 == "private"):
                    access.append(hscript_FieldAccess.APrivate)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 3):
                if (id1 == "var"):
                    name1 = self.getIdent()
                    get = None
                    _hx_set = None
                    if self.maybe(hscript_Token.TPOpen):
                        get = self.getIdent()
                        t = self.token()
                        if (t != hscript_Token.TComma):
                            self.unexpected(t)
                        _hx_set = self.getIdent()
                        t1 = self.token()
                        if (t1 != hscript_Token.TPClose):
                            self.unexpected(t1)
                    _hx_type = (self.parseType() if (self.maybe(hscript_Token.TDoubleDot)) else None)
                    expr = (self.parseExpr() if (self.maybe(hscript_Token.TOp("="))) else None)
                    if (expr is not None):
                        if self.isBlock(expr):
                            self.maybe(hscript_Token.TSemicolon)
                        else:
                            t2 = self.token()
                            if (t2 != hscript_Token.TSemicolon):
                                self.unexpected(t2)
                    else:
                        tmp = None
                        if (_hx_type is not None):
                            if (_hx_type is None):
                                tmp = False
                            elif (_hx_type.index == 2):
                                _g = _hx_type.params[0]
                                tmp = True
                            else:
                                tmp = False
                        else:
                            tmp = False
                        if tmp:
                            self.maybe(hscript_Token.TSemicolon)
                        else:
                            t3 = self.token()
                            if (t3 != hscript_Token.TSemicolon):
                                self.unexpected(t3)
                    return _hx_AnonObject({'name': name1, 'meta': meta, 'access': access, 'kind': hscript_FieldKind.KVar(_hx_AnonObject({'get': get, 'set': _hx_set, 'type': _hx_type, 'expr': expr}))})
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 8):
                if (id1 == "function"):
                    name = self.getIdent()
                    inf = self.parseFunctionDecl()
                    return _hx_AnonObject({'name': name, 'meta': meta, 'access': access, 'kind': hscript_FieldKind.KFunction(_hx_AnonObject({'args': inf.args, 'expr': inf.body, 'ret': inf.ret}))})
                elif (id1 == "override"):
                    access.append(hscript_FieldAccess.AOverride)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 6):
                if (id1 == "inline"):
                    access.append(hscript_FieldAccess.AInline)
                elif (id1 == "public"):
                    access.append(hscript_FieldAccess.APublic)
                elif (id1 == "static"):
                    access.append(hscript_FieldAccess.AStatic)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            else:
                self.unexpected(hscript_Token.TId(id))
                break
        return None

    def readChar(self):
        s = self.input
        index = self.readPos
        self.readPos = (self.readPos + 1)
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    def readString(self,until):
        c = 0
        b_b = python_lib_io_StringIO()
        esc = False
        old = self.line
        s = self.input
        while True:
            s = self.input
            index = self.readPos
            self.readPos = (self.readPos + 1)
            c = (-1 if ((index >= len(s))) else ord(s[index]))
            if (c == -1):
                self.line = old
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EUnterminatedString)
                break
            if esc:
                esc = False
                c1 = c
                if (((c1 == 92) or ((c1 == 39))) or ((c1 == 34))):
                    b_b.write("".join(map(chr,[c])))
                elif (c1 == 47):
                    if self.allowJSON:
                        b_b.write("".join(map(chr,[c])))
                    else:
                        self.invalidChar(c)
                elif (c1 == 110):
                    b_b.write("".join(map(chr,[10])))
                elif (c1 == 114):
                    b_b.write("".join(map(chr,[13])))
                elif (c1 == 116):
                    b_b.write("".join(map(chr,[9])))
                elif (c1 == 117):
                    if (not self.allowJSON):
                        self.invalidChar(c)
                    k = 0
                    _g = 0
                    while (_g < 4):
                        i = _g
                        _g = (_g + 1)
                        k = (k << 4)
                        s1 = self.input
                        index1 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                        char1 = char
                        if ((((((((((char1 == 57) or ((char1 == 56))) or ((char1 == 55))) or ((char1 == 54))) or ((char1 == 53))) or ((char1 == 52))) or ((char1 == 51))) or ((char1 == 50))) or ((char1 == 49))) or ((char1 == 48))):
                            k = (k + ((char - 48)))
                        elif ((((((char1 == 70) or ((char1 == 69))) or ((char1 == 68))) or ((char1 == 67))) or ((char1 == 66))) or ((char1 == 65))):
                            k = (k + ((char - 55)))
                        elif ((((((char1 == 102) or ((char1 == 101))) or ((char1 == 100))) or ((char1 == 99))) or ((char1 == 98))) or ((char1 == 97))):
                            k = (k + ((char - 87)))
                        else:
                            if (char == -1):
                                self.line = old
                                if (not self.resumeErrors):
                                    raise haxe_Exception.thrown(hscript_Error.EUnterminatedString)
                            self.invalidChar(char)
                    b_b.write("".join(map(chr,[k])))
                else:
                    self.invalidChar(c)
            elif (c == 92):
                esc = True
            elif (c == until):
                break
            else:
                if (c == 10):
                    _hx_local_4 = self
                    _hx_local_5 = _hx_local_4.line
                    _hx_local_4.line = (_hx_local_5 + 1)
                    _hx_local_5
                b_b.write("".join(map(chr,[c])))
        return b_b.getvalue()

    def token(self):
        if (self.tokens.head is not None):
            _this = self.tokens
            k = _this.head
            if (k is None):
                return None
            else:
                _this.head = k.next
                return k.elt
        char = None
        if (self.char < 0):
            s = self.input
            index = self.readPos
            self.readPos = (self.readPos + 1)
            char = (-1 if ((index >= len(s))) else ord(s[index]))
        else:
            char = self.char
            self.char = -1
        while True:
            if (char == -1):
                self.char = char
                return hscript_Token.TEof
            char1 = char
            if (char1 == 0):
                return hscript_Token.TEof
            elif (char1 == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.line
                _hx_local_0.line = (_hx_local_1 + 1)
                _hx_local_1
            elif (((char1 == 32) or ((char1 == 13))) or ((char1 == 9))):
                pass
            elif (char1 == 35):
                s = self.input
                index = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index >= len(s))) else ord(s[index]))
                if (self.idents[char] if char >= 0 and char < len(self.idents) else None):
                    id = "".join(map(chr,[char]))
                    while True:
                        s1 = self.input
                        index1 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return self.preprocess(id)
                        id = (("null" if id is None else id) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            elif ((char1 == 39) or ((char1 == 34))):
                return hscript_Token.TConst(hscript_Const.CString(self.readString(char)))
            elif (char1 == 40):
                return hscript_Token.TPOpen
            elif (char1 == 41):
                return hscript_Token.TPClose
            elif (char1 == 44):
                return hscript_Token.TComma
            elif (char1 == 46):
                s2 = self.input
                index2 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index2 >= len(s2))) else ord(s2[index2]))
                char2 = char
                if (char2 == 46):
                    s3 = self.input
                    index3 = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index3 >= len(s3))) else ord(s3[index3]))
                    if (char != 46):
                        self.invalidChar(char)
                    return hscript_Token.TOp("...")
                elif ((((((((((char2 == 57) or ((char2 == 56))) or ((char2 == 55))) or ((char2 == 54))) or ((char2 == 53))) or ((char2 == 52))) or ((char2 == 51))) or ((char2 == 50))) or ((char2 == 49))) or ((char2 == 48))):
                    n = (char - 48)
                    exp = 1
                    while True:
                        s4 = self.input
                        index4 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index4 >= len(s4))) else ord(s4[index4]))
                        exp = (exp * 10)
                        char3 = char
                        if ((((((((((char3 == 57) or ((char3 == 56))) or ((char3 == 55))) or ((char3 == 54))) or ((char3 == 53))) or ((char3 == 52))) or ((char3 == 51))) or ((char3 == 50))) or ((char3 == 49))) or ((char3 == 48))):
                            n = ((n * 10) + ((char - 48)))
                        else:
                            self.char = char
                            return hscript_Token.TConst(hscript_Const.CFloat((n / exp)))
                else:
                    self.char = char
                    return hscript_Token.TDot
            elif ((((((((((char1 == 57) or ((char1 == 56))) or ((char1 == 55))) or ((char1 == 54))) or ((char1 == 53))) or ((char1 == 52))) or ((char1 == 51))) or ((char1 == 50))) or ((char1 == 49))) or ((char1 == 48))):
                n1 = (((char - 48)) * 1.0)
                exp1 = 0.
                while True:
                    s5 = self.input
                    index5 = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index5 >= len(s5))) else ord(s5[index5]))
                    exp1 = (exp1 * 10)
                    char4 = char
                    if (char4 == 46):
                        if (exp1 > 0):
                            tmp = None
                            if (exp1 == 10):
                                s6 = self.input
                                index6 = self.readPos
                                self.readPos = (self.readPos + 1)
                                tmp = (((-1 if ((index6 >= len(s6))) else ord(s6[index6]))) == 46)
                            else:
                                tmp = False
                            if tmp:
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(hscript_Token.TOp("..."),_this.head)
                                i = None
                                try:
                                    i = int(n1)
                                except BaseException as _g:
                                    None
                                    i = None
                                i1 = i
                                return hscript_Token.TConst((hscript_Const.CInt(i1) if ((i1 == n1)) else hscript_Const.CFloat(n1)))
                            self.invalidChar(char)
                        exp1 = 1.
                    elif ((((((((((char4 == 57) or ((char4 == 56))) or ((char4 == 55))) or ((char4 == 54))) or ((char4 == 53))) or ((char4 == 52))) or ((char4 == 51))) or ((char4 == 50))) or ((char4 == 49))) or ((char4 == 48))):
                        n1 = ((n1 * 10) + ((char - 48)))
                    elif ((char4 == 101) or ((char4 == 69))):
                        tk = self.token()
                        pow = None
                        if (tk is None):
                            _this1 = self.tokens
                            _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                        else:
                            tmp1 = tk.index
                            if (tmp1 == 1):
                                _g1 = tk.params[0]
                                if (_g1.index == 0):
                                    e = _g1.params[0]
                                    pow = e
                                else:
                                    _this2 = self.tokens
                                    _this2.head = haxe_ds_GenericCell(tk,_this2.head)
                            elif (tmp1 == 3):
                                if (tk.params[0] == "-"):
                                    tk = self.token()
                                    if (tk is None):
                                        _this3 = self.tokens
                                        _this3.head = haxe_ds_GenericCell(tk,_this3.head)
                                    elif (tk.index == 1):
                                        _g2 = tk.params[0]
                                        if (_g2.index == 0):
                                            e1 = _g2.params[0]
                                            pow = -e1
                                        else:
                                            _this4 = self.tokens
                                            _this4.head = haxe_ds_GenericCell(tk,_this4.head)
                                    else:
                                        _this5 = self.tokens
                                        _this5.head = haxe_ds_GenericCell(tk,_this5.head)
                                else:
                                    _this6 = self.tokens
                                    _this6.head = haxe_ds_GenericCell(tk,_this6.head)
                            else:
                                _this7 = self.tokens
                                _this7.head = haxe_ds_GenericCell(tk,_this7.head)
                        if (pow is None):
                            self.invalidChar(char)
                        return hscript_Token.TConst(hscript_Const.CFloat((((Math.pow(10,pow) / exp1) * n1) * 10)))
                    elif (char4 == 120):
                        if ((n1 > 0) or ((exp1 > 0))):
                            self.invalidChar(char)
                        n2 = 0
                        while True:
                            s7 = self.input
                            index7 = self.readPos
                            self.readPos = (self.readPos + 1)
                            char = (-1 if ((index7 >= len(s7))) else ord(s7[index7]))
                            char5 = char
                            if ((((((((((char5 == 57) or ((char5 == 56))) or ((char5 == 55))) or ((char5 == 54))) or ((char5 == 53))) or ((char5 == 52))) or ((char5 == 51))) or ((char5 == 50))) or ((char5 == 49))) or ((char5 == 48))):
                                n2 = ((((n2 << 4)) + char) - 48)
                            elif ((((((char5 == 70) or ((char5 == 69))) or ((char5 == 68))) or ((char5 == 67))) or ((char5 == 66))) or ((char5 == 65))):
                                n2 = (((n2 << 4)) + ((char - 55)))
                            elif ((((((char5 == 102) or ((char5 == 101))) or ((char5 == 100))) or ((char5 == 99))) or ((char5 == 98))) or ((char5 == 97))):
                                n2 = (((n2 << 4)) + ((char - 87)))
                            else:
                                self.char = char
                                return hscript_Token.TConst(hscript_Const.CInt(n2))
                    else:
                        self.char = char
                        i2 = None
                        try:
                            i2 = int(n1)
                        except BaseException as _g3:
                            None
                            i2 = None
                        i3 = i2
                        return hscript_Token.TConst((hscript_Const.CFloat(((n1 * 10) / exp1)) if ((exp1 > 0)) else (hscript_Const.CInt(i3) if ((i3 == n1)) else hscript_Const.CFloat(n1))))
            elif (char1 == 58):
                return hscript_Token.TDoubleDot
            elif (char1 == 59):
                return hscript_Token.TSemicolon
            elif (char1 == 61):
                s8 = self.input
                index8 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index8 >= len(s8))) else ord(s8[index8]))
                if (char == 61):
                    return hscript_Token.TOp("==")
                elif (char == 62):
                    return hscript_Token.TOp("=>")
                self.char = char
                return hscript_Token.TOp("=")
            elif (char1 == 63):
                return hscript_Token.TQuestion
            elif (char1 == 64):
                s9 = self.input
                index9 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index9 >= len(s9))) else ord(s9[index9]))
                if ((self.idents[char] if char >= 0 and char < len(self.idents) else None) or ((char == 58))):
                    id1 = "".join(map(chr,[char]))
                    while True:
                        s10 = self.input
                        index10 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index10 >= len(s10))) else ord(s10[index10]))
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return hscript_Token.TMeta(id1)
                        id1 = (("null" if id1 is None else id1) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            elif (char1 == 91):
                return hscript_Token.TBkOpen
            elif (char1 == 93):
                return hscript_Token.TBkClose
            elif (char1 == 123):
                return hscript_Token.TBrOpen
            elif (char1 == 125):
                return hscript_Token.TBrClose
            else:
                if (self.ops[char] if char >= 0 and char < len(self.ops) else None):
                    op = "".join(map(chr,[char]))
                    while True:
                        s11 = self.input
                        index11 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index11 >= len(s11))) else ord(s11[index11]))
                        if (char == -1):
                            char = 0
                        if (not (self.ops[char] if char >= 0 and char < len(self.ops) else None)):
                            self.char = char
                            return hscript_Token.TOp(op)
                        pop = op
                        op = (("null" if op is None else op) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                        if ((not (op in self.opPriority.h)) and (pop in self.opPriority.h)):
                            if ((op == "//") or ((op == "/*"))):
                                return self.tokenComment(op,char)
                            self.char = char
                            return hscript_Token.TOp(pop)
                if (self.idents[char] if char >= 0 and char < len(self.idents) else None):
                    id2 = "".join(map(chr,[char]))
                    while True:
                        s12 = self.input
                        index12 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index12 >= len(s12))) else ord(s12[index12]))
                        if (char == -1):
                            char = 0
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return hscript_Token.TId(id2)
                        id2 = (("null" if id2 is None else id2) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            s13 = self.input
            index13 = self.readPos
            self.readPos = (self.readPos + 1)
            char = (-1 if ((index13 >= len(s13))) else ord(s13[index13]))

    def preprocValue(self,id):
        return self.preprocesorValues.h.get(id,None)

    def parsePreproCond(self):
        tk = self.token()
        if (tk is None):
            return self.unexpected(tk)
        else:
            tmp = tk.index
            if (tmp == 2):
                id = tk.params[0]
                return hscript_Expr.EIdent(id)
            elif (tmp == 3):
                if (tk.params[0] == "!"):
                    return hscript_Expr.EUnop("!",True,self.parsePreproCond())
                else:
                    return self.unexpected(tk)
            elif (tmp == 4):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(hscript_Token.TPOpen,_this.head)
                return self.parseExpr()
            else:
                return self.unexpected(tk)

    def evalPreproCond(self,e):
        tmp = e.index
        if (tmp == 1):
            id = e.params[0]
            return (self.preprocValue(id) is not None)
        elif (tmp == 3):
            e1 = e.params[0]
            return self.evalPreproCond(e1)
        elif (tmp == 6):
            _g = e.params[1]
            _g1 = e.params[2]
            _g2 = e.params[0]
            if (_g2 == "&&"):
                e1 = _g
                e2 = _g1
                if self.evalPreproCond(e1):
                    return self.evalPreproCond(e2)
                else:
                    return False
            elif (_g2 == "||"):
                e1 = _g
                e2 = _g1
                if (not self.evalPreproCond(e1)):
                    return self.evalPreproCond(e2)
                else:
                    return True
            else:
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
                return False
        elif (tmp == 7):
            _g = e.params[1]
            if (e.params[0] == "!"):
                e1 = e.params[2]
                return (not self.evalPreproCond(e1))
            else:
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
                return False
        else:
            if (not self.resumeErrors):
                raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
            return False

    def preprocess(self,id):
        id1 = id
        _hx_local_0 = len(id1)
        if (_hx_local_0 == 4):
            if (id1 == "else"):
                if (len(self.preprocStack) > 0):
                    if python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r:
                        python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r = False
                        self.skipTokens()
                        return self.token()
                    elif (id == "else"):
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        _this = self.preprocStack
                        _this.append(_hx_AnonObject({'r': True}))
                        return self.token()
                    else:
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        return self.preprocess("if")
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 3):
            if (id1 == "end"):
                if (len(self.preprocStack) > 0):
                    _this = self.preprocStack
                    if (len(_this) != 0):
                        _this.pop()
                    return self.token()
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 6):
            if (id1 == "elseif"):
                if (len(self.preprocStack) > 0):
                    if python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r:
                        python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r = False
                        self.skipTokens()
                        return self.token()
                    elif (id == "else"):
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        _this = self.preprocStack
                        _this.append(_hx_AnonObject({'r': True}))
                        return self.token()
                    else:
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        return self.preprocess("if")
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 2):
            if (id1 == "if"):
                e = self.parsePreproCond()
                if self.evalPreproCond(e):
                    _this = self.preprocStack
                    _this.append(_hx_AnonObject({'r': True}))
                    return self.token()
                _this = self.preprocStack
                _this.append(_hx_AnonObject({'r': False}))
                self.skipTokens()
                return self.token()
            else:
                return hscript_Token.TPrepro(id)
        else:
            return hscript_Token.TPrepro(id)

    def skipTokens(self):
        spos = (len(self.preprocStack) - 1)
        obj = (self.preprocStack[spos] if spos >= 0 and spos < len(self.preprocStack) else None)
        pos = self.readPos
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor("Unclosed"))
            if ((self.preprocStack[spos] if spos >= 0 and spos < len(self.preprocStack) else None) != obj):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                break

    def tokenComment(self,op,char):
        c = HxString.charCodeAt(op,1)
        s = self.input
        if (c == 47):
            while ((char != 13) and ((char != 10))):
                s = self.input
                index = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index >= len(s))) else ord(s[index]))
                if (char == -1):
                    break
            self.char = char
            return self.token()
        if (c == 42):
            old = self.line
            if (op == "/**/"):
                self.char = char
                return self.token()
            while True:
                while (char != 42):
                    if (char == 10):
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.line
                        _hx_local_0.line = (_hx_local_1 + 1)
                        _hx_local_1
                    s = self.input
                    index = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index >= len(s))) else ord(s[index]))
                    if (char == -1):
                        self.line = old
                        if (not self.resumeErrors):
                            raise haxe_Exception.thrown(hscript_Error.EUnterminatedComment)
                        break
                s1 = self.input
                index1 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                if (char == -1):
                    self.line = old
                    if (not self.resumeErrors):
                        raise haxe_Exception.thrown(hscript_Error.EUnterminatedComment)
                    break
                if (char == 47):
                    break
            return self.token()
        self.char = char
        return hscript_Token.TOp(op)

    def constString(self,c):
        tmp = c.index
        if (tmp == 0):
            v = c.params[0]
            return Std.string(v)
        elif (tmp == 1):
            f = c.params[0]
            return Std.string(f)
        elif (tmp == 2):
            s = c.params[0]
            return s
        else:
            pass

    def tokenString(self,t):
        tmp = t.index
        if (tmp == 0):
            return "<eof>"
        elif (tmp == 1):
            c = t.params[0]
            return self.constString(c)
        elif (tmp == 2):
            s = t.params[0]
            return s
        elif (tmp == 3):
            s = t.params[0]
            return s
        elif (tmp == 4):
            return "("
        elif (tmp == 5):
            return ")"
        elif (tmp == 6):
            return "{"
        elif (tmp == 7):
            return "}"
        elif (tmp == 8):
            return "."
        elif (tmp == 9):
            return ","
        elif (tmp == 10):
            return ";"
        elif (tmp == 11):
            return "["
        elif (tmp == 12):
            return "]"
        elif (tmp == 13):
            return "?"
        elif (tmp == 14):
            return ":"
        elif (tmp == 15):
            id = t.params[0]
            return ("@" + ("null" if id is None else id))
        elif (tmp == 16):
            id = t.params[0]
            return ("#" + ("null" if id is None else id))
        else:
            pass

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.line = None
        _hx_o.opChars = None
        _hx_o.identChars = None
        _hx_o.opPriority = None
        _hx_o.opRightAssoc = None
        _hx_o.preprocesorValues = None
        _hx_o.allowJSON = None
        _hx_o.allowTypes = None
        _hx_o.allowMetadata = None
        _hx_o.resumeErrors = None
        _hx_o.input = None
        _hx_o.readPos = None
        _hx_o.char = None
        _hx_o.ops = None
        _hx_o.idents = None
        _hx_o.uid = None
        _hx_o.tokens = None
        _hx_o.preprocStack = None
hscript_Parser._hx_class = hscript_Parser
globalClasses._hx_classes["hscript.Parser"] = hscript_Parser


class hscript_Printer:
    _hx_class_name = "hscript.Printer"
    __slots__ = ("buf", "tabs")
    _hx_fields = ["buf", "tabs"]
    _hx_methods = ["exprToString", "typeToString", "add", "type", "addType", "expr"]
    _hx_statics = ["toString", "errorToString"]

    def __init__(self):
        self.tabs = None
        self.buf = None

    def exprToString(self,e):
        self.buf = StringBuf()
        self.tabs = ""
        self.expr(e)
        return self.buf.b.getvalue()

    def typeToString(self,t):
        self.buf = StringBuf()
        self.tabs = ""
        self.type(t)
        return self.buf.b.getvalue()

    def add(self,s):
        _this = self.buf
        s1 = Std.string(s)
        _this.b.write(s1)

    def type(self,t):
        tmp = t.index
        if (tmp == 0):
            path = t.params[0]
            params = t.params[1]
            s = ".".join([python_Boot.toString1(x1,'') for x1 in path])
            _this = self.buf
            s1 = Std.string(s)
            _this.b.write(s1)
            if (params is not None):
                self.buf.b.write("<")
                first = True
                _g = 0
                while (_g < len(params)):
                    p = (params[_g] if _g >= 0 and _g < len(params) else None)
                    _g = (_g + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.type(p)
                self.buf.b.write(">")
        elif (tmp == 1):
            _g = t.params[0]
            _g1 = t.params[1]
            args = _g
            ret = _g1
            def _hx_local_1(a):
                if (a.index == 5):
                    _g = a.params[0]
                    _g = a.params[1]
                    return True
                else:
                    return False
            if Lambda.exists(args,_hx_local_1):
                self.buf.b.write("(")
                _g2 = 0
                while (_g2 < len(args)):
                    a = (args[_g2] if _g2 >= 0 and _g2 < len(args) else None)
                    _g2 = (_g2 + 1)
                    if (a.index == 5):
                        _g3 = a.params[0]
                        _g4 = a.params[1]
                        self.type(a)
                    else:
                        self.type(hscript_CType.CTNamed("_",a))
                self.buf.b.write(")->")
                self.type(ret)
            else:
                args = _g
                ret = _g1
                if (len(args) == 0):
                    self.buf.b.write("Void -> ")
                else:
                    _g = 0
                    while (_g < len(args)):
                        a = (args[_g] if _g >= 0 and _g < len(args) else None)
                        _g = (_g + 1)
                        self.type(a)
                        self.buf.b.write(" -> ")
                self.type(ret)
        elif (tmp == 2):
            fields = t.params[0]
            self.buf.b.write("{")
            first = True
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                if first:
                    first = False
                    self.buf.b.write(" ")
                else:
                    self.buf.b.write(", ")
                _this = self.buf
                s = Std.string((HxOverrides.stringOrNull(f.name) + " : "))
                _this.b.write(s)
                self.type(f.t)
            self.buf.b.write(("}" if first else " }"))
        elif (tmp == 3):
            t1 = t.params[0]
            self.buf.b.write("(")
            self.type(t1)
            self.buf.b.write(")")
        elif (tmp == 4):
            t1 = t.params[0]
            self.buf.b.write("?")
            self.type(t1)
        elif (tmp == 5):
            name = t.params[0]
            t1 = t.params[1]
            _this = self.buf
            s = Std.string(name)
            _this.b.write(s)
            self.buf.b.write(":")
            self.type(t1)
        else:
            pass

    def addType(self,t):
        if (t is not None):
            self.buf.b.write(" : ")
            self.type(t)

    def expr(self,e):
        if (e is None):
            self.buf.b.write("??NULL??")
            return
        tmp = e.index
        if (tmp == 0):
            c = e.params[0]
            tmp = c.index
            if (tmp == 0):
                i = c.params[0]
                _this = self.buf
                s = Std.string(i)
                _this.b.write(s)
            elif (tmp == 1):
                f = c.params[0]
                _this = self.buf
                s = Std.string(f)
                _this.b.write(s)
            elif (tmp == 2):
                s = c.params[0]
                self.buf.b.write("\"")
                _this = s.split("\"")
                _this1 = "\\\"".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\n")
                _this1 = "\\n".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\r")
                _this1 = "\\r".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\t")
                s = "\\t".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = self.buf
                s1 = Std.string(s)
                _this.b.write(s1)
                self.buf.b.write("\"")
            else:
                pass
        elif (tmp == 1):
            v = e.params[0]
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            _this = self.buf
            s = Std.string(("var " + ("null" if n is None else n)))
            _this.b.write(s)
            self.addType(t)
            if (e1 is not None):
                self.buf.b.write(" = ")
                self.expr(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            self.buf.b.write("(")
            self.expr(e1)
            self.buf.b.write(")")
        elif (tmp == 4):
            el = e.params[0]
            if (len(el) == 0):
                self.buf.b.write("{}")
            else:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.tabs
                _hx_local_0.tabs = (("null" if _hx_local_1 is None else _hx_local_1) + "\t")
                _hx_local_0.tabs
                self.buf.b.write("{\n")
                _g = 0
                while (_g < len(el)):
                    e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                    _g = (_g + 1)
                    _this = self.buf
                    s = Std.string(self.tabs)
                    _this.b.write(s)
                    self.expr(e1)
                    self.buf.b.write(";\n")
                self.tabs = HxString.substr(self.tabs,1,None)
                self.buf.b.write("}")
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            self.expr(e1)
            _this = self.buf
            s = Std.string(("." + ("null" if f is None else f)))
            _this.b.write(s)
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.expr(e1)
            _this = self.buf
            s = Std.string(((" " + ("null" if op is None else op)) + " "))
            _this.b.write(s)
            self.expr(e2)
        elif (tmp == 7):
            op = e.params[0]
            pre = e.params[1]
            e1 = e.params[2]
            if pre:
                _this = self.buf
                s = Std.string(op)
                _this.b.write(s)
                self.expr(e1)
            else:
                self.expr(e1)
                _this = self.buf
                s = Std.string(op)
                _this.b.write(s)
        elif (tmp == 8):
            e1 = e.params[0]
            args = e.params[1]
            if (e1 is None):
                self.expr(e1)
            else:
                tmp = e1.index
                if (tmp == 0):
                    _g = e1.params[0]
                    self.expr(e1)
                elif (tmp == 1):
                    _g = e1.params[0]
                    self.expr(e1)
                elif (tmp == 5):
                    _g = e1.params[0]
                    _g = e1.params[1]
                    self.expr(e1)
                else:
                    self.buf.b.write("(")
                    self.expr(e1)
                    self.buf.b.write(")")
            self.buf.b.write("(")
            first = True
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(a)
            self.buf.b.write(")")
        elif (tmp == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.buf.b.write("if( ")
            self.expr(cond)
            self.buf.b.write(" ) ")
            self.expr(e1)
            if (e2 is not None):
                self.buf.b.write(" else ")
                self.expr(e2)
        elif (tmp == 10):
            cond = e.params[0]
            e1 = e.params[1]
            self.buf.b.write("while( ")
            self.expr(cond)
            self.buf.b.write(" ) ")
            self.expr(e1)
        elif (tmp == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            _this = self.buf
            s = Std.string((("for( " + ("null" if v is None else v)) + " in "))
            _this.b.write(s)
            self.expr(it)
            self.buf.b.write(" ) ")
            self.expr(e1)
        elif (tmp == 12):
            self.buf.b.write("break")
        elif (tmp == 13):
            self.buf.b.write("continue")
        elif (tmp == 14):
            params = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            ret = e.params[3]
            self.buf.b.write("function")
            if (name is not None):
                _this = self.buf
                s = Std.string((" " + ("null" if name is None else name)))
                _this.b.write(s)
            self.buf.b.write("(")
            first = True
            _g = 0
            while (_g < len(params)):
                a = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                if Reflect.field(a,"opt"):
                    self.buf.b.write("?")
                _this = self.buf
                s = Std.string(a.name)
                _this.b.write(s)
                self.addType(Reflect.field(a,"t"))
            self.buf.b.write(")")
            self.addType(ret)
            self.buf.b.write(" ")
            self.expr(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            self.buf.b.write("return")
            if (e1 is not None):
                self.buf.b.write(" ")
                self.expr(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            self.expr(e1)
            self.buf.b.write("[")
            self.expr(index)
            self.buf.b.write("]")
        elif (tmp == 17):
            el = e.params[0]
            self.buf.b.write("[")
            first = True
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(e1)
            self.buf.b.write("]")
        elif (tmp == 18):
            cl = e.params[0]
            args = e.params[1]
            _this = self.buf
            s = Std.string((("new " + ("null" if cl is None else cl)) + "("))
            _this.b.write(s)
            first = True
            _g = 0
            while (_g < len(args)):
                e1 = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(e1)
            self.buf.b.write(")")
        elif (tmp == 19):
            e1 = e.params[0]
            self.buf.b.write("throw ")
            self.expr(e1)
        elif (tmp == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            ecatch = e.params[3]
            self.buf.b.write("try ")
            self.expr(e1)
            _this = self.buf
            s = Std.string((" catch( " + ("null" if v is None else v)))
            _this.b.write(s)
            self.addType(t)
            self.buf.b.write(") ")
            self.expr(ecatch)
        elif (tmp == 21):
            fl = e.params[0]
            if (len(fl) == 0):
                self.buf.b.write("{}")
            else:
                _hx_local_7 = self
                _hx_local_8 = _hx_local_7.tabs
                _hx_local_7.tabs = (("null" if _hx_local_8 is None else _hx_local_8) + "\t")
                _hx_local_7.tabs
                self.buf.b.write("{\n")
                _g = 0
                while (_g < len(fl)):
                    f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                    _g = (_g + 1)
                    _this = self.buf
                    s = Std.string(self.tabs)
                    _this.b.write(s)
                    _this1 = self.buf
                    s1 = Std.string((HxOverrides.stringOrNull(f.name) + " : "))
                    _this1.b.write(s1)
                    self.expr(f.e)
                    self.buf.b.write(",\n")
                self.tabs = HxString.substr(self.tabs,1,None)
                self.buf.b.write("}")
        elif (tmp == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.expr(c)
            self.buf.b.write(" ? ")
            self.expr(e1)
            self.buf.b.write(" : ")
            self.expr(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            self.buf.b.write("switch( ")
            self.expr(e1)
            self.buf.b.write(") {")
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                self.buf.b.write("case ")
                first = True
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.expr(v)
                self.buf.b.write(": ")
                self.expr(c.expr)
                self.buf.b.write(";\n")
            if (_hx_def is not None):
                self.buf.b.write("default: ")
                self.expr(_hx_def)
                self.buf.b.write(";\n")
            self.buf.b.write("}")
        elif (tmp == 24):
            cond = e.params[0]
            e1 = e.params[1]
            self.buf.b.write("do ")
            self.expr(e1)
            self.buf.b.write(" while ( ")
            self.expr(cond)
            self.buf.b.write(" )")
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            self.buf.b.write("@")
            _this = self.buf
            s = Std.string(name)
            _this.b.write(s)
            if ((args is not None) and ((len(args) > 0))):
                self.buf.b.write("(")
                first = True
                _g = 0
                while (_g < len(args)):
                    a = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.expr(e1)
                self.buf.b.write(")")
            self.buf.b.write(" ")
            self.expr(e1)
        elif (tmp == 26):
            e1 = e.params[0]
            t = e.params[1]
            self.buf.b.write("(")
            self.expr(e1)
            self.buf.b.write(" : ")
            self.addType(t)
            self.buf.b.write(")")
        else:
            pass

    @staticmethod
    def toString(e):
        return hscript_Printer().exprToString(e)

    @staticmethod
    def errorToString(e):
        message = None
        message1 = e.index
        if (message1 == 0):
            c = e.params[0]
            message = (((("Invalid character: '" + HxOverrides.stringOrNull((("EOF" if ((c == -1)) else "".join(map(chr,[c])))))) + "' (") + Std.string(c)) + ")")
        elif (message1 == 1):
            s = e.params[0]
            message = (("Unexpected token: \"" + ("null" if s is None else s)) + "\"")
        elif (message1 == 2):
            message = "Unterminated string"
        elif (message1 == 3):
            message = "Unterminated comment"
        elif (message1 == 4):
            _hx_str = e.params[0]
            message = (("Invalid preprocessor (" + ("null" if _hx_str is None else _hx_str)) + ")")
        elif (message1 == 5):
            v = e.params[0]
            message = ("Unknown variable: " + ("null" if v is None else v))
        elif (message1 == 6):
            v = e.params[0]
            message = ("Invalid iterator: " + ("null" if v is None else v))
        elif (message1 == 7):
            op = e.params[0]
            message = ("Invalid operator: " + ("null" if op is None else op))
        elif (message1 == 8):
            f = e.params[0]
            message = ("Invalid access to field " + ("null" if f is None else f))
        elif (message1 == 9):
            msg = e.params[0]
            message = msg
        else:
            pass
        return message

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buf = None
        _hx_o.tabs = None
hscript_Printer._hx_class = hscript_Printer
globalClasses._hx_classes["hscript.Printer"] = hscript_Printer


class hscript_TType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.TType"
    _hx_constructs = ["TMono", "TVoid", "TInt", "TFloat", "TBool", "TDynamic", "TParam", "TUnresolved", "TNull", "TInst", "TEnum", "TType", "TAbstract", "TFun", "TAnon", "TLazy"]

    @staticmethod
    def TMono(r):
        return hscript_TType("TMono", 0, (r,))

    @staticmethod
    def TParam(name):
        return hscript_TType("TParam", 6, (name,))

    @staticmethod
    def TUnresolved(name):
        return hscript_TType("TUnresolved", 7, (name,))

    @staticmethod
    def TNull(t):
        return hscript_TType("TNull", 8, (t,))

    @staticmethod
    def TInst(c,args):
        return hscript_TType("TInst", 9, (c,args))

    @staticmethod
    def TEnum(e,args):
        return hscript_TType("TEnum", 10, (e,args))

    @staticmethod
    def TType(t,args):
        return hscript_TType("TType", 11, (t,args))

    @staticmethod
    def TAbstract(a,args):
        return hscript_TType("TAbstract", 12, (a,args))

    @staticmethod
    def TFun(args,ret):
        return hscript_TType("TFun", 13, (args,ret))

    @staticmethod
    def TAnon(fields):
        return hscript_TType("TAnon", 14, (fields,))

    @staticmethod
    def TLazy(f):
        return hscript_TType("TLazy", 15, (f,))
hscript_TType.TVoid = hscript_TType("TVoid", 1, ())
hscript_TType.TInt = hscript_TType("TInt", 2, ())
hscript_TType.TFloat = hscript_TType("TFloat", 3, ())
hscript_TType.TBool = hscript_TType("TBool", 4, ())
hscript_TType.TDynamic = hscript_TType("TDynamic", 5, ())
hscript_TType._hx_class = hscript_TType
globalClasses._hx_classes["hscript.TType"] = hscript_TType

class hscript_Token(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Token"
    _hx_constructs = ["TEof", "TConst", "TId", "TOp", "TPOpen", "TPClose", "TBrOpen", "TBrClose", "TDot", "TComma", "TSemicolon", "TBkOpen", "TBkClose", "TQuestion", "TDoubleDot", "TMeta", "TPrepro"]

    @staticmethod
    def TConst(c):
        return hscript_Token("TConst", 1, (c,))

    @staticmethod
    def TId(s):
        return hscript_Token("TId", 2, (s,))

    @staticmethod
    def TOp(s):
        return hscript_Token("TOp", 3, (s,))

    @staticmethod
    def TMeta(s):
        return hscript_Token("TMeta", 15, (s,))

    @staticmethod
    def TPrepro(s):
        return hscript_Token("TPrepro", 16, (s,))
hscript_Token.TEof = hscript_Token("TEof", 0, ())
hscript_Token.TPOpen = hscript_Token("TPOpen", 4, ())
hscript_Token.TPClose = hscript_Token("TPClose", 5, ())
hscript_Token.TBrOpen = hscript_Token("TBrOpen", 6, ())
hscript_Token.TBrClose = hscript_Token("TBrClose", 7, ())
hscript_Token.TDot = hscript_Token("TDot", 8, ())
hscript_Token.TComma = hscript_Token("TComma", 9, ())
hscript_Token.TSemicolon = hscript_Token("TSemicolon", 10, ())
hscript_Token.TBkOpen = hscript_Token("TBkOpen", 11, ())
hscript_Token.TBkClose = hscript_Token("TBkClose", 12, ())
hscript_Token.TQuestion = hscript_Token("TQuestion", 13, ())
hscript_Token.TDoubleDot = hscript_Token("TDoubleDot", 14, ())
hscript_Token._hx_class = hscript_Token
globalClasses._hx_classes["hscript.Token"] = hscript_Token


class hscript_Tools:
    _hx_class_name = "hscript.Tools"
    __slots__ = ()
    _hx_statics = ["iter", "map", "expr", "mk"]

    @staticmethod
    def iter(e,f):
        tmp = e.index
        if (tmp == 0):
            _g = e.params[0]
        elif (tmp == 1):
            _g = e.params[0]
        elif (tmp == 2):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            if (e1 is not None):
                f(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            f(e1)
        elif (tmp == 4):
            el = e.params[0]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 5):
            _g = e.params[1]
            e1 = e.params[0]
            f(e1)
        elif (tmp == 6):
            _g = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(e1)
            f(e2)
        elif (tmp == 7):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            f(e1)
        elif (tmp == 8):
            e1 = e.params[0]
            args = e.params[1]
            f(e1)
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                f(a)
        elif (tmp == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(c)
            f(e1)
            if (e2 is not None):
                f(e2)
        elif (tmp == 10):
            c = e.params[0]
            e1 = e.params[1]
            f(c)
            f(e1)
        elif (tmp == 11):
            _g = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            f(it)
            f(e1)
        elif ((tmp == 13) or ((tmp == 12))):
            pass
        elif (tmp == 14):
            _g = e.params[0]
            _g = e.params[2]
            _g = e.params[3]
            e1 = e.params[1]
            f(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is not None):
                f(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            i = e.params[1]
            f(e1)
            f(i)
        elif (tmp == 17):
            el = e.params[0]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 18):
            _g = e.params[0]
            el = e.params[1]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 19):
            e1 = e.params[0]
            f(e1)
        elif (tmp == 20):
            _g = e.params[1]
            _g = e.params[2]
            e1 = e.params[0]
            c = e.params[3]
            f(e1)
            f(c)
        elif (tmp == 21):
            fl = e.params[0]
            _g = 0
            while (_g < len(fl)):
                fi = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                f(fi.e)
        elif (tmp == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(c)
            f(e1)
            f(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            f(e1)
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    f(v)
                f(c.expr)
            if (_hx_def is not None):
                f(_hx_def)
        elif (tmp == 24):
            c = e.params[0]
            e1 = e.params[1]
            f(c)
            f(e1)
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    a = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    f(a)
            f(e1)
        elif (tmp == 26):
            _g = e.params[1]
            e1 = e.params[0]
            f(e1)
        else:
            pass

    @staticmethod
    def map(e,f):
        edef = None
        edef1 = e.index
        if (edef1 == 0):
            _g = e.params[0]
            edef = e
        elif (edef1 == 1):
            _g = e.params[0]
            edef = e
        elif (edef1 == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EVar(n,t,(f(e1) if ((e1 is not None)) else None))
        elif (edef1 == 3):
            e1 = e.params[0]
            edef = hscript_Expr.EParent(f(e1))
        elif (edef1 == 4):
            el = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.EBlock(_g)
        elif (edef1 == 5):
            e1 = e.params[0]
            fi = e.params[1]
            edef = hscript_Expr.EField(f(e1),fi)
        elif (edef1 == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EBinop(op,f(e1),f(e2))
        elif (edef1 == 7):
            op = e.params[0]
            pre = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EUnop(op,pre,f(e1))
        elif (edef1 == 8):
            e1 = e.params[0]
            args = e.params[1]
            edef1 = f(e1)
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = f(a)
                _g.append(x)
            edef = hscript_Expr.ECall(edef1,_g)
        elif (edef1 == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EIf(f(c),f(e1),(f(e2) if ((e2 is not None)) else None))
        elif (edef1 == 10):
            c = e.params[0]
            e1 = e.params[1]
            edef = hscript_Expr.EWhile(f(c),f(e1))
        elif (edef1 == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EFor(v,f(it),f(e1))
        elif ((edef1 == 13) or ((edef1 == 12))):
            edef = e
        elif (edef1 == 14):
            args = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            t = e.params[3]
            edef = hscript_Expr.EFunction(args,f(e1),name,t)
        elif (edef1 == 15):
            e1 = e.params[0]
            edef = hscript_Expr.EReturn((f(e1) if ((e1 is not None)) else None))
        elif (edef1 == 16):
            e1 = e.params[0]
            i = e.params[1]
            edef = hscript_Expr.EArray(f(e1),f(i))
        elif (edef1 == 17):
            el = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.EArrayDecl(_g)
        elif (edef1 == 18):
            cl = e.params[0]
            el = e.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.ENew(cl,_g)
        elif (edef1 == 19):
            e1 = e.params[0]
            edef = hscript_Expr.EThrow(f(e1))
        elif (edef1 == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            c = e.params[3]
            edef = hscript_Expr.ETry(f(e1),v,t,f(c))
        elif (edef1 == 21):
            fl = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fl)):
                fi = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': fi.name, 'e': f(fi.e)})
                _g.append(x)
            edef = hscript_Expr.EObject(_g)
        elif (edef1 == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.ETernary(f(c),f(e1),f(e2))
        elif (edef1 == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            edef1 = f(e1)
            _g = []
            _g1 = 0
            while (_g1 < len(cases)):
                c = (cases[_g1] if _g1 >= 0 and _g1 < len(cases) else None)
                _g1 = (_g1 + 1)
                _g2 = []
                _g3 = 0
                _g4 = c.values
                while (_g3 < len(_g4)):
                    v = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                    _g3 = (_g3 + 1)
                    x = f(v)
                    _g2.append(x)
                x1 = _hx_AnonObject({'values': _g2, 'expr': f(c.expr)})
                _g.append(x1)
            edef = hscript_Expr.ESwitch(edef1,_g,(None if ((_hx_def is None)) else f(_hx_def)))
        elif (edef1 == 24):
            c = e.params[0]
            e1 = e.params[1]
            edef = hscript_Expr.EDoWhile(f(c),f(e1))
        elif (edef1 == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            edef1 = None
            if (args is None):
                edef1 = None
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(a)
                    _g.append(x)
                edef1 = _g
            edef = hscript_Expr.EMeta(name,edef1,f(e1))
        elif (edef1 == 26):
            e1 = e.params[0]
            t = e.params[1]
            edef = hscript_Expr.ECheckType(f(e1),t)
        else:
            pass
        return edef

    @staticmethod
    def expr(e):
        return e

    @staticmethod
    def mk(e,p):
        return e
hscript_Tools._hx_class = hscript_Tools
globalClasses._hx_classes["hscript.Tools"] = hscript_Tools


class hscript_VarMode(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.VarMode"
    _hx_constructs = ["Defined", "ForceSync"]
hscript_VarMode.Defined = hscript_VarMode("Defined", 0, ())
hscript_VarMode.ForceSync = hscript_VarMode("ForceSync", 1, ())
hscript_VarMode._hx_class = hscript_VarMode
globalClasses._hx_classes["hscript.VarMode"] = hscript_VarMode

class hscript__Checker_WithType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript._Checker.WithType"
    _hx_constructs = ["NoValue", "Value", "WithType"]

    @staticmethod
    def WithType(t):
        return hscript__Checker_WithType("WithType", 2, (t,))
hscript__Checker_WithType.NoValue = hscript__Checker_WithType("NoValue", 0, ())
hscript__Checker_WithType.Value = hscript__Checker_WithType("Value", 1, ())
hscript__Checker_WithType._hx_class = hscript__Checker_WithType
globalClasses._hx_classes["hscript._Checker.WithType"] = hscript__Checker_WithType

class hscript__Interp_Stop(Enum):
    __slots__ = ()
    _hx_class_name = "hscript._Interp.Stop"
    _hx_constructs = ["SBreak", "SContinue", "SReturn"]
hscript__Interp_Stop.SBreak = hscript__Interp_Stop("SBreak", 0, ())
hscript__Interp_Stop.SContinue = hscript__Interp_Stop("SContinue", 1, ())
hscript__Interp_Stop.SReturn = hscript__Interp_Stop("SReturn", 2, ())
hscript__Interp_Stop._hx_class = hscript__Interp_Stop
globalClasses._hx_classes["hscript._Interp.Stop"] = hscript__Interp_Stop


anon.classesinmodule(sys.modules[__name__])
