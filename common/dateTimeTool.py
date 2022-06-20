#
# dateTimeTool.py
# @author yanchunhuo
# @description 
# @created 2022-06-20T17:54:29.468Z+08:00
# @last-modified 2022-06-20T17:55:37.545Z+08:00
# github https://github.com/yanchunhuo
import calendar
import datetime
import time

from dateutil.relativedelta import relativedelta


class DateTimeTool:
    @classmethod
    def getNowTime(cls, format='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(format)

    @classmethod
    def getNowDate(cls, format='%Y-%m-%d'):
        return datetime.date.today().strftime(format)

    @classmethod
    def getNowYear(cls,format='%Y'):
        return datetime.date.today().strftime(format)

    @classmethod
    def getNowTimeStampWithSecond(cls):
        return int(time.time())

    @classmethod
    def getNowTimeStampWithMillisecond(cls):
        return int(round(time.time()*1000))

    @classmethod
    def timeStampToDateTime(cls,timeStamp:int,is_with_millisecond=False):
        if is_with_millisecond:
            timeStamp=timeStamp/1000
        resultDateTime=datetime.datetime.fromtimestamp(timeStamp)
        return resultDateTime

    @classmethod
    def strToTimeStamp(cls,str,str_format:str='%Y-%m-%d %H:%M:%S',is_with_millisecond=False):
        dst_dateTime=datetime.datetime.strptime(str,str_format)
        if is_with_millisecond:
            timestamp=int(time.mktime(dst_dateTime.timetuple())*1000)
        else:
            timestamp=int(time.mktime(dst_dateTime.timetuple()))
        return timestamp

    @classmethod
    def getWeekDay(cls):
        """
        获得今天星期几，从1开始
        :return:
        """
        return datetime.datetime.now().weekday()+1

    @classmethod
    def getHowDaysAgo(cls,nowDateTime,nowDateTime_format='%Y-%m-%d %H:%M:%S',howDaysAgo=0,resultDateTime_format='%Y-%m-%d %H:%M:%S'):
        nowDateTime = datetime.datetime.strptime(nowDateTime, nowDateTime_format)
        resultDateTime=nowDateTime-datetime.timedelta(days=howDaysAgo)
        resultDateTime=resultDateTime.strftime(resultDateTime_format)
        return resultDateTime

    @classmethod
    def getHowDaysFuture(cls,nowDateTime,nowDateTime_format='%Y-%m-%d %H:%M:%S',howDaysFuture=0,resultDateTime_format='%Y-%m-%d %H:%M:%S'):
        nowDateTime = datetime.datetime.strptime(nowDateTime, nowDateTime_format)
        resultDateTime=nowDateTime+datetime.timedelta(days=howDaysFuture)
        resultDateTime=resultDateTime.strftime(resultDateTime_format)
        return resultDateTime

    @classmethod
    def dateTimeToStr(cls,theDateTime,format='%Y-%m-%d'):
        return theDateTime.strftime(format)

    @classmethod
    def strToDateTime(cls,str,str_format:str='%Y-%m-%d %H:%M:%S'):
        dst_dateTime=datetime.datetime.strptime(str,str_format)
        return dst_dateTime

    @classmethod
    def getHowYearsAgo(cls,nowDate,howYearsAgo=0,nowDate_format='%Y-%m-%d'):
        nowDateTime = datetime.datetime.strptime(nowDate, nowDate_format)
        resultDate = nowDateTime - datetime.timedelta(days=howYearsAgo * 366)
        return resultDate

    @classmethod
    def getMondayDateByAnyDate(cls, dateTime, dateTime_format='%Y-%m-%d %H:%M:%S'):
        dateTime = datetime.datetime.strptime(dateTime, dateTime_format)
        while (not dateTime.weekday() == 0):
            dateTime = dateTime - datetime.timedelta(days=1)
        return cls.dateTimeToStr(dateTime, dateTime_format)


    @classmethod
    def getSeparateCurrentMonth(cls, Separate):
        """
        获取当前月份前面或者后面的月份日期信息
        :param Separate: -1表示往后一个月，+1表示往前一个月
        :return:
        """
        return datetime.date.today() - relativedelta(months=Separate)
    
    @classmethod
    def getCurrentMonthFirstDayOrLastDay(cls,type=1):
        """获取当前月第一天或者最后一天日期

        Args:
            type (int, optional): 第一天:1，最后一天:-1

        Returns:
            [type]: [description]
        """
        now = datetime.datetime.now()
        year=now.year
        month=now.month
        last_day = calendar.monthrange(year,month)[1]
        if type==1:
            start = datetime.date(year,month,1)
            return start
        if type==-1: 
            end = datetime.date(year,month,last_day)
            return end

    @classmethod
    def time_cmp(self,systemtime=None, parmatime=None,format ="%H%M"):
        """
        :param systemtime:默认系统时间
        :param parmatime:默认系统时间
        :param format:比对格式
        :return:state
        0：系统时间大于当前时间、1：系统时间等于当前时间、2：系统时间小于当前时间
        """
        #传入时间与当前系统时间比对，根据参数：format进行哪些字段比较
        if systemtime ==None:
            systemtime = int(time.strptime(DateTimeTool.getNowTime(format), format))
        if parmatime ==None:
            parmatime = int(time.strptime(DateTimeTool.getNowTime(format), format))
        time1 = int(time.strftime(format, systemtime))
        time2 = int(time.strftime(format, parmatime))
        if time1>time2:
            state = 0
        elif time1==time2:
            state = 1
        else:
            state = 2
        return state

    @classmethod
    def get_today_in_weekday(self,currentday=None):
        """
        按数值（1-7）返回今天是周几的英文
        :return:
        """
        if currentday == None:
            currentday = self.getWeekDay()
        if currentday == 1:
            weekday = "Monday"
        elif currentday == 2:
            weekday = "Tuesday"
        elif currentday == 3:
            weekday = "Wednesday"
        elif currentday == 4:
            weekday = "Thursday"
        elif currentday == 5:
            weekday = "Friday"
        elif currentday == 6:
            weekday = "Saturday"
        else:
            weekday = "Sunday"
        return weekday

    @classmethod
    def get_str_date_to_format_date(self, strday=None, split_type="-"):
        """
        根据(年月日)日期分割返回格式化后的日期
        :param strday: 自定义年月日
        :param split_type: 自定义分割符
        :return:
        """
        y, m, d = strday.split(split_type)
        falmt_date = datetime.date(int(y), int(m), int(d))
        return falmt_date

    @classmethod
    def getTimeStampWithMillisecondCurrentMonth(cls, Separate=None):
        """
        获取距离当前月份的月份第一天的毫秒级时间戳
        :param Separate: -1表示往后一个月，+1表示往前一个月
        :return:
        """
        if Separate > 0:
            return int(
                time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month + abs(Separate),
                                          1).timetuple())) * 1000
        else:
            return int(
                time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month - abs(Separate),
                                          1).timetuple())) * 1000

    def get_timestamp_spec_time(days: int = 0, hour: int = None, minute: int = 0, second: int = 0,
                                is_with_millisecond=True):
        """
        获取指定的时间点的时间戳
        :param days:  与当前时间的相差的天数。-1 表示昨天；0 表示当天(默认)；1 表示明天
        :param hour: 时;指定的时间,比如当天的凌晨一点,时即为1(24小时制)
        :param minute: 分;指定的时间,比如当天某小时的1分钟,分即为1(24小时制)
        :param second: 秒;指定的时间,比如当天的某小时的某分钟1秒,秒即为1(24小时制)
        :return:      返回时间戳
        """
        nowTime = datetime.datetime.now() + datetime.timedelta(days=days)
        specified_time = nowTime.strftime("%Y-%m-%d") + " {}:{}:{}".format(hour, minute, second)
        timeArray = time.strptime(specified_time, "%Y-%m-%d %H:%M:%S")
        if is_with_millisecond:
            specified_time_stamp = int(time.mktime(timeArray)) * 1000
        else:
            specified_time_stamp = int(time.mktime(timeArray))
        return specified_time_stamp

    def get_timestamp_before_current_time(howDaysAgo: int = 0, hoursAgo: int = 0, minutesAgo: int = 0,
                                          secondsAgo: int = 0, is_with_millisecond=True):
        """
        获取当前时间距离指定天/时/分/秒的时间戳
        :param hoursAgo:  小时 -1：1小时后，0：当前小时，1:1小时前
        :param minutesAgo: 分钟
        :param secondsAgo: 秒钟
        :return:
        """
        resultDateTime = datetime.datetime.now()
        if howDaysAgo:
            resultDateTime -= datetime.timedelta(days=howDaysAgo)
        if hoursAgo:
            resultDateTime -= datetime.timedelta(hours=hoursAgo)
        if minutesAgo:
            resultDateTime -= datetime.timedelta(minutes=minutesAgo)
        if secondsAgo:
            resultDateTime -= datetime.timedelta(seconds=secondsAgo)
        if is_with_millisecond:
            timestamp = int(resultDateTime.timestamp()) * 1000
        else:
            timestamp = int(resultDateTime.timestamp())
        return timestamp

    @classmethod
    def zonetimeToTime(cls, str, hours=0, format="%Y-%m-%d %H:%M:%S"):
        """
        处理“2021-10-21T10:15:00.000+0000“格式的时间
        :param str:
        :param hours:
        :param format:
        :return:
        """
        t = str[:-10]
        utc_date2 = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
        formatTime = utc_date2 + datetime.timedelta(hours=hours)
        return datetime.datetime.strftime(formatTime, format)
