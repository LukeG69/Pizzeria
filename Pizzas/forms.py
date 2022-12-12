from django import forms 
from .models import Pizza, Toppings, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}
        


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = ['topping_name']
        labels = {'topping_name':''}
        widgets = {'topping_name':forms.Textarea(attrs={'cols':80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}