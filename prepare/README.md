
docker build -t sa-gan .

docker run -it -u $(id -u):$(id -g)  --runtime=nvidia --gpus=1 -v /mnt/hd:/mnt/hd -v /mnt/hd1:/mnt/hd1 -v /mnt/hd2:/mnt/hd2 sa-gan bash


python3 convert_imagenet_to_records.py

python3 train_imagenet.py --generator_type test --discriminator_type test --data_dir /mnt/hd/myfolder
