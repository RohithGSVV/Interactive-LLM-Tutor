# Locally Run React Development Environment

## Overview

This is a locally runnable interactive LLM (Large Language Model) tutor application. The app is based on React and uses Docker (or Podman) to containerize the environment, making it easy to install, run, and develop. This guide will provide instructions on setting up the project, building the container, and running the React application in development mode.

## Prerequisites

Make sure that either Docker or Podman is installed on your system, as the script will look for one of these commands to execute the application container.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Podman Installation Guide](https://podman.io/getting-started/installation)

## Usage

This repository contains a script that will allow you to manage the lifecycle of your React application container. The following options are available:

### Commands

- **install**: Build the container image for the application.
- **run**: Run the container interactively for development purposes.
- **create**: Create a new React application based on the name provided by the script.
- **build**: Build the static assets for the React application.
- **start**: Start the React application in development mode.

## Instructions

First, clone the repository and navigate to the directory containing the script.

### Running the Script

```bash
./<script-name>.sh/.ps1 [command]
```

Replace `<script-name>` with the name of the script provided in the repository.

### Example Commands

#### 1. Build the Container Image

```bash
./<script-name>.sh/.ps1 install
```
This command builds the container image for the application.

#### 2. Run the Application in Development Mode

```bash
./<script-name>.sh/.ps1 run
```
This command runs the container interactively and mounts the `src` folder for local development.

#### 3. Create a New React Application

```bash
./<script-name>.sh/.ps1 create
```
This command will create a new React application. Make sure to run this command before attempting to build or start.

#### 4. Build the React Application

```bash
./<script-name>.sh/.ps1 build
```
This command will build the React application, creating static assets suitable for production.

#### 5. Start the Application in Development Mode

```bash
./<script-name>.sh/.ps1 start
```
This command will start the container and run the React application in development mode.

### Default Variables and Environment Settings

- The container name is generated using your username and the application name.
- The script uses environment variables defined in a `.env` file located in the `src` directory of the application.
- Port `3000` is used for local development, and this can be modified by changing the `LOCAL_PORT` variable within the script.

### Help

If no command is provided, the script will output usage instructions.

```bash
./<script-name>.sh/.ps1
```

This will display all available commands.

## Notes

- The script uses either Docker or Podman to build and run containers.
- Environment variables, such as API base URLs, are set in the `.env` file.
- The `src` directory is mounted for local development, allowing for changes to be reflected in real time.

## Troubleshooting

- Make sure Docker or Podman is installed before running the script.
- Ensure that all environment variables are correctly defined in the `.env` file.
- If you encounter permission issues, try running the commands with `sudo`.

## Copyright

&copy; 2024 Georgia State University. This application was developed by Rohith Ganni and is proprietary to Georgia State University. Unauthorized distribution or copying of this code is prohibited.

---

**Developed By:** Georgia State University - Rohith Ganni
**Contact:** rohithganni79@gmail.com

