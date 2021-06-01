# NN-stocks

## Setup 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
mkdir TA
cd TA/
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install

conda create --name NN-stocks python=3
conda activate NN-stocks
conda install TA-Lib plotly pandas


