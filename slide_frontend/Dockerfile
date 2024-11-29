# Base Node.js image
FROM node:18

# Set work directory
WORKDIR /app

# Install dependencies
COPY package*.json /app/
RUN npm install

# Copy the application
COPY . /app/

# Build the frontend
RUN npm run build

# Install a lightweight server for static files
RUN npm install -g serve

# Expose the application port
EXPOSE 3000

# Serve the application
CMD ["serve", "-s", "dist", "-l", "3000"]
