from django.shortcuts import render, redirect
from tauschboerse.models import Gegenstand
from tauschboerse.forms import GegenstandForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from guardian.shortcuts import assign_perm
from guardian.mixins import PermissionRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


class GegenstandCreate(LoginRequiredMixin, CreateView):
    model = Gegenstand
    template_name_suffix = "_create_form"
    fields = ["title", "description", "image", "status", "is_draft"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(gegenstand_detail, kwargs={'pk':self.object.pk})


class GegenstandUpdate(PermissionRequiredMixin, UpdateView):
    model = Gegenstand
    template_name_suffix = "_update_form"
    fields = ["title", "description", "image", "status", "is_draft"]
    permission_required = "change_gegenstand"
    def get_success_url(self):
        return reverse(gegenstand_detail, kwargs={'pk':self.object.pk})


class GegenstandDelete(PermissionRequiredMixin, DeleteView):
    model = Gegenstand
    template_name_suffix = "_check_delete"
    permission_required = "delete_gegenstand"
    return_403 = True
    def get_success_url(self):
        return reverse(gegenstaende_index)


@login_required
def gegenstand_create(request):
    if request.method == 'GET':
        context = {
            "form": GegenstandForm
        }
        return render(request, 'tauschboerse/gegenstand_create_form.html', context)
    elif request.method == 'POST':
        form = GegenstandForm(request.POST, request.FILES)
        if form.is_valid():
            gegenstand = form.save()
            return redirect(gegenstaende_index)


def gegenstaende_index(request):
    gegenstaende = Gegenstand.objects.filter(is_draft=False)
    context = {
        "gegenstaende": gegenstaende
        }
    return render(request, "gegenstaende_index.html", context)


def gegenstaende_user(request, user_name):
    gegenstaende = Gegenstand.objects.filter(user__username__contains=user_name, is_draft=False)
    context = {
        "gegenstaende": gegenstaende
        }
    return render(request, "gegenstaende_index.html", context)

def gegenstand_detail(request, pk): #pk = primary key
    gegenstand = Gegenstand.objects.get(pk=pk)
    context = {
        "gegenstand": gegenstand
        }
    return render(request, "gegenstand_detail.html", context)




@receiver(post_save, sender=Gegenstand)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_gegenstand",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )
    assign_perm(
        "delete_gegenstand",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )