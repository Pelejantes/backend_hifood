from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Usuario, EnderecoEntrega, Endereco
from ..serializers import Usuario_Serializer, Endereco_Serializer, EnderecoEntrega_Serializer, CodVerif
from utils.func_gerais import gerar_code, listarErros, serializersValidos
import time


def exibir_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = Usuario_Serializer(usuarios, many=True)
    return Response(serializer.data)


def exibir_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        enderecoEntrega = EnderecoEntrega.objects.get(usuarioId=pk)
        endereco = Endereco.objects.get(enderecoId=enderecoEntrega.enderecoId)
        usuario_serializer = Usuario_Serializer(usuario, many=False)
        endereco_serializer = Endereco_Serializer(endereco, many=False)
        response = {
            "usuario": usuario_serializer,
            "endereco": endereco_serializer
        }
        return Response(response)
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def criar_usuarioCompleto(request):
    usuarioSerializer = Usuario_Serializer(data=request.data['usuario'])
    serializers = [usuarioSerializer]
    enderecos_serializers = []
    for endereco in request.data['enderecos']:
        serializers.append(Endereco_Serializer(data=endereco))
        enderecos_serializers.append(Endereco_Serializer(data=endereco))

    if serializersValidos(serializers):
        # ----Criar Table Usuario
        usuarioInstancia = usuarioSerializer.save()
        usuarioId = usuarioInstancia.__dict__['usuarioId']

        # ----Criar Table Endereco
        for serializer in enderecos_serializers:
            if serializer.is_valid():
                enderecoInstancia = serializer.save()
                enderecoId = enderecoInstancia.__dict__['enderecoId']
            # ----Criar Table Endereco Entrega
            enderecoEntregaData = {
                "usuarioId": usuarioId,
                "enderecoId": enderecoId
            }
            enderecoEntregaSerializer = EnderecoEntrega_Serializer(
                data=enderecoEntregaData)
            
            if enderecoEntregaSerializer.is_valid():
                enderecoEntregaSerializer.save()
        return Response({"message": "Usuário Completo criado com sucesso!"}, status=200)
    else:
        error_messages = listarErros(serializers)
        return Response({"message": "Não foi possível criar o usuário.", "errors": error_messages}, status=400)


def criar_usuario(request):
    serializer = Usuario_Serializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        usuario = serializer.save()
        return Response({"message": "Usuário criado com sucesso!", "usuarioId": usuario.__dict__['usuarioId']}, status=200)
    else:
        return Response({"message": "Não foi possível criar o usuário, revise os campos e tente novamente!"}, status=404)


def inativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 1:
            usuario.statusAtivo = 0
            usuario.save()
            return Response({"message": f"Usuário {pk} inativado com sucesso!"})
        else:
            return Response({"message": f"Usuário {pk} já estava inativado!"})
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def ativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 0:
            usuario.statusAtivo = 1
            usuario.save()
            return Response({"message": f"Usuário {pk} ativado com sucesso!"})
        else:
            return Response({"message": f"Usuário {pk} já estava ativado!"})
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def editar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        enderecoEntrega = EnderecoEntrega.objects.get(usuarioId=pk)
        endereco = Endereco.objects.get(enderecoId=enderecoEntrega.enderecoId)
        serializer = Usuario_Serializer(instance=usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Usuário {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def deletar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response({"message": f"Usuário {pk} deletado com sucesso!"}, status=200)
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)
