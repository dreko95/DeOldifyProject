if __name__ == '__main__':
    from deoldify.loss import FeatureLoss
    from deoldify.generators import gen_learner_deep
    from fastai.vision import *
    from pathlib import Path
    import torch
    import warnings
    import os


    os.environ['NUMEXPR_MAX_THREADS'] = '12'
    warnings.filterwarnings("ignore")

    from deoldify import device
    from deoldify.device_id import DeviceId
    device.set(device=DeviceId.GPU0)
    torch.backends.cudnn.benchmark = True

    path = Path('Datasets/combined_256x256')

    bw_files = list((path/'bw').glob('*.jpg')) + list((path/'bw').glob('*.png'))
    color_files = list((path/'color').glob('*.jpg')) + list((path/'color').glob('*.png'))
    print(f"Found {len(bw_files)} files in bw folder")
    print(f"Found {len(color_files)} files in color folder")

    data = (ImageImageList.from_folder(path/'bw')
        .split_by_rand_pct(0.1, seed=42)
        .label_from_func(lambda x: path/'color'/x.name)
        .transform(size=256)
        .databunch(bs=4, num_workers=2)
        .normalize(([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])))

    learn = gen_learner_deep(
        data=data,
        gen_loss=FeatureLoss(),
        arch=models.resnet34,
        nf_factor=1.5
    )
    learn.model_dir = 'models'
    learn.load('combined_128x128') 
    
    learn.fit_one_cycle(6, 1e-6, pct_start=0.2)
    learn.save('combined_256x256')