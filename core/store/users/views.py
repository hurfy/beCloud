from typing                      import Any
from rest_framework              import status
from rest_framework.views        import APIView
from rest_framework.response     import Response
from rest_framework.permissions  import IsAuthenticated
from django.contrib.auth.hashers import make_password
from .serializers                import UserProfileSerializer


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Any) -> Response:
        """
        Реализация GET запроса на получение информации о пользователе
        :param request:     request
        :return:  Response: Ответ
        """
        user       = request.user
        serializer = UserProfileSerializer(user)

        return Response(serializer.data)


class UserCreateView(APIView):
    def post(self, request: Any):
        """
        Реализация POST запроса для создания нового пользователя
        :param request:     request
        :return:  Response: Ответ
        """
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            password        = request.data.get('password')
            hashed_password = make_password(password)

            serializer.validated_data['password'] = hashed_password
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
