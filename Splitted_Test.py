import os
import shutil
import random

source_dir = r"F:\Major Project\Indian_bovine_breeds\Indian_bovine_breeds"
train_dir = r"F:\Major Project\split_data\train"
test_dir = r"F:\Major Project\split_data\test"

os.makedirs(test_dir, exist_ok=True)

for breed in os.listdir(source_dir):
    breed_path = os.path.join(source_dir, breed)
    train_breed_path = os.path.join(train_dir, breed)
    test_breed_path = os.path.join(test_dir, breed)

    if os.path.isdir(breed_path):
        os.makedirs(test_breed_path, exist_ok=True)

        all_images = set(os.listdir(breed_path))
        train_images = set(os.listdir(train_breed_path))

        # Remaining images = test images
        test_images = list(all_images - train_images)

        for img in test_images:
            shutil.copy(os.path.join(breed_path, img),
                        os.path.join(test_breed_path, img))

print("✅ Test dataset (20%) created successfully!")