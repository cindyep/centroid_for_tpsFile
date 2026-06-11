This program calculates the centroid of the structure that has been outlined with landmarks using tpsDig, i.e. centroid of a set of points.
To use this, please consider the tps file structure example that was used to program the algorithm:

LM=8
1,00000 1,00000
2,00000 2,00000
3,00000 2,00000
4,00000 1,00000
1,00000 3,00000
2,00000 4,00000
3,00000 4,00000
4,00000 3,00000
IMAGE=xyz.jpg
ID=0
LM=3
1,00000 1,00000
2,00000 2,00000
1,00000 3,00000
IMAGE=yzx.jpg
ID=1

To run the program, open the command prompt inside the folder where is both the tps file and this file
Type the command:

python2 getCentroid.py <your_file's_name>.tps
or
python3 getCentroid.py <your_file's_name>.tps

After it's done, the results will be saved in the same folder in a file named <your_file's_name>_CENTROID.tps
