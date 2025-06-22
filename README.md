# HuMMan 2D Keypoint Extraction

This repository provides instructions and a script to extract 2D joint coordinates from the HuMMan dataset using SMPL model parameters and camera intrinsics.

---

## 📦 Required Files

Before starting, download the following from the [HuMMan Hugging Face page](https://huggingface.co/datasets/caizhongang/HuMMan/tree/main/humman_release_v1.0_point):

- `smpl_params.7z` — Contains SMPL pose data (`smpl_params.npz` per sequence)
- `point_cameras.7z` — Contains camera intrinsics (`cameras.json` per sequence)
- `SMPL_NEUTRAL.pkl` — SMPL body model file  
  👉 [Download from the official SMPL site](https://smpl.is.tue.mpg.de/index.html)  
  Use **version 1.1.0** for Python 2.7 (female/male/neutral, 300 shape PCs)

---

## 🧰 Python Environment Setup

> Python **3.9** is required!

### Step-by-step instructions:

```bash
# 1. Install Python 3.9 (locally, not globally) into ./python/

# 2. Create and activate a virtual environment
.\python\python.exe -m venv env
.\env\Scripts\activate.bat

# 3. Install dependencies
pip install torch==1.12.1
pip install opencv-python==4.10.0.84
pip install smplx==0.1.28 --no-deps
pip install chumpy==0.70
pip install trimesh==4.4.3
pip install tqdm==4.66.4
pip install open3d
pip install numpy==1.23.5

# 4. Install archive extraction tool
pip install py7zr

# 5. Extract the dataset files
py7zr x Smpl_params.7z
py7zr x Point_cameras.7z
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
```
