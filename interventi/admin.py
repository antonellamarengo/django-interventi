from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
    Fornitore, Intervento, InterventoAllegato, InterventoCommento, PuntoVendita,
    Preventivo, PreventivoAllegato, Scadenza, ScadenzaAllegato,
    StatoInterventoCliente, StatoInterventoInterno, TipoIntervento,
)


class InterventoAllegatoInline(admin.TabularInline):
    model = InterventoAllegato
    verbose_name_plural = 'File Allegati'
    extra = 0


class InterventoCommentoInline(admin.TabularInline):
    model = InterventoCommento
    verbose_name_plural = 'Commenti'
    extra = 0


class PreventivoInline(admin.TabularInline):
    model = Preventivo
    verbose_name_plural = 'preventivi'
    extra = 0
    show_change_link = True
    fieldsets = (
        (None, {
            'fields': (
                'fornitore', 'numero', 'is_confermato', 'importo',
                'data_inizio_lavori', 'data_fine_lavori',
            )
        }),
    )


class PreventivoAllegatoInline(admin.TabularInline):
    model = PreventivoAllegato
    verbose_name_plural = 'allegati'
    extra = 0


class ScadenzaAllegatoInline(admin.TabularInline):
    model = ScadenzaAllegato
    verbose_name_plural = 'allegati'
    extra = 0


class FornitoreAdmin(admin.ModelAdmin):
    """
    Custom Fornitore admin class
    """
    list_display = (
        'nome', 'tipo_servizio_offerto', 'citta', 'referente', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'citta', 'referente',
    )
    search_fields = (
        'nome', 'citta', 'referente',
    )


class InterventoAdmin(admin.ModelAdmin):
    """
    Custom Intervento admin class
    """
    inlines = (
        InterventoAllegatoInline, PreventivoInline, InterventoCommentoInline,
    )
    readonly_fields = (
        'data_inserimento', 'data_ultima_modifica',
    )
    list_display = (
        'titolo', 'tipo_intervento', 'urgente', 'punto_vendita', 'segnalatore',
        'data_inserimento', 'data_ultima_modifica',
        'stato_cliente', 'stato_interno',
    )
    ordering = (
        '-urgente', '-data_inserimento',
    )
    list_filter = (
        ('tipo_intervento', admin.RelatedOnlyFieldListFilter),
        'urgente',
        ('punto_vendita', admin.RelatedOnlyFieldListFilter),
        ('stato_cliente', admin.RelatedOnlyFieldListFilter),
        ('stato_interno', admin.RelatedOnlyFieldListFilter),
        'data_inserimento', 'data_ultima_modifica',
        'segnalatore',
    )
    search_fields = (
        'titolo', 'segnalatore',
    )


class InterventoAllegatoAdmin(admin.ModelAdmin):
    """
    Custom InterventoAllegato admin class
    """
    list_display = (
        'file_name', 'file_size_kb', 'data_inserimento',
        'titolo_intervento', 'punto_vendita_intervento',
    )
    ordering = (
        '-data_inserimento',
    )
    list_filter = (
        'data_inserimento',
        ('intervento__punto_vendita', admin.RelatedOnlyFieldListFilter),
        ('intervento', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        'file',
    )

    def titolo_intervento(self, obj):
        return obj.intervento.titolo

    def punto_vendita_intervento(self, obj):
        return obj.intervento.punto_vendita


class InterventoCommentoAdmin(admin.ModelAdmin):
    """
    Custom InterventoCommento admin class
    """
    list_display = (
        'data_inserimento', 'utente',
        'titolo_intervento', 'punto_vendita_intervento',
    )
    ordering = (
        '-data_inserimento',
    )
    list_filter = (
        'data_inserimento',
        ('intervento__punto_vendita', admin.RelatedOnlyFieldListFilter),
        ('intervento', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        'testo',
    )

    def titolo_intervento(self, obj):
        return obj.intervento.titolo

    def punto_vendita_intervento(self, obj):
        return obj.intervento.punto_vendita


class PreventivoAdmin(admin.ModelAdmin):
    inlines = (PreventivoAllegatoInline,)


class PuntoVenditaAdmin(admin.ModelAdmin):
    """
    Custom PuntoVendita admin class
    """
    list_display = (
        'nome', 'citta', 'regione', 'responsabile', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'regione', 'citta', 'responsabile',
    )
    search_fields = (
        'nome', 'regione', 'citta', 'responsabile',
    )


class ScadenzaAdmin(admin.ModelAdmin):
    """
    Custom Scadenza admin class
    """
    inlines = (ScadenzaAllegatoInline,)
    list_display = (
        'descrizione', 'data_scadenza', 'gestita',
        'punto_vendita', 'fornitore',
    )
    ordering = (
        'gestita', 'data_scadenza',
    )
    list_filter = (
        'gestita',
        'data_scadenza',
        ('punto_vendita', admin.RelatedOnlyFieldListFilter),
        ('fornitore', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        'descrizione', 'annotazioni',
    )


class StatoInterventoClienteAdmin(admin.ModelAdmin):
    """
    Custom StatoInterventoCliente admin class
    """
    ordering = ('ordine', 'descrizione')
    search_fields = ('descrizione',)


class StatoInterventoInternoAdmin(admin.ModelAdmin):
    """
    Custom StatoInterventoInterno admin class
    """
    ordering = ('ordine', 'descrizione')
    search_fields = ('descrizione',)


class TipoInterventoAdmin(admin.ModelAdmin):
    """
    Custom TipoInterventoCliente admin class
    """
    ordering = ('ordine', 'descrizione')
    search_fields = ('descrizione',)


admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(Intervento, InterventoAdmin)
admin.site.register(InterventoAllegato, InterventoAllegatoAdmin)
admin.site.register(InterventoCommento, InterventoCommentoAdmin)
admin.site.register(Preventivo, PreventivoAdmin)
admin.site.register(PuntoVendita, PuntoVenditaAdmin)
admin.site.register(Scadenza, ScadenzaAdmin)
admin.site.register(StatoInterventoCliente, StatoInterventoClienteAdmin)
admin.site.register(StatoInterventoInterno, StatoInterventoInternoAdmin)
admin.site.register(TipoIntervento, TipoInterventoAdmin)
