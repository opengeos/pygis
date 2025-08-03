# ------------------------------
# Base image from Jupyter stack
# ------------------------------
FROM quay.io/jupyter/base-notebook:latest

# ------------------------------
# 1. Switch to root to install system packages
# ------------------------------
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    bash \
    bash-completion \
    git \
    unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ------------------------------
# 2. Install conda packages into base env
# ------------------------------
RUN mamba install -n base -c conda-forge -y \
    gdal \
    pygis \
    rasterio \
    rioxarray \
    && mamba clean --all --yes \
    && fix-permissions $CONDA_DIR

# RUN pip install -U --find-links https://girder.github.io/large_image_wheels GDAL && \
#     ln -s $CONDA_DIR/share/bash-completion/completions/gdal /etc/bash_completion.d/gdal && \
#     echo 'source /etc/bash_completion' >> /etc/bash.bashrc
# ------------------------------
# 2b. Create missing sqlite symlinks (after files exist)
# ------------------------------
RUN ln -s $CONDA_PREFIX/lib/libsqlite3.so.3.50.0 $CONDA_PREFIX/lib/libsqlite3.so \
    && ln -s $CONDA_PREFIX/lib/libsqlite3.so.3.50.0 $CONDA_PREFIX/lib/libsqlite3.so.0 \
    && sed -i 's/"display_name": ".*"/"display_name": "Python 3"/' $CONDA_DIR/share/jupyter/kernels/python3/kernel.json


# ------------------------------
# 3. Set pygis environment variables
# ------------------------------
ENV PROJ_LIB=$CONDA_DIR/share/proj \
    GDAL_DATA=$CONDA_DIR/share/gdal \
    LOCALTILESERVER_CLIENT_PREFIX='proxy/{port}'


# ------------------------------
# 5. Install pygis from source
# ------------------------------
# Prevent version resolution errors in CI

RUN python -m bash_kernel.install && \
    rm -rf ./build ./dist *.egg-info && \
    mkdir -p /home/jovyan/work && \
    fix-permissions /home/jovyan

# ------------------------------
# 6. Fix permissions and switch back to default user
# ------------------------------
# RUN chown -R $NB_UID:$NB_GID $CONDA_DIR && \
#     chmod -R ug+rwX $CONDA_DIR


# ------------------------------
# 6. Switch back to default user
# ------------------------------
USER $NB_UID
WORKDIR /home/jovyan

# ------------------------------
# Usage:
# docker build -t giswqs/pygis:latest .
# docker buildx build --platform linux/amd64,linux/arm64 -t giswqs/pygis:latest --push .    
# docker pull giswqs/pygis:latest
# docker run -it -p 8888:8888 -v $(pwd):/home/jovyan/work giswqs/pygis:latest
# ------------------------------
