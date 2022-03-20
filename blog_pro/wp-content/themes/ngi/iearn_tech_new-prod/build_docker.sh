sudo chmod 777 /var/run/docker.sock
cd iearn_tech_new/
#git pull
docker stop $1_iearn_tech_ui
docker rm $1_iearn_tech_ui
docker rmi $1_iearn_tech_ui:latest
docker build -t $1_iearn_tech_ui .
#docker run -d -v /opt/tomcat/latest/webapps/ROOT/image/student/:/opt/tomcat/latest/webapps/ROOT/image/student/ -v /opt/tomcat/latest/webapps/ROOT/image/employer/:/opt/tomcat/latest/webapps/ROOT/image/employer/ -v /opt/tomcat/latest/webapps/ROOT/videos/testing/:/opt/tomcat/latest/webapps/ROOT/videos/testing/ -p $2:8000 --name $1_iearn_tech_ui $1_iearn_tech_ui
docker run -d -v /opt/tomcat/latest/webapps/ROOT/:/opt/tomcat/latest/webapps/ROOT/ -p $2:8000 --name $1_iearn_tech_ui $1_iearn_tech_ui
echo "SUCCESS"