FROM python:3

WORKDIR /home

COPY . .

RUN pip install pipenv gunicorn
RUN pipenv install --system

ENV PORT "5000"
ENV MONGO "mongo"

ENTRYPOINT ["/bin/bash"]
CMD ["run.sh"]
