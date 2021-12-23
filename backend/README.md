# Django4_Basic

## Run Using Docker
  Place .env File First 
#### Step 1 : First Install docker & docker-compose (if already installed then skip this step)
```
sudo apt update
sudo apt upgrade
sudo apt install docker.io
```
##### Install Docker compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

## Docker command text to run this project
```
docker build --tag python-django .
```
```
docker run --publish 8000:8000 python-django
```

### Docker Basic Info
![Docker Basic 1.1 ](https://github.com/MdNazmul9/Django4_Basic/blob/main/doc/1.1.png)
![Docker Basic 1.2 ](https://github.com/MdNazmul9/Django4_Basic/blob/main/doc/1.2.png)


# Run Project:
  - 1. clone the project
  - 2. 
  ```
  docker-compose build
  docker-compose up
  docker-compose down
  ```
