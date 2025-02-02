from django.contrib import admin
from .models import Category, Product, Commande
# Register your models here.
admin.site.site_header = "Commerce en Ligne"
admin.site.site_title = "Sarti-Shop"
admin.site.index_title = "Gestion des Produits"
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    search_fields = ('name',)

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'total', 'date_commande')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)

