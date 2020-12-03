FROM python:3.7.3-stretch

# RUN pip install --no-cache pyfaidx pysam Pillow pytabix bamsnap

RUN pip install --no-cache pyfaidx
RUN pip install --no-cache pysam
RUN pip install --no-cache Pillow
RUN pip install --no-cache pytabix
RUN pip install --no-cache bamsnap

# RUN mkdir -p /src
# WORKDIR /src

# COPY requirements.txt /src/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /src
# CMD [ "python", "./your-daemon-or-script.py" ]