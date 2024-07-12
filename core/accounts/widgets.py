from django import forms

class MultiSelectWithCheckboxes(forms.SelectMultiple):
    template_name = 'widgets/multi_select_with_checkboxes.html'

    class Media:
        css = {
            'all': ('css/multi_select_with_checkboxes.css',)
        }
        js = ('js/multi_select_with_checkboxes.js',)
