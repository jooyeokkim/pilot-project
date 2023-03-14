from django import forms

from snack.models import SnackRequest


class SnackEditForm(forms.ModelForm):

    class Meta:
        model = SnackRequest
        fields = ['user', 'snack', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['snack'].disabled = True
        self.fields['user'].label = "신청자 이메일"
        self.fields['snack'].label = "과자 이름"
        self.fields['description'].label = "설명"


class SnackManageForm(forms.ModelForm):

    class Meta:
        model = SnackRequest
        fields = ['user', 'snack', 'description', 'is_accepted', 'supply_year', 'supply_month']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['snack'].disabled = True
        self.fields['user'].label = "신청자 이메일"
        self.fields['snack'].label = "과자 이름"
        self.fields['description'].label = "설명"
        self.fields['is_accepted'].label = "승인 여부"
        self.fields['supply_year'].label = "비치 예정 연도"
        self.fields['supply_month'].label = "비치 예정 월"


class SnackRequestForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    image = forms.ImageField()
    url = forms.URLField(max_length=500)

    class Meta:
        model = SnackRequest
        fields = ['snack', 'name', 'image', 'url', 'description']