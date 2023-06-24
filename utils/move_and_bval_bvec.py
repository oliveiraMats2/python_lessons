import os
import shutil

source_dir = "/media/paim/Eduarda/HCP_diffusion_sample"
destination_dir = "/mnt/arquivos_linux/wile_C/python_lessons/data_b_s"


def copy_bvals_bvecs(source_dir, subject_id):
    try:
        subject_dir = f"{source_dir}/{subject_id}_3T_Diffusion_preproc/{subject_id}/T1w/Diffusion"
        dest_dir = os.path.join(destination_dir, subject_id)

        os.makedirs(dest_dir, exist_ok=True)

        bvals_path = os.path.join(subject_dir, "bvals")
        bvecs_path = os.path.join(subject_dir, "bvecs")

        shutil.copy(bvals_path, dest_dir)
        shutil.copy(bvecs_path, dest_dir)
    except:
        print(subject_id)


subject_ids = [x.replace("_3T_Diffusion_preproc", "") for x in os.listdir(source_dir)]

for subject_id in subject_ids:
    copy_bvals_bvecs(source_dir, subject_id)
