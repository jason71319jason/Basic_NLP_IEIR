Elasticsearch install

- Mac terminal command -

if u install 'homebrew'
brew install elasticsearch

lastest version is 6.3.0
curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.0.tar.gz
tar -xvf elasticsearch-6.3.0.tar.gz
cd elasticsearch-6.3.0/bin
./elasticsearch (launch)

- Windows -
https://www.elastic.co/downloads/elasticsearch
https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html

P.S u need to install JAVA first

After launching ES
plz check http://127.0.0.1:9200/

----------------------------------------------------------------------------------

Install kibana
Visualize data and management tool

- Mac terminal command -

if u install 'Homebrew'
brew install kibana

lastest version is 6.3.0
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-6.3.0-darwin-x86_64.tar.gz
shasum -a 512 kibana-6.3.0-darwin-x86_64.tar.gz
tar -xzf kibana-6.3.0-darwin-x86_64.tar.gz
cd kibana-6.3.0-darwin-x86_64/

- Windows -
https://www.elastic.co/guide/en/kibana/current/windows.html

After launching kibana
plz check http://localhost:5601

----------------------------------------------------------------------------------

ES basic concept
https://www.tutorialspoint.com/elasticsearch/elasticsearch_basic_concepts.htm
