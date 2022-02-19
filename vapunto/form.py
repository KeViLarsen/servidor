from datetime import datetime

from django.forms import *

from vapunto.models import Sale


# VENTAS
class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #
        # self.fields['cli'].widget.attrs['autofocus'] = True
        # self.fields['cli'].widget.attrs['class'] = 'form-control select2'
        # self.fields['cli'].widget.attrs['style'] = 'width: 100%'

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'pay': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'iva': TextInput(attrs={ #para que el iva sea de tipo texto
                'class': 'form-control',
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

