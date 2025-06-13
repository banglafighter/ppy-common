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


class SecondsToOther:
    day: int = None
    hour: int = None
    minute: int = None
    second: int = None

    def get_short_form(self):
        formatted_text = ""
        if self.day:
            formatted_text += f" {int(self.day)}d"
        if self.hour:
            formatted_text += f" {int(self.hour)}h"
        if self.minute:
            formatted_text += f" {int(self.minute)}m"
        if self.second:
            formatted_text += f" {int(self.second)}s"
        return formatted_text.strip()


class TimeData:
    hour24: str
    hour12: str
    minute: int
    second: int
    amPm: str


class DateTimeData(DateData, TimeData):
    pass
