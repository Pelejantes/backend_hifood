from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import EnderecoEntrega, Endereco
from ..serializers import EnderecoEntrega_Serializer, Endereco_Serializer
from utils.func_gerais import gerar_code, listarErros, serializersValidos


def exibir_enderecosEntrega(request):
    enderecosEntrega_model = EnderecoEntrega.objects.all()
    enderecosEntrega = []
    for enderecoEntrega_model in enderecosEntrega_model:
        enderecoEntrega = EnderecoEntrega_Serializer(
            enderecoEntrega_model).data
        enderecosEntrega.append(enderecoEntrega)
    return Response(enderecosEntrega)


def exibir_enderecosUsuario(request, pk):
    # pk == usuarioId
    enderecos = []
    enderecoEntregaModel = EnderecoEntrega.objects.filter(usuarioId=pk)
    for enderecoEntrega in enderecoEntregaModel:
        enderecoEntregaId = enderecoEntrega.enderecoEntregaId
        enderecoId = enderecoEntrega.enderecoId.enderecoId
        enderecoModel = Endereco.objects.get(enderecoId=enderecoId)
        endereco = Endereco_Serializer(enderecoModel).data
        endereco['enderecoEntregaId'] = enderecoEntregaId
        enderecos.append(endereco)
    return Response(enderecos)


# def exibir_enderecoEntrega(request, pk):
#     try:
#         todosEnderecosEntrega = EnderecoEntrega.objects.filter(usuarioId=pk)
#         response = []
#         # Puxar todos os enderecoId's
#         for enderecoEntrega in todosEnderecosEntrega:
#             enderecoId = EnderecoEntrega_Serializer(
#                 enderecoEntrega).data['enderecoId']
#             # Puxar endereço por seu id
#             endereco = Endereco.objects.get(enderecoId=enderecoId)
#             # Adicionar á lista do response
#             response.append(Endereco_Serializer(endereco).data)
#         return Response({"mensagem": response}, status=200)
#     except EnderecoEntrega.DoesNotExist:
#         return Response({"mensagem": f"enderecoEntrega {pk} não encontrado"}, status=404)


def criar_enderecoUsuario(request, pk):
    # pk == id_usuario
    enderecoSerializer = Endereco_Serializer(data=request.data)
    if serializersValidos([enderecoSerializer]):
        endereco = enderecoSerializer.save()
        enderecoEntrega = {
            'usuarioId': pk,
            'enderecoId': endereco.__dict__['enderecoId']
        }
        enderecoEntregaSerializer = EnderecoEntrega_Serializer(
            data=enderecoEntrega)
        if serializersValidos([enderecoEntregaSerializer]):
            enderecoEntrega = enderecoEntregaSerializer.save()
            return Response({"mensagem": f"Endereço do usuario id_{pk} criado com sucesso!", "enderecoEntregaId": enderecoEntrega.__dict__['enderecoEntregaId']}, status=200)
        else:
            error_messages = listarErros([enderecoEntregaSerializer])
            return Response({"mensagem": "Não foi possível criar o endereço.", "errors": error_messages}, status=400)

    else:
        error_messages = listarErros([enderecoSerializer])
        return Response({"mensagem": "Não foi possível criar o endereço.", "errors": error_messages}, status=400)


# def criar_enderecoEntrega(request):
#     serializer = EnderecoEntrega_Serializer(data=request.data)
#     if serializer.is_valid():
#         enderecoEntrega = serializer.save()
#         return Response({"mensagem": "enderecoEntrega criado com sucesso!", "enderecoId": enderecoEntrega.__dict__['enderecoEntregaId']}, status=200)
#     else:
#         error_messages = listarErros([serializer])
#         return Response({"mensagem": "Não foi possível criar o endereço, revise os campos e tente novamente!", "errors": error_messages}, status=400)


def editar_enderecoEntrega(request, pk):
    try:
        enderecos = request.data['enderecos']
        for endereco in enderecos:
            # Puxar endereço especifico por seu id
            endereco_model = Endereco.objects.get(
                enderecoId=endereco['enderecoId'])
            # Instanciar serializador do model
            endereco_Serializer = Endereco_Serializer(
                instance=endereco_model, data=endereco)
            # Validar dados e armazenar
            if serializersValidos([endereco_Serializer]):
                endereco_Serializer.save()
        return Response({"mensagem": f"Endereço(s) do usuario {pk} alterados."}, status=200)
    except EnderecoEntrega.DoesNotExist:
        error_messages = listarErros([endereco_Serializer])
        return Response({"mensagem": f"enderecoEntrega {pk} não encontrado", "errors": error_messages}, status=404)


def deletar_enderecoEntrega(request, pk):
    try:
        enderecoEntrega = EnderecoEntrega.objects.get(enderecoEntregaId=pk)
        enderecoEntrega.delete()
        endereco = Endereco.objects.get(enderecoId=pk)
        endereco.delete()
        return Response({"mensagem": f"enderecoEntrega {pk} deletado com sucesso!"}, status=200)
    except EnderecoEntrega.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"enderecoEntrega {pk} não encontrado"}, status=404)
