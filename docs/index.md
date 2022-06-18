# Welcome to pygis

[![image](https://img.shields.io/pypi/v/pygis.svg)](https://pypi.python.org/pypi/pygis)
[![image](https://img.shields.io/conda/vn/conda-forge/pygis.svg)](https://anaconda.org/conda-forge/pygis)
[![image](https://pepy.tech/badge/pygis)](https://pepy.tech/project/pygis)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pygis.svg)](https://anaconda.org/conda-forge/pygis)
[![Conda Recipe](https://img.shields.io/badge/recipe-pygis-green.svg)](https://github.com/conda-forge/pygis-feedstock)
[![image](https://img.shields.io/badge/YouTube-Channel-red)](https://www.youtube.com/c/QiushengWu)
[![image](https://img.shields.io/twitter/follow/giswqs?style=social)](https://twitter.com/giswqs)

**A Python package for installing optional dependencies for geemap and leafmap.**

- Free software: MIT license
- Documentation: <https://pygis.gishub.org>

## Disclaimer

Currently, the `pygis` package only helps you install optional dependencies for [geemap](https://geemap.org/) and [leafmap](https://leafmap.org/), making it easier to set up a conda environment for geospatial analysis and avoid dependency conflicts during installation. The `pygis` package itself does not have any meaningful functions yet. After installation, you can continue to the commonly used geospatial packages as usual.

## Installation

Installing optional dependencies for [geemap](https://geemap.org/) and [leafmap](https://leafmap.org/) with only one command.

```bash
mamba install -c conda-forge pygis
```

## Video Tutorial

[![Introducing pygis](images/thumbnail.png)](https://youtu.be/4eY4cmnOGVI "Introducing pygis")

## Conda-forge recipe

The [recipe](https://github.com/conda-forge/pygis-feedstock/blob/main/recipe/meta.yaml) of the pygis Python package on the conda-forge channel:

    - python >=3.7
    - datapane
    - geedim
    - geemap >=0.14.0
    - geopandas
    - here-map-widget-for-jupyter
    - ipynb-py-convert
    - keplergl
    - leafmap >=0.9.4
    - localtileserver >=0.5.8
    - netcdf4
    - osmnx
    - owslib
    - palettable
    - plotly
    - pydeck
    - python-mss
    - rio-cogeo
    - rioxarray
    - voila

## Installed packages

The complete list of Python packages that will be installed along with pygis.

```bash
!conda list
```

```text
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                 conda_forge    conda-forge
_openmp_mutex             4.5                  2_kmp_llvm    conda-forge
abseil-cpp                20211102.0           h27087fc_1    conda-forge
affine                    2.3.1              pyhd8ed1ab_0    conda-forge
aiohttp                   3.8.1            py39hb9d737c_1    conda-forge
aiosignal                 1.2.0              pyhd8ed1ab_0    conda-forge
alsa-lib                  1.2.3.2              h166bdaf_0    conda-forge
altair                    4.2.0              pyhd8ed1ab_1    conda-forge
aniso8601                 9.0.1              pyhd8ed1ab_0    conda-forge
anyio                     3.6.1            py39hf3d152e_0    conda-forge
aom                       3.3.0                h27087fc_1    conda-forge
argon2-cffi               21.1.0           py39h3811e60_2    conda-forge
arrow-cpp                 6.0.1           py39h15c4769_19_cpu    conda-forge
asttokens                 2.0.5              pyhd8ed1ab_0    conda-forge
async-timeout             4.0.2              pyhd8ed1ab_0    conda-forge
attr                      2.5.1                h166bdaf_0    conda-forge
attrs                     21.4.0             pyhd8ed1ab_0    conda-forge
aws-c-cal                 0.5.11               h95a6274_0    conda-forge
aws-c-common              0.6.2                h7f98852_0    conda-forge
aws-c-event-stream        0.2.7               h3541f99_13    conda-forge
aws-c-io                  0.10.5               hfb6a706_0    conda-forge
aws-checksums             0.1.11               ha31a3da_7    conda-forge
aws-sdk-cpp               1.8.186              hb4091e7_3    conda-forge
babel                     2.10.2             pyhd8ed1ab_0    conda-forge
backcall                  0.2.0              pyh9f0ad1d_0    conda-forge
backoff                   1.11.1             pyhd8ed1ab_0    conda-forge
backports                 1.0                        py_2    conda-forge
backports.functools_lru_cache 1.6.4              pyhd8ed1ab_0    conda-forge
beautifulsoup4            4.11.1             pyha770c72_0    conda-forge
bleach                    5.0.0              pyhd8ed1ab_0    conda-forge
blosc                     1.21.1               h83bc5f7_3    conda-forge
boltons                   21.0.0             pyhd8ed1ab_0    conda-forge
boost-cpp                 1.74.0               h6cacc03_7    conda-forge
bqplot                    0.12.33            pyhd8ed1ab_0    conda-forge
branca                    0.4.2              pyhd8ed1ab_0    conda-forge
brotli                    1.0.9                h166bdaf_7    conda-forge
brotli-bin                1.0.9                h166bdaf_7    conda-forge
brotlipy                  0.7.0           py39hb9d737c_1004    conda-forge
bzip2                     1.0.8                h7f98852_4    conda-forge
c-ares                    1.18.1               h7f98852_0    conda-forge
ca-certificates           2022.6.15            ha878542_0    conda-forge
cachetools                4.2.4              pyhd8ed1ab_0    conda-forge
cairo                     1.16.0            ha12eb4b_1010    conda-forge
certifi                   2022.6.15        py39hf3d152e_0    conda-forge
cffi                      1.15.0           py39hd667e15_1
cfitsio                   4.1.0                hd9d235c_0    conda-forge
cftime                    1.6.0            py39hd257fcd_1    conda-forge
chardet                   4.0.0            py39hf3d152e_3    conda-forge
charset-normalizer        2.0.12             pyhd8ed1ab_0    conda-forge
click                     8.1.3            py39hf3d152e_0    conda-forge
click-plugins             1.1.1                      py_0    conda-forge
click-spinner             0.1.10             pyh9f0ad1d_0    conda-forge
cligj                     0.7.2              pyhd8ed1ab_1    conda-forge
colorama                  0.4.4              pyh9f0ad1d_0    conda-forge
colorlog                  6.6.0            py39hf3d152e_1    conda-forge
colour                    0.1.5                      py_0    conda-forge
conda                     4.13.0           py39hf3d152e_1    conda-forge
conda-package-handling    1.8.1            py39hb9d737c_1    conda-forge
cryptography              37.0.2           py39hd97740a_0    conda-forge
curl                      7.83.1               h7bff187_0    conda-forge
cycler                    0.11.0             pyhd8ed1ab_0    conda-forge
dacite                    1.6.0              pyhd3deb0d_0    conda-forge
dataclasses               0.8                pyhc8e2a94_3    conda-forge
datapane                  0.14.0             pyhd8ed1ab_0    conda-forge
dbus                      1.13.6               h5008d03_3    conda-forge
debugpy                   1.6.0            py39h5a03fae_0    conda-forge
decorator                 5.1.1              pyhd8ed1ab_0    conda-forge
defusedxml                0.7.1              pyhd8ed1ab_0    conda-forge
dominate                  2.6.0              pyhd8ed1ab_0    conda-forge
earthengine-api           0.1.315            pyhd8ed1ab_0    conda-forge
ee_extra                  0.0.13             pyhd8ed1ab_0    conda-forge
entrypoints               0.4                pyhd8ed1ab_0    conda-forge
executing                 0.8.3              pyhd8ed1ab_0    conda-forge
expat                     2.4.8                h27087fc_0    conda-forge
face                      20.1.1                     py_0    conda-forge
ffmpeg                    5.0.1                h594f047_0    conda-forge
ffmpeg-python             0.2.0                      py_0    conda-forge
fftw                      3.3.10          nompi_h77c792f_102    conda-forge
filelock                  3.7.1              pyhd8ed1ab_0    conda-forge
fiona                     1.8.21           py39h83acdc4_1    conda-forge
flask                     2.1.2              pyhd8ed1ab_1    conda-forge
flask-caching             1.10.1             pyhd8ed1ab_0    conda-forge
flask-cors                3.0.10             pyhd8ed1ab_0    conda-forge
flask-restx               0.5.1              pyhd8ed1ab_0    conda-forge
folium                    0.12.1.post1       pyhd8ed1ab_1    conda-forge
font-ttf-dejavu-sans-mono 2.37                 hab24e00_0    conda-forge
font-ttf-inconsolata      3.000                h77eed37_0    conda-forge
font-ttf-source-code-pro  2.038                h77eed37_0    conda-forge
font-ttf-ubuntu           0.83                 hab24e00_0    conda-forge
fontconfig                2.14.0               h8e229c2_0    conda-forge
fonts-conda-ecosystem     1                             0    conda-forge
fonts-conda-forge         1                             0    conda-forge
fonttools                 4.33.3           py39hb9d737c_0    conda-forge
freetype                  2.10.4               h0708190_1    conda-forge
freexl                    1.0.6                h7f98852_0    conda-forge
frozenlist                1.3.0            py39hb9d737c_1    conda-forge
furl                      2.1.3              pyhd8ed1ab_0    conda-forge
future                    0.18.2           py39hf3d152e_5    conda-forge
gdal                      3.4.3            py39hc691d54_0    conda-forge
gdown                     4.4.0              pyhd8ed1ab_0    conda-forge
geeadd                    0.5.4              pyhd8ed1ab_0    conda-forge
geemap                    0.13.11            pyhd8ed1ab_0    conda-forge
geocoder                  1.38.1                     py_1    conda-forge
geojson                   2.5.0                      py_0    conda-forge
geopandas                 0.10.2             pyhd8ed1ab_1    conda-forge
geopandas-base            0.10.2             pyha770c72_1    conda-forge
geos                      3.10.2               h9c3ff4c_0    conda-forge
geotiff                   1.7.1                h509b78c_1    conda-forge
gettext                   0.19.8.1          h73d1719_1008    conda-forge
gflags                    2.2.2             he1b5a44_1004    conda-forge
giflib                    5.2.1                h36c2ea0_2    conda-forge
glog                      0.6.0                h6f12383_0    conda-forge
glom                      20.11.0            pyhd3deb0d_0    conda-forge
gmp                       6.2.1                h58526e2_0    conda-forge
gnutls                    3.6.13               h85f3911_1    conda-forge
google-api-core           1.31.5             pyhd8ed1ab_0    conda-forge
google-api-python-client  1.12.8             pyhd3deb0d_0    conda-forge
google-auth               1.35.0             pyh6c4a22f_0    conda-forge
google-auth-httplib2      0.1.0              pyhd8ed1ab_1    conda-forge
google-cloud-core         2.3.1              pyhd8ed1ab_0    conda-forge
google-cloud-storage      2.4.0              pyh6c4a22f_0    conda-forge
google-crc32c             1.1.2            py39h8db88ab_3    conda-forge
google-resumable-media    2.3.3              pyhd8ed1ab_0    conda-forge
googleapis-common-protos  1.56.2           py39hf3d152e_0    conda-forge
grpc-cpp                  1.45.2               he70e3f0_3    conda-forge
grpcio                    1.46.3           py39h0f497a6_0    conda-forge
gst-plugins-base          1.18.5               hf529b03_3    conda-forge
gstreamer                 1.20.2               hd4edc92_1    conda-forge
hdf4                      4.2.15               h10796ff_3    conda-forge
hdf5                      1.12.1          nompi_h2386368_104    conda-forge
here-map-widget-for-jupyter 1.1.3              pyhd8ed1ab_0    conda-forge
httplib2                  0.20.4             pyhd8ed1ab_0    conda-forge
httplib2shim              0.0.3              pyh9f0ad1d_0    conda-forge
icu                       69.1                 h9c3ff4c_0    conda-forge
idna                      3.3                pyhd8ed1ab_0    conda-forge
importlib-metadata        4.11.4           py39hf3d152e_0    conda-forge
importlib_metadata        4.11.4               hd8ed1ab_0    conda-forge
importlib_resources       5.7.1              pyhd8ed1ab_1    conda-forge
ipyevents                 2.0.1              pyhd8ed1ab_0    conda-forge
ipyfilechooser            0.6.0              pyhd8ed1ab_0    conda-forge
ipykernel                 6.14.0           py39hef51801_0    conda-forge
ipyleaflet                0.16.0             pyhd8ed1ab_4    conda-forge
ipynb-py-convert          0.4.6              pyh9f0ad1d_0    conda-forge
ipysheet                  0.5.0              pyhd8ed1ab_0    conda-forge
ipython                   8.4.0            py39hf3d152e_0    conda-forge
ipython_genutils          0.2.0                      py_1    conda-forge
ipytree                   0.2.1              pyhd8ed1ab_0    conda-forge
ipywidgets                7.7.0              pyhd8ed1ab_0    conda-forge
itsdangerous              2.1.2              pyhd8ed1ab_0    conda-forge
jack                      1.9.18            hfd4fe87_1001    conda-forge
jedi                      0.18.1           py39hf3d152e_1    conda-forge
jinja2                    3.0.3              pyhd8ed1ab_0    conda-forge
joblib                    1.1.0              pyhd8ed1ab_0    conda-forge
jpeg                      9e                   h166bdaf_1    conda-forge
json-c                    0.16                 hc379101_0    conda-forge
json5                     0.9.5              pyh9f0ad1d_0    conda-forge
jsonschema                4.6.0              pyhd8ed1ab_0    conda-forge
jupyter_client            7.3.4              pyhd8ed1ab_0    conda-forge
jupyter_core              4.10.0           py39hf3d152e_0    conda-forge
jupyter_server            1.17.1             pyhd8ed1ab_0    conda-forge
jupyterlab                3.4.3              pyhd8ed1ab_0    conda-forge
jupyterlab_pygments       0.2.2              pyhd8ed1ab_0    conda-forge
jupyterlab_server         2.14.0             pyhd8ed1ab_0    conda-forge
jupyterlab_widgets        1.1.0              pyhd8ed1ab_0    conda-forge
kealib                    1.4.14               hfe1a663_4    conda-forge
keplergl                  0.3.2              pyhd8ed1ab_0    conda-forge
keyutils                  1.6.1                h166bdaf_0    conda-forge
kiwisolver                1.4.3            py39hf939315_0    conda-forge
krb5                      1.19.3               h3790be6_0    conda-forge
lame                      3.100             h7f98852_1001    conda-forge
large-image               1.14.5             pyhd8ed1ab_0    conda-forge
large-image-source-gdal   1.14.5             pyhd8ed1ab_0    conda-forge
lcms2                     2.12                 hddcbb42_0    conda-forge
ld_impl_linux-64          2.38                 h1181459_1
leafmap                   0.9.4              pyhd8ed1ab_0    conda-forge
lerc                      3.0                  h9c3ff4c_0    conda-forge
libarchive                3.5.2                hccf745f_1    conda-forge
libblas                   3.9.0           15_linux64_openblas    conda-forge
libbrotlicommon           1.0.9                h166bdaf_7    conda-forge
libbrotlidec              1.0.9                h166bdaf_7    conda-forge
libbrotlienc              1.0.9                h166bdaf_7    conda-forge
libcap                    2.64                 ha37c62d_0    conda-forge
libcblas                  3.9.0           15_linux64_openblas    conda-forge
libclang                  13.0.1          default_hc23dcda_0    conda-forge
libcrc32c                 1.1.2                h9c3ff4c_0    conda-forge
libcups                   2.3.3                hf5a7f15_1    conda-forge
libcurl                   7.83.1               h7bff187_0    conda-forge
libdap4                   3.20.6               hd7c4107_2    conda-forge
libdb                     6.2.32               h9c3ff4c_0    conda-forge
libdeflate                1.12                 h166bdaf_0    conda-forge
libdrm                    2.4.111              h166bdaf_0    conda-forge
libedit                   3.1.20191231         he28a2e2_2    conda-forge
libev                     4.33                 h516909a_1    conda-forge
libevent                  2.1.10               h9b69904_4    conda-forge
libffi                    3.4.2                h7f98852_5    conda-forge
libflac                   1.3.4                h27087fc_0    conda-forge
libgcc-ng                 12.1.0              h8d9b700_16    conda-forge
libgdal                   3.4.3                h56144a5_0    conda-forge
libgfortran-ng            12.1.0              h69a702a_16    conda-forge
libgfortran5              12.1.0              hdcd56e2_16    conda-forge
libglib                   2.70.2               h174f98d_4    conda-forge
libiconv                  1.16                 h516909a_0    conda-forge
libkml                    1.3.0             h238a007_1014    conda-forge
liblapack                 3.9.0           15_linux64_openblas    conda-forge
libllvm13                 13.0.1               hf817b99_2    conda-forge
libmamba                  0.24.0               hd8a31e3_1    conda-forge
libmambapy                0.24.0           py39hd55135b_1    conda-forge
libnetcdf                 4.8.1           nompi_h329d8a1_102    conda-forge
libnghttp2                1.47.0               h727a467_0    conda-forge
libnsl                    2.0.0                h7f98852_0    conda-forge
libogg                    1.3.4                h7f98852_1    conda-forge
libopenblas               0.3.20          pthreads_h78a6416_0    conda-forge
libopus                   1.3.1                h7f98852_1    conda-forge
libpciaccess              0.16                 h516909a_0    conda-forge
libpng                    1.6.37               h21135ba_2    conda-forge
libpq                     14.2                 hd57d9b9_0    conda-forge
libprotobuf               3.20.1               h6239696_0    conda-forge
librttopo                 1.1.0                hf69c175_9    conda-forge
libsndfile                1.0.31               h9c3ff4c_1    conda-forge
libsodium                 1.0.18               h36c2ea0_1    conda-forge
libsolv                   0.7.22               h6239696_0    conda-forge
libspatialindex           1.9.3                h9c3ff4c_4    conda-forge
libspatialite             5.0.1               ha867d66_15    conda-forge
libssh2                   1.10.0               ha56f1ee_2    conda-forge
libstdcxx-ng              12.1.0              ha89aaad_16    conda-forge
libthrift                 0.16.0               h519c5ea_1    conda-forge
libtiff                   4.4.0                hc85c160_1    conda-forge
libtool                   2.4.6             h9c3ff4c_1008    conda-forge
libudev1                  249                  h166bdaf_4    conda-forge
libutf8proc               2.7.0                h7f98852_0    conda-forge
libuuid                   2.32.1            h7f98852_1000    conda-forge
libva                     2.14.0               h7f98852_0    conda-forge
libvorbis                 1.3.7                h9c3ff4c_0    conda-forge
libvpx                    1.11.0               h9c3ff4c_3    conda-forge
libwebp                   1.2.2                h3452ae3_0    conda-forge
libwebp-base              1.2.2                h7f98852_1    conda-forge
libxcb                    1.13              h7f98852_1004    conda-forge
libxkbcommon              1.0.3                he3ba5ed_0    conda-forge
libxml2                   2.9.12               h885dcf4_1    conda-forge
libxslt                   1.1.33               h0ef7038_3    conda-forge
libzip                    1.8.0                h4de3113_1    conda-forge
libzlib                   1.2.12               h166bdaf_1    conda-forge
llvm-openmp               14.0.4               he0ac6c6_0    conda-forge
localtileserver           0.5.8              pyhd8ed1ab_0    conda-forge
logzero                   1.7.0            py39hf3d152e_2    conda-forge
lxml                      4.8.0            py39hb9d737c_2    conda-forge
lz4-c                     1.9.3                h9c3ff4c_1    conda-forge
lzo                       2.10              h516909a_1000    conda-forge
mamba                     0.24.0           py39hfa8f2c8_1    conda-forge
mapclassify               2.4.3              pyhd8ed1ab_0    conda-forge
markupsafe                2.1.1            py39hb9d737c_1    conda-forge
matplotlib                3.5.2            py39hf3d152e_0    conda-forge
matplotlib-base           3.5.2            py39h700656a_0    conda-forge
matplotlib-inline         0.1.3              pyhd8ed1ab_0    conda-forge
micawber                  0.5.4              pyhd8ed1ab_0    conda-forge
mistune                   0.8.4           py39h3811e60_1005    conda-forge
monotonic                 1.5                        py_0    conda-forge
morecantile               3.1.2              pyhd8ed1ab_0    conda-forge
multidict                 6.0.2            py39hb9d737c_1    conda-forge
munch                     2.5.0                      py_0    conda-forge
munkres                   1.1.4              pyh9f0ad1d_0    conda-forge
mysql-common              8.0.29               haf5c9bc_1    conda-forge
mysql-libs                8.0.29               h28c427c_1    conda-forge
nbclassic                 0.3.7              pyhd8ed1ab_0    conda-forge
nbclient                  0.5.13             pyhd8ed1ab_0    conda-forge
nbconvert                 6.5.0              pyhd8ed1ab_0    conda-forge
nbconvert-core            6.5.0              pyhd8ed1ab_0    conda-forge
nbconvert-pandoc          6.5.0              pyhd8ed1ab_0    conda-forge
nbformat                  5.4.0              pyhd8ed1ab_0    conda-forge
ncurses                   6.3                  h7f8727e_2
nest-asyncio              1.5.5              pyhd8ed1ab_0    conda-forge
netcdf4                   1.5.8           nompi_py39h64b754b_101    conda-forge
nettle                    3.6                  he412f7d_0    conda-forge
networkx                  2.8.4              pyhd8ed1ab_0    conda-forge
notebook                  6.4.12             pyha770c72_0    conda-forge
notebook-shim             0.1.0              pyhd8ed1ab_0    conda-forge
nspr                      4.32                 h9c3ff4c_1    conda-forge
nss                       3.78                 h2350873_0    conda-forge
numpy                     1.22.4           py39hc58783e_0    conda-forge
openh264                  2.1.1                h780b84a_0    conda-forge
openjpeg                  2.4.0                hb52868f_1    conda-forge
openssl                   1.1.1o               h166bdaf_0    conda-forge
orc                       1.7.4                h6c59b99_1    conda-forge
orderedmultidict          1.0.1                      py_0    conda-forge
osmnx                     1.2.0              pyhd8ed1ab_0    conda-forge
owslib                    0.25.0             pyhd8ed1ab_0    conda-forge
packaging                 21.3               pyhd8ed1ab_0    conda-forge
palettable                3.3.0                      py_0    conda-forge
pandas                    1.4.2            py39h1832856_2    conda-forge
pandoc                    2.18                 ha770c72_0    conda-forge
pandocfilters             1.5.0              pyhd8ed1ab_0    conda-forge
parquet-cpp               1.5.1                         2    conda-forge
parso                     0.8.3              pyhd8ed1ab_0    conda-forge
pcre                      8.45                 h9c3ff4c_0    conda-forge
pexpect                   4.8.0              pyh9f0ad1d_2    conda-forge
pickleshare               0.7.5                   py_1003    conda-forge
pillow                    9.1.1            py39hae2aec6_1    conda-forge
pip                       21.2.4           py39h06a4308_0
pixman                    0.40.0               h36c2ea0_0    conda-forge
plotly                    5.8.2              pyhd8ed1ab_0    conda-forge
poppler                   22.04.0              h1434ded_1    conda-forge
poppler-data              0.4.11               hd8ed1ab_0    conda-forge
postgresql                14.2                 h2510834_0    conda-forge
posthog                   1.4.8              pyhd8ed1ab_0    conda-forge
proj                      9.0.0                h93bde94_1    conda-forge
prometheus_client         0.14.1             pyhd8ed1ab_0    conda-forge
prompt-toolkit            3.0.29             pyha770c72_0    conda-forge
protobuf                  3.20.1           py39h5a03fae_0    conda-forge
pscript                   0.7.5              pyhd3deb0d_0    conda-forge
psutil                    5.9.1            py39hb9d737c_0    conda-forge
pthread-stubs             0.4               h36c2ea0_1001    conda-forge
ptyprocess                0.7.0              pyhd3deb0d_0    conda-forge
pulseaudio                14.0                 hbc9ff1d_7    conda-forge
pure_eval                 0.2.2              pyhd8ed1ab_0    conda-forge
pyarrow                   6.0.1           py39h42d110c_19_cpu    conda-forge
pyasn1                    0.4.8                      py_0    conda-forge
pyasn1-modules            0.2.7                      py_0    conda-forge
pybind11-abi              4                    hd8ed1ab_3    conda-forge
pycosat                   0.6.3           py39hb9d737c_1010    conda-forge
pycparser                 2.21               pyhd8ed1ab_0    conda-forge
pycrs                     1.0.2                      py_0    conda-forge
pydantic                  1.9.1            py39hb9d737c_0    conda-forge
pydeck                    0.7.1              pyh6c4a22f_0    conda-forge
pygis                     0.2.0              pyhd8ed1ab_1    conda-forge
pygments                  2.12.0             pyhd8ed1ab_0    conda-forge
pyopenssl                 22.0.0             pyhd8ed1ab_0    conda-forge
pyparsing                 3.0.9              pyhd8ed1ab_0    conda-forge
pyproj                    3.3.1            py39hcadae2f_0    conda-forge
pyqt                      5.15.4           py39h5a03fae_0    conda-forge
pyqt5-sip                 12.9.0           py39h5a03fae_0    conda-forge
pyrsistent                0.18.1           py39hb9d737c_1    conda-forge
pyshp                     2.3.0              pyhd8ed1ab_0    conda-forge
pysocks                   1.7.1            py39hf3d152e_5    conda-forge
pystac                    1.4.0              pyhd8ed1ab_0    conda-forge
pystac-client             0.4.0              pyhd8ed1ab_0    conda-forge
python                    3.9.13          h9a8a25e_0_cpython    conda-forge
python-box                6.0.2              pyhd8ed1ab_0    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python-fastjsonschema     2.15.3             pyhd8ed1ab_0    conda-forge
python-mss                6.1.0              pyhd3deb0d_0    conda-forge
python_abi                3.9                      2_cp39    conda-forge
pytz                      2022.1             pyhd8ed1ab_0    conda-forge
pyu2f                     0.1.5              pyhd8ed1ab_0    conda-forge
pyyaml                    6.0              py39hb9d737c_4    conda-forge
pyzmq                     23.1.0           py39headdf64_0    conda-forge
qt-main                   5.15.2               hdf1cb14_3    conda-forge
rasterio                  1.2.10           py39h2e4b6e6_5    conda-forge
ratelim                   0.1.6                      py_2    conda-forge
re2                       2022.04.01           h27087fc_0    conda-forge
readline                  8.1.2                h7f8727e_1
reproc                    14.2.3               h7f98852_0    conda-forge
reproc-cpp                14.2.3               h9c3ff4c_0    conda-forge
requests                  2.28.0             pyhd8ed1ab_0    conda-forge
requests-toolbelt         0.9.1                      py_0    conda-forge
rio-cogeo                 3.2.0              pyhd8ed1ab_0    conda-forge
rioxarray                 0.11.1             pyhd8ed1ab_0    conda-forge
rsa                       4.8                pyhd8ed1ab_0    conda-forge
rtree                     1.0.0            py39hb102c33_1    conda-forge
ruamel.yaml               0.17.21          py39hb9d737c_1    conda-forge
ruamel.yaml.clib          0.2.6            py39hb9d737c_1    conda-forge
ruamel_yaml               0.15.80         py39hb9d737c_1007    conda-forge
s2n                       1.0.10               h9b69904_0    conda-forge
sankee                    0.0.7              pyhd8ed1ab_0    conda-forge
scikit-learn              1.1.1            py39h4037b75_0    conda-forge
scipy                     1.8.1            py39he49c0e8_0    conda-forge
scooby                    0.5.12             pyhd8ed1ab_0    conda-forge
send2trash                1.8.0              pyhd8ed1ab_0    conda-forge
server-thread             0.1.0              pyhd8ed1ab_0    conda-forge
setuptools                61.2.0           py39h06a4308_0
shapely                   1.8.2            py39h73b9895_1    conda-forge
simplejson                3.17.6           py39hb9d737c_1    conda-forge
sip                       6.5.1            py39he80948d_2    conda-forge
six                       1.16.0             pyh6c4a22f_0    conda-forge
snappy                    1.1.9                hbd366e4_1    conda-forge
sniffio                   1.2.0            py39hf3d152e_3    conda-forge
snuggs                    1.4.7                      py_0    conda-forge
soupsieve                 2.3.1              pyhd8ed1ab_0    conda-forge
sqlite                    3.38.5               h4ff8645_0    conda-forge
stack_data                0.3.0              pyhd8ed1ab_0    conda-forge
stringcase                1.2.0                      py_0    conda-forge
svt-av1                   0.9.1                h27087fc_0    conda-forge
tabulate                  0.8.9              pyhd8ed1ab_0    conda-forge
tenacity                  8.0.1              pyhd8ed1ab_0    conda-forge
terminado                 0.15.0           py39hf3d152e_0    conda-forge
threadpoolctl             3.1.0              pyh8a188c0_0    conda-forge
tiledb                    2.8.3                h1e4a385_1    conda-forge
tinycss2                  1.1.1              pyhd8ed1ab_0    conda-forge
tk                        8.6.12               h1ccaba5_0
toml                      0.10.2             pyhd8ed1ab_0    conda-forge
toolz                     0.11.2             pyhd8ed1ab_0    conda-forge
tornado                   6.1              py39hb9d737c_3    conda-forge
tqdm                      4.64.0             pyhd8ed1ab_0    conda-forge
traitlets                 5.2.2.post1        pyhd8ed1ab_0    conda-forge
traittypes                0.2.1              pyh9f0ad1d_2    conda-forge
typing-extensions         4.2.0                hd8ed1ab_1    conda-forge
typing_extensions         4.2.0              pyha770c72_1    conda-forge
tzcode                    2022a                h166bdaf_0    conda-forge
tzdata                    2022a                hda174b7_0
unicodedata2              14.0.0           py39hb9d737c_1    conda-forge
uritemplate               3.0.1                      py_0    conda-forge
urllib3                   1.26.9             pyhd8ed1ab_0    conda-forge
validators                0.18.2             pyhd3deb0d_0    conda-forge
vega_datasets             0.9.0              pyhd3deb0d_0    conda-forge
voila                     0.3.5              pyhd8ed1ab_0    conda-forge
wcwidth                   0.2.5              pyh9f0ad1d_2    conda-forge
webencodings              0.5.1                      py_1    conda-forge
websocket-client          1.3.2              pyhd8ed1ab_0    conda-forge
websockets                10.3             py39hb9d737c_0    conda-forge
werkzeug                  2.1.2              pyhd8ed1ab_1    conda-forge
wheel                     0.37.1             pyhd3eb1b0_0
whitebox                  2.1.2              pyhd8ed1ab_0    conda-forge
whiteboxgui               0.7.0              pyhd8ed1ab_0    conda-forge
widgetsnbextension        3.6.0            py39hf3d152e_0    conda-forge
x264                      1!161.3030           h7f98852_1    conda-forge
x265                      3.5                  h924138e_3    conda-forge
xarray                    2022.3.0           pyhd8ed1ab_0    conda-forge
xerces-c                  3.2.3                h8ce2273_4    conda-forge
xorg-fixesproto           5.0               h7f98852_1002    conda-forge
xorg-kbproto              1.0.7             h7f98852_1002    conda-forge
xorg-libice               1.0.10               h7f98852_0    conda-forge
xorg-libsm                1.2.3             hd9c2040_1000    conda-forge
xorg-libx11               1.7.2                h7f98852_0    conda-forge
xorg-libxau               1.0.9                h7f98852_0    conda-forge
xorg-libxdmcp             1.1.3                h7f98852_0    conda-forge
xorg-libxext              1.3.4                h7f98852_1    conda-forge
xorg-libxfixes            5.0.3             h7f98852_1004    conda-forge
xorg-libxrender           0.9.10            h7f98852_1003    conda-forge
xorg-renderproto          0.11.1            h7f98852_1002    conda-forge
xorg-xextproto            7.3.0             h7f98852_1002    conda-forge
xorg-xproto               7.0.31            h7f98852_1007    conda-forge
xyzservices               2022.4.0           pyhd8ed1ab_0    conda-forge
xz                        5.2.5                h7f8727e_1
yaml                      0.2.5                h7f98852_2    conda-forge
yaml-cpp                  0.7.0                h27087fc_1    conda-forge
yarl                      1.7.2            py39hb9d737c_2    conda-forge
zeromq                    4.3.4                h9c3ff4c_1    conda-forge
zipp                      3.8.0              pyhd8ed1ab_0    conda-forge
zlib                      1.2.12               h166bdaf_1    conda-forge
zstd                      1.5.2                h8a70e8d_1    conda-forge
```

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
