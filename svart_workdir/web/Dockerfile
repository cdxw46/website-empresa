FROM node:22-slim@sha256:8833056542b4e17c27154beeabbc27c3e14ddfe3fb9183f43b3adf7eb0462923

WORKDIR /app

COPY package.json .
RUN npm i

COPY index.js .
COPY public public

USER node

EXPOSE 1337

CMD [ "node", "index.js" ]
