from django import forms

from main.models import Reservation


class ReservationForm(forms.ModelForm):

    def clean_name(self):
        name = self.data['name']
        return name.title()



    class Meta:
        model = Reservation
        fields =  ('name', 'email', 'phone','count', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Your name',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chats'}),

            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name': 'email',
                                             'placeholder':'Your email', 'data-rule': 'minlen:4',
                                             'data-msg': 'Please enter at least 4 chats'}),

            'phone': forms.TextInput(attrs={'class':'form-control', 'id':'phone', 'placeholder':'Your phone'}),

            'count': forms.NumberInput(attrs={'class':'form-control', 'id':'people', 'placeholder':'Your count', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chats'}),

            'message': forms.Textarea(attrs={'class':'form-control', 'name':'message', 'rows': '5', 'placeholder':'Your message to us'}),
        }



