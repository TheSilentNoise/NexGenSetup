cd Github/Compiler/
cd /home/ubuntu/Github/$1/iearn_tech_new
docker stop compiler_iearn
docker rm compiler_iearn
docker rmi compiler_iearn:latest
docker build -t compiler_iearn .
docker run -p $2:80 -d --name compiler_iearn compiler_iearn
