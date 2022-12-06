class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "getUTCHours", "getUTCMinutes", "getUTCSeconds", "getUTCFullYear", "getUTCMonth", "getUTCDate", "getUTCDay", "getTimezoneOffset", "toString"]
    _hx_statics = ["now", "fromTime", "makeLocal", "UTC", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def getTime(self):
        return (self.date.timestamp() * 1000)

    def getHours(self):
        return self.date.hour

    def getMinutes(self):
        return self.date.minute

    def getSeconds(self):
        return self.date.second

    def getFullYear(self):
        return self.date.year

    def getMonth(self):
        return (self.date.month - 1)

    def getDate(self):
        return self.date.day

    def getDay(self):
        return HxOverrides.mod(self.date.isoweekday(), 7)

    def getUTCHours(self):
        return self.dateUTC.hour

    def getUTCMinutes(self):
        return self.dateUTC.minute

    def getUTCSeconds(self):
        return self.dateUTC.second

    def getUTCFullYear(self):
        return self.dateUTC.year

    def getUTCMonth(self):
        return (self.dateUTC.month - 1)

    def getUTCDate(self):
        return self.dateUTC.day

    def getUTCDay(self):
        return HxOverrides.mod(self.dateUTC.isoweekday(), 7)

    def getTimezoneOffset(self):
        x = (self.date.utcoffset() / python_lib_datetime_Timedelta(0,60))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        return -tmp

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def fromTime(t):
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def makeLocal(date):
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

    @staticmethod
    def UTC(year,month,day,hour,_hx_min,sec):
        return (python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0,python_lib_datetime_Timezone.utc).timestamp() * 1000)

    @staticmethod
    def fromString(s):
        _g = len(s)
        if (_g == 8):
            k = s.split(":")
            return Date.fromTime((((Std.parseInt((k[0] if 0 < len(k) else None)) * 3600000.) + ((Std.parseInt((k[1] if 1 < len(k) else None)) * 60000.))) + ((Std.parseInt((k[2] if 2 < len(k) else None)) * 1000.))))
        elif (_g == 10):
            k = s.split("-")
            return Date(Std.parseInt((k[0] if 0 < len(k) else None)),(Std.parseInt((k[1] if 1 < len(k) else None)) - 1),Std.parseInt((k[2] if 2 < len(k) else None)),0,0,0)
        elif (_g == 19):
            k = s.split(" ")
            _this = (k[0] if 0 < len(k) else None)
            y = _this.split("-")
            _this = (k[1] if 1 < len(k) else None)
            t = _this.split(":")
            return Date(Std.parseInt((y[0] if 0 < len(y) else None)),(Std.parseInt((y[1] if 1 < len(y) else None)) - 1),Std.parseInt((y[2] if 2 < len(y) else None)),Std.parseInt((t[0] if 0 < len(t) else None)),Std.parseInt((t[1] if 1 < len(t) else None)),Std.parseInt((t[2] if 2 < len(t) else None)))
        else:
            raise haxe_Exception.thrown(("Invalid date format : " + ("null" if s is None else s)))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.date = None
        _hx_o.dateUTC = None
Date._hx_class = Date
_hx_classes["Date"] = Date


