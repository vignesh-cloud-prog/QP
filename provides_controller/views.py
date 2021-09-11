from django.shortcuts import render
from provides.models import Provide
from question_papers.models import Question_paper
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Function helps to get all the items need to be pushed which availed from Provide function
def push(request):
    pushes = Provide.objects.all()
    push = {'pushes': pushes}
    return render(request, 'provides_controller/push.html', push)

# function helps to upload and delete papers uploaded by users
def pushed(request):
    if request.method == 'POST':
        username = request.POST['pro']
        from_user=User.objects.get(username=username)
        paper_type = request.POST['paper_type']
        emailid = request.POST['email']
        college = request.POST['college']
        university = request.POST['university']
        course = request.POST['course']
        print(paper_type)
        if paper_type=="board":
            course="board"
        print(course)
        year = request.POST['semister']
        subject = request.POST['subject']
        examination_year = request.POST['examination_year']
      
        examination_title = request.POST['examination_title']
        paper = request.POST['paper']
        date = request.POST['date']
       
        pro_id = request.POST['id']
        emailid = request.POST['email']
        push = Question_paper(provider=from_user, paper_type=paper_type, education_type=college, governing_body=university,
                               course_name=course, period=year, subject_name=subject, paper_year=examination_year,paper_title=examination_title, paper_doc=paper)
        push.save()

        pull = Provide(id=pro_id)
        pull.delete()

        send_mail(
            'hello',
            'i am vignesh',
            'qpcom80@gmail.com',
            [emailid],
            fail_silently=True,
        )
    return render(request, 'provides_controller/push.html',)