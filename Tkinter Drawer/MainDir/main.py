import tkinter as tk
import time
import math


def shorten_fraction(a, b):
    a2, b2 = divmod(a, b)
    if b2 == 0:
        return a2, 1
    a3, b3 = shorten_fraction(b, b2)
    return b3 + a2 * a3, a3


def calc_star_fraction(a, b):
    a2, b2 = shorten_fraction(a, b)
    return a2, b2, a // a2


def get_star_points(n, step, x, y, r, start_angle=-math.pi/2):
    for i in range(n):
        angle = (i * step) * ((2 * math.pi)/n) + start_angle
        yield x + r * math.cos(angle), y + r * math.sin(angle)

    yield x + r * math.cos(start_angle), y + r * math.sin(start_angle)


def get_star_lines(n, step, x, y, r, start_angle=-math.pi/2, direct=False, cross=False):
    if step == 1 and not direct:
        return
    if n % 2 == 0 and step == n // 2 and not cross:
        return
    sub_n, step, nr = calc_star_fraction(n, step)
    for i in range(nr):
        angle = i * ((2 * math.pi) / n) + start_angle
        sub_points = get_star_points(sub_n, step, x, y, r, angle)
        prev = next(sub_points)
        for current in sub_points:
            yield prev, current
            prev = current
    # if n % step == 0:
    #     for i in range(step):
    #         angle = i * ((2 * math.pi) / n) + start_angle
    #         sub_points = get_star_points(n // step, 1, x, y, r, angle)
    #         prev = next(sub_points)
    #         for current in sub_points:
    #             yield prev, current
    #             prev = current
    # else:
    #     points = get_star_points(n, step, x, y, r, start_angle)
    #     prev = next(points)
    #     for current in points:
    #         yield prev, current
    #         prev = current


