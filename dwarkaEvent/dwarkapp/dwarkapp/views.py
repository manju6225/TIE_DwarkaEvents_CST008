from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from database.models import connect
from database.admin import connectadmin
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def base(request):
    return render(request, "base.html")


def gallery(request):
    return render(request, "gallery.html")


def dtabase(request):
    if request.method == "POST":

        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        event = request.POST.get('event')
        cc = request.POST.get('cc')
        exp = request.POST.get('exp')
        cvv = request.POST.get('cvv')
        dt = connect(name=name, city=city, address=address,
                     pincode=pincode, event=event, cc=cc, exp=exp, cvv=cvv)
        dt.save()
        if dt.save():
            print("success")
    return render(request, "checkout.html")


def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
         # Get other form fields as needed
            message = request.POST.get('message')

         # Create the congratulatory message
            congratulatory_message = f"Hello {name},\n\nCongratulations! Your message has been received. We will get back to you soon.\n\nThank you for contacting us!\n"

         # Send the congratulatory email
            send_mail(
                'Congratulations on Contacting Us',
                congratulatory_message,
                'your_email@example.com',  # Replace with your email address
                [email],  # The recipient's email address
                fail_silently=False,
            )
            print("success")
    except Exception as e:

        print(e)

        # Redirect to a success page or the same contact page

    return render(request, "contact.html")


def header(request):
    return render(request, "header.html")


def price(request):
    return render(request, "price.html")


def review(request):
    return render(request, "review.html")


def service(request):
    return render(request, "service.html")


def checkout(request):
    # event = Event.objects.get(pk=event_id)

    # if request.method == 'POST':
    #     attendee_form = AttendeeForm(request.POST)
    #     order_form = OrderForm(request.POST)

    #     if attendee_form.is_valid() and order_form.is_valid():
    #         attendee = attendee_form.save()
    #         order = Order(
    #             event=event,
    #             attendee=attendee,
    #             total_amount=event.price
    #         )
    #         order.save()
    #         return redirect('checkout_success')
    # else:
    #     attendee_form = AttendeeForm()
    #     order_form = OrderForm(initial={'event_id': event_id})

    # return render(request, 'checkout.html', {'event': event, 'attendee_form': attendee_form, 'order_form': order_form})
    return render(request, 'checkout.html')


def checkout_success(request):
    return render(request, 'checkout_success.html')
