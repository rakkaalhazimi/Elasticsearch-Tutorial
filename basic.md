# How to Establish ElasticSearch Local Server
1. Download elasticsearch from [here][elasticdownload]
2. Unzip the file into your desired directory
3. Add `<ES directory>/bin`into your PATH variables. 
4. Use `elasticsearch.bat` command in cmd
5. You will be given a password in the first run, write it on the note
6. The default user is "elastic"
7. If you accidently close your cmd, you can reset your password with `elasticsearch-resetpassword -u elastic` command
8. Open new terminal and type `curl -k -u elastic:<password> GET https://localhost:9200`, you will get a JSON-like reply if you success.
9.  Try adding data with `curl -k -u elastic:ukPIFFhT0YVkh-epZtoE POST https://localhost:9200/user/_doc -H "Content-Type: application/json" -d "{\"name\":\"test\", \"age\": \"test\"}"`, use any `<index-name>`.
10. Then, try to search the data with `curl -k -u elastic:<password> GET https://localhost:9200/<index-name>/_search`
11. For further command please refer to elasticsearch documentations [here][elasticdocs].


[elasticdownload]: https://www.elastic.co/downloads/elasticsearch
[elasticdocs]: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html