import os

# 🔹 Path to your preprocessed data
base_dir = r"F:\Major Project\2.processed_data\train"

for breed in os.listdir(base_dir):
    breed_path = os.path.join(base_dir, breed)

    if os.path.isdir(breed_path):
        images = sorted(os.listdir(breed_path))

        count = 1
        for img in images:
            old_path = os.path.join(breed_path, img)

            if os.path.isfile(old_path):
                new_name = f"{breed.lower()}_{count:03d}.jpg"
                new_path = os.path.join(breed_path, new_name)

                os.rename(old_path, new_path)
                count += 1

        print(f"✅ Renamed images in {breed}")

print("✅ All labels renamed successfully!")