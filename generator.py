# generator.py
import os
import random
from PIL import Image
import json

# Update this path to your actual main directory
main_path = "./path/to/directory"

# Ensure images and metadata directories exist
output_dir = os.path.join(main_path, "output")
os.makedirs(f"{output_dir}/images", exist_ok=True)
os.makedirs(f"{output_dir}/metadata", exist_ok=True)

# Define layers and their paths
# Adjust the paths according to your directory structure
# Example: layers_raw = [{"name": "Background", "path": "layers/background"}
layers_raw = [
    {"name": "Background", "path": "layers/background"},
    {"name": "‌Body", "path": "layers/body"},
    {"name": "Hat", "path": "layers/hat"}  # Optional
    # An optional layer is a layer in which the sum of the occurrence percentages of its items is not necessarily 100%
]

layers = list(map(lambda layer: {
    "name": layer["name"],
    "path": os.path.join(main_path, layer["path"])
}, layers_raw))


# Function to parse options from the layer directory
def parse_options(path):
    options = []
    for filename in os.listdir(path):
        if "#" in filename and filename.endswith(".png"):
            name_part = filename.split("#")[0]
            rarity_part = int(filename.split("#")[1].replace(".png", ""))
            options.append({
                "filename": filename,
                "name": name_part,
                "rarity": rarity_part
            })
    return options


# Function to select a weighted random option based on rarity
def weighted_random_choice(options):
    total = sum(opt["rarity"] for opt in options)
    r = random.randint(1, total)
    upto = 0
    for opt in options:
        upto += opt["rarity"]
        if upto >= r:
            return opt
    return options[-1]  # fallback


# Function to generate image and metadata for a given token ID
def generate_image_and_metadata(token_id):
    traits = []
    base = None

    for layer in layers:
        options = parse_options(layer["path"])
        total_rarity = sum(opt["rarity"] for opt in options)

        if total_rarity < 100:
            appear_chance = total_rarity / 100.0
            if random.random() > appear_chance:
                traits.append(
                    {"trait_type": layer["name"], "value": "None"}
                )
                continue

        selected = weighted_random_choice(options)

        traits.append({"trait_type": layer["name"], "value": selected["name"]})

        img = Image.open(os.path.join(
            layer["path"], selected["filename"])).convert("RGBA")
        base = img if base is None else Image.alpha_composite(base, img)

    img_path = f"{output_dir}/images/{token_id}.png"
    base = base.resize((750, 750))
    base.save(img_path)
    print(f"✅ Generated image: {img_path}")

    metadata = {
        "name": f"Item #{token_id}",
        "description": "My awesome NFT collection",
        "image": f"{token_id}.png",
        "attributes": traits
    }

    with open(f"{output_dir}/metadata/{token_id}.json", "w") as f:
        json.dump(metadata, f, indent=4)


# Generate images and metadata for n (100) tokens
for i in range(100):
    generate_image_and_metadata(i)
