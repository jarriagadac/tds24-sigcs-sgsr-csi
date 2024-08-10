# from django.forms import DateInput, ModelForm

# from .models import Movimiento, Lote


# class CreateMovimiento(ModelForm):
#     """Form to create a new movement."""

#     class Meta:
#         model = Movimiento
#         fields = ["institucion", "lote", "fecha"]
#         widgets = {
#             "fecha": DateInput(attrs={"type": "date"}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(CreateMovimiento, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs = {"class": "form-control"}

#         if self.fields.get("lote"):
#             self.fields["lote"].queryset = Lote.objects.filter(has_transfer=False)
