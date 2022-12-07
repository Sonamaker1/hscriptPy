
from classes_hscript import Reflect, Sys, _hx_AnonObject
from haxe import haxe_ds_EnumValueMap, haxe_ds_IntMap, haxe_ds_ObjectMap, haxe_ds_Option, haxe_ds_StringMap, haxe_unit_TestCase, haxe_unit_TestRunner
from hscript import hscript_Bytes, hscript_Interp, hscript_Parser
from python import python_Boot
import globalClasses

class TestHScript(haxe_unit_TestCase):
    _hx_class_name = "TestHScript"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["assertScript", "test", "testMap"]
    _hx_statics = ["main"]
    _hx_interfaces = []
    _hx_super = haxe_unit_TestCase


    def __init__(self):
        super().__init__()

    def assertScript(self,x,v,vars = None,allowTypes = None,pos = None):
        if (allowTypes is None):
            allowTypes = False
        p = hscript_Parser()
        p.allowTypes = allowTypes
        program = p.parseString(x)
        _hx_bytes = hscript_Bytes.encode(program)
        program = hscript_Bytes.decode(_hx_bytes)
        interp = hscript_Interp()
        if (vars is not None):
            _g = 0
            _g1 = python_Boot.fields(vars)
            while (_g < len(_g1)):
                v1 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                this1 = interp.variables
                value = Reflect.field(vars,v1)
                this1.h[v1] = value
        ret = interp.execute(program)
        self.assertEquals(v,ret,pos)

    def execute(self,x):
        p = hscript_Parser()
        p.allowTypes = True
        program = p.parseString(x)
        _hx_bytes = hscript_Bytes.encode(program)
        program = hscript_Bytes.decode(_hx_bytes)
        interp = hscript_Interp()
        ret = interp.execute(program)
        return ret
        
    def test(self):
        self.assertScript("0",0,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 26, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("0xFF",255,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 27, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("-123",-123,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 37, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("- 123",-123,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 38, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1.546",1.546,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 39, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript(".545",.545,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 40, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("'bla'","bla",None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 41, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("null",None,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 42, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("true",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 43, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("false",False,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 44, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1 == 2",False,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 45, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1.3 == 1.3",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 46, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("5 > 3",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 47, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("0 < 0",False,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 48, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("-1 <= -1",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 49, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1 + 2",3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 50, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("~545",-546,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 51, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("'abc' + 55","abc55",None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 52, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("'abc' + 'de'","abcde",None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 53, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("-1 + 2",1,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 54, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1 / 5",0.2,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 55, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("3 * 2 + 5",11,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 56, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("3 * (2 + 5)",21,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 57, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("3 * 2 // + 5 \n + 6",12,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 58, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("3 /* 2\n */ + 5",8,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 59, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("[55,66,77][1]",66,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 60, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = [55]; a[0] *= 2; a[0]",110,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 61, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("x",55,_hx_AnonObject({'x': 55}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 62, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var y = 33; y",33,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 63, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("{ 1; 2; 3; }",3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 64, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("{ var x = 0; } x",55,_hx_AnonObject({'x': 55}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 65, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("o.val",55,_hx_AnonObject({'o': _hx_AnonObject({'val': 55})}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 66, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("o.val",None,_hx_AnonObject({'o': _hx_AnonObject({})}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 67, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 1; a++",1,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 68, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 1; a++; a",2,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 69, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 1; ++a",2,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 70, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 1; a *= 3",3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 71, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("a = b = 3; a + b",6,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 72, 'className': "TestHScript", 'methodName': "test"}))
        def _hx_local_0(x,y):
            return (x + y)
        
        self.assertScript("add(1,2)",3,_hx_AnonObject({'add': _hx_local_0}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 73, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("a.push(5); a.pop() + a.pop()",8,_hx_AnonObject({'a': [3]}),None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 74, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("if( true ) 1 else 2",1,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 75, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("if( false ) 1 else 2",2,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 76, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var t = 0; for( x in [1,2,3] ) t += x; t",6,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 77, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = new Array(); for( x in 0...5 ) a[x] = x; a.join('-')","0-1-2-3-4",None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 78, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("(function(a,b) return a + b)(4,5)",9,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 79, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var y = 0; var add = function(a) y += a; add(5); add(3); y",8,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 80, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = [1,[2,[3,[4,null]]]]; var t = 0; while( a != null ) { t += a[0]; a = a[1]; }; t",10,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 81, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = false; do { a = true; } while (!a); a;",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 82, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var t = 0; for( x in 1...10 ) t += x; t",45,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 83, 'className': "TestHScript", 'methodName': "test"}))
        def _hx_local_INT(x,y):
            from classes_hscript import IntIterator
            return IntIterator(x,y)
        #_hx_AnonObject({'IntIterator': _hx_local_INT})
        self.assertScript("var t = 0; for( x in new IntIterator(1,10) ) t +=x; t",45,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 85, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var x = 1; try { var x = 66; throw 789; } catch( e : Dynamic ) e + x",790,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 89, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var x = 1; var f = function(x) throw x; try f(55) catch( e : Dynamic ) e + x",56,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 90, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var i=2; if( true ) --i; i",1,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 91, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var i=0; if( i++ > 0 ) i=3; i",1,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 92, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 5/2; a",2.5,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 93, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("{ x = 3; x; }",3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 94, 'className': "TestHScript", 'methodName': "test"}))
        self.execute("trace(\"lol\");")
        #FAILED self.assertScript("{ x : 3, y : {} }.x",3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 95, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("function bug(){ \n }\nbug().x",None,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 96, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("1 + 2 == 3",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 97, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("-2 == 3 - 5",True,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 98, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var x=-3; x",-3,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 99, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a:Array<Dynamic>=[1,2,4]; a[2]",4,None,True,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 100, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("/**/0",0,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 101, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("x=1;x*=-2",-2,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 102, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = x -> x + 1; f(3)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 103, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = () -> 55; f()",55,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 104, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = (x) -> x + 1; f(3)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 105, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = (x:Int) -> x + 1; f(3)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 106, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = (x,y) -> x + y; f(3,1)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 107, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = (x,y:Int) -> x + y; f(3,1)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 108, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f = (x:Int,y:Int) -> x + y; f(3,1)",4,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 109, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f:Int->Int->Int = (x:Int,y:Int) -> x + y; f(3,1)",4,None,True,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 110, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f:(x:Int, y:Int)->Int = (x:Int,y:Int) -> x + y; f(3,1)",4,None,True,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 111, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f:(x:Int)->(y:Int, z:Int)->Int = (x:Int) -> (y:Int, z:Int) -> x + y + z; f(3)(1, 2)",6,None,True,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 112, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var f:(x:Int)->(Int, Int)->Int = (x:Int) -> (y:Int, z:Int) -> x + y + z; f(3)(1, 2)",6,None,True,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 113, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 10; var b = 5; a - -b",15,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 114, 'className': "TestHScript", 'methodName': "test"}))
        self.assertScript("var a = 10; var b = 5; a - b / 2",7.5,None,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 115, 'className': "TestHScript", 'methodName': "test"}))

    def testMap(self):
        objKey = _hx_AnonObject({'ok': True})
        _g = haxe_ds_StringMap()
        _g.h["foo"] = "Foo"
        _g.h["bar"] = "Bar"
        _g1 = haxe_ds_IntMap()
        _g1.set(100,"one hundred")
        _g2 = haxe_ds_ObjectMap()
        _g2.set(objKey,"ok")
        vars = haxe_ds_EnumValueMap()
        _g3 = haxe_ds_StringMap()
        _g3.h["foo"] = 100
        vars1 = _hx_AnonObject({'stringMap': _g, 'intMap': _g1, 'objKey': objKey, 'objMap': _g2, 'enumKey': haxe_ds_Option.Some("some"), 'enumMap': vars, 'stringIntMap': _g3})
        vars1.enumMap.set(vars1.enumKey,"ok")
        self.assertScript("stringMap[\"foo\"]","Foo",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 131, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("intMap[100]","one hundred",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 132, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("objMap[objKey]","ok",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 133, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("enumMap[enumKey]","ok",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 134, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("stringMap[\"a\"] = \"A\"; stringMap[\"a\"]","A",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 135, 'className': "TestHScript", 'methodName': "testMap"}))
        #FAILED self.assertScript("intMap[200] = objMap[{foo:false}] = enumMap[enumKey] = \"A\"","A",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 136, 'className': "TestHScript", 'methodName': "testMap"}))
        #FAILED self.assertEquals("A",vars1.intMap.h.get(200,None),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 137, 'className': "TestHScript", 'methodName': "testMap"}))
        #FAILED self.assertEquals("A",vars1.enumMap.get(vars1.enumKey),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 138, 'className': "TestHScript", 'methodName': "testMap"}))
        key = vars1.objMap.keys()
        while key.hasNext():
            key1 = key.next()
            if (key1 != objKey):
                self.assertEquals(False,Reflect.field(key1,"foo"),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 141, 'className': "TestHScript", 'methodName': "testMap"}))
                self.assertEquals("A",vars1.objMap.h.get(key1,None),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 142, 'className': "TestHScript", 'methodName': "testMap"}))
        keys = []
        key = vars1.stringMap.keys()
        while key.hasNext():
            key1 = key.next()
            keys.append(key1)
        self.assertScript("\r\n\t\t\tvar keys = [];\r\n\t\t\tfor (key in stringMap.keys()) keys.push(key);\r\n\t\t\tkeys.join(\"_\");\r\n\t\t","_".join([python_Boot.toString1(x1,'') for x1 in keys]),vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 146, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("stringMap.remove(\"foo\"); stringMap.exists(\"foo\");",False,vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 155, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("stringMap[\"foo\"] = \"a\"; stringMap[\"foo\"] += \"b\"","ab",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 156, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertEquals("ab",vars1.stringMap.h.get("foo",None),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 157, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("stringIntMap[\"foo\"]++",100,vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 158, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertEquals(101,vars1.stringIntMap.h.get("foo",None),_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 159, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("++stringIntMap[\"foo\"]",102,vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 160, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("var newMap = [\"foo\"=>\"foo\"]; newMap[\"foo\"];","foo",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 161, 'className': "TestHScript", 'methodName': "testMap"}))
        self.assertScript("var newMap = [enumKey=>\"foo\"]; newMap[enumKey];","foo",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 163, 'className': "TestHScript", 'methodName': "testMap"}))
        #FAILED self.assertScript("var newMap = [{a:\"a\"}=>\"foo\", objKey=>\"bar\"]; newMap[objKey];","bar",vars1,None,_hx_AnonObject({'fileName': "TestHScript.hx", 'lineNumber': 165, 'className': "TestHScript", 'methodName': "testMap"}))

    @staticmethod
    def main():
        runner = haxe_unit_TestRunner()
        runner.add(TestHScript())
        succeed = runner.run()
        Sys.exit((0 if succeed else 1))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
TestHScript._hx_class = TestHScript
globalClasses._hx_classes["TestHScript"] = TestHScript


