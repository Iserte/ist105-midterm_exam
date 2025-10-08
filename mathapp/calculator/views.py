from django.shortcuts import render
from .forms import MathForm

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['input1']
            b = form.cleaned_data['input2']
            op = form.cleaned_data['operation']

            try:
                if op == 'add':
                    result = a + b
                elif op == 'sub':
                    result = a - b
                elif op == 'mul':
                    result = a * b
                elif op == 'div':
                    if b != 0:
                        result = a / b
                    else:
                        error = "Error: Division by zero"
                elif op == 'for_loop_sum':
                    if a > b:
                        a, b = b, a
                    result = sum(range(int(a), int(b)+1))
                elif op == 'while_loop_product':
                    if a > b:
                        a, b = b, a
                    result = 1
                    i = int(a)
                    while i <= int(b):
                        result *= i
                        i += 1

                if result is not None:
                    if result > 100:
                        result *= 2
                    elif result < 0:
                        result += 50

            except ValueError:
                error = "Invalid number input"
            except Exception as e:
                error = str(e)

            return render(request, 'result.html', {'result': result, 'error': error})
    else:
        form = MathForm()

    return render(request, 'math_form.html', {'form': form})