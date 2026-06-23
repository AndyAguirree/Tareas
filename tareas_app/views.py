from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from .forms import TareaForm
from .models import Tarea, Prioridad


class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'

    context_object_name = 'tareas'
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset().select_related('prioridad').prefetch_related('etiquetas')
        q = self.request.GET.get('q', '').strip()
        prioridad_id = self.request.GET.get('prioridad', '').strip()

        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(descripcion__icontains=q))
        if prioridad_id:
            qs = qs.filter(prioridad_id=prioridad_id)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['prioridades'] = Prioridad.objects.all()
        ctx['q'] = self.request.GET.get('q', '')
        ctx['prioridad'] = self.request.GET.get('prioridad', '')
        return ctx


class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:tarea_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Crear tarea'
        return ctx


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:tarea_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Editar tarea'
        return ctx


class IsStaffOrSuperUser(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return u.is_authenticated and (u.is_staff or u.is_superuser)


class TareaDeleteView(IsStaffOrSuperUser, DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:tarea_list')

