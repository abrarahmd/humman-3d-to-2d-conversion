import os
import json
import numpy as np
import torch
import smplx

DATASET_ROOT = "Datasets"
SMPL_MODEL_DIR = "body_models"
OUTPUT_ROOT = os.path.join(DATASET_ROOT, "output_2d")
CAM_NAME = "kinect_color_000"

smpl = smplx.create(
    model_path=SMPL_MODEL_DIR,
    model_type="smpl",
    gender="neutral",
    use_pca=False,
    batch_size=1
)

all_seqs = [d for d in os.listdir(DATASET_ROOT)
            if os.path.isdir(os.path.join(DATASET_ROOT, d)) and d.startswith("p")]

print(f"🔎 Found {len(all_seqs)} sequences.")

for seq in all_seqs:
    print(f"\nProcessing {seq}...")
    seq_path = os.path.join(DATASET_ROOT, seq)
    smpl_file = os.path.join(seq_path, "smpl_params.npz")
    cam_file = os.path.join(seq_path, "cameras.json")

    if not os.path.exists(smpl_file) or not os.path.exists(cam_file):
        print(f"[!] Skipping {seq} — missing data.")
        continue

    save_dir = os.path.join(OUTPUT_ROOT, seq)
    os.makedirs(save_dir, exist_ok=True)

    data = np.load(smpl_file)
    global_orient = torch.tensor(data["global_orient"], dtype=torch.float32)
    body_pose = torch.tensor(data["body_pose"], dtype=torch.float32)
    betas = torch.tensor(data["betas"][0:1], dtype=torch.float32)
    transl = torch.tensor(data["transl"], dtype=torch.float32)
    n_frames = global_orient.shape[0]

    with open(cam_file, "r") as f:
        cam = json.load(f)[CAM_NAME]
    K = np.array(cam["K"])
    R = np.array(cam["R"])
    T = np.array(cam["T"])

    for i in range(n_frames):
        out = smpl(
            global_orient=global_orient[i].unsqueeze(0),
            body_pose=body_pose[i].unsqueeze(0),
            transl=transl[i].unsqueeze(0),
            betas=betas,
            return_verts=False
        )
        joints_world = out.joints[0].detach().numpy()
        joints_cam = (R @ joints_world.T).T + T
        proj = (K @ joints_cam.T).T
        joints_2d = proj[:, :2] / proj[:, 2:3]

        np.save(os.path.join(save_dir, f"frame_{i:04d}.npy"), joints_2d)

    print(f"{n_frames} frames saved to {save_dir}")

print("\nAll sequences processed.")
