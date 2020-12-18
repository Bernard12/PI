from user_profile.models import UserProfile

def get_user(id=0):
    return UserProfile.objects.get(id=id)

def get_user_by_name(name=''):
    return UserProfile.objects.get(name=name)
