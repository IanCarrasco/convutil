# convutil
A command-line utility for calculating 2D convolution output sizes. 




## Usage
```
input_size => Size of Input Volume (Width, Height, Channels/Filters)
num_filters => Number of output filters
filter_size => Size of 2D Convolution Kernel
stride => 2D Convolution Stride Length
padding => Padding Mode (same:valid)

$ python convutil.py --input_size='(256, 256, 128)' --num_filters=1 --filter_size=4 --stride=2 --padding='same'

>> Input:(256, 256, 128) ➡ Output:(128, 128, 1)
```
