cd resume-builder/
docker stop resume_builder_iearn
docker rm resume_builder_iearn
docker rmi resume_builder_iearn:latest
docker build -t resume_builder_iearn .
docker run -p 3001:3000 -d --name resume_builder_iearn resume_builder_iearn
