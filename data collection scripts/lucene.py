# import lucene
# from lupyne import engine   # don't forget to call lucene.initVM
# from lupyne.engine.indexers import Indexer
# indexer = Indexer()                      # create an in-memory index (no filename supplied)
# indexer.set('name', stored=True)                # create stored 'name' field
# indexer.set('text')                             # create indexed 'text' field (the default)
# indexer.add(name='sample', text='hello world')  # add a document to the index
# indexer.commit()                                # commit changes; document is now searchable
# hits = indexer.search('text:hello')             # run search and return sequence of documents
# len(hits), hits.count                           # 1 hit retrieved (out of a total of 1)
# hit, = hits
# hit['name']                                     # hits support mapping interface for their stored fields
# u'sample'
# print(hit.id, hit.score)                               # plus internal doc number and score
# # (0, 0.19178301095962524)
# print(hit.dict())


# import lucene

from lupy.indexer import Index
# we create index named "foobar", create True = overwrite existing
index = Index('foobar', create=True)
