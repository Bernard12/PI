from user_profile.models import UserProfile

def get_user(id=0):
    return UserProfile.objects.get(id=id)
