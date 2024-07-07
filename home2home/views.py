from django.shortcuts import render

def trigger_error(request):
    # This view will raise an exception and trigger a 500 error
    raise Exception("This is a test exception")