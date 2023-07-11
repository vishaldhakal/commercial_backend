from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import UserProfile
from .serializers import UserProfileDetailSerializer, ChangePasswordSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import generics


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "accessToken": token.key,
            "user": {
                'user': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role
            }
        }, status=200)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserProfile
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_user_profile(request):
    userid = request.GET.get("user")
    userpr = UserProfile.objects.get(id=userid)
    userpr.is_verified = True
    userpr.save()
    return Response({"detail": "Verified Sucessfully"}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_detail(request):
    user = request.user
    users_ser = UserProfileDetailSerializer(user)
    return Response({
        'user': users_ser.data,
    }, status=200)


@api_view(['POST'])
def create_user_profile(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    user_type = request.POST.get('user_type', "is_agent")

    # Check if email already exists
    if UserProfile.objects.filter(email=email).exists():
        return Response({'detail': 'Email address already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if username already exists
    if UserProfile.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if all required fields are present
    if not all([first_name, last_name, email, password, username, user_type]):
        return Response({'detail': 'All required fields are not present'}, status=status.HTTP_400_BAD_REQUEST)

    if user_type == "is_agent":
        user = UserProfile.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name, role='Agent')
        user.save()

    elif user_type == "is_admin":
        user = UserProfile.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name, role='Admin')
        user.save()

    elif user_type == "is_blog_writer":
        user = UserProfile.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name, role='Blog Writer')
        user.save()

    else:
        user = UserProfile.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name, role='Other')
        user.save()

    return Response({
        "success": "User Created Sucessfully"
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    if user.is_verified:
        data = {
            'user': {
                'id': user.id,
                'email': user.email,
                'displayName': user.first_name+" "+user.last_name,
                'role': user.role,
                'photoURL': user.avatar or " ",
                'address': user.address,
                'about': user.bio,
                'phoneNumber': user.phone_number,
            }
        }
        return Response(data, status=200)
    else:
        return Response({"detail": "User not verified"}, status=403)


@api_view(['GET'])
def get_users(request):
    users = UserProfile.objects.all()
    users_serializer = UserProfileDetailSerializer(users, many=True)
    return Response({"users": users_serializer.data}, status=200)


@api_view(['GET'])
def get_user_detail(request):
    username = request.GET.get("name")
    user = UserProfile.objects.get(username=username)
    users_serializer = UserProfileDetailSerializer(user)
    return Response({"user": users_serializer.data}, status=200)


@api_view(['POST'])
def update_user_detail(request):
    username = request.POST.get("username")
    user = UserProfile.objects.get(username=username)

    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.phone_number = request.POST.get("phone_number", " ")
    user.address = request.POST.get("address", " ")
    user.bio = request.POST.get("bio", " ")
    user.status = request.POST.get("status", "Active")
    user.is_verified = request.POST.get("is_verified", "False") == "True"
    user.role = request.POST.get("role")
    user.avatar = request.FILES.get("avatar")

    user.facebook_link = request.POST.get("facebook_link", " ")
    user.instagram_link = request.POST.get("instagram_link", " ")
    user.website_link = request.POST.get("website_link", " ")
    user.youtube_link = request.POST.get("youtube_link", " ")
    user.twitter_link = request.POST.get("twitter_link", " ")
    user.linkedin_link = request.POST.get("linkedin_link", " ")

    user.save()

    return Response({"success": "Updated sucess"}, status=200)
