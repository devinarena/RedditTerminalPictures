from PIL import Image
from io import BytesIO


class ImageHandler:
    """
    Processes images, taking an input image and converting it to ASCII art.
    """

    def __init__(self):
        # Generate a list of ASCII characters based on brightness.
        self.grey_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "

    def convert_image_to_ascii(self, image_bytes):
        """
        Converts an image to ASCII art.
        """
        # Load the image from bytes taken from a GET request to the image URL
        image = Image.open(BytesIO(image_bytes))
        image.thumbnail((270, 270), Image.ANTIALIAS)
        px = image.load()

        ## Convert the image to ASCII art.
        ascii_art = ""
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel = px[x, y]
                # Get the brightness of the pixel using luminance formula.
                bright = 0.2126 * pixel[0] + 0.7152 * pixel[
                    1] + 0.0722 * pixel[2]
                # Get the ASCII character for the pixel.
                ascii_art += self.get_ascii_char(bright)
            ascii_art += "\n"
        
        return ascii_art

    def get_ascii_char(self, bright):
        """
        Looks up the ASCII character for a pixel based on brightness.
        """
        return self.grey_map[int((1 - (bright / 256)) * (len(self.grey_map) - 1))]