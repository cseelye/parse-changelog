FROM ghcr.io/cseelye/ubuntu-base
RUN apt-get update && apt-get install -y \
        git \
        make \
        python3-pip
RUN pip install --upgrade pip && \
    pip install \
        bump2version \
        pylint
        setuptools \
        twine \
        wheel
