import math


HEIGHT = 1000
WIDTH = int(1.5 * HEIGHT)


def get_rgb(point, gradient=0, color_scheme=0, color_values=((0, HEIGHT), (200, 0), (200, 0), (0, 255))):
    reference_point, red_values, green_values, blue_values = color_values
    sx, sy = point
    # Good color combos
    if gradient == 0:
        if color_scheme == 0:
            rpx, rpy = reference_point  # (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = red_values  # (0, 100)
            grange, gmin = green_values  # (100, 0)
            brange, bmin = blue_values  # (100, 100)
        elif color_scheme == 1:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (40, 40)
            grange, gmin = (0, 0)
            brange, bmin = (0, 0)
        elif color_scheme == 2:
            rpx, rpy = (WIDTH / 2, 0)
            rrange, rmin = (-255, 255)
            grange, gmin = (-255, 255)
            brange, bmin = (-255, 255)
        elif color_scheme == 3:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (0, 100)
            grange, gmin = (100, 0)
            brange, bmin = (100, 0)
        elif color_scheme == 4:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (0, 100)
            grange, gmin = (100, 0)
            brange, bmin = (100, 100)
        elif color_scheme == 5:
            rpx, rpy = (WIDTH, 0)
            rrange, rmin = (0, 255)
            grange, gmin = (100, 0)
            brange, bmin = (100, 100)
        elif color_scheme == 6:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (100, 25)
            grange, gmin = (100, 0)
            brange, bmin = (0, 100)
        elif color_scheme == 7:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (56, 199)
            grange, gmin = (87, 0)
            brange, bmin = (6, 57)
        elif color_scheme == 8:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (167, 88)
            grange, gmin = (171, 24)
            brange, bmin = (69, 69)
        elif color_scheme == 9:
            rpx, rpy = (WIDTH / 2, HEIGHT / 2)
            rrange, rmin = (195, 53)
            grange, gmin = (85, 92)
            brange, bmin = (24, 125)
        if sx != rpx:
            cartesian_angle = math.atan(
                math.fabs((rpy - sy) / (rpx - sx)))
            relative_x = math.cos(cartesian_angle)
            relative_y = math.sin(cartesian_angle)
            i_relative_y = math.sin(
                math.atan(math.fabs(((HEIGHT - rpy) - sy) / (rpx - sx))))
            i_relative_x = math.cos(
                math.atan(math.fabs((rpy - sy) / ((WIDTH - rpx) - sx))))
            red = ((rrange * relative_x) + rmin)
            green = (grange * i_relative_x) + gmin
            blue = (brange * relative_x) + bmin
        # If you use the relative_y value replace the variable with a 1 and replace relative_x with a 0
        else:
            red = (rmin)
            green = gmin
            blue = (bmin)
    elif gradient == 1:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        color4 = (100, 50, 150)

        reference_point1 = (WIDTH/2, 0)
        reference_point2 = (WIDTH, HEIGHT/2)
        reference_point3 = (WIDTH/2, HEIGHT)
        reference_point4 = (0, HEIGHT/2)

        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 1:
            color1 = (40, 0, 0)
            color2 = (60, 0, 0)
            color3 = (80, 0, 0)
            color4 = (60, 0, 0)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
            color4 = (127, 127, 127)
        elif color_scheme == 3:
            color1 = (100, 0, 0)
            color2 = (50, 50, 50)
            color3 = (0, 100, 100)
            color4 = (50, 50, 50)
        elif color_scheme == 4:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
            color4 = (255, 50, 150)
        elif color_scheme == 6:
            color1 = (25, 0, 100)
            color2 = (75, 50, 100)
            color3 = (125, 100, 100)
            color4 = (75, 50, 100)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
            color4 = (108, 91, 123)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (0, 255, 0)
            color3 = (0, 0, 255)
            color4 = (255, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (255, 255, 255)
            color4 = (255, 255, 255)
        red1, green1, blue1 = color1
        red2, green2, blue2 = color2
        red3, green3, blue3 = color3
        red4, green4, blue4 = color4
        rpx1, rpy1 = reference_point1
        rpx2, rpy2 = reference_point2
        rpx3, rpy3 = reference_point3
        rpx4, rpy4 = reference_point4
        distance = math.sqrt(math.pow(WIDTH, 2) + math.pow(HEIGHT, 2))
        increment = 255 / distance
        distance1 = math.sqrt(
            math.pow(sx - rpx1, 2) + math.pow(sy - rpy1, 2))
        distance2 = math.sqrt(
            math.pow(sx - rpx2, 2) + math.pow(sy - rpy2, 2))
        distance3 = math.sqrt(
            math.pow(sx - rpx3, 2) + math.pow(sy - rpy3, 2))
        distance4 = math.sqrt(
            math.pow(sx - rpx4, 2) + math.pow(sy - rpy4, 2))
        red = ((red1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
               + (red2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
               + (red3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
               + (red4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
        green = ((green1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                 + (green2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                 + (green3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
                 + (green4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
        blue = ((blue1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                + (blue2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                + (blue3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
                + (blue4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
    elif gradient == 2:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        color4 = (100, 50, 150)

        reference_point1 = (0, 0)
        reference_point2 = (0, HEIGHT)
        reference_point3 = (WIDTH, HEIGHT)
        reference_point4 = (WIDTH, 0)

        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 1:
            color1 = (40, 0, 0)
            color2 = (60, 0, 0)
            color3 = (80, 0, 0)
            color4 = (60, 0, 0)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
            color4 = (127, 127, 127)
        elif color_scheme == 3:
            color1 = (100, 0, 0)
            color2 = (50, 50, 50)
            color3 = (0, 100, 100)
            color4 = (50, 50, 50)
        elif color_scheme == 4:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
            color4 = (255, 50, 150)
        elif color_scheme == 6:
            color1 = (25, 0, 100)
            color2 = (75, 50, 100)
            color3 = (125, 100, 100)
            color4 = (75, 50, 100)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
            color4 = (108, 91, 123)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (0, 255, 0)
            color3 = (0, 0, 255)
            color4 = (255, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (255, 255, 255)
            color4 = (255, 255, 255)
        red1, green1, blue1 = color1
        red2, green2, blue2 = color2
        red3, green3, blue3 = color3
        red4, green4, blue4 = color4
        rpx1, rpy1 = reference_point1
        rpx2, rpy2 = reference_point2
        rpx3, rpy3 = reference_point3
        rpx4, rpy4 = reference_point4
        distance = math.sqrt(math.pow(WIDTH, 2) + math.pow(HEIGHT, 2))
        increment = 255 / distance
        distance1 = math.sqrt(
            math.pow(sx - rpx1, 2) + math.pow(sy - rpy1, 2))
        distance2 = math.sqrt(
            math.pow(sx - rpx2, 2) + math.pow(sy - rpy2, 2))
        distance3 = math.sqrt(
            math.pow(sx - rpx3, 2) + math.pow(sy - rpy3, 2))
        distance4 = math.sqrt(
            math.pow(sx - rpx4, 2) + math.pow(sy - rpy4, 2))
        red = ((red1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
               + (red2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
               + (red3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
               + (red4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
        green = ((green1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                 + (green2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                 + (green3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
                 + (green4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
        blue = ((blue1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                + (blue2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                + (blue3 * (math.pow(distance3, 2) / math.pow(distance, 2)))
                + (blue4 * (math.pow(distance4, 2) / math.pow(distance, 2)))) / 2
    elif gradient == 3:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        color4 = (100, 50, 150)

        reference_point1 = (WIDTH/2, 0)
        reference_point2 = (WIDTH, HEIGHT/2)
        reference_point3 = (WIDTH/2, HEIGHT)
        reference_point4 = (0, HEIGHT/2)

        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
            color4 = (207, 186, 225)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
            color4 = (127, 127, 127)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
            color4 = (202, 231, 223)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
            color4 = (255, 222, 0)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
            color4 = (255, 50, 150)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
            color4 = (68, 11, 212)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
            color4 = (108, 91, 123)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
            color4 = (255, 255, 255)
        elif color_scheme == 9:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (255, 255, 255)
            color4 = (255, 255, 255)
        rpx1, rpy1 = reference_point1
        rpx2, rpy2 = reference_point2
        rpx3, rpy3 = reference_point3
        rpx4, rpy4 = reference_point4
        distance1 = math.sqrt(
            math.pow(sx - rpx1, 2) + math.pow(sy - rpy1, 2))
        distance2 = math.sqrt(
            math.pow(sx - rpx2, 2) + math.pow(sy - rpy2, 2))
        distance3 = math.sqrt(
            math.pow(sx - rpx3, 2) + math.pow(sy - rpy3, 2))
        distance4 = math.sqrt(
            math.pow(sx - rpx4, 2) + math.pow(sy - rpy4, 2))
        if min(distance1, distance2, distance3, distance4) == distance1:
            red, green, blue = color1
        elif min(distance1, distance2, distance3, distance4) == distance2:
            red, green, blue = color2
        elif min(distance1, distance2, distance3, distance4) == distance3:
            red, green, blue = color3
        elif min(distance1, distance2, distance3, distance4) == distance4:
            red, green, blue = color4
    elif gradient == 4:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        color4 = (100, 50, 150)

        reference_point1 = (0, 0)
        reference_point2 = (0, HEIGHT)
        reference_point3 = (WIDTH, HEIGHT)
        reference_point4 = (WIDTH, 0)

        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
            color4 = (100, 50, 150)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
            color4 = (207, 186, 225)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
            color4 = (127, 127, 127)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
            color4 = (202, 231, 223)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
            color4 = (255, 222, 0)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
            color4 = (255, 50, 150)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
            color4 = (68, 11, 212)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
            color4 = (108, 91, 123)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
            color4 = (255, 255, 255)
        elif color_scheme == 9:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (255, 255, 255)
            color4 = (255, 255, 255)
        rpx1, rpy1 = reference_point1
        rpx2, rpy2 = reference_point2
        rpx3, rpy3 = reference_point3
        rpx4, rpy4 = reference_point4
        distance1 = math.sqrt(
            math.pow(sx - rpx1, 2) + math.pow(sy - rpy1, 2))
        distance2 = math.sqrt(
            math.pow(sx - rpx2, 2) + math.pow(sy - rpy2, 2))
        distance3 = math.sqrt(
            math.pow(sx - rpx3, 2) + math.pow(sy - rpy3, 2))
        distance4 = math.sqrt(
            math.pow(sx - rpx4, 2) + math.pow(sy - rpy4, 2))
        if min(distance1, distance2, distance3, distance4) == distance1:
            red, green, blue = color1
        elif min(distance1, distance2, distance3, distance4) == distance2:
            red, green, blue = color2
        elif min(distance1, distance2, distance3, distance4) == distance3:
            red, green, blue = color3
        elif min(distance1, distance2, distance3, distance4) == distance4:
            red, green, blue = color4
    elif gradient == 5:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 255, 255)
            color2 = (255, 0, 0)
            color3 = (255, 255, 255)
        if sx < (WIDTH / 3):
            red, green, blue = color1
        elif sx < ((2 * WIDTH) / 3):
            red, green, blue = color2
        elif sx < WIDTH:
            red, green, blue = color3
    elif gradient == 6:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 255, 255)
            color2 = (255, 0, 0)
            color3 = (255, 255, 255)
        if sy < (WIDTH / 3):
            red, green, blue = color1
        elif sy < ((2 * WIDTH) / 3):
            red, green, blue = color2
        elif sy < WIDTH:
            red, green, blue = color3
    elif gradient == 7:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 255, 255)
            color2 = (255, 0, 0)
            color3 = (255, 255, 255)
        if sx % 30 < 10:
            red, green, blue = color1
        elif sx % 30 < 20:
            red, green, blue = color2
        else:
            red, green, blue = color3
    elif gradient == 8:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 255, 255)
            color2 = (255, 0, 0)
            color3 = (255, 255, 255)
        if sy % 30 < 10:
            red, green, blue = color1
        elif sy % 30 < 20:
            red, green, blue = color2
        else:
            red, green, blue = color3
    elif gradient == 9:
        color1 = (100, 0, 100)
        color2 = (100, 50, 150)
        color3 = (100, 100, 200)
        reference_point1 = (0, 0)
        reference_point2 = (WIDTH / 2, HEIGHT / 2)
        reference_point3 = (WIDTH, HEIGHT)
        if color_scheme == 0:
            color1 = (100, 0, 100)
            color2 = (100, 50, 150)
            color3 = (100, 100, 200)
        elif color_scheme == 1:
            color1 = (151, 249, 249)
            color2 = (193, 224, 247)
            color3 = (197, 159, 201)
        elif color_scheme == 2:
            color1 = (255, 255, 255)
            color2 = (127, 127, 127)
            color3 = (0, 0, 0)
        elif color_scheme == 3:
            color1 = (238, 120, 121)
            color2 = (244, 171, 170)
            color3 = (42, 49, 102)
        elif color_scheme == 4:
            color1 = (255, 0, 0)
            color2 = (204, 0, 0)
            color3 = (59, 76, 202)
        elif color_scheme == 5:
            color1 = (255, 0, 100)
            color2 = (255, 50, 150)
            color3 = (255, 100, 200)
        elif color_scheme == 6:
            color1 = (233, 46, 251)
            color2 = (255, 32, 121)
            color3 = (4, 0, 94)
        elif color_scheme == 7:
            color1 = (248, 177, 149)
            color2 = (246, 114, 128)
            color3 = (53, 92, 125)
        elif color_scheme == 8:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (0, 0, 255)
        elif color_scheme == 9:
            color1 = (255, 0, 0)
            color2 = (255, 255, 255)
            color3 = (255, 255, 255)
        red1, green1, blue1 = color1
        red2, green2, blue2 = color2
        red3, green3, blue3 = color3
        rpx1, rpy1 = reference_point1
        rpx2, rpy2 = reference_point2
        rpx3, rpy3 = reference_point3
        distance = math.sqrt(math.pow(WIDTH, 2) + math.pow(HEIGHT, 2))
        increment = 255 / distance
        distance1 = math.sqrt(
            math.pow(sx - rpx1, 2) + math.pow(sy - rpy1, 2))
        distance2 = math.sqrt(
            math.pow(sx - rpx2, 2) + math.pow(sy - rpy2, 2))
        distance3 = math.sqrt(
            math.pow(sx - rpx3, 2) + math.pow(sy - rpy3, 2))
        red = ((red1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
               + (red2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
               + (red3 * (math.pow(distance3, 2) / math.pow(distance, 2)))) / 2
        green = ((green1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                 + (green2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                 + (green3 * (math.pow(distance3, 2) / math.pow(distance, 2)))) / 2
        blue = ((blue1 * (math.pow(distance1, 2) / math.pow(distance, 2)))
                + (blue2 * (math.pow(distance2, 2) / math.pow(distance, 2)))
                + (blue3 * (math.pow(distance3, 2) / math.pow(distance, 2)))) / 2
    return (red, green, blue)
