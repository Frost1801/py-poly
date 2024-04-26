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
    #rotates and adds text to an image
    def add_rotated_text(self, text, position, order , tilt):
            position = self.getMultilineTextPosition(position, order, tilt)
            textWidth, textHeight = self.font.getsize(text)
            tempImage = Image.new('RGBA', (textWidth, textHeight), (0, 0, 0, 100))
            tempDraw = ImageDraw.Draw(tempImage)
            tempDraw.text((0, 0), text, font=self.font, fill=(0, 0, 0))
            tempImage = tempImage.rotate(tilt, expand=1)
            self.image.paste(tempImage, position, tempImage)
    
    # calculates the offsett to the position of the text
    def getMultilineTextPosition(self, position, order , tilt):
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

path = "resources/img/DEFAULT/blankBoard.png"
editor = ImageEditor(path)
editor.add_text("Hello\nWorld\nCiao\nTest\nAncora\nTesto", (1000, 1000), 45)
#editor.add_text("Hello\nWorld\nCiao", (100, 100), 0)
editor.save_image("test.png")

