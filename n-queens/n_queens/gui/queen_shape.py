"""
این فایل تصویری از مهره وزیر (crown.png) را با اندازه مناسب برای خانه‌های صفحه‌ی شطرنج برمی‌گرداند.
اگر تصویر واقعی تاج وجود داشته باشد، از آن استفاده می‌کند. در غیر این صورت، یک دایره رسم می‌کند.
"""

#کتابخانه ها
import os
from PIL import Image, ImageDraw, ImageTk  # برای کار با تصاویر و تبدیل آن‌ها به فرمت مناسب 


def get_queen_image(cell_size):


    # دریافت مسیر فعلی فایل ( queen_shape.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # ساخت مسیر کامل به فایل (crown.png) در کنار فایل فعلی
    crown_path = os.path.join(current_dir, "crown.png")

    # بررسی اینکه آیا تصویر واقعی تاج وجود دارد یا نه؟
    if os.path.exists(crown_path):
        # اگر تصویر (crown.png) وجود دارد، آن را باز کرده و به اندازه مناسب کوچک می‌کنیم
        crown_image = Image.open(crown_path).resize((cell_size - 20, cell_size - 20))
    else:
        # اگر فایل (crown.png) وجود ندارد، یک تصویر جایگزین ساده ایجاد می‌کنیم
        size = (cell_size - 20, cell_size - 20)

        # ایجاد یک تصویر خالی با پس‌زمینه شفاف (RGBA)
        crown_image = Image.new("RGBA", size, (0, 0, 0, 0))

        # رسم یک دایره به عنوان جایگزین تصویر تاج
        draw = ImageDraw.Draw(crown_image)
        draw.ellipse((0, 0, size[0] - 1, size[1] - 1), fill="gold", outline="orange")

    # تبدیل تصویر نهایی به فرمت قابل استفاده در Tkinter
    return ImageTk.PhotoImage(crown_image)

