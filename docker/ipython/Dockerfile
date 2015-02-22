# created based on ipython/ipython
FROM ubuntu:14.04

MAINTAINER Gavin Noronha <gavinln@hotmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Python binary dependencies, developer tools
RUN apt-get update && apt-get install -y -q \
    build-essential \
    wget \
    python \
    python-zmq \
    python-dev \
    python-pip

# needed for the Microsoft ODBC driver
RUN apt-get install -y -q \
    aptitude \
    libkrb5-3 \
    libgssapi-krb5-2

WORKDIR /msodbc

RUN mkdir -p /msodbc

# extract Microsoft ODBC driver
COPY driver_files/msodbcsql-11.0.2270.0.tar.gz /msodbc/
RUN tar xvzf /msodbc/msodbcsql-11.0.2270.0.tar.gz -C /msodbc

# setup Unix ODBC Driver Manager
WORKDIR /msodbc/msodbcsql-11.0.2270.0
COPY driver_files/unixODBC-2.3.0.tar.gz /msodbc/msodbcsql-11.0.2270.0/
COPY driver_files/ubuntu_build_dm.sh /msodbc/msodbcsql-11.0.2270.0/

RUN chmod +x ubuntu_build_dm.sh
RUN ./ubuntu_build_dm.sh --accept-warning --download-url=file://unixODBC-2.3.0.tar.gz

# install Unix ODBC driver manager
RUN cd `find /tmp -name unixODBC-2.3.0` && make install

WORKDIR /msodbc/msodbcsql-11.0.2270.0
COPY driver_files/ubuntu_install.sh /msodbc/msodbcsql-11.0.2270.0/
RUN chmod +x ubuntu_install.sh
RUN ./ubuntu_install.sh install --accept-license

RUN pip install --allow-external pyodbc --allow-unverified pyodbc pyodbc

# export library path for Microsoft ODBC driver
ENV LD_LIBRARY_PATH /usr/lib64

# link libraries required for Microsoft ODBC driver
RUN ln -s /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /usr/lib64/libcrypto.so.10 && \
    ln -s /lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib64/libssl.so.10

RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

RUN pip install "ipython[notebook]"
RUN apt-get install -y python-numpy
RUN pip install pandas
RUN apt-get install -y libfreetype6-dev \
    pkg-config
RUN pip install matplotlib
#RUN apt-get install -y python-matplotlib
RUN apt-get install -y python-scipy
RUN pip install statsmodels
RUN pip install seaborn

#WORKDIR /root

#RUN echo 'export PATH=/opt/anaconda/bin:$PATH' > /etc/profile.d/conda.sh
#RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda-3.7.0-Linux-x86_64.sh
#RUN /bin/bash Miniconda-3.7.0-Linux-x86_64.sh -b -p /opt/anaconda
#RUN rm Miniconda-3.7.0-Linux-x86_64.sh
#ENV PATH /opt/anaconda/bin:$PATH

#RUN conda install --yes -q ipython-notebook
#RUN conda install --yes -q numpy
#RUN conda install --yes -q pandas
#RUN conda install --yes -q matplotlib
#RUN conda install --yes -q scipy
#RUN conda install --yes -q seaborn

VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

ADD notebook.sh /
RUN chmod u+x /notebook.sh

# create a directory for the notebooks
RUN mkdir /notebook-dir

CMD ["/notebook.sh"]
#CMD while true; do echo 'Hit CTRL+C'; sleep 1; done
