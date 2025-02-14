from ... import pe_vars as _vars

pyv = _vars.engine

ANCHOR_UPPERLEFT = (0, 0)
ANCHOR_UPPERRIGHT = (2, 0)
ANCHOR_CENTER = (1, 1)
ANCHOR_LOWERLEFT = (0, 2)
ANCHOR_LOWERRIGHT = (2, 2)
ANCHOR_TOP = (1, 0)
ANCHOR_LEFT = (0, 1)
ANCHOR_RIGHT = (2, 1)


class Frect(object):
    """Floating rect- changes position depending on the screen dimensions."""

    def __init__(self, dx, dy, w, h, anchor=ANCHOR_CENTER, parent=None):
        self.dx = dx
        self.dy = dy
        self.w = w
        self.h = h
        self.anchor = anchor
        self.parent = parent

    def get_rect(self):
        if self.parent:
            prect = self.parent.get_rect()
            x0 = prect.left + (prect.w // 2) * self.anchor[0]
            y0 = prect.top + (prect.h // 2) * self.anchor[1]
        else:
            sw, sh = _vars.screen.get_size()
            x0 = (sw // 2) * self.anchor[0]
            y0 = (sh // 2) * self.anchor[1]
        return pyv.new_rect_obj(self.dx + x0, self.dy + y0, self.w, self.h)
