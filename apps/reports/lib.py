import xlrd
from datetime import datetime


def get_or_none(classmodel, **kwargs):
    """
        the function will get the from the Model if exist other
        wise will return none

        @author : Arun Gopi
        @date   : 3/4/2016
    """
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def date_from_excel(d, dm):
    """
        return date from excel file

        @author : Arun Gopi
        @date   : 6/4/2016
    """

    if d:

        try:
            if isinstance(d, float) or isinstance(d, int):
                year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(
                    d, dm)
                d = "%04d-%02d-%02d" % (year, month, day)
            elif isinstance(d, str) or isinstance(d, unicode):
                d = datetime.strptime(d, '%d-%m-%Y').strftime('%Y-%m-%d')
            else:
                print "ERROR : Unknown datatype", type(d)
        except ValueError:
            d = None
    else:
        d = None
    return d
