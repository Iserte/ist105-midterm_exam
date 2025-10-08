from django import forms

class MathForm(forms.Form):
    input1 = forms.FloatField(label='Input 1')
    input2 = forms.FloatField(label='Input 2')
    operation = forms.ChoiceField(choices=[
        ('add', 'Add'),
        ('sub', 'Subtract'),
        ('mul', 'Multiply'),
        ('div', 'Divide'),
        ('for_loop_sum', 'For Loop Sum'),
        ('while_loop_product', 'While Loop Product'),
    ])
