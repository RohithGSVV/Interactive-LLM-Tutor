# Accounting Tutor

### Links:
- [Project Management (Jira)](https://gsu-team-qnddq56g.atlassian.net/jira/your-work)
- [Document Repository (Teams)](https://teams.microsoft.com/l/channel/19%3A3BHfwfHpSPCe26OJGHfc9ZOT_YkbBDbO3q-HFNWby6M1%40thread.tacv2/General?groupId=3a37e321-a8b3-4447-b218-043acf44af08&tenantId=515ad73d-8d5e-4169-895c-9789dc742a70)
- [Wiki (GitLab)](https://git.insight.gsu.edu:8000/genai_research/accounting-tutor/-/wikis/home)


## GPU-Server
The GPU-Server hosts Ollama instances (and vector database) with nginx as load balancer. Access is controlled through a private API key.

## Backend-Server
The Backend-Server hosts the web application, databases and authentication server.

## User Account
User: 
    `genai_tutor:x:3017:3017:Project> GenAI Tutor <pmolnar@gsu.edu>:/home1/genai_tutor:/bin/sh`

Group:
    `genai_tutor:x:3017:`


```
sudo groupadd -g 3017 genai_tutor
sudo useradd -u 3017 -g 3017 -b /home1 -c "Project> GenAI Tutor <pmolnar@gsu.edu>" genai_tutor
sudo mkdir /home1/genai_tutor
sudo chown genai_tutor.genai_tutor /home1/genai_tutor/
sudo chmod 750 /home1/genai_tutor/
sudo mkdir -p /staging/users/genai_tutor
```

On GPU server run
1. Add `genai_tutor` to `gpu_podman_users` group in `/etc/group`
2. Run this script to create staging directory and update SUBUID and SUBGID ranges ```sudo /root/update_gpu_podman_users.pl```

On Backend server create staging directory
```
sudo chown genai_tutor.genai_tutor /staging/users/genai_tutor/
sudo chmod 750 /staging/users/genai_tutor/ 
```

## CI/CD Pipeline

Manual CI/CD pipeline for `develop`, `uat`, and `main` branches only. There are two GitLab runners for this project: one on the GPU server, one on the Backend server. The GitLab runners are started as `genai_tutor`.

Launch gitlab-runners on host `gpu-01` and `compute-05`. The GPU runner has the tag `gpu`, the other node has the tag `compute`

### Runners
- [gentai_tutor@gpu-01](https://git.insight.gsu.edu:8000/genai_research/accounting-tutor/-/runners/10)
- [genai_tutor@compute-05](https://git.insight.gsu.edu:8000/genai_research/accounting-tutor/-/runners/11)