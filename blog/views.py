from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from blog.forms import ContactForms
from blog.models import Manclothes, Wclothes, Banner, Devices, Laptops, Mbanner, Wbanner, Aboutus


def index(request):
    manclothe = Manclothes.objects.all()
    wclothe = Wclothes.objects.all()
    ban = Banner.objects.all()
    device = Devices.objects.all()
    laptop = Laptops.objects.all()
    mbanner = Mbanner.objects.all()
    wbanner = Wbanner.objects.all()
    about = Aboutus.objects.all()

    context = {
        "manclothe": manclothe,
        "wclothe": wclothe,
        "ban": ban,
        "device": device,
        "laptop": laptop,
        "mbanner": mbanner,
        "wbanner": wbanner,
        "about": about
    }
    return render(request, "index.html", context=context)


def contact(request):
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    context = {
        "form": form,
    }
    return render(request, 'contact.html', context=context)

def computers(request):
    laptop = Laptops.objects.all()
    device = Devices.objects.all()
    context = {
        "laptop": laptop,
        "device": device,
    }
    return render(request, "computers.html", context=context)

def mans_clothes(request):
    manclothe = Manclothes.objects.all()
    mbanner = Mbanner.objects.all()
    context = {
        "manclothe": manclothe,
        "mbanner": mbanner,
    }
    return render(request, "mans_clothes.html", context=context)

def womans_clothes(request):
    wclothe = Wclothes.objects.all()
    wbanner = Wbanner.objects.all()
    context = {
        "wclothe": wclothe,
        "wbanner": wbanner
    }
    return render(request, "womans_clothes.html", context=context)

def devicedetailview(request, id):
    try:
        device = Devices.objects.get(id=id)
        context = {
            "device": device
        }
    except device.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "device_detail.html", context=context)

def buy(request):

    context = {

    }
    return render(request, "buy.html", context=context)

def about(request):
    about = Aboutus.objects.all()
    context = {
        "about": about

    }
    return render(request, "about.html", context=context)


def laptopDetail(request, laptop):
    laptop = get_object_or_404(Laptops, slug=laptop)
    context = {
        "laptop": laptop
    }
    return render(request, "laptopDetail.html", context=context)


class LaptopsCreateView(CreateView):
    model = Laptops
    template_name = "laptopsCreate.html"
    fields = ("name", "oldprice", "price", "brand", "img")

class LaptopsUpdateView(UpdateView):
    model = Laptops
    fields = ('name', 'oldprice', 'price', 'brand', 'img')
    template_name = 'laptopsEdit.html'

class LaptopsDeleteView(DeleteView):
    name = Laptops
    template_name = 'laptopsDelete.html'
    success_url = reverse_lazy('index')
