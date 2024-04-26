from PIL import Image, ImageDraw, ImageFont
import math

FONT_TYPE = "arial.ttf"
FONT_COLOR = (0,0,0)
FONT_SIZE = 50
BOARD_SIZE = (4096, 4096)
LINE_SPACING = 50

DECIMALS = 10

class ImageEditor:
        def __init__(self, image_path, font_type=FONT_TYPE, font_size=FONT_SIZE, font_color=FONT_COLOR):
                self.image = Image.open(image_path)
                self.draw = ImageDraw.Draw(self.image)
                self.font = ImageFont.truetype(font_type, font_size) 
                self.text_color = font_color
        def addRectangle (self, position, size, fill_color, outline_color, outline_width = 10):
                self.draw.rectangle([position, (position[0]+size[0], position[1]+size[1])], fill=fill_color, outline=outline_color, width=outline_width)

        #rotates and adds text to an image
        def add_rotated_text(self, text, position, order , tilt):
                position = self._getMultilineTextPosition(position, order, tilt)
                textWidth, textHeight = self.font.getsize(text)
                tempImage = Image.new('RGBA', (textWidth,textHeight), (0, 0, 0, 10))
                tempDraw = ImageDraw.Draw(tempImage)
                tempDraw.text((0, 0), text, font=self.font, fill=(0, 0, 0))
                tempImage = tempImage.rotate(tilt, expand=1)
                self.image.paste(tempImage, position, tempImage)

        # calculates the offsett to the position of the text
        def _getMultilineTextPosition(self, position, order , tilt):
                offsetx = order *LINE_SPACING* round (math.sin(math.radians(tilt)), DECIMALS) 
                offsety = order *LINE_SPACING* round(math.cos(math.radians(tilt)), DECIMALS)
                position = (position[0] + int(offsetx), position[1] + int(offsety))
                return position
        # adds text to the image
        def add_text(self, text, position, tilt = 0):
                lines = text.split("\n")
                for i in range (0, len(lines)):
                        self.add_rotated_text(lines[i], position, i,tilt)   
        def save_image(self, output_path):
                self.image.save(output_path)
        def add_image (self, imagePath, position, size = 100):
                image = Image.open(imagePath)
                if size != 100: 
                        image = image.resize((int(image.width*size/100), int(image.height*size/100)))
                self.image.paste(image, position, image)




path = "resources/img/DEFAULT/blankBoard.png"
editor = ImageEditor(path)
#TODO design a way to get an accurate centered position for the text
editor.add_text("Vicolone\nCortone", (3330, 3750), 0)
editor.add_text("Vicolone\nCortone", (100, 3750), 90)
editor.add_text("Vicolone\nCortone\nCartone", (3330 , 100), 270)
editor.add_text("Vicolone\nCortone\nCartone", (330 , 1000), 180)
editor.addRectangle ((1000,1000),(500,200), (255,0,0), (0,0,0))
editor.add_image ("resources/img/DEFAULT/train.png", (1000, 1000), 50)

editor.save_image("test.png")

        