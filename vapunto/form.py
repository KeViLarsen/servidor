from datetime import datetime

from django.forms import *

from core.erp.models import Category, Product, Supplier, Client, Expenses, Sale, Buy


# CATEGORIAS
class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs[
                'class'] = 'form-control'  # esta clase form control muestra la casilla  para completar alargada
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # con esto ya  no aparece el autocompletar al agregar uno nuevo

    class Meta:
        model = Category  # thay que importar el modelo
        fields = '__all__'  # estas son las columanas que se van a presentar en mi formulario
        # si quiero mandar las columnas en un  orden especifico hay que poner entre corchetes: ['...','...']
        # tambien se puede hacer una exclusion de que  campos no quiero = exclude ['...', '...']
        widgets = {  # esta propiedad me permite personalizar mis componentes
            'name': TextInput(
                attrs={  # estos son atributos que le podemos agregar a nuestro  componente
                    'placeholder': 'Ingrese una categoria',  # la leyenda que tiene el componente
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

        exclude = ['user_update', 'user_creation', 'user_delete']

    # save es un metodo de los formularios y se puede sobreecribir
    def save(self, commit=True):
        data = {}  # variable que tiene el dicciionario
        form = super()  # recuperar el objeto (el formulario)
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# PRODUCTOS
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['autofocus'] = True
        for form in self.visible_fields():
            form.field.widget.attrs[
                'class'] = 'form-control'  # esta clase form control muestra la casilla  para completar alargada
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # con esto ya  no aparece el autocompletar al agregar uno nuevo

        self.fields['cate'].widget.attrs = {
            'autofocus': True,
            'class': 'form-control select2',
            'style': 'width: 100%'
        }

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'cate': Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%'
                }
            ),
        }

        exclude = ['user_update2', 'user_creation2']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# PROVEEDOR
class SupplierForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['names'].widget.attrs['autofocus'] = True

        for form in self.visible_fields():
            form.field.widget.attrs[
                'class'] = 'form-control'  # esta clase form control muestra la casilla  para completar alargada
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # con esto ya  no aparece el autocompletar al agregar uno nuevo

    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido',
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de teléfono',
                }
            ),
            'address': Textarea(
                attrs={
                    'placeholder': 'Ingrese la dirección',
                    'rows': 3,
                    'cols': 3,
                }
            ),
        }

        exclude = ['user_update3', 'user_creation3']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# CLIENTES
class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs[
                'class'] = 'form-control'  # esta clase form control muestra la casilla  para completar alargada
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # con esto ya  no aparece el autocompletar al agregar uno nuevo

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su CI',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_update4', 'user_creation4']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# GASTOS
class ExpensesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['names'].widget.attrs['autofocus'] = True

        for form in self.visible_fields():
            form.field.widget.attrs[
                'class'] = 'form-control'  # esta clase form control muestra la casilla  para completar alargada
            form.field.widget.attrs[
                'autocomplete'] = 'off'  # con esto ya  no aparece el autocompletar al agregar uno nuevo

    class Meta:
        model = Expenses
        fields = '__all__'
        widgets = {
            'desc': TextInput(
                attrs={
                    'placeholder': 'Ingrese la razón del gasto',
                }
            ),
            'total': TextInput(
                attrs={
                    'placeholder': 'Ingrese el monto del gasto',
                }
            ),
            'date': TextInput(
                attrs={
                    'placeholder': 'Ingrese la fecha',
                }
            ),
        }

        exclude = ['user_update5', 'user_creation5']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


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


# COMPRAS
class BuyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        self.fields['prov'].widget.attrs = {
            'autofocus': True,
            'class': 'form-control select2',
            'style': 'width: 100%'
        }

    class Meta:
        model = Buy
        fields = '__all__'
        widgets = {
            'prov': Select(attrs={
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
            'iva': TextInput(attrs={
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


# TEST
class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
    # AJXA
    # search = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ingrese una descripción'
    # }))
    # SELECT2
    search = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
