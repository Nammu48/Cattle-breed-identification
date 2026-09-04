import os
import shutil
import random

# 🔹 Input: processed training data
source_dir = r"F:\Major Project\processed_data\train"

# 🔹 Output: final training folder (85%)
train_dir = r"F:\Major Project\final_data\train"

# 🔥 Clear old data to avoid duplicates
if os.path.exists(train_dir):
    shutil.rmtree(train_dir)

os.makedirs(train_dir, exist_ok=True)

split_ratio = 0.85

for breed in os.listdir(source_dir):
    breed_path = os.path.join(source_dir, breed)

    if os.path.isdir(breed_path):
        images = os.listdir(breed_path)
        random.shuffle(images)

        split_index = int(len(images) * split_ratio)
        train_images = images[:split_index]

        os.makedirs(os.path.join(train_dir, breed), exist_ok=True)

        for img in train_images:
            shutil.copy(os.path.join(breed_path, img),
                        os.path.join(train_dir, breed, img))

print("✅ 85% Training data created successfully!")