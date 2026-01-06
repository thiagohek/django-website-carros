from django import forms
from cars.models import Car

          
class CarModelForm(forms.ModelForm):    
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self): # Regra para valor mínimo do carro cadastrado
        value = self.cleaned_data.get('value')
        if value < 5000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$ 5.000,00')
        return value
    
    def clean_factory_year(self): # Regra para ano de fabricação mínimo para cadastrar carro
        factory_year = self.cleaned_data.get('factor_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros com ano de fabricação anterior a 1975')
        return factory_year
