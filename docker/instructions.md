### Docker pipeline
1. Create Dockerfile in repo
2. Dockerfile builds/generates Image, run with (for pathing to work): ```docker build -f path/to/Dockerfile -t name-of-image:version .``` (-f specifies filename, -t sets name and version)
3A.  Run single container with: ```docker run -d -p local-port:default-port --name name-to-give-container name-of-image``` (-d runs in detached mode/background, -p sets port)
3B. Run several containers with ```docker compose -f earendil.yaml up -d```

### Useful
- Check for memory usage: ```docker system df```
- Check images with: ```docker images```
- Check containers with: ```docker ps```
