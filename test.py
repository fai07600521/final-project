from generate import generate_images
import torch

if __name__ == '__main__':
    generate_images( 
       # --outdir=r"C:\Users\Admin\temp\stylegan2-ada-pytorch\sexy"
        #--trunc=1 
        #--seeds=200000-201000  
        network=r"C:\Users\Admin\temp\stylegan2-ada-pytorch\sexy\network-snapshot-000920.pkl")