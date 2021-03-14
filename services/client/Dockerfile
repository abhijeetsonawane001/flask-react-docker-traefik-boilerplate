FROM node:12.2.0-alpine

WORKDIR /usr/src/app

COPY package*.json /usr/src/app/

RUN npm install --silent

RUN npm install react-scripts@4.0.3 -g --silent

COPY . /usr/src/app

EXPOSE 80