from django import form


class ContactForm(forms.Form):
	Full_Name = forms.charfield(label=' Your Name',max_length=200)
	Email = forms.Emailfield()
	Phone_No = forms.charfield()
	Message = forms.charfield(widget=forms.Textarea)

