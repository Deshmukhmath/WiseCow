FROM alpine:latest

# Install necessary packages (cowsay, fortune, etc.) via an alternative method
RUN apk add --no-cache fortune bash ncurses netcat-openbsd perl && \
    cpan install App::cowsay

# Set the working directory
WORKDIR /app

# Copy the wisecow file to the /app directory
COPY wisecow /app/wisecow

# Make sure the wisecow script is executable
RUN chmod +x /app/wisecow

# Expose the required port
EXPOSE 4499

# Set the default command to run the wisecow script
CMD ["/app/wisecow"]
