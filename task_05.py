import datetime


def date_in_future(integer: int):
    if isinstance(integer, int):
        a = (datetime.datetime.now())
        b = datetime.timedelta(days = integer)
        c = a + b
        return c.strftime("%d-%m-%Y %H:%M:%S")
    else:
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
