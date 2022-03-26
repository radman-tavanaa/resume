from django.shortcuts import render , get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
# /// home ///
def Home(request):

    return render(request , 'pages/index.html' )


# /// about ///
def About_Page(request):
    
    #  /// about ///
    abouts = get_object_or_404(About)

    #  /// skills ///
    skill_intro = get_object_or_404(Skill_Intro)
    c_skill  = CodingSkills.objects.all()
    c_skill2 = CodingSkills2.objects.all()
    
    # /// comment & testimonials ///
    comment_intro = get_object_or_404(T_Intro)
    comments = testimonials.objects.all()
    
    # /// fact view ///
    fact = get_object_or_404(FACTS)

    context = {
        'abouts'   : abouts ,
        'skill_intro' : skill_intro,
        'c_skill'  : c_skill ,
        'c_skill2' : c_skill2 ,
        'comment_intro' : comment_intro ,
        'comments' : comments ,
        'fact'     : fact,
        
    }

    return render(request , 'pages/about.html' , context=context)



def Contact_Page(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
       
        
    
        context = {
            'name' : name , 
            'email' : email ,
            'subject': subject ,
            'message': message ,
            
            
        }

        message = '''
            new message: {}

            From: {}

        '''.format(context['message'] , context['email'])
        send_mail(context['subject'] , message , '' , ['radmantavanaa@gmail.com'])
        
        
        
        return  render(request , 'pages/send_message.html' )
        


    return render(request , 'pages/contact.html' , {} )    

    
    
















    