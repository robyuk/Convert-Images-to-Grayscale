# Install opencv-python

import cv2
from pathlib import Path

rootdir=Path('images')

for path in rootdir.rglob('*'):
  image = cv2.imread(f'{rootdir.name}/{path.name}',0)
  cv2.imwrite(f'grey-{rootdir.name}/{path.name}', image)
