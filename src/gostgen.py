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

        self.make_rect((0, 0), self._size.raw(), 0.5, "white")

    def save(self):
        self._dwg.save()

    def make_line(self, start, end, thickness):
        self._dwg.add(
            self._dwg.line(
                start, end,
                stroke=svgwrite.rgb(0, 0, 0, '%'),
                stroke_width=thickness))

    def make_rect(self, left_top, right_bottom, thickness, fill="none"):
        size = (right_bottom[0] - left_top[0],
                right_bottom[1] - left_top[1])
        left_top_flip = (left_top[0],
                         -left_top[1] - size[1] + self._size.raw()[1])
        self._dwg.add(
            self._dwg.rect(
                left_top_flip, size,
                stroke=svgwrite.rgb(0, 0, 0, '%'),
                stroke_width=thickness,
                fill=fill))

    def make_text(self):
        pass


gost_page = A4Page("test.svg")

gost_page.make_rect((20, 5), (205, 292), 0.5)
gost_page.make_rect((20, 5), (205, 5+40), 0.5)
gost_page.make_rect((20, 5), (20+65, 5+40), 0.5)
gost_page.make_rect((20, 5), (20+65, 5+30), 0.5)
gost_page.make_rect((20, 5), (205, 5+25), 0.5)

for y in range(10, 45, 5):
    gost_page.make_rect((20, 5), (20+65, y), 0.5)

for y in (10, 25, 48):
    gost_page.make_rect((20, 5), (20+65-y, 5+40), 0.5)

gost_page.make_rect((20, 5+25), (20+7, 5+40), 0.5)
gost_page.make_rect((205-50, 5), (205, 5+25), 0.5)
gost_page.make_rect((205-50, 5), (205, 5+15), 0.5)

for y in (0, 35, 40, 45):
    gost_page.make_rect((205-50, 5+15), (205-y, 5+20), 0.5)

gost_page.make_rect((205-50, 5+15), (205-35, 5+25), 0.5)
gost_page.make_rect((205-50, 5+15), (205-20, 5+25), 0.5)

gost_page.save()
# dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