def get_stars(n, x, y, r, direct=False, cross=False):
    x_offset = 0
    for i in range(1, (n // 2) + 1):
        lines = get_star_lines(n, i, x + x_offset, y, r, direct=direct, cross=cross)
        if not (i == 1 and not direct):
            x_offset += r * 2.2
        for line in lines:
            yield line


def animate_lines(lines, step=1):
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        dx = x2 - x1
        dy = y2 - y1

        steps = dx // step if abs(dx) > abs(dy) else dy // step
        for i in range(int(steps + 1)):
            yield line[0], tuple(round(w[0] + w[1] * (i / steps)) for w in ((x1, dx), (y1, dy)))



def get_multi_points(n, step, x, y, r, start_angle=-math.pi/2):
    for i in range(step):
        angle = i * ((2 * math.pi)/n) + start_angle
        # yield get_star_points(n, step, x, y, r, angle)
        g = get_star_points(n // step, 1, x, y, r, angle)
        prev = next(g)
        for current in g:
            yield prev, current
            prev = current
        # for line in get_star_points(n // step, 1, x, y, r, angle):
        #     yield line
        # g = get_star_points(n, step, x, y, r, angle)
        # prev = next(g)
        # for current in g:
        #     yield prev, current
        #     prev = current

# def get_multi_points(n, step, x, y, r, start_angle=-math.pi/2):
#     for i in range(step):
#         angle = i * ((2 * math.pi)/n) + start_angle
#         yield get_star_points(n, step, x, y, r, angle)


def get_stars_from_star_type(n, x, y, r, direct=False, cross=False):
    x_offset = 0
    if direct:
        g = get_star_points(n, 1, x + x_offset, y, r)
        prev = next(g)
        for current in g:
            yield prev, current
            prev = current
        x_offset += r*2.2

    half, rem = divmod(n, 2)
    if rem == 0:
        half -= 1

    for i in range(2, half + 1):
        print(i)
        if n % i == 0:
            print("A")
            # yield get_multi_points(n, i, x + x_offset, y, r)
            g = get_multi_points(n, i, x + x_offset, y, r)
            prev = next(g)
            for current in g:
                yield prev, current
                prev = current
            x_offset += r*2.2
        else:
            print("B")
            g = get_star_points(n, i, x + x_offset, y, r)
            prev = next(g)
            for current in g:
                yield prev, current
                prev = current
            x_offset += r*2.2

    if cross and n % 2 == 0:
        # yield get_multi_points(n, i, x + x_offset, y, r)
        g = get_multi_points(n, i, x + x_offset, y, r)
        prev = next(g)
        for current in g:
            yield prev, current
            prev = current
        x_offset += r*2.2

# def get_stars_from_star_type(n, x, y, r, direct=False, cross=False):
#     x_offset = 0
#     if direct:
#         yield True, get_star_points(n, 1, x + x_offset, y, r)
#         x_offset += r*2.2
#
#     half, rem = divmod(n, 2)
#     if rem == 0:
#         half -= 1
#
#     for i in range(2, half + 1):
#         print(i)
#         if n % i == 0:
#             print("A")
#             yield False, get_multi_points(n, i, x + x_offset, y, r)
#             x_offset += r*2.2
#         else:
#             print("B")
#             yield True, get_star_points(n, i, x + x_offset, y, r)
#             x_offset += r*2.2
#
#     if cross and n % 2 == 0:
#         yield False, get_multi_points(n, i, x + x_offset, y, r)
#         x_offset += r*2.2






class CanvasWindow:
    def __init__(self, width=800, height=600, background="#FAFAFA", sleep_time=0.01):
        self._wnd = tk.Tk()
        self._wnd.protocol("WM_DELETE_WINDOW", self._on_close)

        self._canvas = tk.Canvas(self._wnd, width=width, height=height, background=background)
        self._running_loop = False
        self._sleep_time = sleep_time

        self._stars = []

    def _on_close(self):
        self._running_loop = False
        self._wnd.destroy()

    def _setup_canvas(self):
        # self._coord = [400, 50, 600, 550, 50, 250, 750, 250, 150, 550, 400, 50]
        # self._coord2 = [400, 50, 600, 550, 50, 250, 750, 250, 400, 50]
        # self._coord = list(get_star_points(5, 2, 200, 200, 100))
        # self._coord2 = list(get_star_points(7, 3, 400, 200, 100))
        #
        # self._line = self._canvas.create_line(self._coord, width=3, fill="#00F")
        # self._line = self._canvas.create_line(self._coord2, width=3, fill="#00F")

        # stars = calc_start_types(9, 200, 200, 150)
        # stars = calc_start_types(7, 200, 200, 100, direct=False, cross=True)

        # self._stars = get_stars_from_star_type(self._stars[0], 200, 200, 100)
        self._stars = get_stars(self._stars[0], 200, 200, 100)
        self._stars = animate_lines(self._stars)

        # for star_type in self._stars:
        #     stars = calc_start_types(star_type, 200, 200, 100)
        #
        #     for star in stars:
        #         if star[0]:
        #             self._canvas.create_line(list(star[1]), width=3, fill="#00F")
        #         else:
        #             for star_part in star[1]:
        #                 self._canvas.create_line(list(star_part), width=3, fill="#00F")

        pause = 2
        self._clk = time.perf_counter() + pause
        self._changed = False

        self._canvas.pack()
        self._running_loop = True

    def _run_loop(self):
        while self._running_loop:
            self._do_loop_actions()
            self._wnd.update_idletasks()
            self._wnd.update()
            # if self._sleep_time != 0:
            #     time.sleep(self._sleep_time)

    def start_loop(self):
        self._setup_canvas()
        self._run_loop()

    def _do_loop_actions(self):
        if not self._changed:
            # time.sleep(0.05)
            line = next(self._stars, None)
            if line is not None:
                # print(line)
                self._canvas.create_line(line, width=3, fill="#00F")
                self._canvas.update()
                # self._changed = True
                # if star[0]:
                #     self._canvas.create_line(list(star[1]), width=3, fill="#00F")
                #     self._canvas.update()
                # else:
                #     for star_part in star[1]:
                #         self._canvas.create_line(list(star_part), width=3, fill="#00F")
                #         self._canvas.update()
            else:
                self._changed = True
                print("Done")

    def draw_star(self, n):
        self._stars.append(n)


def main():
    cv = CanvasWindow(width=1600)

    cv.draw_star(15)

    cv.start_loop()
    # s = get_star_points(5, 2, 0, 0, 1)
    # print(next(s))
    # print(next(s))
    # print(next(s))


if __name__ == '__main__':
    main()
