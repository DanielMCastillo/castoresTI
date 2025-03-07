from django import forms
from .models import Producto, SalidaProducto, MovimientoProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion": forms.Textarea(attrs={'class': 'form-control'}),
            "cantidad": forms.NumberInput(attrs={'class': 'form-control'}),
            "estatus": forms.Select(attrs={'class': 'form-control'}),
            
        }
class SalidaProductoForm(forms.ModelForm):
    class Meta:
        model = SalidaProducto
        fields = ['producto', 'cantidad_salida']  # Solo los campos relevantes
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_salida': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad_salida(self):
        cantidad_salida = self.cleaned_data.get('cantidad_salida')
        producto = self.cleaned_data.get('producto')

        if cantidad_salida > producto.cantidad:
            raise forms.ValidationError(
                f"No puedes retirar {cantidad_salida} unidades. Solo hay {producto.cantidad} disponibles."
            )
        return cantidad_salida
    
class MovimientoProductoForm(forms.ModelForm):
    class Meta:
        model = MovimientoProducto
        fields = ['producto', 'tipo_movimiento', 'cantidad']

    # No es necesario configurar el 'realizado_por' aquí. Lo haremos en la vista.