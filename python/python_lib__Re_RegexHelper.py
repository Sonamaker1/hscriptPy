class python_lib__Re_RegexHelper:
    _hx_class_name = "python.lib._Re.RegexHelper"
    __slots__ = ()
    _hx_statics = ["findallDynamic"]

    @staticmethod
    def findallDynamic(r,string,pos = None,endpos = None):
        if (endpos is None):
            if (pos is None):
                return r.findall(string)
            else:
                return r.findall(string,pos)
        else:
            return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper
_hx_classes["python.lib._Re.RegexHelper"] = python_lib__Re_RegexHelper


