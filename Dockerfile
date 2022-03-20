FROM python:3.8-buster

# Install postgres 12
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
RUN apt-get update
RUN apt-get -y install postgresql-12
RUN apt autoremove && apt autoclean

RUN pip install pipenv

RUN mkdir /src
WORKDIR /src
COPY ["Pipfile", "Pipfile.lock", "/src/"]
RUN pipenv install --system --dev

COPY . .

CMD ["/src/docker-entrypoint"]