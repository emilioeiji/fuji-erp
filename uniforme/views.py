from django.shortcuts import redirect, render

from .forms import ItemSolicitacaoFormSet, SolicitacaoUniformeForm


def solicitar_uniformes(request):
    if request.method == 'POST':
        form = SolicitacaoUniformeForm(request.POST)
        formset = ItemSolicitacaoFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.usuario = request.user
            solicitacao.save()

            instances = formset.save(commit=False)
            for instance in instances:
                instance.solicitacao = solicitacao
                instance.save()

            # Redireciona para uma página de sucesso
            return redirect('sucesso')
    else:
        form = SolicitacaoUniformeForm()
        formset = ItemSolicitacaoFormSet()

    return render(request, 'uniforme/solicitar_uniformes.html', {'form': form, 'formset': formset})
