

import os
from PIL import Image

def resize_and_convert(input_folder, output_folder, size=(800, 800), fmt='JPEG'):
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        path_in = os.path.join(input_folder, file)
        if not os.path.isfile(path_in):
            continue

        try:
            with Image.open(path_in) as img:
                img.thumbnail(size)
                if fmt.upper() == 'JPEG' and img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                name, _ = os.path.splitext(file)
                path_out = os.path.join(output_folder, f"{name}.{fmt.lower()}")
                img.save(path_out, fmt)
                print(f"Saved: {path_out}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

# Example usage
resize_and_convert("input_images", "output_images", (1024, 1024), 'JPEG')
