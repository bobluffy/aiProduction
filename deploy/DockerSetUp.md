#1. Registry
##1.1 Server side
1.docker pull registry (download registry image)<br/>
2.docker run -d -p 5000:5000 -v  /etc/images/registry:/var/lib/registry registry (launch registry image)

##1.2 Client side
1.docker tag busybox:latest server_ip:server_port/busybox:test1.0  (tag the server image to be served, busybox is an example here )

2.add *"insecure-registries":["server_ip:server_port"]* into */etc/docker/daemon.json* (add the ip:port of the server registry in che client config)
edit */usr/lib/systemd/system/docker.service*，and put '--insecure-registry XXXX:5000' after 'ExecStart=/usr/bin/dockerd', then restart the docker service
*systemctl daemon-reload &&systemctl restart docker*

3.docker push XXXX:5000/ai_server:v1.0 (push the tagged image into the registry for servering)

4.put *http://XXXX:5000/v2/_catalog* in to chrome (check if the pushed image is servered in the server's registry)

##1.3 Examine
docker pull XXXX:5000/ai_server:v1.0 (Now, you can pull the new docker image every pc connecting in the same network environment)

#2. Customed docker image
##2.1 make docker image(make customed docker image via Dockerfile)
docker build -f Dockerfile -t smart_tagger:v0.1 .

##2.2 launch the docker container
docker run -v /home/ftp1/smart_tagger:/data/smart_tagger/logs -p XXXX:6661:6661 -dti smart_tagger:v1.0
docker run -v /home/yuan/workplace/docker_env/smart_tagger/logs:/data/smart_tagger/logs -v /home/yuan/workplace/docker_env/smart_tagger/confs:/data/smart_tagger/confs -v /home/yuan/workplace/docker_env/smart_tagger/models:/data/smart_tagger/models -p XXXX:6661:6661 -dti smart_tagger:v0.1

##2.3 run the web service
 docker exec -it 0b3746770b75 /bin/sh
 sh ./start.sh
 
 
##2.4 save docker as a local file
docker save smart_tagger:v0.1 -o ./smart_taggerV0.1.tar

#3. Clean the docker files
1. docker stop $(docker ps -aq)        stop all containers
2. docker rm $(docker ps -aq)          delete all docker containers
3. docker rmi $(docker images -q)      delete all docker images
##alternative:
1. docker image prune --force --all /docker image prune -f -a       delete all unused docker images
2. docker container prune -f                                        delete all stop containers



