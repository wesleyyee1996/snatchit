# [Choice] Node.js version (use -bullseye variants on local arm64/Apple Silicon): 18, 16, 14, 18-bullseye, 16-bullseye, 14-bullseye, 18-buster, 16-buster, 14-buster
FROM node:15.13-alpine

WORKDIR /app
COPY src/react_app/package.json .
RUN npm install
COPY src .
RUN apk update && apk add py3-pip 
RUN pip3 install flask && \
  pip3 install flask-restful && \
  pip3 install flask-cors
EXPOSE 3000
EXPOSE 5000

CMD ["npm", "start","--prefix","react_app"]