cd /home/ubuntu/Github/$1/intearn_v1/intearn_v1
git pull
docker stop $1_intearn_api
docker rm $1_intearn_api
docker rmi $1_intearn_api:latest
docker build -t $1_intearn_api .
docker run -d -p $2:8889 --name $1_intearn_api $1_intearn_api
