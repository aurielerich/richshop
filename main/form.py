from django import forms
from .models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        """
        Konfigurasi utama untuk ProductForm.
        Menghubungkan form dengan model Product dan mendefinisikan field yang akan digunakan.
        """
        model = Product
        fields = [
            "name", 
            "price", 
            "description", 
            "thumbnail",
            "category",
            "is_featured"
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500',
                'placeholder': 'Contoh: Jersey Real Madrid 2024/25'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500',
                'placeholder': 'Masukkan harga tanpa titik, contoh: 500000'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500',
                'placeholder': 'Jelaskan detail produk Anda di sini...',
                'rows': 4
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500',
                'placeholder': 'https://example.com/gambar.jpg'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-green-600 border-gray-300 rounded focus:ring-green-500'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            return strip_tags(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            return strip_tags(description)
        return description