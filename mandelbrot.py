import numpy as np
kMandelbrotBound = 2.0
kCanvasWidth = 1000
kCanvasHeight = 1000
kMaxUnfoldSteps = 1000

def setup_ppm(f, width, height):
    f.write("P3\n")
    f.write("{} {}\n".format(int(width), int(height)))
    f.write("255\n")

def converges(c):
    z = 0
    for i in range(kMaxUnfoldSteps):
        z = z**2 + c
        if abs(z) > kMandelbrotBound:
            return False
    return True    

def paint_pixel(x, y):
    a = -int(kMandelbrotBound / 2.0) + x
    b = int(kMandelbrotBound / 2.0) - y
    red, green, blue = (0, 0, 0)
    if converges(complex(a, b)):
        red, green, blue = (0, 0, 0)
    else:
        red, green, blue = (255, 0, 0)
    f.write(str(red)+"\n")
    f.write(str(green)+"\n")
    f.write(str(blue)+"\n")

if __name__ == "__main__":
    f = open("mandelbrot.ppm", "w")
    setup_ppm(f, kCanvasWidth, kCanvasHeight)
    for y in np.arange(0.0, kMandelbrotBound, kMandelbrotBound / kCanvasHeight):
        for x in np.arange(0.0, kMandelbrotBound, kMandelbrotBound / kCanvasWidth):
            paint_pixel(x, y)
    f.close()
