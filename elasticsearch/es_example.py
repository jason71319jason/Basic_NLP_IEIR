from elasticsearch import Elasticsearch, helpers
import os
import json
import sys
import pprint

SRC_DIR = '../data/law'
INDEX_NAME = '104_hackathon_qa'
DOC_TYPE = 'law'
# mapping
law_mapping = {
    "properties": {
        "title": {"type": "text"},
        "content": {"type": "text"}
    }
}


def open_files():
    for f in os.listdir(SRC_DIR):
        if f.endswith('json'):
            with open(os.path.join(SRC_DIR, f), 'r') as f:
                for l in f:
                    j = eval(l)
                    yield json.dumps(j)


def load():

    es = Elasticsearch()
    if not es.indices.exists(INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
        es.indices.put_mapping(
            index=INDEX_NAME, doc_type=DOC_TYPE, body=law_mapping)

    success, _ = helpers.bulk(
        es, open_files(), index=INDEX_NAME, doc_type=DOC_TYPE, ignore=400)
    print(success, 'doc success.')


def query(text, num=5):
    query_mapping = {
        "query": {
            "match": {"content": text}
        },
        "size": num
    }
    es = Elasticsearch()
    result = es.search(index=INDEX_NAME, doc_type=DOC_TYPE, body=query_mapping)

    for r in result['hits']['hits']:
        pprint('score: {0}, source:{1}'.format(
            r['_score'], str(r['_source'])))


def delete(index):
    es = Elasticsearch()
    if es.indices.exists(index):
        es.indices.delete(index)


if __name__ == '__main__':
    if sys.argv[1] == 'q':
        query(sys.argv[2])
    else:
        load()
