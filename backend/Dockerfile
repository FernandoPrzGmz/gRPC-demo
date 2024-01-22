FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VERSION=3.10
ARG PROJECT_DIR=/app

# Django superadmin credentials
ENV DJANGO_SUPERUSER_EMAIL admin@example.com
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin123

EXPOSE 8000


RUN apt update

# region Install pyenv
#Install some system dependencies for the python version management (pyenv)
# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
RUN apt install -y \
        git \
        nano \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev

# Install pyenv
RUN curl https://pyenv.run | bash

# env vars for pyenv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
# endregion



# Install python 
RUN set -ex \
    && pyenv update \
    && pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && pyenv rehash



# region Install poetry
RUN curl -sSL https://install.python-poetry.org | python -
# env vars for poetry
ENV POETRY_ROOT /root/.local
ENV PATH $POETRY_ROOT/bin:$PATH
# Configure Poetry to disable automatic virtual environment creation
RUN poetry config virtualenvs.create false
# endregion



# region Install project's requirements
RUN apt install -y \
    libmysqlclient-dev

WORKDIR ${PROJECT_DIR}
COPY pyproject.toml pyproject.toml
RUN poetry install
# endregion



# region Project installation
# Copy project source
COPY . .

RUN apt install -y \
    netcat

RUN chmod a+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
# endregion

#CMD ["tail", "-f", "/dev/null"]
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
