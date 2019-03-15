from PIL import Image

def perception(path):
    img = Image.open(path)
    pixels = img.load()
    brightness = []

    for i in range(img.size[0]):
        brightness.append([0] * img.size[1])

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = pixels[i, j][0]
            g = pixels[i, j][1]
            b = pixels[i, j][2]
            brightness[i][j] = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return brightness


def sorting(brightness, x, y):
    d = dict()
    for i in range(x):
        avg = sum(brightness[i]) / y
        d[i] = avg

    pattern = list(d.items())
    pattern = [list(x) for x in pattern]

    for i in pattern:
        i[0], i[1] = i[1], i[0]

    pattern.sort()
    return pattern


def building(pattern, x, y, pixels, destination):
    img = Image.new('RGB', (x, y), 'black')
    result = img.load()
    col = 0

    for i in pattern:
        for j in range(y):
            result[col, j] = pixels[i[1], j]
        col += 1

    img.save(destination)

def pixelmap(path):
    img = Image.open(path)
    return img.load()

def col(path):
    img = Image.open(path)
    return img.size[0]

def row(path):
    img = Image.open(path)
    return img.size[1]

#building(sorting(perception(path), col(path), row(path)), col(path), row(path), pixelmap(path))
