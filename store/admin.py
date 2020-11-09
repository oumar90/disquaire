from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
# from django.contrib.contenttypes.models import ContentType
from .models import Booking, Contact, Artist, Album
# Register your models here.



# Affiche le model dans le panneau d'administration
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']
    fields = ['created_at', 'contact_link', 'album_link', 'contacted']
    readonly_fields = ['created_at', 'contact_link', 'album_link', 'contacted']

    def album_link(self, booking):
        path = "admin:store_album_change"
        url = reverse(path, args=(booking.album.id,))
        return mark_safe('<a href="{}">{}</a>'.format(url, booking.album.title))

    def contact_link(self, booking):
        path = "admin:store_contact_change"
        url = reverse(path, args=(booking.contact,))
        return mark_safe('<a href="{}">{}</a>'.format(url, booking.contact.name))

# Affiche les informations supplementaire dans le panneau d'administration
class BookingInline(admin.TabularInline):

    model = Booking
    extra = 0
    readonly_fields = ["created_at", "album_link", "contacted"]
    fields = ["created_at", "album_link", "contacted"]
   
    # Change Booking en Réservation ou Réservations
    verbose_name = 'Réservation'
    verbose_name_plural = 'Réservations'


    def album_link(self, booking):
        path = "admin:store_album_change"
        url = reverse(path, args=(booking.album,))
        return mark_safe('<a href="{}">{}</a>'.format(url, booking.album.title))

    album_link.short_description = "Album"

# Affiche le model dans le panneau d'administration
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]



# Affiche le model dans le panneau d'administration
class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = 'Disque'
    verbose_name_plural = 'Disques'

# Affiche le model dans le panneau d'administration
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline]

# Affiche le model dans le panneau d'administration
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']