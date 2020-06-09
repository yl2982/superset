
cd superset-frontend/

npm run build

cd ..

time=$(date "+%Y%m%d%H%M%S")

echo atta/superset:${time}

docker build -t atta/superset:${time} .