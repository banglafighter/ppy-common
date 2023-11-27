class DateData:
    day: int
    month: int
    monthName: str
    monthShort: str
    year: int
    yearShort: int
    weekday: str
    dayOfYear: str
    weekOfYear: str


class TimeData:
    hour24: str
    hour12: str
    minute: int
    second: int
    amPm: str


class DateTimeData(DateData, TimeData):
    pass
