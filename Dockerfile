FROM alpine:latest

# Install required packages
RUN apk add --no-cache cowsay fortune bash ncurses netcat-openbsd

# Set the working directory
WORKDIR /app

# Copy the wisecow script into the container
COPY wisecow /app/wisecow

# Make the script executable
RUN chmod +x /app/wisecow

# Expose the port the app will run on
EXPOSE 4499

# Run the wisecow application
CMD ["/app/wisecow"]
