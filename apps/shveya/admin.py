from django.contrib import admin
from .models import Party, Material


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ("id", "batch_number", "design", "created_at")
    search_fields = ("batch_number", "design")
    ordering = ("-created_at",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "party",
        "color",
        "quantity_line",
        "tshirt_count",
        "four_x_count",
        "raspash_count",
        "beika_count",
        "strochka_count",
        "gorlo_count",
        "ytyg_count",
        "otk_count",
        "ypakovka_count",
    )

    list_display_links = ("id", "party", "color")

    list_filter = (
        "party",
        "color",
    )

    search_fields = (
        "party__batch_number",
        "color",
    )

    ordering = ("-id",)

