from django import forms

from  accounts.models import CustomUser #accounts.models.pyのクラスを継承する。

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','furigana','email','postal_code','address','phone_number') #accounts/models.pyのフィールドのデータを参照

    #全フォームフィールドに一括でBootstrapのform-controlクラスを追加できる。
    def __init__(self,*args,**kwargs):  
        super().__init__(*args,**kwargs)
        for field in self.fields.values(): #selfはインスタンス化されたクラス自身
            field.widget.attrs['class'] = 'form-control' 


