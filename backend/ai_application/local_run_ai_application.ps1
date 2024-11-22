Write-Host @"
 █████╗ ██╗     █████╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║    ██╔══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██║    ███████║██████╔╝██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██║    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║  ██║██║    ██║  ██║██║     ██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                 
Local run of AI application
"@

# Define variables
$OLLAMA_BASE_URL = "http://10.230.100.240:17030"
$ENDPOINT_PORT_NUMBER = 8000

# Check if podman or docker command is installed
$CONTAINER_CMD = $null

if (Get-Command "podman" -ErrorAction SilentlyContinue) {
    $CONTAINER_CMD = "podman"
    Write-Host "podman found"
}
elseif (Get-Command "docker" -ErrorAction SilentlyContinue) {
    $CONTAINER_CMD = "docker"
    Write-Host "docker found"
}
else {
    Write-Host "Neither podman nor docker command found. Please install one of them."
    exit 1
}

# Build container
Write-Host "Building container"
if ([string]::IsNullOrEmpty($env:CI_ENVIRONMENT_SLUG)) {
    $CONTAINER_NAME = "local/$env:USERNAME/ai-application"
}
else {
    $CONTAINER_NAME = "local/$env:USERNAME/ai-application-$env:CI_ENVIRONMENT_SLUG"
}

& $CONTAINER_CMD build -t $CONTAINER_NAME .

# Run container
Write-Host "Running container"
& $CONTAINER_CMD run -it --rm `
    -p "${ENDPOINT_PORT_NUMBER}:8000" `
    -e "OLLAMA_BASE_URL=${OLLAMA_BASE_URL}" `
    $CONTAINER_NAME
