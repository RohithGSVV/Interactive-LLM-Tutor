#!/bin/bash
# set -x
source .env

# ALPINE_CONTAINER_IAMGE=alpine:latest
# ALPINE_HOST_NAME=alpine
# BASTION_PORT=7778
# CI_API_GRAPHQL_URL=https://git.insight.gsu.edu:8000/api/graphql
# CI_API_V4_URL=https://git.insight.gsu.edu:8000/api/v4
# CI_BUILDS_DIR=/home1/genai_tutor/builds
# CI_COMMIT_AUTHOR=Péter Molnár <pmolnar@gsu.edu>
# CI_COMMIT_BEFORE_SHA=f1dba5ac6fd69896a8350671a6d642a920b617ef
# CI_COMMIT_BRANCH=develop
# CI_COMMIT_DESCRIPTION=
# CI_COMMIT_MESSAGE=fix loop with while?
# CI_COMMIT_REF_NAME=develop
# CI_COMMIT_REF_PROTECTED=false
# CI_COMMIT_REF_SLUG=develop
# CI_COMMIT_SHA=00227bcc6ac150f4114c6ceceeea33eb3b5b9e9a
# CI_COMMIT_SHORT_SHA=00227bcc
# CI_COMMIT_TIMESTAMP=2024-09-27T12:09:59-04:00
# CI_COMMIT_TITLE=fix loop with while?
# CI_CONCURRENT_ID=0
# CI_CONCURRENT_PROJECT_ID=0
# CI_CONFIG_PATH=.gitlab-ci.yml
# CI_DEFAULT_BRANCH=develop
# CI_DEPENDENCY_PROXY_DIRECT_GROUP_IMAGE_PREFIX=git.insight.gsu.edu:8000/genai_research/dependency_proxy/containers
# CI_DEPENDENCY_PROXY_GROUP_IMAGE_PREFIX=git.insight.gsu.edu:8000/genai_research/dependency_proxy/containers
# CI_DEPENDENCY_PROXY_PASSWORD=[MASKED]
# CI_DEPENDENCY_PROXY_SERVER=git.insight.gsu.edu:8000
# CI_DEPENDENCY_PROXY_USER=gitlab-ci-token
# CI_ENVIRONMENT_ACTION=start
# CI_ENVIRONMENT_NAME=development
# CI_ENVIRONMENT_SLUG=development
# CI_ENVIRONMENT_TIER=development
# CI_JOB_ID=980
# CI_JOB_JWT=[MASKED]
# CI_JOB_JWT_V1=[MASKED]
# CI_JOB_JWT_V2=[MASKED]
# CI_JOB_NAME=deploy-gpu-dev
# CI_JOB_NAME_SLUG=deploy-gpu-dev
# CI_JOB_STAGE=deploy
# CI_JOB_STARTED_AT=2024-09-27T16:10:10Z
# CI_JOB_STATUS=running
# CI_JOB_TIMEOUT=3600
# CI_JOB_TOKEN=[MASKED]
# CI_JOB_URL=https://git.insight.gsu.edu:8000/genai_research/accounting-tutor/-/jobs/980
# CI_NODE_TOTAL=1
# CI_PAGES_DOMAIN=example.com
# CI_PAGES_URL=http://genai_research.example.com/accounting-tutor
# CI_PIPELINE_CREATED_AT=2024-09-27T16:10:03Z
# CI_PIPELINE_ID=270
# CI_PIPELINE_IID=59
# CI_PIPELINE_NAME=
# CI_PIPELINE_SOURCE=push
# CI_PIPELINE_URL=https://git.insight.gsu.edu:8000/genai_research/accounting-tutor/-/pipelines/270
# CI_PROJECT_CLASSIFICATION_LABEL=
# CI_PROJECT_DESCRIPTION=
# CI_PROJECT_DIR=/home1/genai_tutor/builds/FDZhygSgi/0/genai_research/accounting-tutor
# CI_PROJECT_ID=15
# CI_PROJECT_NAME=accounting-tutor
# CI_PROJECT_NAMESPACE=genai_research
# CI_PROJECT_NAMESPACE_ID=13
# CI_PROJECT_PATH=genai_research/accounting-tutor
# CI_PROJECT_PATH_SLUG=genai-research-accounting-tutor
# CI_PROJECT_REPOSITORY_LANGUAGES=shell,html
# CI_PROJECT_ROOT_NAMESPACE=genai_research
# CI_PROJECT_TITLE=Accounting Tutor
# CI_PROJECT_URL=https://git.insight.gsu.edu:8000/genai_research/accounting-tutor
# CI_PROJECT_VISIBILITY=private
# CI_REGISTRY_PASSWORD=[MASKED]
# CI_REGISTRY_USER=gitlab-ci-token
# CI_REPOSITORY_URL=https://gitlab-ci-token:[MASKED]@git.insight.gsu.edu:8000/genai_research/accounting-tutor.git
# CI_RUNNER_DESCRIPTION=gentai_tutor@gpu-01
# CI_RUNNER_EXECUTABLE_ARCH=linux/amd64
# CI_RUNNER_ID=10
# CI_RUNNER_REVISION=66269445
# CI_RUNNER_SHORT_TOKEN=FDZhygSgi
# CI_RUNNER_TAGS=["gpu"]
# CI_RUNNER_VERSION=17.3.1
# CI_SERVER_HOST=git.insight.gsu.edu
# CI_SERVER_NAME=GitLab
# CI_SERVER_PORT=8000
# CI_SERVER_PROTOCOL=https
# CI_SERVER_REVISION=cc62007c12d
# CI_SERVER_SHELL_SSH_HOST=git.insight.gsu.edu
# CI_SERVER_SHELL_SSH_PORT=22
# CI_SERVER_TLS_CA_FILE=/home1/genai_tutor/builds/FDZhygSgi/0/genai_research/accounting-tutor.tmp/CI_SERVER_TLS_CA_FILE
# CI_SERVER_URL=https://git.insight.gsu.edu:8000
# CI_SERVER_VERSION=16.9.1-ee
# CI_SERVER_VERSION_MAJOR=16
# CI_SERVER_VERSION_MINOR=9
# CI_SERVER_VERSION_PATCH=1
# CI_SERVER=yes
# CI_SHARED_ENVIRONMENT=true
# CI_TEMPLATE_REGISTRY_HOST=registry.gitlab.com
# CI=true
# CONFIG_FILE=/home1/genai_tutor/.gitlab-runner/config.toml
# FF_CLEAN_UP_FAILED_CACHE_EXTRACT=false
# FF_DISABLE_AUTOMATIC_TOKEN_ROTATION=false
# FF_DISABLE_POWERSHELL_STDIN=false
# FF_DISABLE_UMASK_FOR_DOCKER_EXECUTOR=false
# FF_DISABLE_UMASK_FOR_KUBERNETES_EXECUTOR=false
# FF_ENABLE_BASH_EXIT_CODE_CHECK=false
# FF_ENABLE_JOB_CLEANUP=false
# FF_KUBERNETES_HONOR_ENTRYPOINT=false
# FF_LOG_IMAGES_CONFIGURED_FOR_JOB=false
# FF_NETWORK_PER_BUILD=false
# FF_POSIXLY_CORRECT_ESCAPES=false
# FF_PRINT_POD_EVENTS=false
# FF_RESOLVE_FULL_TLS_CHAIN=false
# FF_RETRIEVE_POD_WARNING_EVENTS=true
# FF_SCRIPT_SECTIONS=false
# FF_SECRET_RESOLVING_FAILS_IF_MISSING=true
# FF_SET_PERMISSIONS_BEFORE_CLEANUP=true
# FF_SKIP_NOOP_BUILD_STAGES=true
# FF_TEST_FEATURE=false
# FF_TIMESTAMPS=false
# FF_USE_ADVANCED_POD_SPEC_CONFIGURATION=false
# FF_USE_DIRECT_DOWNLOAD=true
# FF_USE_DOCKER_AUTOSCALER_DIAL_STDIO=true
# FF_USE_DUMB_INIT_WITH_KUBERNETES_EXECUTOR=false
# FF_USE_DYNAMIC_TRACE_FORCE_SEND_INTERVAL=false
# FF_USE_FASTZIP=false
# FF_USE_GIT_BUNDLE_URIS=true
# FF_USE_INIT_WITH_DOCKER_EXECUTOR=false
# FF_USE_LEGACY_GCS_CACHE_ADAPTER=false
# FF_USE_LEGACY_KUBERNETES_EXECUTION_STRATEGY=false
# FF_USE_NEW_BASH_EVAL_STRATEGY=false
# FF_USE_POD_ACTIVE_DEADLINE_SECONDS=true
# FF_USE_POWERSHELL_PATH_RESOLVER=false
# FF_USE_WINDOWS_JOB_OBJECT=false
# FF_USE_WINDOWS_LEGACY_PROCESS_STRATEGY=false
# GENAI_TUTOR_SECRET=arc/genai-tutor
# GITLAB_CI=true
# GITLAB_ENV=/home1/genai_tutor/builds/FDZhygSgi/0/genai_research/accounting-tutor.tmp/gitlab_runner_env
# GITLAB_FEATURES=
# GITLAB_USER_EMAIL=pmolnar@gsu.edu
# GITLAB_USER_ID=1
# GITLAB_USER_LOGIN=pmolnar
# GITLAB_USER_NAME=Peter Molnar
# GPUS=0,1,2,3
# HOME=/home1/genai_tutor
# LANG=en_US.UTF-8
# LOGNAME=genai_tutor
# MAIL=/var/mail/genai_tutor
# NGINX_CONTAINER_IMAGE=nginx:latest
# NGINX_HOST_NAME=nginx
# NGINX_OLLAMA_BACKEND_LIST=server ollama1;
# NUMBER_OLLAMA_INSTANCES=2
# OLDPWD=/home1/genai_tutor/builds/FDZhygSgi/0/genai_research/accounting-tutor
# OLLAMA_API_KEY=Os/42BUfqLaEDC6Ye22C2fiE/LVKSMvpqZzHDeA8nd4=
# OLLAMA_CONTAINER_IMAGE=ollama/ollama:latest
# OLLAMA_HOST_NAME=ollama
# OLLAMA_STAGING_DIR=/staging/users/genai_tutor/ollama
# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# POSTGRES_APP_PASSWORD=mavens49SUMMER37routed
# POSTGRES_APP_USER=genai_tutor
# POSTGRES_DB=genai_tutor
# POSTGRES_PASSWORD=poisha67EPACTS13tanist
# POSTGRES_USER=postgres
# PROXY_PORT=7779
# PWD=/staging/users/genai_tutor/v1/development
# RUNNER_TEMP_PROJECT_DIR=/home1/genai_tutor/builds/FDZhygSgi/0/genai_research/accounting-tutor.tmp

