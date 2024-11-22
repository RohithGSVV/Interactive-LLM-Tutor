sudo mkdir -p /home1
sudo groupadd -g 3017 genai_tutor
sudo useradd -u 3017 -g 3017 -b /home1 -m -s /bin/bash -c "Project> GenAI Tutor <pmolnar@gsu.edu>" genai_tutor
sudo mkdir -p /tau/containers/storage/genai_tutor 
sudo chown -R genai_tutor.genai_tutor /tau/containers/storage/genai_tutor  
sudo chmod -R o-rwx /tau/containers/storage/genai_tutor

sudo su - genai_tutor
gitlab-runner status
gitlab-runner list
