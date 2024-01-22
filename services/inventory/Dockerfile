FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
ARG PROJECT_DIR=/app

# Create the work directory
RUN mkdir -p ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

# Copy project source
COPY ./ ${PROJECT_DIR}

EXPOSE 3000
CMD ["tail", "-f", "/dev/null"]
