import os
from tkinter import Tk, filedialog
from rembg import remove, new_session
from PIL import Image, ImageEnhance
import numpy as np
import io

def extract_foreground_from_images(restored_image: Image.Image, product_image: Image.Image) -> Image.Image:
    restored = restored_image.convert('RGBA')
    product = product_image.convert('RGBA')
    restored_np = np.array(restored)
    product_np = np.array(product)
    alpha_mask = product_np[:, :, 3]
    output_np = restored_np.copy()
    output_np[:, :, 3] = alpha_mask
    return Image.fromarray(output_np)

Tk().withdraw()
input_dir = filedialog.askdirectory(title="Select the input folder of images")
output_dir = filedialog.askdirectory(title="Select a folder to save the output")

background_path = filedialog.askopenfilename(title="Select the background image", filetypes=[("PNG Files", "*.png")])
watermark_path = filedialog.askopenfilename(title="Select the watermark image", filetypes=[("PNG Files", "*.png")])
margin = 50
session = new_session('isnet-general-use')

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    if not input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.jfif')):
        continue

    try:
        image = Image.open(input_path)
        original_image = image.copy()

        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)

        with io.BytesIO() as output_buffer:
            image.save(output_buffer, format='WEBP')
            input_data = output_buffer.getvalue()

        output_data = remove(
            input_data,
            session=session,
            only_mask=False,
            alpha_matting=True,
            alpha_matting_foreground_threshold=230,
            alpha_matting_background_threshold=15,
            alpha_matting_erode_size=3
        )

        product_img = Image.open(io.BytesIO(output_data)).convert('RGBA')
        restored_img = original_image.copy()
        final_img = extract_foreground_from_images(restored_img, product_img)

        background = Image.open(background_path)
        watermark = Image.open(watermark_path)

        bg_width, bg_height = background.size
        final_width, final_height = final_img.size

        new_width = bg_width - 2 * margin
        new_height = int(final_height * (new_width / final_width))

        final_img = final_img.resize((new_width, new_height), Image.LANCZOS)

        x_offset = margin
        y_offset = (bg_height - new_height) // 2

        composed_image = background.copy()
        composed_image.paste(final_img, (x_offset, y_offset), final_img.convert('RGBA').getchannel('A'))
        composed_image.paste(watermark, (0, 0), watermark.convert('RGBA').getchannel('A'))

        output_filename = os.path.splitext(filename)[0] + '.png'
        output_path = os.path.join(output_dir, output_filename)
        composed_image.save(output_path, quality=100, optimize=False)
        print(f'✅ Done: {output_filename}')
    except Exception as e:
        print(f'❌ Failed: {filename} | Error: {e}')
