#! /bin/bash
response_json=$(curl --request POST \
  --url http://api.openapi-generator.tech/api/gen/clients/python \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --cookie __cfduid=d7567cdaa06265533ca8e271e544f00031605573760 \
  --data '{
	"openAPIUrl": "https://api.weather.gov/openapi.json"
    }')

url=$(python3 - << EOF
url = ${response_json}['link']
print(url)
EOF
)

wget ${url} -O nws-python-openapi.zip
unzip -o nws-python-openapi.zip
cp -r python-client/* .
rm -rf python-client
rm -f nws-python-openapi.zip