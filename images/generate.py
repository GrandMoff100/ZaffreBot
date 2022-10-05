import itertools
from PIL import Image


def main():
    with Image.open("images/bg.png") as img:
        scale = 120
        x_shift = 430
        y_shift = 0
        img = img.crop((x_shift, y_shift, x_shift + img.height - scale, y_shift + img.height - scale))
        with Image.open("images/github.webp") as layer:
            layer_px = layer.load()
            for i, j in itertools.product(range(layer.width), range(layer.height)):
                layer_px[i,j] = (220, 220, 220, layer_px[i,j][-1])
                # if (i-layer.width//2) ** 2 + (j-layer.height//2) ** 2 >= 250 ** 2:
                #     layer_px[i,j] = (0, 0, 0, 255)
            pasted = Image.new("RGBA", img.size, (0,0,0,255))
            pasted.paste(img.resize((img.width, img.height)), (0, 0))
            
            pasted.paste(layer.resize(img.size), (0, 0), layer.resize(img.size))
            pasted.save("output.png")

if __name__ == "__main__":
    main()