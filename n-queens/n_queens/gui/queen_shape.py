import os
from PIL import Image, ImageDraw, ImageTk

def get_queen_image(cell_size):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    crown_path = os.path.join(current_dir, "crown.png")

    if os.path.exists(crown_path):
        crown_image = Image.open(crown_path).resize((cell_size - 20, cell_size - 20))
    else:
        size = (cell_size - 20, cell_size - 20)
        crown_image = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(crown_image)
        draw.ellipse((0, 0, size[0] - 1, size[1] - 1), fill="gold", outline="orange")

    return ImageTk.PhotoImage(crown_image)
