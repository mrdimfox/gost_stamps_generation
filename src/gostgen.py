import svgwrite

class Size:
    def __init__(self, w = 0, h = 0):
        self._width = w
        self._height = h

    def with_uints(self, units):
        return ('{}{}'.format(self._width, units),
                '{}{}'.format(self._height, units))

    def raw(self):
        return (self._width, self._height)

class A4Page:
    def __init__(self, name):
        self._size = Size(210, 297)

        self._dwg = svgwrite.Drawing(
            name, 
            size=self._size.with_uints("mm"),
            viewBox=('0 0 {} {}'.format(*self._size.raw())))

        # self._dwg.add(self._dwg.line((0, 0), self._size.raw(), stroke=svgwrite.rgb(10, 10, 16, '%')))
        # self._dwg.add(svgwrite.shapes.Rect((0, 0), size = self._size.raw()))

    def save(self):
        self._dwg.save()

    def make_line(self):
        pass

    def make_rect(self):
        pass

    def make_text(self):
        pass


gost_page = A4Page("test.svg")
gost_page.save()
# dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
