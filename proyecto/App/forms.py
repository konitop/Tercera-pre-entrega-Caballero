from django import forms
 
class ViewerFormulario(forms.Form):
    id= forms.IntegerField()
    realname= forms.CharField()
    surname = forms.CharField()
    mail = forms.EmailField()

class StreamerFormulario(forms.Form):
    id= forms.IntegerField()
    username= forms.CharField()
    realname= forms.CharField()
    surname= forms.CharField()
    mail= forms.EmailField()
    link= forms.CharField()
    img= forms.CharField()

class VideoFormulario(forms.Form):
    id= forms.IntegerField()
    title= forms.CharField()
    mins= forms.IntegerField()
    sec= forms.IntegerField()
    day= forms.IntegerField()
    month= forms.IntegerField()
    year= forms.IntegerField()
    author= forms.CharField()
    views= forms.IntegerField()
    link= forms.CharField()
    gif= forms.CharField()
