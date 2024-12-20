from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from picture.models import Picture



class CommentView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, picture_id):
        try:
            picture = Picture.objects.get(id=picture_id)
        except Picture.DoesNotExist:
            return Response({'error': 'Picture not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, picture=picture)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)