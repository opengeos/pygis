# pygis

[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/opengeos/pygis/HEAD)
[![image](https://img.shields.io/pypi/v/pygis.svg)](https://pypi.python.org/pypi/pygis)
[![image](https://img.shields.io/conda/vn/conda-forge/pygis.svg)](https://anaconda.org/conda-forge/pygis)
[![image](https://pepy.tech/badge/pygis)](https://pepy.tech/project/pygis)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pygis.svg)](https://anaconda.org/conda-forge/pygis)
[![Conda Recipe](https://img.shields.io/badge/recipe-pygis-green.svg)](https://github.com/conda-forge/pygis-feedstock)
[![image](https://img.shields.io/badge/YouTube-Channel-red)](https://www.youtube.com/c/QiushengWu)
[![image](https://img.shields.io/twitter/follow/giswqs?style=social)](https://twitter.com/giswqs)

**A Python package for installing commonly used packages for GIS programming.**

- Free software: MIT license
- Documentation: https://pygis.gishub.org

[![](https://i.imgur.com/bKFts2R.png)](https://pygis.gishub.org)

To use pygis with Docker, you can pull the image from Docker Hub:

```bash
docker pull giswqs/pygis:latest
docker run -it -p 8888:8888 -v $(pwd):/home/jovyan/work giswqs/pygis:latest
```

To build the Docker image from scratch using the Dockerfile in the root directory, you can run:

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t giswqs/pygis:latest .
docker push giswqs/pygis:latest
```
