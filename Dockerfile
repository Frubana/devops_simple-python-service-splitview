FROM python:3.8-slim-buster
RUN pip3 install Flask
COPY app.py app.py
EXPOSE 8080
ARG SONAR_TOKEN
ARG SONAR_URL
RUN echo "${SONAR_TOKEN}  ${SONAR_URL}"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]


