from PIL import Image, ImageDraw, ImageFont

FONT_TYPE = "arial.ttf"
FONT_COLOR = (0,0,0)
FONT_SIZE = 50
BOARD_SIZE = (4096, 4096)

class ImageEditor:
    def __init__(self, image_path, font_type=FONT_TYPE, font_size=FONT_SIZE, font_color=FONT_COLOR):
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(font_type, font_size) 
        self.text_color = font_color  



    def add_text(self, text, position, tilt = 0):
        if tilt != 0:
            textWidth, textHeight = self.font.getsize(text)
            tempImage = Image.new('RGBA', (textWidth, textHeight ), (0, 0, 0, 0))
            tempDraw = ImageDraw.Draw(tempImage)
            tempDraw.text((0, 0), text, font=self.font, fill=(0, 0, 0))
            tempImage = tempImage.rotate(tilt, expand=1)
            sx, sy = tempImage.size
            self.image.paste(tempImage, (position[0], position[1]), tempImage)
  
        else:
            self.draw.text(position, text, fill=self.text_color, font=self.font)
        
    def save_image(self, output_path):
        self.image.save(output_path)

path = "resources/img/DEFAULT/blankBoard.png"
editor = ImageEditor(path)
editor.add_text("Hello\nWorld", (100, 100), 180)
editor.add_text("Hello\nWorld", (100, 100), 0)
editor.save_image("test.png")

