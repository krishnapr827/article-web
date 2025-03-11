from django.shortcuts import render

# Create your views here.
articles=[
    {'id':1,
     'title':'The Rise of Remote Work: Transforming the Modern Workplace',
     'desc':'The COVID-19 pandemic has accelerated a major shift in the workplace, making remote work a norm rather than an exception. This transformation has been driven by advancements in technology, changing workforce expectations, and the necessity for business continuity during challenging times. The rise of remote work has prompted organizations to rethink traditional office spaces, embracing flexible work arrangements and digital collaboration tools.'},
    {'id':2,
     'title':'The Impact of Artificial Intelligence on Healthcare',
     'desc':'Artificial Intelligence (AI) is revolutionizing various industries, with healthcare being one of the most significant beneficiaries. AI technologies, including machine learning, natural language processing, and robotics, are transforming how medical professionals diagnose, treat, and manage diseases. These advancements are enhancing the efficiency and accuracy of healthcare delivery, offering promising solutions for complex medical challenges.'},
    {'id':3,
     'title':'Sustainable Living: Simple Steps to Reduce Your Environmental Footprint',
     'desc':'Sustainable living is increasingly important as concerns about environmental degradation and climate change grow. Adopting eco-friendly practices can significantly reduce one\'s environmental footprint and contribute to a healthier planet. Sustainable living involves making conscious choices that minimize waste, conserve resources, and promote environmental stewardship'},
    {'id':4,
     'title':'Exploring the Benefits of Mindfulness Meditation',
     'desc':'Mindfulness meditation has gained popularity as a powerful practice for enhancing mental well-being and managing stress. Rooted in ancient contemplative traditions, mindfulness meditation involves focusing on the present moment with a non-judgmental and accepting attitude. This practice offers a range of benefits for mental, emotional, and physical health.'}
]


def home(request):
    context={
        'articles':articles,
        'title':'Home Page'
    }
    return render(request,'article_files/home.html',context)

def article(request,id):
    #id = 2 <-- can't come every time here and change to take as argument
    data=None
    for i in articles:
        if i['id']==id:
            data = i
            break

    context={
        'data':data,
        'title':'Article Page'
    }
    return render(request,'article_files/article.html',context)

def about(request):
    context={
        'title':'About Page'
    }
    return render(request,'article_files/about.html',context)

def contact(request):
    context={
        'title':'Contact Page'
    }
    return render(request,'article_files/contact.html',context)
