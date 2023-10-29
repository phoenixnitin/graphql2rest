# graphql2rest
Python code to create service layer with swagger to convert graphql into rest endpoints

## Build docker image
Execute below from root directory  
`
docker build -t flask-app .
`

## Run image
`
docker run -d -p 5000:8000 flask-app
`