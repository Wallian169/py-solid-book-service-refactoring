import json
import xml.etree.ElementTree as ElTree
from app.models import Book


class Serializer:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ElTree.Element("book")
            title = ElTree.SubElement(root, "title")
            title.text = book.title
            content = ElTree.SubElement(root, "content")
            content.text = book.content
            return ElTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
