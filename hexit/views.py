from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.core.paginator import Paginator
import pyperclip

def index(request):
    """This function displays the index page and does all its work like creating RGBs and Pagination"""
    if request.method == 'POST':
        copied_rgb = request.POST.get('copy-clipboard')
        pyperclip.copy(copied_rgb)
    rgb_li = []

    rgb_li_var = []
    for main_rgb in range(200):
        r = random.randrange(60, 155)
        g = random.randrange(60, 155)
        b = random.randrange(60, 155)
        rgb1 = (r, g, b)
        rgb_li_var.append(rgb1)
    
    for common_rgb in range(10):
        r = random.randrange(160, 255)
        g = random.randrange(160, 255)
        b = random.randrange(160, 255)
        rgb2 = (r, g, b)
        rgb_li.append(rgb2)
    
    paginator = Paginator(rgb_li_var, 20)
    page_number = request.GET.get('page')
    print(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    

    return render(request, "index.html", {
        "rgb_li_var": rgb_li_var,
        "rgb_li": rgb_li,
        'page_obj': page_obj
    })

def hex_check(hex_code):
    convert = None
    for item in range(len(hex_code)):
        if hex_code[item] == "a":
            hex_code[item] = 10
            convert = True
        elif hex_code[item] == "b":
            hex_code[item] = 11
            convert = True
        elif hex_code[item] =="c":
            hex_code[item] = 12
            convert = True
        elif hex_code[item] == "d":
            hex_code[item] = 13
            convert = True
        elif hex_code[item] == "e":
            hex_code[item] = 14
            convert = True
        elif hex_code[item] == "f":
            hex_code[item] = 15
            convert = True
        elif hex_code[item].isnumeric() == True:
            hex_code[item] = int(hex_code[item])
            convert = True
        else:
            convert = False
    return convert

def converter(request):
    converted_rgb = ""
    if request.method == 'POST':
            hex_code = list(request.POST.get('hex-code').lower())
            convert = hex_check(hex_code)
            if len(hex_code) == 7 and convert == True:
                red = (hex_code[1]*16) + (hex_code[2])
                green = (hex_code[3]*16) + (hex_code[4])
                blue = (hex_code[5]*16) + (hex_code[6])
                converted_rgb = (red, green, blue)
            else:
                pass
            
    return render(request, "converter.html", {
        "converted_rgb": converted_rgb,
    })
