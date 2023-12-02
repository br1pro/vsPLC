FROM python:3.10.13-slim-bullseye

LABEL maintainer="br1pro" \
      author="br1pro" \
      dockerfile-author="mguyard"

WORKDIR /app

COPY requirements.txt requirements.txt
COPY run.py /app/
COPY modbus_setter.py /app/

RUN pip install -r requirements.txt

CMD ["/bin/bash"]