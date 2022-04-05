from elasticsearch import Elasticsearch


es = Elasticsearch(hosts="https://localhost:9200", http_auth=("elastic", "ukPIFFhT0YVkh-epZtoE"), verify_certs=False)

doc = {
    "name": "Rakka",
    "age": 25,
    "citizen": "Indonesia"
}

# es.index(index="user", id=1, document=doc)

# resp = es.get(index="user", id=1)
resp = es.search(index="user")
print(resp)