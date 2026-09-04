import os
from PIL import Image

# 🔹 Input: your 80% training data
input_dir = r"F:\Major Project\1.split_data\train"

# 🔹 Output: processed training data
output_dir = r"F:\Major Project\2.processed_data\train"

IMG_SIZE = (224, 224)

for breed in os.listdir(input_dir):
    breed_input = os.path.join(input_dir, breed)
    breed_output = os.path.join(output_dir, breed)

    os.makedirs(breed_output, exist_ok=True)

    for img_name in os.listdir(breed_input):
        img_path = os.path.join(breed_input, img_name)

        try:
            img = Image.open(img_path).convert("RGB")
            img = img.resize(IMG_SIZE)

            new_name = os.path.splitext(img_name)[0] + ".jpg"
            img.save(os.path.join(breed_output, new_name), "JPEG")

        except Exception as e:
            print("Error:", img_name, e)

print("✅ Preprocessing completed!")