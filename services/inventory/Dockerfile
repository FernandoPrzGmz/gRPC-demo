# Check out https://hub.docker.com/_/node to select a new base image
FROM node:20-alpine

ENV HOST=0.0.0.0 PORT=3000

EXPOSE ${PORT}

WORKDIR /app

# Install app dependencies
COPY package.json .

RUN npm install

# region Project installation
COPY . .
RUN npm run build


RUN apk add --no-cache netcat-openbsd
RUN chmod a+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
# endregion


CMD [ "node", "." ]
