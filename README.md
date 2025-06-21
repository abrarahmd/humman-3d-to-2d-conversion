# HuMMan 2D Keypoint Extraction

This repository contains all the instructions and scripts to extract 2D joint coordinates from the HuMMan dataset using SMPL model parameters and camera intrinsics.

---

## 📦 Required Files

Before starting, make sure you have the following:

- `Smpl_params.7z` — contains SMPL pose data (`smpl_params.npz` files per sequence)
- `Point_cameras.7z` — contains camera intrinsics (`cameras.json` files per sequence)
- `SMPL_NEUTRAL.pkl` — SMPL body model file  
  👉 [Download from the official SMPL site](https://smpl.is.tue.mpg.de/index.html)

---

## 🧰 Python Environment Setup

> Python **3.9** is required for compatibility with `chumpy`

### Step-by-step instructions:

```bash
# 1. Install Python 3.9 (locally, not globally) into ./python/

# 2. Create and activate a virtual environment
.\python\python.exe -m venv env
.\env\Scripts\activate.bat

# 3. Install archive extraction tool
pip install py7zr

# 4. Extract the dataset files
py7zr x Smpl_params.7z
py7zr x Point_cameras.7z

# 5. Install dependencies
pip install torch==1.12.1
pip install opencv-python==4.10.0.84
pip install smplx==0.1.28 --no-deps
pip install chumpy==0.70
pip install trimesh==4.4.3
pip install tqdm==4.66.4
pip install open3d
pip install numpy==1.23.5
```
## Project Structure
HuMMan-Project/
```
├── Datasets/
│   ├── p000438_a000040/
│   │   ├── smpl_params.npz
│   │   └── cameras.json
│   └── output_2d/
│       └── p000438_a000040/
│           ├── frame_0000.npy
│           ├── frame_0001.npy
│           └── ...
├── body_models/
│   └── smpl/
│       └── SMPL_NEUTRAL.pkl
├── python/                   # Local Python 3.9 install
├── env/                      # Virtual environment
├── 2D_extraction.py          # Main projection script
└── README.md
```
## ▶️ Run the 2D_extraction.py Script

After setting up your environment and extracting the `.7z` files, run the following:

```bash
# Activate your virtual environment
.\env\Scripts\activate.bat

# Run the script
python 2D_extraction.py
