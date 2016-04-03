
def get_or_none(classmodel,**kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def insertcolx():
    style = xlwt.XFStyle()
    borders = xlwt.Borders()
    borders.bottom =borders.top= borders.left = borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    style.borders = borders
    style.pattern.pattern = 26
    style.pattern.pattern_fore_colour = 0x16
    style.protection.cell_locked = False
    style.protection.formula_hidden = False
    return style