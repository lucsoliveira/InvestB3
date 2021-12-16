from django import forms


class AddAlertForm(forms.Form):
    code = forms.CharField(max_length=8)
    interval_notify = forms.IntegerField()
    higher_limit = forms.FloatField()
    lower_limit = forms.FloatField()


class UpdateAlertForm(forms.Form):

    id_alert = forms.IntegerField()
    code = forms.CharField(max_length=8)
    interval_notify = forms.IntegerField()
    higher_limit = forms.FloatField()
    lower_limit = forms.FloatField()


class RemoveAlertForm(forms.Form):

    id_alert = forms.IntegerField()
