class haxe_rtti_CTypeTools:
    _hx_class_name = "haxe.rtti.CTypeTools"
    __slots__ = ()
    _hx_statics = ["toString", "nameWithParams", "functionArgumentName", "classField"]

    @staticmethod
    def toString(t):
        tmp = t.index
        if (tmp == 0):
            return "unknown"
        elif (tmp == 1):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 2):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 3):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 4):
            args = t.params[0]
            ret = t.params[1]
            if (len(args) == 0):
                return ("Void -> " + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(ret)))
            else:
                _this = list(map(haxe_rtti_CTypeTools.functionArgumentName,args))
                return ((HxOverrides.stringOrNull(" -> ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " -> ") + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(ret)))
        elif (tmp == 5):
            fields = t.params[0]
            _this = list(map(haxe_rtti_CTypeTools.classField,fields))
            return (("{ " + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "}")
        elif (tmp == 6):
            d = t.params[0]
            if (d is None):
                return "Dynamic"
            else:
                return (("Dynamic<" + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(d))) + ">")
        elif (tmp == 7):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        else:
            pass

    @staticmethod
    def nameWithParams(name,params):
        if (len(params) == 0):
            return name
        _this = list(map(haxe_rtti_CTypeTools.toString,params))
        return (((("null" if name is None else name) + "<") + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")

    @staticmethod
    def functionArgumentName(arg):
        return (((HxOverrides.stringOrNull((("?" if (arg.opt) else ""))) + HxOverrides.stringOrNull((("" if ((arg.name == "")) else (HxOverrides.stringOrNull(arg.name) + ":"))))) + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(arg.t))) + HxOverrides.stringOrNull((("" if ((Reflect.field(arg,"value") is None)) else (" = " + HxOverrides.stringOrNull(Reflect.field(arg,"value")))))))

    @staticmethod
    def classField(cf):
        return ((HxOverrides.stringOrNull(cf.name) + ":") + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(cf.type)))
haxe_rtti_CTypeTools._hx_class = haxe_rtti_CTypeTools
_hx_classes["haxe.rtti.CTypeTools"] = haxe_rtti_CTypeTools


