from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from aplicacion.models import Producto, Proveedor, Tienda

class FormProducto(forms.ModelForm):
    fecha_caducidad = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha de caducidad'
    )

    class Meta:
        model = Producto
        fields = '__all__'

    def clean_fecha_caducidad(self):
        fecha_caducidad = self.cleaned_data.get('fecha_caducidad')
        if fecha_caducidad and fecha_caducidad < date.today():
            raise ValidationError("La fecha de salida no puede ser en el pasado.") #este codigo es para el tema de los validores
        return fecha_caducidad


class FormProveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields= '__all__'



class FormTienda(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'