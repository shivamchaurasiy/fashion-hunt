from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm


def feedback(req):
    fm = FeedbackForm()
    return render(req, 'feedback.html', {'form':fm})

def feedback_data(req):
    if req.method=="POST":
        fm=FeedbackForm(req.POST)
        if fm.is_valid():
            fm.save()
            fm = FeedbackForm()
            return redirect('/feedback/')
    else:
        fm = FeedbackForm()
    return render(req, 'feedback.html')
            
