# Use an official Node.js image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application’s code to the working directory
COPY . .

# Expose the port your React app runs on
EXPOSE 3000

# Command to run your application
CMD ["npm", "start"]
