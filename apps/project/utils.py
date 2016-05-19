import xlwt


def get_or_none(classmodel, **kwargs):
    """ the function will get the from the Model if exist other
        wise will return none

        @author : Arun Gopi
        @date   : 3/4/2016 """
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def insertcolx():
    """ Excel row/colum style for excel
            @Author  : Arun Gopi
            @date    : 3/4/2016 """

    style = xlwt.XFStyle()
    borders = xlwt.Borders()
    borders.bottom = borders.top = borders.left\
        = borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    style.borders = borders
    style.pattern.pattern = 26
    style.pattern.pattern_fore_colour = 0x16
    style.protection.cell_locked = False
    style.protection.formula_hidden = False
    return style
