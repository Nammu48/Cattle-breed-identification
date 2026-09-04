import os
import shutil
import random

# 🔹 Path to your original dataset
source_dir = r"F:\Major Project\Indian_bovine_breeds\Indian_bovine_breeds"

# 🔹 Path where 80% training data will be stored
train_dir = r"F:\Major Project\split_data\train"

os.makedirs(train_dir, exist_ok=True)

split_ratio = 0.8

for breed in os.listdir(source_dir):
    breed_path = os.path.join(source_dir, breed)

    if os.path.isdir(breed_path):
        images = os.listdir(breed_path)
        random.shuffle(images)

        split_index = int(len(images) * split_ratio)
        train_images = images[:split_index]

        # Create breed folder inside train
        os.makedirs(os.path.join(train_dir, breed), exist_ok=True)

        for img in train_images:
            src = os.path.join(breed_path, img)
            dst = os.path.join(train_dir, breed, img)

            shutil.copy(src, dst)

print("✅ 80% Training data created successfully!")