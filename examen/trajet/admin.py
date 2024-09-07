from django.contrib import admin

from .models import Conducteur, Client, ClientSpecial, Trajet, TrRegulier, TrSpecial, TrajectEffect, Reservation, Troncon

# Register your models here.

class TronconAdmin(admin.ModelAdmin):
    list_display = ('villeDep', 'villeDest', 'distance', 'prix')

class TrajetAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')
    filter_horizontal = ('troncons',)

class TrajectEffectAdmin(admin.ModelAdmin):
    list_display = ('effectTrajet', 'dateDepart', 'conducteur', 'trajet')
    list_filter = ('dateDepart', 'conducteur')
    search_fields = ('effectTrajet',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'trajectEffect', 'dateReserve')
    list_filter = ('dateReserve',)
    search_fields = ('client__nom', 'trajectEffect__effectTrajet')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone')
    search_fields = ('nom', 'prenom')

class ConducteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'matricule')
    search_fields = ('matricule', 'nom')

admin.site.register(Conducteur, ConducteurAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientSpecial, ClientAdmin)  # Use the same admin as Client for simplicity
admin.site.register(Trajet, TrajetAdmin)
admin.site.register(TrRegulier, TrajetAdmin)  # Use the same admin as Trajet for simplicity
admin.site.register(TrSpecial, TrajetAdmin)   # Use the same admin as Trajet for simplicity
admin.site.register(TrajectEffect, TrajectEffectAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Troncon, TronconAdmin)
