from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint, sample


# Create your views here.

def home(request):
    return render(request, "generator/home.html", {"password": "Fuckery"})


def password(request):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "abcdefghijklmnopqrstuvwxyz".upper()
    numbers = "0123456789"
    symbols = "@#$%^&*+?"
    length = int(request.GET.get("length"))
    want_lower = "Y"
    want_upper = request.GET.get("upper", "")
    want_number = request.GET.get("number", "")
    want_symbols = request.GET.get("special", "")
    res = ""

    def three(first, second, third, num):
        return choice(first) + choice(second) + choice(third) + "".join(sample(first + second + third, num - 3))

    def two(first, second, num):
        r = choice(first) + choice(second)
        return r + "".join(sample(first + second, num - 2))

    if want_upper == "Y" and want_lower == "Y" and want_number == "Y" and want_symbols == "Y":
        combined = choice(lower_case) + choice(upper_case) + choice(numbers) + choice(symbols)
        res = combined + "".join(sample(lower_case + upper_case + symbols + numbers, length - 4))
    elif want_upper == "Y" and want_lower == "Y" and want_number == "Y":
        res = three(upper_case, lower_case, numbers, length)
    elif want_lower == "Y" and want_symbols == "Y" and want_number == "Y":
        res = three(lower_case, symbols, numbers, length)
    elif want_upper == "Y" and want_symbols == "Y" and want_number == "Y":
        res = three(upper_case, symbols, numbers, length)
    elif want_upper == "Y" and want_lower == "Y" and want_symbols == "Y":
        res = three(upper_case, symbols, lower_case, length)
    elif want_lower == "Y" and want_upper == "Y":
        res = two(lower_case, upper_case, length)
    elif want_lower == "Y" and want_symbols == "Y":
        res = two(lower_case, symbols, length)
    elif want_lower == "Y" and want_number == "Y":
        res = two(lower_case, numbers, length)
    elif want_upper == "Y" and want_symbols == "Y":
        res = two(upper_case, symbols, length)
    elif want_upper == "Y" and want_number == "Y":
        res = two(upper_case, numbers, length)
    elif want_number == "Y" and want_symbols == "Y":
        res = two(numbers, symbols, length)
    elif want_lower == "Y":
        res = "".join(sample(lower_case, length))
    elif want_upper == "Y":
        res = "".join(sample(upper_case, length))
    elif want_number == "Y":
        for x in range(length):
            res += str(randint(0, length))
    elif want_symbols == "Y":
        for x in range(length):
            res += choice(symbols)
    return render(request, "generator/password.html", {"password": res})


def about(request):
    return render(request, "generator/about.html")
