FROM python:3.9-slim-buster AS build-stage
WORKDIR /project
COPY . .
RUN pip install -r requirements.txt
#RUN  coverage run --source=test/ -m pytest
#RUN  coverage xml

#Sonar scan
#FROM  sonarsource/sonar-scanner-cli AS sonar-stage
#WORKDIR /project
#COPY --from=build-stage /project /project
#ARG SONARQUBE_TOKEN
#ARG SONARQUBE_URL
#ARG SONARQUBE_ENV
#RUN if [ $SONARQUBE_ENV = "prod" ] ; then sonar-scanner -Dsonar.host.url=$SONARQUBE_URL -Dsonar.login=$SONARQUBE_TOKEN ; else echo "$SONARQUBE_ENV no envia a sonar"; fi

FROM build-stage
WORKDIR /project
EXPOSE 8080
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]

