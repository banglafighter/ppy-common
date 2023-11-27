from datetime import date, datetime
from ppy_common.ppy_data import DateData, TimeData


class DateUtil:

    @staticmethod
    def string_date_to_date(string_date: str, date_format: str = "%d/%m/%Y"):
        date_time_data = datetime.strptime(string_date, date_format)
        if date_time_data:
            return date_time_data.date()
        return None

    @staticmethod
    def split_data_into(input_date: date = None) -> DateData:
        if not input_date:
            input_date = date.today()
        date_data = DateData()
        date_data.year = input_date.year
        date_data.month = input_date.month
        date_data.yearShort = input_date.strftime("%y")
        date_data.monthName = input_date.strftime("%B")
        date_data.monthShort = input_date.strftime("%b")
        date_data.day = input_date.day
        date_data.weekday = input_date.strftime("%A")
        date_data.dayOfYear = input_date.strftime("%j")
        date_data.weekOfYear = input_date.strftime("%W")
        return date_data

    @staticmethod
    def split_time_into(input_datetime: datetime = None) -> TimeData:
        if not input_datetime:
            input_datetime = datetime.now()
        time_data = TimeData()
        time_data.minute = input_datetime.minute
        time_data.second = input_datetime.second
        time_data.hour12 = input_datetime.strftime("%I")
        time_data.hour24 = input_datetime.strftime("%H")
        time_data.amPm = input_datetime.strftime("%p")
        return time_data
