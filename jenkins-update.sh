# update the stack deployment based on docker-compose.yaml

# Build Images
sudo docker-compose build

# Push new images to registry (Docker Hub)
# We have saved the Docker Hub credentials securely in Jenkins
sudo docker login -u ${docker_user_var} -p ${docker_pass_var}
# Now logged in, push to Docker Hub
sudo docker-compose push

# note: we tried it twice and the second time it worked
# SSH into Swarm master (SwarmManagerVM) IP: 52.170.72.70
# Deploy from latest image
# << EOF to stay SSH'd in, run commands
ssh andreasandrews@52.170.72.70 << EOF
sudo docker stack deploy --compose-file /home/andreasandrews/fortune-teller/docker-compose.yaml fortune-teller
EOF
