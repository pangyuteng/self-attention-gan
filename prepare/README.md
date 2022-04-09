

```

cd prepare
docker build -t sa-gan .
cd ..
docker run -it --runtime=nvidia -w /workdir -v $PWD:/workdir --gpus=1 sa-gan bash

cd /workdir/prepare
python3 download.py
python3 convert_imagenet_to_records.py

cd /workdir
python3 train_imagenet.py --generator_type test --discriminator_type test --data_dir /workdir/preapre/ --batch_size 8

```
