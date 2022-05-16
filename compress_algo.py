import image


def get_avg_pxl(_image, col: int, row: int, ratio: int, width: int, height: int):
    r: int = 0
    g: int = 0
    b: int = 0

    col_start: int = col * ratio
    col_end: int = (col + 1) * ratio
    row_start: int = row * ratio
    row_end: int = (row + 1) * ratio
    count: int = 0

    if col_end > width:
        col_end = width
    if row_end > height:
        row_end = height
    for pxl_col in range(col_start, col_end):
        for pxl_row in range(row_start, row_end):
            pxl = _image.get_pixel(pxl_col, pxl_row)
            r = r + pxl.red
            g = g + pxl.green
            b = b + pxl.blue
            count = count + 1
    if int(r / count) > 255:
        print("error red : ", r, " - ", count, " - ", int(r / count))
        pxl.red = 0
    else:
        pxl.red = int(r / count)
    if int(g / count) > 255:
        print("error green : ", g, " - ", count, " - ", int(g / count))
    pxl.green = int(g / count)

    if int(b / count) > 255:
        print("error blue : ", b, " - ", count, " - ", int(b / count))
    pxl.blue = int(b / count)

    return pxl


def reduc_resol(original_image: image, ratio: int):
    width: int = original_image.get_width()
    height: int = original_image.get_height()
    height_target: int = int(height / ratio)
    width_target: int = int(width / ratio)

    compressed_img = image.AbstractImage(height=height_target, width=width_target)

    for row in range(height_target):
        for col in range(width_target):
            pxl_val = get_avg_pxl(original_image, col, row, ratio, width, height)
            compressed_img.set_pixel(col, row, pxl_val)
    return compressed_img


def change_color_depth(img, nb_color: int):
    range_size: int = int(256 / nb_color)
    width: int = img.get_width()
    height: int = img.get_height()
    new_img = image.AbstractImage(height=height, width=width)
    for row in range(height):
        for col in range(width):
            pxl_val = img.get_pixel(col, row)
            pxl_val.red = int(pxl_val.red / range_size) * range_size
            pxl_val.green = int(pxl_val.green / range_size) * range_size
            pxl_val.blue = int(pxl_val.blue / range_size) * range_size
            new_img.set_pixel(col, row, pxl_val)
    return new_img


def read_img(img_name: str):
    img = image.FileImage(img_name)
    return img, img_name


def save_img(img: image, img_name: str, compress_type: str = ""):
    img_name = "Compressed_" + compress_type + "_" + img_name
    img.save(img_name)


def draw_img(img: image, img_name="Draw image"):
    width: int = img.get_width()
    height: int = img.get_height()
    win = image.ImageWin(width, height, img_name)
    img.draw(win)
    return win


def main_resol(img: str, compress_ratio: int):
    #    print("start")
    #    print("Open image")
    original_image, img_name = read_img(img)

    #    print("Compress image")
    compressed_img = reduc_resol(original_image, compress_ratio)

    #    print("Save image")
    save_img(compressed_img, img_name, "resolution")

    #    print("Draw image")
    win1 = draw_img(original_image)
    win2 = draw_img(compressed_img, img)

    #    print("End")
    win1.exit_on_click()
    win2.exit_on_click()


def main_color(img: str, new_color_deepth: int) -> None:
    #    print("start")
    #    print("Open image")
    original_image, img_name = read_img(img)

    #    print("change color image")
    colored_img = change_color_depth(original_image, new_color_deepth)

    #    print("Save image")
    save_img(colored_img, img_name, "color")

    #    print("Draw image")
    win1 = draw_img(original_image)
    win2 = draw_img(colored_img, img)

    #    print("End")
    win1.exit_on_click()
    win2.exit_on_click()


#main_resol("Csud.png", 20)
#
main_color("Csud2.jpg", 16)
