
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import contact
from .serializers import ContactSerializer


class ContactList(APIView):


    def get(self, request, format=None):
        contacts = contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)

        return Response(serializer.data)


class ContactCreate(APIView):


    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ContactDetail(APIView):


    def get(self, request, pk, format=None):
        try:
            contact_object = contact.objects.get(pk=pk)
        except contact.DoesNotExist:
            return Response(
                {"detail": "Контакт не найден."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ContactSerializer(contact_object)

        return Response(serializer.data)


class ContactUpdate(APIView):

    def put(self, request, pk, format=None):
        try:
            contact_object = contact.objects.get(pk=pk)
        except contact.DoesNotExist:
            return Response(
                {"detail": "Контакт не найден."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ContactSerializer(
            contact_object,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ContactPartialUpdate(APIView):

    def patch(self, request, pk, format=None):
        try:
            contact_object = contact.objects.get(pk=pk)
        except contact.DoesNotExist:
            return Response(
                {"detail": "Контакт не найден."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ContactSerializer(
            contact_object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ContactDelete(APIView):


    def delete(self, request, pk, format=None):
        try:
            contact_object = contact.objects.get(pk=pk)
        except contact.DoesNotExist:
            return Response(
                {"detail": "Контакт не найден."},
                status=status.HTTP_404_NOT_FOUND
            )

        contact_object.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )