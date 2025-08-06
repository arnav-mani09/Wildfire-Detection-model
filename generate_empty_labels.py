import os

# Path to your nonfire images
image_dir = "datasets/images/train"  # or datasets/images/val

# Path where you want to save the label files
label_dir = "datasets/labels/train"  # or labels/val
os.makedirs(label_dir, exist_ok=True)

# Supported image extensions
image_exts = ['.jpg', '.jpeg', '.png']

# Loop through images and create empty .txt files
count = 0
for filename in os.listdir(image_dir):
    if os.path.splitext(filename)[1].lower() in image_exts:
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(label_dir, txt_filename)

        # Create empty label file
        with open(txt_path, 'w') as f:
            pass
        count += 1

print(f"✅ Created {count} empty .txt files in {label_dir}")
