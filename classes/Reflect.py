class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "isClosure", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

    @staticmethod
    def hasField(o,field):
        return python_Boot.hasField(o,field)

    @staticmethod
    def field(o,field):
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def getProperty(o,field):
        if (o is None):
            return None
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if isinstance(o,_hx_AnonObject):
            return Reflect.field(o,field)
        tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
        if ((tmp is not None) and callable(tmp)):
            return tmp()
        else:
            return Reflect.field(o,field)

    @staticmethod
    def setProperty(o,field,value):
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if isinstance(o,_hx_AnonObject):
            setattr(o,field1,value)
        elif hasattr(o,("set_" + ("null" if field1 is None else field1))):
            getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
        else:
            setattr(o,field1,value)

    @staticmethod
    def callMethod(o,func,args):
        if callable(func):
            return func(*args)
        else:
            return None

    @staticmethod
    def fields(o):
        return python_Boot.fields(o)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1

    @staticmethod
    def isClosure(v):
        return isinstance(v,python_internal_MethodClosure)

    @staticmethod
    def compareMethods(f1,f2):
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False

    @staticmethod
    def isObject(v):
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 4):
            return True
        elif (tmp == 6):
            _g1 = _g.params[0]
            return True
        else:
            return False

    @staticmethod
    def isEnumValue(v):
        if not HxOverrides.eq(v,Enum):
            return isinstance(v,Enum)
        else:
            return False

    @staticmethod
    def deleteField(o,field):
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if (not python_Boot.hasField(o,field)):
            return False
        o.__delattr__(field)
        return True

    @staticmethod
    def copy(o):
        if (o is None):
            return None
        o2 = _hx_AnonObject({})
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        return o2

    @staticmethod
    def makeVarArgs(f):
        def _hx_local_0(*v):
            this1 = v
            return f((list(this1) if ((not Std.isOfType(this1,list))) else this1))
        return _hx_local_0
Reflect._hx_class = Reflect
_hx_classes["Reflect"] = Reflect


