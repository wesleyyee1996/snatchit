# [Choice] Node.js version (use -bullseye variants on local arm64/Apple Silicon): 18, 16, 14, 18-bullseye, 16-bullseye, 14-bullseye, 18-buster, 16-buster, 14-buster
FROM node:16.10.0

WORKDIR /app
COPY package.json .
RUN npm config set legacy-peer-deps true &&\
  npm install
RUN npm install styled-components
RUN npm install --save read-yaml
COPY . .
EXPOSE 3000

CMD ["npm", "start"]