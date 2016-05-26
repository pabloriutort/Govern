from django import forms
from .models import *
from functools import partial

ESTAT = (
    ('PE','Pendent'),
    ('PR','Progres'),
    ('RE','Rebutjat'),
    ('FI','Finalitzat'),
)

TIPUS = (
    ('F2P','Free To Play'),
    ('CO','Convencional'),
    ('ALT','Altres'),
)

# El Datepicker s'activa al template mitjansant un script de jQuery
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PrincipiForm(forms.Form):
	principi = forms.CharField(max_length=100)

class PrincipiEditForm(forms.Form):

	# Cream __init__ per poder passar-li arguments al model del formulari
	def __init__(self, *args, **kwargs):
		# Aquest if es un truco que he hagut de fer ja que quan enviaves el formulari, com no li pass sa id petava 
		if 'principi_id' in kwargs:
			self.principi_id = kwargs.pop('principi_id')
		super(PrincipiEditForm, self).__init__(*args, **kwargs)
		if hasattr(self, 'principi_id'):
			principi = Principi.objects.get(id=self.principi_id)
			# Id's dels objectius actuals
			objectiusActuals = principi.objectiu.all().values_list('id', flat=True)
			# Cream els inputs
			self.fields['Objectius'] = forms.ModelMultipleChoiceField(queryset=principi.objectiu.all())
			self.fields['Restants'] = forms.ModelMultipleChoiceField(queryset=Objectiu.objects.all().exclude(id__in=objectiusActuals))
		self.fields['principi_id'] = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
		self.fields['principi'] = forms.CharField(max_length=100)

class ObjectiuForm(forms.Form):
	objectiu = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	principis = forms.ModelMultipleChoiceField(queryset=Principi.objects.all())

class ObjectiuEditForm(forms.Form):

	# Cream __init__ per poder passar-li arguments al model del formulari
	def __init__(self, *args, **kwargs):
		# Aquest if es un truco que he hagut de fer ja que quan enviaves el formulari, com no li pass sa id petava 
		if 'objectiu_id' in kwargs:
			self.objectiu_id = kwargs.pop('objectiu_id')
		super(ObjectiuEditForm, self).__init__(*args, **kwargs)
		if hasattr(self, 'objectiu_id'):
			objectiu = Objectiu.objects.get(id=self.objectiu_id)
			# Id's dels principis i metriques actuals
			principisActuals = objectiu.principis_objectius.all().values_list('id', flat=True)
			metriquesActuals = Metrica.objects.filter(objectiu_id=self.objectiu_id)
			# Cream els inputs
			self.fields['Principis'] = forms.ModelMultipleChoiceField(queryset=objectiu.principis_objectius.all())
			self.fields['Principis_Restants'] = forms.ModelMultipleChoiceField(queryset=Principi.objects.all().exclude(id__in=principisActuals))
			self.fields['Metriques'] = forms.ModelMultipleChoiceField(queryset=Metrica.objects.filter(objectiu_id=self.objectiu_id))

		self.fields['objectiu_id'] = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
		self.fields['objectiu'] = forms.CharField(max_length=100)
		self.fields['descripcio'] = forms.CharField(widget=forms.Textarea)

class ProjecteForm(forms.Form):
	projecte = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	presupost = forms.IntegerField()
	estat = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=ESTAT)
	tipus = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=TIPUS)
	data_inici = forms.DateField(widget=DateInput())
	data_fi = forms.DateField(widget=DateInput())
	objectius = forms.ModelMultipleChoiceField(queryset=Objectiu.objects.all())
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()

class ProjecteEditForm(forms.Form):
	projecte_id = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
	projecte = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	presupost = forms.IntegerField()
	estat = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=ESTAT)
	tipus = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=TIPUS)
	data_inici = forms.DateField(widget=DateInput())
	data_fi = forms.DateField(widget=DateInput())
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()

class MetricaForm(forms.Form):
	metrica = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	unitat = forms.CharField(max_length=100)
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()
	objectiu = forms.ModelChoiceField(queryset=Objectiu.objects.all(), empty_label=None)

class MetricaEditForm(forms.Form):
	metrica_id = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
	metrica = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	unitat = forms.CharField(max_length=100)
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()