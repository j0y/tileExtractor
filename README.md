 
This project is made to create tile images from full textures/patterns

cases:
- make cropped wallpaper bigger
- extract tile from staggered tiles
- get tile from patterns with empty space around tiles


use:

To activate this project's virtualenv, run `pipenv shell`.   
Alternatively, run a command inside the virtualenv with `pipenv run`.

`pipenv run python plot.py`

`plot.py` for finding tile size   
`compare.py` for comparing generated maps from test tiles and finding one that identical to original

algo:
- find tiling sizes
- if information is conflicted create several tiles of specified sizes from original map corner
- recreate map from tiles (make sure size is the same)
- compare each map with original


bugs:
Had to remove libqxcb.so from `~/.local/lib/python3.10/site-packages/cv2/qt/plugins/platforms` to run plt for `compare.py` file.
