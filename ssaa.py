from PIL import Image

def ssaa(path_in, factor=2, path_out=""):
    # open source signal and convert to rgb
    source = Image.open(path_in).convert("RGB")
    sw, sh = source.size

    # new dimensions (downsample)
    wl = sw // factor
    hl = sh // factor

    # box filter to downsample
    out = source.resize((wl, hl), resample=Image.BOX)
    out.save(path_out)
    return out

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python ssaa.py <input_image> <output_image> [factor]")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]
    factor = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    ssaa(input, factor, output)