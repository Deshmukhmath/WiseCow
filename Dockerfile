# Step 1: Use a base image with a shell environment
FROM ubuntu:latest

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the shell script and any other necessary files into the container
COPY wisecow.sh /app/

# Step 4: Ensure the script has execution permissions
RUN chmod +x wisecow.sh

# Step 5: Set the command to run the script
CMD ["./wisecow.sh"]
