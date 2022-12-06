class haxe_xml_Parser:
    _hx_class_name = "haxe.xml.Parser"
    __slots__ = ()
    _hx_statics = ["escapes", "parse", "doParse", "isValidChar"]

    @staticmethod
    def parse(_hx_str,strict = None):
        if (strict is None):
            strict = False
        doc = Xml.createDocument()
        haxe_xml_Parser.doParse(_hx_str,strict,0,doc)
        return doc

    @staticmethod
    def doParse(_hx_str,strict,p = None,parent = None):
        if (p is None):
            p = 0
        xml = None
        state = 1
        next = 1
        aname = None
        start = 0
        nsubs = 0
        nbrackets = 0
        buf = StringBuf()
        escapeNext = 1
        attrValQuote = -1
        while (p < len(_hx_str)):
            c = ord(_hx_str[p])
            state1 = state
            if (state1 == 0):
                c1 = c
                if ((((c1 == 32) or ((c1 == 13))) or ((c1 == 10))) or ((c1 == 9))):
                    pass
                else:
                    state = next
                    continue
            elif (state1 == 1):
                if (c == 60):
                    state = 0
                    next = 2
                else:
                    start = p
                    state = 13
                    continue
            elif (state1 == 2):
                c2 = c
                if (c2 == 33):
                    index = (p + 1)
                    if (((-1 if ((index >= len(_hx_str))) else ord(_hx_str[index]))) == 91):
                        p = (p + 2)
                        if (HxString.substr(_hx_str,p,6).upper() != "CDATA["):
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <![CDATA[",_hx_str,p))
                        p = (p + 5)
                        state = 17
                        start = (p + 1)
                    else:
                        tmp = None
                        index1 = (p + 1)
                        if (((-1 if ((index1 >= len(_hx_str))) else ord(_hx_str[index1]))) != 68):
                            index2 = (p + 1)
                            tmp = (((-1 if ((index2 >= len(_hx_str))) else ord(_hx_str[index2]))) == 100)
                        else:
                            tmp = True
                        if tmp:
                            if (HxString.substr(_hx_str,(p + 2),6).upper() != "OCTYPE"):
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!DOCTYPE",_hx_str,p))
                            p = (p + 8)
                            state = 16
                            start = (p + 1)
                        else:
                            tmp1 = None
                            index3 = (p + 1)
                            if (((-1 if ((index3 >= len(_hx_str))) else ord(_hx_str[index3]))) == 45):
                                index4 = (p + 2)
                                tmp1 = (((-1 if ((index4 >= len(_hx_str))) else ord(_hx_str[index4]))) != 45)
                            else:
                                tmp1 = True
                            if tmp1:
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!--",_hx_str,p))
                            else:
                                p = (p + 2)
                                state = 15
                                start = (p + 1)
                elif (c2 == 47):
                    if (parent is None):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    start = (p + 1)
                    state = 0
                    next = 10
                elif (c2 == 63):
                    state = 14
                    start = p
                else:
                    state = 3
                    start = p
                    continue
            elif (state1 == 3):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (p == start):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    xml = Xml.createElement(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(xml)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 4
                    continue
            elif (state1 == 4):
                c3 = c
                if (c3 == 47):
                    state = 11
                elif (c3 == 62):
                    state = 9
                else:
                    state = 5
                    start = p
                    continue
            elif (state1 == 5):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected attribute name",_hx_str,p))
                    tmp2 = HxString.substr(_hx_str,start,(p - start))
                    aname = tmp2
                    if xml.exists(aname):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Duplicate attribute [" + ("null" if aname is None else aname)) + "]"),_hx_str,p))
                    state = 0
                    next = 6
                    continue
            elif (state1 == 6):
                if (c == 61):
                    state = 0
                    next = 7
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected =",_hx_str,p))
            elif (state1 == 7):
                c4 = c
                if ((c4 == 39) or ((c4 == 34))):
                    buf = StringBuf()
                    state = 8
                    start = (p + 1)
                    attrValQuote = c
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected \"",_hx_str,p))
            elif (state1 == 8):
                c5 = c
                if (c5 == 38):
                    _hx_len = (p - start)
                    s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                    buf.b.write(s)
                    state = 18
                    escapeNext = 8
                    start = (p + 1)
                elif ((c5 == 62) or ((c5 == 60))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Invalid unescaped " + HxOverrides.stringOrNull("".join(map(chr,[c])))) + " in attribute value"),_hx_str,p))
                    elif (c == attrValQuote):
                        len1 = (p - start)
                        s1 = (HxString.substr(_hx_str,start,None) if ((len1 is None)) else HxString.substr(_hx_str,start,len1))
                        buf.b.write(s1)
                        val = buf.b.getvalue()
                        buf = StringBuf()
                        xml.set(aname,val)
                        state = 0
                        next = 4
                elif (c == attrValQuote):
                    len2 = (p - start)
                    s2 = (HxString.substr(_hx_str,start,None) if ((len2 is None)) else HxString.substr(_hx_str,start,len2))
                    buf.b.write(s2)
                    val1 = buf.b.getvalue()
                    buf = StringBuf()
                    xml.set(aname,val1)
                    state = 0
                    next = 4
            elif (state1 == 9):
                p = haxe_xml_Parser.doParse(_hx_str,strict,p,xml)
                start = p
                state = 1
            elif (state1 == 10):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    v = HxString.substr(_hx_str,start,(p - start))
                    if ((parent is None) or ((parent.nodeType != 0))):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unexpected </" + ("null" if v is None else v)) + ">, tag is not open"),_hx_str,p))
                    if (parent.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                    if (v != parent.nodeName):
                        if (parent.nodeType != Xml.Element):
                            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Expected </" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
                    state = 0
                    next = 12
                    continue
            elif (state1 == 11):
                if (c == 62):
                    state = 1
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 12):
                if (c == 62):
                    if (nsubs == 0):
                        parent.addChild(Xml.createPCData(""))
                    return p
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 13):
                if (c == 60):
                    len3 = (p - start)
                    s3 = (HxString.substr(_hx_str,start,None) if ((len3 is None)) else HxString.substr(_hx_str,start,len3))
                    buf.b.write(s3)
                    child = Xml.createPCData(buf.b.getvalue())
                    buf = StringBuf()
                    parent.addChild(child)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 2
                elif (c == 38):
                    len4 = (p - start)
                    s4 = (HxString.substr(_hx_str,start,None) if ((len4 is None)) else HxString.substr(_hx_str,start,len4))
                    buf.b.write(s4)
                    state = 18
                    escapeNext = 13
                    start = (p + 1)
            elif (state1 == 14):
                tmp3 = None
                if (c == 63):
                    index5 = (p + 1)
                    tmp3 = (((-1 if ((index5 >= len(_hx_str))) else ord(_hx_str[index5]))) == 62)
                else:
                    tmp3 = False
                if tmp3:
                    p = (p + 1)
                    str1 = HxString.substr(_hx_str,(start + 1),((p - start) - 2))
                    parent.addChild(Xml.createProcessingInstruction(str1))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 15):
                tmp4 = None
                tmp5 = None
                if (c == 45):
                    index6 = (p + 1)
                    tmp5 = (((-1 if ((index6 >= len(_hx_str))) else ord(_hx_str[index6]))) == 45)
                else:
                    tmp5 = False
                if tmp5:
                    index7 = (p + 2)
                    tmp4 = (((-1 if ((index7 >= len(_hx_str))) else ord(_hx_str[index7]))) == 62)
                else:
                    tmp4 = False
                if tmp4:
                    parent.addChild(Xml.createComment(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 16):
                if (c == 91):
                    nbrackets = (nbrackets + 1)
                elif (c == 93):
                    nbrackets = (nbrackets - 1)
                elif ((c == 62) and ((nbrackets == 0))):
                    parent.addChild(Xml.createDocType(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 17):
                tmp6 = None
                tmp7 = None
                if (c == 93):
                    index8 = (p + 1)
                    tmp7 = (((-1 if ((index8 >= len(_hx_str))) else ord(_hx_str[index8]))) == 93)
                else:
                    tmp7 = False
                if tmp7:
                    index9 = (p + 2)
                    tmp6 = (((-1 if ((index9 >= len(_hx_str))) else ord(_hx_str[index9]))) == 62)
                else:
                    tmp6 = False
                if tmp6:
                    child1 = Xml.createCData(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(child1)
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 18):
                if (c == 59):
                    s5 = HxString.substr(_hx_str,start,(p - start))
                    if (((-1 if ((0 >= len(s5))) else ord(s5[0]))) == 35):
                        c6 = (Std.parseInt(("0" + HxOverrides.stringOrNull(HxString.substr(s5,1,(len(s5) - 1))))) if ((((-1 if ((1 >= len(s5))) else ord(s5[1]))) == 120)) else Std.parseInt(HxString.substr(s5,1,(len(s5) - 1))))
                        s6 = "".join(map(chr,[c6]))
                        buf.b.write(s6)
                    elif (not (s5 in haxe_xml_Parser.escapes.h)):
                        if strict:
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Undefined entity: " + ("null" if s5 is None else s5)),_hx_str,p))
                        s7 = Std.string((("&" + ("null" if s5 is None else s5)) + ";"))
                        buf.b.write(s7)
                    else:
                        s8 = Std.string(haxe_xml_Parser.escapes.h.get(s5,None))
                        buf.b.write(s8)
                    start = (p + 1)
                    state = escapeNext
                elif ((not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))) and ((c != 35))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Invalid character in entity: " + HxOverrides.stringOrNull("".join(map(chr,[c])))),_hx_str,p))
                    s9 = "".join(map(chr,[38]))
                    buf.b.write(s9)
                    len5 = (p - start)
                    s10 = (HxString.substr(_hx_str,start,None) if ((len5 is None)) else HxString.substr(_hx_str,start,len5))
                    buf.b.write(s10)
                    p = (p - 1)
                    start = (p + 1)
                    state = escapeNext
            else:
                pass
            p = (p + 1)
        if (state == 1):
            start = p
            state = 13
        if (state == 13):
            if (parent.nodeType == 0):
                if (parent.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unclosed node <" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
            if ((p != start) or ((nsubs == 0))):
                _hx_len = (p - start)
                s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                buf.b.write(s)
                parent.addChild(Xml.createPCData(buf.b.getvalue()))
                nsubs = (nsubs + 1)
            return p
        if (((not strict) and ((state == 18))) and ((escapeNext == 13))):
            s = "".join(map(chr,[38]))
            buf.b.write(s)
            _hx_len = (p - start)
            s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
            buf.b.write(s)
            parent.addChild(Xml.createPCData(buf.b.getvalue()))
            nsubs = (nsubs + 1)
            return p
        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Unexpected end",_hx_str,p))

    @staticmethod
    def isValidChar(c):
        if (not ((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))))):
            return (c == 45)
        else:
            return True
haxe_xml_Parser._hx_class = haxe_xml_Parser
_hx_classes["haxe.xml.Parser"] = haxe_xml_Parser


