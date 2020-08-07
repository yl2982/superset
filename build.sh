
cd superset-frontend/

npm install

npm run build

cd ..

time=$(date "+%Y%m%d%H%M%S")

echo atta/superset:${time}

docker build -f atta/Dockerfile -t atta/superset:${time} .