import os
import shutil

# 🔹 Input folders
source_dir = r"F:\Major Project\processed_data\train"
train_dir = r"F:\Major Project\final_data\train"
val_dir = r"F:\Major Project\final_data\validation"

# 🔥 Clear old validation folder if exists
if os.path.exists(val_dir):
    shutil.rmtree(val_dir)

os.makedirs(val_dir, exist_ok=True)

for breed in os.listdir(source_dir):
    source_breed = os.path.join(source_dir, breed)
    train_breed = os.path.join(train_dir, breed)
    val_breed = os.path.join(val_dir, breed)

    if os.path.isdir(source_breed):
        os.makedirs(val_breed, exist_ok=True)

        all_images = set(os.listdir(source_breed))
        train_images = set(os.listdir(train_breed))

        # Remaining images = validation images (15%)
        val_images = list(all_images - train_images)

        for img in val_images:
            shutil.copy(os.path.join(source_breed, img),
                        os.path.join(val_breed, img))

print("✅ 15% Validation data created successfully!")