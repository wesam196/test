from django import forms



class regist1(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(),label="الاسم")
    number=forms.CharField(required=True,widget=forms.TextInput(),label="رقم الجوال")

class regist2(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(),label="الاسم")
    number=forms.CharField(required=True,widget=forms.TextInput(),label="رقم الجوال")

class regist3(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(),label="الاسم")
    number=forms.CharField(required=True,widget=forms.TextInput(),label="رقم الجوال")
