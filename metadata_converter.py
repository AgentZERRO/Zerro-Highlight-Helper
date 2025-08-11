# metadata_converter.py
import os
import json
import random

token_name = "Item"
token_description = "My awesome NFT collection."

# Update this path to your actual main directory
main_path = "./path/to/directory"

# Ensure input/output directories exist
input_folder = os.path.join(main_path, "output", "metadata")
output_file = os.path.join(main_path, "metadata.json")  # Converted Metadata

# Get a sorted list of all JSON files in the input folder
file_list = sorted(
    [f for f in os.listdir(input_folder) if f.endswith(".json")],
    key=lambda x: int(x.split(".")[0])
)

total = len(file_list)
token_indices = list(range(total))
metadata_ids = list(range(1, total + 1))
random.shuffle(metadata_ids)

merged = []

for metadata_id, token_index in zip(metadata_ids, token_indices):
    filepath = os.path.join(input_folder, f"{token_index}.json")
    with open(filepath, "r") as f:
        data = json.load(f)

    entry = {
        "metadataId": metadata_id,
        "imageRef": f"{token_index}.png",
        "name": data.get("name", f'{token_name} #{token_index}'),
        "description": data.get("description", token_description)
    }

    for attr in data.get("attributes", []):
        trait = attr.get("trait_type")
        value = attr.get("value")
        if trait and value:
            entry[trait] = value

    merged.append(entry)

merged_sorted = sorted(merged, key=lambda x: x["metadataId"])

with open(output_file, "w") as f:
    json.dump(merged_sorted, f, indent=4)

print(f"✅ Done. Randomized metadataId. Static imageRef/token_index preserved.")
