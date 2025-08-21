from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsSupervisor, IsStaff

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin!"})


class SupervisorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsSupervisor]

    def get(self, request):
        return Response({"message": "Hello Supervisor!"})


class StaffOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsStaff]

    def get(self, request):
        return Response({"message": "Hello Staff!"})
