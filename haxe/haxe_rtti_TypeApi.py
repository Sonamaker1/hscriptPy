class haxe_rtti_TypeApi:
    _hx_class_name = "haxe.rtti.TypeApi"
    __slots__ = ()
    _hx_statics = ["typeInfos", "isVar", "leq", "rightsEq", "typeEq", "fieldEq", "constructorEq"]

    @staticmethod
    def typeInfos(t):
        inf = None
        tmp = t.index
        if (tmp == 0):
            _g = t.params[0]
            _g = t.params[1]
            _g = t.params[2]
            raise haxe_Exception.thrown("Unexpected Package")
        elif (tmp == 1):
            c = t.params[0]
            inf = c
        elif (tmp == 2):
            e = t.params[0]
            inf = e
        elif (tmp == 3):
            t1 = t.params[0]
            inf = t1
        elif (tmp == 4):
            a = t.params[0]
            inf = a
        else:
            pass
        return inf

    @staticmethod
    def isVar(t):
        if (t.index == 4):
            _g = t.params[0]
            _g = t.params[1]
            return False
        else:
            return True

    @staticmethod
    def leq(f,l1,l2):
        it_current = 0
        it_array = l2
        _g = 0
        while (_g < len(l1)):
            e1 = (l1[_g] if _g >= 0 and _g < len(l1) else None)
            _g = (_g + 1)
            if (it_current >= len(it_array)):
                return False
            e2 = it_current
            it_current = (it_current + 1)
            e21 = (it_array[e2] if e2 >= 0 and e2 < len(it_array) else None)
            if (not f(e1,e21)):
                return False
        if (it_current < len(it_array)):
            return False
        return True

    @staticmethod
    def rightsEq(r1,r2):
        if (r1 == r2):
            return True
        if (r1.index == 2):
            m1 = r1.params[0]
            if (r2.index == 2):
                m2 = r2.params[0]
                return (m1 == m2)
        return False

    @staticmethod
    def typeEq(t1,t2):
        tmp = t1.index
        if (tmp == 0):
            return (t2 == haxe_rtti_CType.CUnknown)
        elif (tmp == 1):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 1):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 2):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 2):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 3):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 3):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 4):
            args = t1.params[0]
            ret = t1.params[1]
            if (t2.index == 4):
                args2 = t2.params[0]
                ret2 = t2.params[1]
                def _hx_local_0(a,b):
                    if ((a.name == b.name) and ((a.opt == b.opt))):
                        return haxe_rtti_TypeApi.typeEq(a.t,b.t)
                    else:
                        return False
                if haxe_rtti_TypeApi.leq(_hx_local_0,args,args2):
                    return haxe_rtti_TypeApi.typeEq(ret,ret2)
                else:
                    return False
        elif (tmp == 5):
            fields = t1.params[0]
            if (t2.index == 5):
                fields2 = t2.params[0]
                def _hx_local_2():
                    def _hx_local_1(a,b):
                        return haxe_rtti_TypeApi.fieldEq(a,b)
                    return haxe_rtti_TypeApi.leq(_hx_local_1,fields,fields2)
                return _hx_local_2()
        elif (tmp == 6):
            t = t1.params[0]
            if (t2.index == 6):
                t21 = t2.params[0]
                if ((t is None) != ((t21 is None))):
                    return False
                if (t is not None):
                    return haxe_rtti_TypeApi.typeEq(t,t21)
                else:
                    return True
        elif (tmp == 7):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 7):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        else:
            pass
        return False

    @staticmethod
    def fieldEq(f1,f2):
        if (f1.name != f2.name):
            return False
        if (not haxe_rtti_TypeApi.typeEq(f1.type,f2.type)):
            return False
        if (f1.isPublic != f2.isPublic):
            return False
        if (f1.doc != f2.doc):
            return False
        if (not haxe_rtti_TypeApi.rightsEq(f1.get,f2.get)):
            return False
        if (not haxe_rtti_TypeApi.rightsEq(f1.set,f2.set)):
            return False
        if ((f1.params is None) != ((f2.params is None))):
            return False
        tmp = None
        if (f1.params is not None):
            _this = f1.params
            tmp1 = ":".join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = f2.params
            tmp = (tmp1 != ":".join([python_Boot.toString1(x1,'') for x1 in _this]))
        else:
            tmp = False
        if tmp:
            return False
        return True

    @staticmethod
    def constructorEq(c1,c2):
        if (c1.name != c2.name):
            return False
        if (c1.doc != c2.doc):
            return False
        if ((c1.args is None) != ((c2.args is None))):
            return False
        def _hx_local_0(a,b):
            if ((a.name == b.name) and ((a.opt == b.opt))):
                return haxe_rtti_TypeApi.typeEq(a.t,b.t)
            else:
                return False
        if ((c1.args is not None) and (not haxe_rtti_TypeApi.leq(_hx_local_0,c1.args,c2.args))):
            return False
        return True
haxe_rtti_TypeApi._hx_class = haxe_rtti_TypeApi
_hx_classes["haxe.rtti.TypeApi"] = haxe_rtti_TypeApi


