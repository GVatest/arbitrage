from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application, Withdraw
from rest_framework import permissions, status
from django.db import IntegrityError

class ApplicationView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        try:
            tg = data["tg"]
            email = data["email"]
            payment = data["payment"]
        except KeyError:
            return Response({"error": "Вы забыли заполнить нужные поля"}, status=status.HTTP_400_BAD_REQUEST)

        if not tg:
            return Response({"error": "Заполните поле Telegram ID"}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({"error": "Заполните поле Email"}, status=status.HTTP_400_BAD_REQUEST)
        if not payment:
            return Response({"error": "Заполните поле Сумма взноса"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            payment = int(payment)
            print(payment)
            if payment < 500 or payment > 5000:
                return Response({"error": "Сумма взноса должна быть меньше чем 5000 и больше 500"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "В поле Сумма взноса должно быть введено целое число"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            application = Application(tg=tg, email=email, payment=payment)
            application.save()
        except IntegrityError:
            return Response({"error": "Юзер с таким telegram ID или email уже отправлял заявку"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": "Заявка отправлена успешно"}, status=status.HTTP_200_OK)


class WithdrawView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        user = self.request.user
        withdraw = Withdraw(user=user)
        withdraw.save()

        return Response({"success": "Заявка отправлена успешно"}, status=status.HTTP_200_OK)