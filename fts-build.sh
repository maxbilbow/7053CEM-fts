#!/usr/bin/env bash

## Build React App
cd fts-web || exit
npm install
npm run build

## Copy web assets
cd ..
mkdir -p ./fts-server/build/static
cp -r ./fts-server/templates/* ./fts-server/build/ && cp -r ./fts-server/static/* ./fts-server/build/static/
cp -r ./fts-web/build/* ./fts-server/build/

