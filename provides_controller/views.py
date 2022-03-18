from django.shortcuts import render
from provides.models import Provide
from question_papers.models import Question_paper
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def push(request):
    """
    Displays all the question papers provided by the users, which are to be reviewed. :model:`provides.Provide`.

    **Context**

    ``mymodel``
        Instances of :model:`provides.Provide`.

    **Template:**

    :template:`provides_controller/push.html`
    """
    if request.method == 'POST'or None or request.FILES:
        try:
            username = request.POST.get('pro')
            from_user = User.objects.get(username=username)
            paper_type = request.POST.get('paper_type')
            emailid = request.POST.get('email')
            college = request.POST.get('college')
            university = request.POST.get('university')
            course = request.POST.get('course')
            print(paper_type)
            if paper_type == "board":
                course = "board"
            print(course)
            year = request.POST.get('semister')
            subject = request.POST.get('subject')
            examination_year = request.POST.get('examination_year')

            examination_title = request.POST.get('examination_title')
            paper = request.FILES.get('paper')
            date = request.POST.get('date')
            print(paper)
            pro_id = request.POST.get('id')
            emailid = request.POST.get('email')
            push = Question_paper(provider=from_user, paper_type=paper_type, education_type=college, governing_body=university,
                                  course_name=course, period=year, subject_name=subject, paper_year=examination_year, paper_title=examination_title, paper_doc=paper)
            push.save()

            pull = Provide(id=pro_id)
            pull.delete()

            send_mail(
                'Your paper is now live on QP Web',
                f"The paper provided by you, ({university}, {course}, {year}, {subject}, {examination_title}, {examination_year}) has been appproved.\nYou can check on our website ➡  https://qpweb.herokuapp.com/.",
                'qpcom80@gmail.com',
                [emailid],
                fail_silently=True,
            )
            messages.success(request, f"The paper has been uploaded")
        except Exception as e:
            messages.error(request, f"something went wrong ({e})")

    pushes = Provide.objects.all()
    push = {'pushes': pushes}
    return render(request, 'provides_controller/push.html', push)
