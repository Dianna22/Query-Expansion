import mwxml, os
import elasticsearchHelper as es

class XMLDumpsIndexer:
    def __init__(self, folder_path, index_name="wiki", replace_index=False):
        self.paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                      if os.path.splitext(os.path.join(folder_path, file))[1] == ".xml"]
        self.index_name = index_name
        self.replace = replace_index
        self.index = self._getIndex()

    def index_wiki_xml_dump(self, index, path):
        if not index.exists():
            index.create()
        dump = mwxml.Dump.from_file(open(path, encoding="utf-8"))
        print(dump.site_info.name, dump.site_info.dbname)
        for page in dump:
            for revision in page:
                obj={"title": page.title,"revision": revision.text}
                index.addJSONBuffering(obj)

    def _getIndex(self):
        index = es.IndexHelper(self.index_name)
        if index.exists():
            if self.replace:
                index.delete()
        else:
            index.create()
        return index

    def indexAll(self):
        for p in self.paths:
            self.index_wiki_xml_dump(self.index, p)
            print("indexed xml: " + p)

# indexed f:\wiki\wiki-articles