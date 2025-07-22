# HuMMan 3D to 2D Keypoint Extraction

This repository provides instructions and a script to extract 2D joint coordinates from the HuMMan dataset using SMPL model parameters and camera intrinsics.

---

## 📦 Required Files

Before starting, download the following from the [HuMMan Hugging Face page](https://huggingface.co/datasets/caizhongang/HuMMan/tree/main/humman_release_v1.0_point):

- `smpl_params.7z` — Contains SMPL pose data (`smpl_params.npz` per sequence)
- `point_cameras.7z` — Contains camera intrinsics (`cameras.json` per sequence)
- `SMPL_NEUTRAL.pkl` — SMPL body model file  
  👉 [Download from the official SMPL site](https://smpl.is.tue.mpg.de/index.html)  
  Use **version 1.1.0** for Python 2.7 (female/male/neutral, 300 shape PCs)

> **After download:**  
Create the following folder structure:
```
body_models/
└── smpl/
└── SMPL_NEUTRAL.pkl # Rename from the downloaded .pkl
```

---

## 🧰 Python Environment Setup

> ⚠️ Requires Python **3.9** (not 3.11+ due to compatibility issues)

### 🔧 Step-by-step:

```bash
# Step 1 — Install Python 3.9 locally (do not add to PATH)
# Install it into: ./python/ inside your project folder

# Step 2 — Create and activate a virtual environment
.\python\python.exe -m venv env
.\env\Scripts\activate.bat

# Step 3 — Select the interpreter in VS Code
# Press Ctrl + Shift + P → "Python: Select Interpreter"
# Choose: D:\WorkoutAnalysisProject\python\python.exe

# Step 4 — Install dependencies
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
├── python/                  
├── env/                
├── 2D_extraction.py      
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
Contact If you have any questions, suggestions, or feedback, please feel free to contact me at [abrargroad2000@gmail.com].
