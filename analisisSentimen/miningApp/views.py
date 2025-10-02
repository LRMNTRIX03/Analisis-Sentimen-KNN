from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Teks
from django.contrib import messages
from django.core.paginator import Paginator
from .services.Preprocessing import PreprocessingServices
# Create your views here.
@login_required
def dashboard(request):
    title = "Dashboard"
    context = {
        'title': title
    }
    return render(request, 'miningApp/index.html', context)

@login_required
def inputData(request):
    title = "Input Data"
  
    teks_list = Teks.objects.all().order_by('teks_id')
    paginator = Paginator(teks_list, 10)
    page_number = request.GET.get('page')   
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj
    }
    if request.method == 'POST':
        try:
            file = request.FILES['inputFile']
            if file.size > 10485760:
                messages.error(request, "Ukuran file tidak boleh lebih dari 10MB")
                return redirect('input.index')
            if file.name.split('.')[-1] not in ['csv', 'xlsx', 'xls']:
                messages.error(request, "Format file tidak sesuai")
                return redirect('input.index')
            data =pd.read_csv(file)
            if 'full_text' not in data.columns:
                messages.error(request, "Format file tidak sesuai")
                return redirect('input.index')
            full_text = data['full_text'].dropna().tolist()
            teks_obj = [Teks(teks=text) for text in full_text]
            Teks.objects.bulk_create(teks_obj)
            messages.success(request, "Data berhasil diupload")
            return redirect('input.index')
        except Exception as e:
            print(e)
            messages.error(request, "Data gagal diupload")
            return redirect('input.index')
            
    return render(request, 'miningApp/inputData/index.html', context)

@login_required
def Preprocessing(request):
    title = "Preprocessing"
    context = {
        'title': title
    }
    return render(request, 'miningApp/preprocessing/index.html', context)
