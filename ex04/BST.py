import urllib

class Node:
    def __init__(self, word:str):
        self.word = word
        self.left = None
        self.right = None

class BST:
    def __init__(self,source:str,**kwargs):
        self.root = None
        self.results: list[str] = []
        url_bool=kwargs.get('url',False)
        file_bool=kwargs.get('file',False)
        if url_bool and file_bool: raise ValueError("Both 'url' and 'file' cannot be True.")
        if url_bool:
            with urllib.request.urlopen(source) as u:
                text = u.read().decode("utf-8")
                words = text.splitlines()
        elif file_bool:
            with open(source,"r",encoding="utf-8") as f:
                words=[line.strip() for line in f]
        else:
            raise ValueError("You must specify either url=True or file=True.")
        
        words=sorted(words)

        #create balanced bst
        def build_balanced(start:int ,end:int):
            if start>end: return None
            mid = (start+end)//2
            node = Node(words[mid])
            node.left = build_balanced(start,mid-1)
            node.right = build_balanced(mid+1,end)
            return node

        self.root=build_balanced(0,len(words)-1)

    def autocomplete(self,prefix:str) -> list[str]:
        results=[]
        self._collect(self.root,prefix,results)
        return results

    def _collect(self,node:Node,prefix:str,result:list[str])->None:
        if node is None: return
        #try to go left
        if node.left is not None: self._collect(node.left,prefix,result)
        # current node
        if node.word.startswith(prefix): result.append(node.word)
        #try to go right
        if node.right is not None: self._collect(node.right,prefix,result)
            