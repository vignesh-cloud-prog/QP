from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from question_papers.models import Question_paper
from provides.models import Provider

# Create your views here.
def profile_view(request):
    my_papers_reviewing = Provider.objects.filter(name=request.user)
    my_papers_uploaded = Question_paper.objects.filter(provider=request.user)
    print(my_papers_uploaded)
    my_recs = request.user.profile.get_recomended_profiles()
    print(my_recs)
    context = {
        "my_papers_reviewing": my_papers_reviewing,
        "my_papers_uploaded": my_papers_uploaded,
        "my_recs": my_recs,
    }

    return render(request, 'profiles/profile.html', context)

def profile_settings(request):
    if request.method == "POST" or None or request.FILES:

        user_id = request.POST.get('user_id')
        name = request.POST.get('full_name')
        pic = request.FILES.get('pic')
        bio = request.POST.get('bio')
        college = request.POST.get('college')
        try:
            if name is "" or bio is "" or college == "":
                messages.warning(request, 'Values can not be null.')
                return render(request, 'profiles/profile_edit.html')

            userObj = User.objects.get(id=user_id)
            userObj.first_name = name
            userObj.save()

            profileObj = Profile.objects.get(user=request.user)

            profileObj.college = college
            if pic is not None:
                profileObj.pic = pic
            profileObj.bio = bio
            profileObj.save()
            messages.success(request, 'Your profile updated successfully.')

            return redirect("profile")
        except Exception as e:
            messages.error(request, f"Profile not updated successfully\n {e}")
            return render(request, 'profiles/profile_edit.html')

    return render(request, 'profiles/profile_edit.html')