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
_hx_classes["hscript.AsyncInterp"] = hscript_AsyncInterp


