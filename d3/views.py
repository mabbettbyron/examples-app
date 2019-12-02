from django.shortcuts import render

def viewbarlinegraph(request):
    return render(request, 'barline.html', {})

def viewbargraph(request):
    return render(request, 'bar.html', {})

def viewgroupedbargraph(request):
    return render(request, 'groupedbar.html', {})

def viewhistogramgraph(request):
    return render(request, 'histogram.html', {})
