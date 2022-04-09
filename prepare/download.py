
import os
import gdown
from zipfile import ZipFile


"""
## Prepare CelebA data

We'll use face images from the CelebA dataset, resized to 64x64.
"""
if not os.path.exists("celeba_gan"):
    os.makedirs("celeba_gan")

    url = "https://drive.google.com/uc?id=1O7m1010EJjLE5QxLZiM9Fpjs7Oj6e684"
    output = "celeba_gan/data.zip"
    gdown.download(url, output, quiet=True)

    with ZipFile("celeba_gan/data.zip", "r") as zipobj:
        zipobj.extractall("celeba_gan")
print('done')