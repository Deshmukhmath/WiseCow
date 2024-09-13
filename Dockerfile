
FROM alpine:latest


RUN apk add --no-cache cowsay fortune bash ncurses netcat-openbsd


WORKDIR /app


COPY wisecow /wisecow


RUN chmod +x /wisecow


EXPOSE 4499


CMD ["/app/wisecow"]
