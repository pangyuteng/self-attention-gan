

```

cd prepare
export DOCKER_BUILDKIT=1
docker build -t sa-gan .
cd ..
docker run -it --runtime=nvidia -w /workdir -v $PWD:/workdir --gpus=1 sa-gan bash

cd /workdir/prepare
python3 download.py
python3 convert_imagenet_to_records.py

cd /workdir
python3 train_imagenet.py --generator_type test --discriminator_type test --data_dir /workdir/prepare/celeba_gan_tfr --batch_size 8


docker run -it -p 6006:6006 --runtime=nvidia -w /workdir -v $PWD:/workdir tensorflow/tensorflow:1.5.1-devel-gpu-py3 bash
tensorboard --bind_all --logdir=checkpoint

```
