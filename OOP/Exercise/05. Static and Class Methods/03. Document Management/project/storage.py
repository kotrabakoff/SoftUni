from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return

        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        final = self.__find_by_id(self.categories, category_id)
        final.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        final = self.__find_by_id(self.topics, topic_id)
        final.edit(new_topic, new_storage_folder)


    def edit_document(self, document_id, new_file_name):
        final = self.__find_by_id(self.documents, document_id)
        final.edit(new_file_name)


    def delete_category(self, category_id):
        final = self.__find_by_id(self.categories, category_id)
        self.categories.remove(final)


    def delete_topic(self, topic_id):
        final = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(final)


    def delete_document(self, document_id):
        final = self.__find_by_id(self.documents, document_id)
        self.documents.remove(final)

    def get_document(self, document_id):
        final = self.__find_by_id(self.documents, document_id)
        return final

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity