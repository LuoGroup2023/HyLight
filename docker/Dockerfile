FROM continuumio/miniconda3
SHELL ["/bin/bash", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        less \
        libboost-all-dev \
        make \
        g++ \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /tools
WORKDIR /tools
COPY environment.yaml .
RUN . /opt/conda/bin/activate && \
    conda env create -n hylight -f environment.yaml && \
    conda clean -ya
RUN git clone https://github.com/kangxiongbin/HyLight.git && \
    cd /tools/HyLight/tools/HaploConduct && \
    make clean && \
    make &&\
    cd /tools/HyLight/tools/miniasm && \
    make clean && \
    make    
ENV PATH=/opt/conda/envs/hylight/bin/:$PATH
CMD ["conda", "run", "-n", "hylight"]
