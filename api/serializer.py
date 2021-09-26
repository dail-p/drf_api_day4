from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from api.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'name', 'email', #'fame'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    def get_or_create_packages(self, authors):
        author_ids = []
        for author in authors:
            author_instance, created = Author.objects.get_or_create(name=author.get('name'), email=author.get('email'))
            author_ids.append(author_instance.pk)
        return author_ids

    def create_or_update_packages(self, authors):
        author_ids = []
        for author in authors:
            author_instance, created = Author.objects.update_or_create(name=author.get('name'), email=author.get('email'))
            author_ids.append(author_instance.pk)
        return author_ids

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        #fame = validated_data.pop('fame')
        book = Book.objects.create(**validated_data)
        book.authors.set(self.get_or_create_packages(authors))
        #book.fame = book.fame + fame
        book.save()
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors', [])
        instance.authors.set(self.create_or_update_packages(authors))
        fields = ['title', 'body']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = 'title', 'authors', #'fame'