function container_command() {
    if [ -n "`command -v docker`" ]; then
        echo "docker"
        return 0 
    elif [ -n "`command -v podman`" ]; then
        echo "podman"
        return 0 
    else
        echo "Neither 'docker' nor 'podman' found." >> /dev/stderr
        echo "echo"
        return -1
    fi
}

COMMAND=$(container_command)


function ollama_start() { # SERVER_NUM, GPUS, OLLAMA_STAGING_DIR, OLLAMA_HOST_NAME, PRIVATE_NETWORK_NAME, OLLAMA_PORT, OLLAMA_CONTAINER_IMAGE
    SERVER_NUM=$1
    GPUS=$2
    OLLAMA_STAGING_DIR=$3
    OLLAMA_DIR="${OLLAMA_STAGING_DIR}/${SERVER_NUM}"
    OLLAMA_HOST_NAME=$4
    PRIVATE_NETWORK_NAME=$5
    OLLAMA_PORT=$6
    OLLAMA_CONTAINER_IMAGE=$7

    my_port=$(($OLLAMA_PORT + $SERVER_NUM - 1))
    my_name="${OLLAMA_HOST_NAME}_${SERVER_NUM}"


    if [ "${GPUS}" == "none" ]; then
        echo "Using CPU only"
        DEVICE=""
    else
        if [ "${GPUS}" == "all" ]; then
            GPUS=`nvidia-smi --query-gpu=index --format=csv,noheader | paste -sd ","`
        fi
        echo "Using GPU(s): ${GPUS}"
        DEVICE=`echo "${GPUS}" | tr ',' '\n' | while read N; do echo -n " --device nvidia.com/gpu=$N "; done`
        DEVICE="${DEVICE} --security-opt=label=disable"
    fi
    mkdir -p $OLLAMA_DIR
    
    export OLLAMA_HOST=0.0.0.0

    # ${COMMAND} run -d \
    #     ${DEVICE} \
    #     --network "${PRIVATE_NETWORK_NAME}" \
    #     --name "${CONTAINER_NAME}" \
    #     -e OLLAMA_HOST \
    #     -v $PWD:/workspace/host \
    #     -v ${OLLAMA_DIR}:/root/.ollama \
    #     --restart always \
    #      "${OLLAMA_CONTAINER_IMAGE}"
    ${COMMAND} run -d \
        ${DEVICE} \
        --name "${my_name}" \
        --hostname "${my_name}" \
        -p ${my_port}:11434 \
        -e OLLAMA_HOST \
        -v $PWD:/workspace/host \
        -v ${OLLAMA_DIR}:/root/.ollama \
        --restart always \
            "${OLLAMA_CONTAINER_IMAGE}"

}

echo "Verifying Environment"
echo '==================================================================================='
printenv
echo '==================================================================================='

ACTION=$1

echo "ACTION: $ACTION"



case $ACTION in
    pull)
        echo "Pulling containers"
        $COMMAND pull ${OLLAMA_CONTAINER_IMAGE}
        $COMMAND pull ${NGINX_CONTAINER_IMAGE}
        $COMMAND pull ${AlPINE_CONTAINER_IAMGE}
        ;;

    start)
        ## Create network
        # $COMMAND network create ${PRIVATE_NETWORK_NAME}

        ## Start Ollama servers
        seq 1 $NUMBER_OLLAMA_INSTANCES | while read N
        do
            echo "Starting Ollama server #${N}"
            # SERVER_NUM, GPUS, OLLAMA_STAGING_DIR, OLLAMA_HOST_NAME, PRIVATE_NETWORK_NAME, OLLAMA_CONTAINER_IMAGE
            # SERVER_NUM=$1
            ollama_start $N $GPUS \
                $OLLAMA_STAGING_DIR \
                $OLLAMA_HOST_NAME \
                $PRIVATE_NETWORK_NAME \
                $OLLAMA_PORT \
                $OLLAMA_CONTAINER_IMAGE
            echo "Ollama server #${N} started"
        done

        # Update Nginx configuration
        envsubst < ./nginx.conf.template > ./nginx.conf
        # Start Nginx container
        echo "Starting Nginx container"
        # $COMMAND run -d --name $NGINX_HOST_NAME \
        # --network ${PRIVATE_NETWORK_NAME},podman \
        # --name $NGINX_HOST_NAME \
        # -p $PROXY_PORT:80 \
        # -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
        # $NGINX_CONTAINER_IMAGE
        # $COMMAND run -d --name $NGINX_HOST_NAME \
        # --name $NGINX_HOST_NAME \
        # -p $PROXY_PORT:80 \
        # -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
        # $NGINX_CONTAINER_IMAGE

        # # Start Alpine Linux container
        # podman run -d --name $ALPINE_HOST_NAME \
        # --network ${PRIVATE_NETWORK_NAME},podman \
        # --name $ALPINE_HOST_NAME \
        # -p $BASTION_PORT:22 \
        # $ALPINE_CONTAINER_IAMGE sleep infinity
        # Start Alpine Linux container
        # podman run -d --name $ALPINE_HOST_NAME \
        # --name $ALPINE_HOST_NAME \
        # -p $BASTION_PORT:22 \
        # $ALPINE_CONTAINER_IAMGE sleep infinity
        ;;

    stop)
        echo "Stopping containers"
        seq 1 $NUMBER_OLLAMA_INSTANCES | while read N
        do
            CONTAINER_NAME="${OLLAMA_HOST_NAME}${N}"
            echo "Stopping $CONTAINER_NAME"
            $COMMAND stop -i $CONTAINER_NAME
            $COMMAND rm -i $CONTAINER_NAME
        done
        $COMMAND stop -i $NGINX_HOST_NAME
        $COMMAND rm -i $NGINX_HOST_NAME
        $COMMAND stop -i $ALPINE_HOST_NAME
        $COMMAND rm -i $ALPINE_HOST_NAME
        $COMMAND network rm -f ${PRIVATE_NETWORK_NAME}
        ;;

    status)
        echo "Status of containers"
        $COMMAND ps

esac