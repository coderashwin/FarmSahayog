from django.shortcuts import render
from django.db import connection

def index(request):
    if request.method == 'POST':
        # Get registration details from POST request
        district = request.POST.get('district')
        tehsil = request.POST.get('tehsil')
        village = request.POST.get('village')
        khasra = request.POST.get('khasra')
        captcha = request.POST.get('captcha')
        
        # Insert registration details into the database
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO registrations (district, tehsil, village, khasra) VALUES (%s, %s, %s, %s)', [district, tehsil, village, khasra])
        
        # Redirect to thank you page
        return render(request, 'thankyou.html')
    
    # Render the index.html template
    return render(request, 'index.html')
