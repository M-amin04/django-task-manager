from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = [
            ('todo', 'To Do', 'secondary'),
            ('doing', 'Doing', 'warning'),
            ('done', 'Done', 'success'),
        ]
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status']
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task_list')