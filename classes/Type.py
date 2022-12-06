class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def getEnum(o):
        if (o is None):
            return None
        return o.__class__

    @staticmethod
    def getSuperClass(c):
        return python_Boot.getSuperClass(c)

    @staticmethod
    def getClassName(c):
        if hasattr(c,"_hx_class_name"):
            return c._hx_class_name
        else:
            if (c == list):
                return "Array"
            if (c == Math):
                return "Math"
            if (c == str):
                return "String"
            try:
                return c.__name__
            except BaseException as _g:
                None
                return None

    @staticmethod
    def getEnumName(e):
        return e._hx_class_name

    @staticmethod
    def resolveClass(name):
        if (name == "Array"):
            return list
        if (name == "Math"):
            return Math
        if (name == "String"):
            return str
        cl = _hx_classes.get(name,None)
        tmp = None
        if (cl is not None):
            o = cl
            tmp = (not (((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))))
        else:
            tmp = True
        if tmp:
            return None
        return cl

    @staticmethod
    def resolveEnum(name):
        if (name == "Bool"):
            return Bool
        o = Type.resolveClass(name)
        if hasattr(o,"_hx_constructs"):
            return o
        else:
            return None

    @staticmethod
    def createInstance(cl,args):
        return cl(*args)

    @staticmethod
    def createEmptyInstance(cl):
        i = cl.__new__(cl)
        callInit = None
        def _hx_local_0(cl):
            sc = Type.getSuperClass(cl)
            if (sc is not None):
                callInit(sc)
            if hasattr(cl,"_hx_empty_init"):
                cl._hx_empty_init(i)
        callInit = _hx_local_0
        callInit(cl)
        return i

    @staticmethod
    def createEnum(e,constr,params = None):
        f = Reflect.field(e,constr)
        if (f is None):
            raise haxe_Exception.thrown(("No such constructor " + ("null" if constr is None else constr)))
        if Reflect.isFunction(f):
            if (params is None):
                raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
            return Reflect.callMethod(e,f,params)
        if ((params is not None) and ((len(params) != 0))):
            raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
        return f

    @staticmethod
    def createEnumIndex(e,index,params = None):
        c = python_internal_ArrayImpl._get(e._hx_constructs, index)
        if (c is None):
            raise haxe_Exception.thrown((Std.string(index) + " is not a valid enum constructor index"))
        return Type.createEnum(e,c,params)

    @staticmethod
    def getInstanceFields(c):
        return python_Boot.getInstanceFields(c)

    @staticmethod
    def getClassFields(c):
        return python_Boot.getClassFields(c)

    @staticmethod
    def getEnumConstructs(e):
        if hasattr(e,"_hx_constructs"):
            x = e._hx_constructs
            return list(x)
        else:
            return []

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown

    @staticmethod
    def asEnumImpl(x):
        return x

    @staticmethod
    def enumEq(a,b):
        if HxOverrides.eq(a,b):
            return True
        try:
            if ((b is None) and (not HxOverrides.eq(a,b))):
                return False
            if (a.tag != b.tag):
                return False
            p1 = a.params
            p2 = b.params
            if (len(p1) != len(p2)):
                return False
            _g = 0
            _g1 = len(p1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not Type.enumEq(p1[i],p2[i])):
                    return False
            if (a._hx_class != b._hx_class):
                return False
        except BaseException as _g:
            None
            return False
        return True

    @staticmethod
    def enumConstructor(e):
        return e.tag

    @staticmethod
    def enumParameters(e):
        return list(e.params)

    @staticmethod
    def enumIndex(e):
        return e.index

    @staticmethod
    def allEnums(e):
        ctors = Type.getEnumConstructs(e)
        ret = []
        _g = 0
        while (_g < len(ctors)):
            ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
            _g = (_g + 1)
            v = Reflect.field(e,ctor)
            if Std.isOfType(v,e):
                ret.append(v)
        return ret
Type._hx_class = Type
_hx_classes["Type"] = Type


