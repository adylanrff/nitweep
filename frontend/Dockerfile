FROM node:14.10

WORKDIR /app

COPY package*.json /app

RUN npm install

COPY . .

RUN npm run generate