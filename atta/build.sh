
buildBase=false

while [ $# -gt 0 ]; do
  case "$1" in
  -h)
    echo 'This command is used to build docker image with superset'
    echo 'Command:  atta/build.sh [option]'
    echo ''
    echo 'option :'
    echo '  -base : default is false; build with base docker file'
    echo '  -help : echo options'
    echo '  -h : echo options'
    exit
    ;;
  -base)
    buildBase=yes
    shift
    ;;

  -help)
    echo 'This command is used to build docker image with superset'
    echo 'Command:  atta/build.sh [option]'
    echo ''
    echo 'option :'
    echo '  -base : default is false; build with base docker file'
    echo '  -help : echo options'
    echo '  -h : echo options'
    exit
    ;;
  *)
    echo ''
    break
    ;;
  esac
done


if [ $buildBase == true ];
  then
    echo "build docker image atta/base_superset"
    docker build -f atta/base/Dockerfile -t atta/base_superset .
  else
    echo "build docker image without atta/base_superset"
fi

echo "build superset frontend"

cd superset-frontend/

npm install

npm run build

rm -rf node_modules

cd ..

echo "build docker image atta/superset"

time=$(date "+%Y%m%d%H%M%S")

docker build -f atta/Dockerfile -t atta/superset:${time} .

echo "build docker image success, the image is  "
echo atta/superset:${time}
