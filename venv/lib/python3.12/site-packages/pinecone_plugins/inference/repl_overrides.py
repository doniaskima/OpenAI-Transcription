from .core.client.models import EmbeddingsList as OpenAPIEmbeddingsList
from .core.client.models import Embedding as OpenAPIEmbedding

def present_list(mylist):
    if (len(mylist) <= 5):
        # Show list as usual when fewer than 5 items.
        # This number is arbitrary and can be adjusted
        # but it seems silly to show the abbreviated
        # message with (2  more) or whatever when the
        # number of items is so small and it's no problem
        # to display the real values.
        return f"[{', '.join(repr(x) for x in mylist)}]"
    first_part = ', '.join(repr(x) for x in mylist[:2])
    last_part = ', '.join(repr(x) for x in mylist[-2:])
    formatted_values=f"[{first_part}, ..., {last_part}]"
    return formatted_values

def embedding_to_str(self: OpenAPIEmbedding):
    formatted_values=present_list(self.values)
    return """{{'values': {formatted_values}}}""".format(
        self=self, 
        formatted_values=formatted_values
    )
   
def embedding_list_to_string(self: OpenAPIEmbeddingsList):
    if len(self.data) == 0:
        formatted_embeddings = '[]'
    elif len(self.data) <= 5:
        formatted_embeddings = '[\n    ' + ',\n    '.join([embedding.to_str() for embedding in self.data]) + '\n  ]'
    else:
        omitted_msg = f"... ({len(self.data) - 4} more embeddings) ..."
        items_to_show = [e.to_str() for e in self.data[:2]] + [omitted_msg] + [e.to_str() for e in self.data[-2:]]
        formatted_embeddings = '[\n    ' + ',\n    '.join(items_to_show) + '\n  ]'

    return """EmbeddingsList(
  model='{self.model}',
  data={formatted_embeddings},
  usage={self.usage}
)""".format(self=self, formatted_embeddings=formatted_embeddings)


def install_repl_overrides():
    OpenAPIEmbedding.to_str = embedding_to_str
    OpenAPIEmbeddingsList.to_str = embedding_list_to_string