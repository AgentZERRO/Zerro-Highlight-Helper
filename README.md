# 🥷🏻 ZERRO HIGHLIGHT HELPER 🆉🅷🅷
ZHH (**Z**erro **H**ighlight **H**elper) | A helper for ZERѲ users to deploy their NFT collections (series) on [highlight.xyz](https://highlight.xyz).

## Resources:
* [Highlight Series Studio](https://highlight.xyz/tools/collections/create/type/Series)
* [Standard Series Example](https://tools.highlight.xyz/files/highlight-example-project.zip)
---

This repository contains two main scripts for creating and preparing an NFT collection:

1. **`generator.py`** — Generates images and initial metadata for the collection based on layered assets.
2. **`metadata_convertor.py`** — Converts the generated metadata into the [highlight.xyz](https://highlight.xyz) standard format.

---

## 📂 Folder Structure

You must create a `layers` folder containing your artwork layers.  
Each layer contains multiple trait images.  
**The rarity percentage for all items in a single layer must add up to 100%.**

**Example:**
```
layers/
├── background/
│ ├── Blue#40.png
│ ├── Red#30.png
│ ├── Green#30.png
├── body/
│ ├── Human#60.png
│ ├── Robot#40.png
├── hat/ # Optional layer example
│ ├── Cap#20.png
│ ├── Crown#20.png
```


**Notes:**
- File names must include the rarity percentage after the `#` symbol.  
  Example: `Blue#40.png` means this trait has a 40% occurrence rate.
- Optional layers can be automatically detected when the sum of percentages in a trait folder is less than 100%.

---

## 💻 Installation
Install all required dependencies before running the scripts:
```bash
pip install -r requirements.txt
```

## 📦 Dependencies
* pillow — Image processing library for Python.
* numpy — Numerical computations and array handling.
* tqdm — Progress bar utility for loops and iterations (makes it easy to track generation progress).
  
## 🛠 How to Use

### 1. Generate the base collection
```bash
python generator.py
```
This will create your collection's images and base metadata JSON files.

### 2. Convert metadata to the Highlight format
```bash
python metadata_convertor.py
```
This will transform the base metadata into a format compatible with highlight.xyz.

## 🚀 Output
After running both scripts, you will have:
* A folder containing the generated NFT images, ready for upload.
* Corresponding metadata in JSON format.
* Metadata converted to the highlight.xyz standard, ready for upload.

  
## 📌 Example Project Structure
```
project_root/
├── output/
│   ├── images/...
│   ├── metadata/...
├── metadata.json
├── generator.py
├── metadata_convertor.py
├── layers/
│   ├── background/
│   │   ├── Blue#40.png
│   │   ├── Red#30.png
│   │   ├── Green#30.png
│   ├── body/
│   │   ├── Human#60.png
│   │   ├── Robot#40.png
│   ├── hat/
│   │   ├── Cap#20.png
│   │   ├── Crown#20.png
```

---

Hope you enjoy it!
Made with ❤️

[![MΞHDI ⧗](https://img.shields.io/badge/M%CE%9EHDI-Zerion-darkblue)](https://link.zerion.io/)

---
