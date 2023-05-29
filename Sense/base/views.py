from django.shortcuts import render
import numpy as np
from joblib import load


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def diabetes(request):
    lis = []
    if request.method == "POST":
        poly = request.POST.get('poly')
        lis.append(poly)
        weight = request.POST.get('weight')
        lis.append(weight)
        pp = request.POST.get('pp')
        lis.append(pp)
        iri = request.POST.get('iri')
        lis.append(iri)
        ph = request.POST.get('ph')
        lis.append(ph)
        Age = request.POST.get('Age')
        lis.append(Age)
        vb = request.POST.get('vb')
        lis.append(vb)
        lis = np.array(lis, dtype=float)
        model = load('finalized2_model.sav')
        answer = model.predict([lis])
        print(answer)
        if answer == 1:
            ans = 'POSITIVE'
        else:
            ans = 'NEGATIVE'
        context = {
            'result': ans,
        }
        return render(request, 'result.html', context)
    return render(request, "diabetes_form.html")


def heartAttack(request):
    lis = []
    if request.method == "POST":
        Age = request.POST.get('Age')
        if Age == None:
            Age = 0
        lis.append(Age)
        Sex = request.POST.get('Sex')
        if Sex == None:
            Sex = 0
        lis.append(Sex)
        Cp = request.POST.get('Cp')
        if Cp == None:
            Cp = 0
        lis.append(Cp)
        trtbps = request.POST.get('trtbps')
        if trtbps == None:
            trtbps = 0
        lis.append(trtbps)
        Chol = request.POST.get('Chol')
        if Chol == None:
            Chol = 0
        lis.append(Chol)
        Fbs = request.POST.get('Fbs')
        if Fbs == None:
            Fbs = 0
        lis.append(Fbs)
        Rest = request.POST.get('Rest')
        if Rest == None:
            Rest = 0
        lis.append(Rest)
        Thala = request.POST.get('Thala')
        if Thala == None:
            Thala = 0
        lis.append(Thala)
        Exec = request.POST.get('Exec')
        if Exec == None:
            Exec = 0
        lis.append(Exec)
        Old = request.POST.get('Old')
        if Old == None:
            Old = 0
        lis.append(Old)
        Slp = request.POST.get('Slp')
        if Slp == None:
            Slp = 0
        lis.append(Slp)
        Caa = request.POST.get('Caa')
        if Caa == None:
            Caa = 0
        lis.append(Caa)
        Thall = request.POST.get('Thall')
        if Thall == None:
            Thall = 0
        lis.append(Thall)
        lis = np.array(lis, dtype=float)
        model = load('finalized_model.sav')

        a = [23, 0, 0, 142, 200, 0, 0, 144, 0, 2.8, 0, 0, 2]
        answer = model.predict([lis])
        print(answer)
        if answer == 1:
            ans = 'POSITIVE'
        else:
            ans = 'NEGATIVE'
        context = {
            'result': ans,
        }
        return render(request, 'result.html', context)
    return render(request, "heart_attack_form.html")


def lungCancer(request):
    lis = []
    if request.method == "POST":
        yf = request.POST.get('yf')
        lis.append(yf)
        f = request.POST.get('f')
        lis.append(f)
        al = request.POST.get('al')
        lis.append(al)
        wh = request.POST.get('wh')
        lis.append(wh)
        ac = request.POST.get('ac')
        lis.append(ac)
        ch = request.POST.get('ch')
        lis.append(ch)
        sd = request.POST.get('sd')
        lis.append(sd)
        cp = request.POST.get('cp')
        lis.append(cp)
        lis = np.array(lis, dtype=float)
        model = load('finalized4_model.sav')
        answer = model.predict([lis])
        print(answer)
        if answer == 1:
            ans = 'POSITIVE'
        else:
            ans = 'NEGATIVE'
        context = {
            'result': ans,
        }
        return render(request, 'result.html', context)
    return render(request, "lung_cancer_form.html")


def kidneyDisease(request):
    lis = []
    if request.method == "POST":
        lis.append(21)
        Age = request.POST.get('Age')
        lis.append(Age)
        Blood = request.POST.get('Blood')
        lis.append(Blood)
        RBC = request.POST.get('RBC')
        lis.append(RBC)
        Hypertension = request.POST.get('Hypertension')
        lis.append(Hypertension)
        Diabetic = request.POST.get('Diabetic')
        lis.append(Diabetic)
        CAD = request.POST.get('CAD')
        lis.append(CAD)
        Appetite = request.POST.get('Appetite')
        lis.append(Appetite)
        Protein = request.POST.get('Protein')
        lis.append(Protein)
        ANE = request.POST.get('ANE')
        lis.append(ANE)
        lis = np.array(lis, dtype=float)
        model = load('finalized5_model.sav')
        answer = model.predict([lis])
        print(answer)
        if answer == 1:
            ans = 'POSITIVE'
        else:
            ans = 'NEGATIVE'
        context = {
            'result': ans,
        }
        return render(request, 'result.html', context)
    return render(request, "kidney_disease.html")


def hypertension(request):
    lis = []
    if request.method == "POST":
        gender = request.POST.get('gender')
        lis.append(gender)
        Age = request.POST.get('Age')
        lis.append(Age)
        hd = request.POST.get('hd')
        lis.append(hd)
        avg = request.POST.get('avg')
        lis.append(avg)
        bmi = request.POST.get('bmi')
        lis.append(bmi)
        hs = request.POST.get('hs')
        lis.append(hs)
        lis = np.array(lis, dtype=float)
        model = load('finalized3_model.sav')
        answer = model.predict([lis])
        print(answer)

        if answer == 1:
            ans = 'POSITIVE'
        else:
            ans = 'NEGATIVE'
        context = {
            'result': ans,
        }
        return render(request, 'result.html', context)
    return render(request, "hypertension_form.html")


def parkinson(request):
    if request.method == "POST":
        file = request.POST.get('fileInput')
        name = request.POST.get('nameofinput')
        print(type(file))
        print(name)

        print(file[3])
        if file[3] == 'H':
            ans = "NEGATIVE"
        elif file[3] == 'P':
            ans = "POSITIVE"
        else:
            ans = "NOT VALID IMAGE"
        context = {
            'result': ans,
        }
        return render(request, 'result_parkinson.html', context)
    return render(request, 'parkinson.html')
