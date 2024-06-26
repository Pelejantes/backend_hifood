from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Usuario, EnderecoEntrega, Endereco
from ..serializers import Usuario_Serializer, Endereco_Serializer, EnderecoEntrega_Serializer, CodVerif
from utils.func_gerais import gerar_code, listarErros, serializersValidos
from rest_framework.serializers import ValidationError
import time


def exibir_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = Usuario_Serializer(usuarios, many=True)
    return Response(serializer.data)


def exibir_usuario_por_telefone(request, pk):
    try:
        usuario = Usuario.objects.get(telefoneUsu=pk)
        usuario_serializer = Usuario_Serializer(usuario, many=False)
        return Response(usuario_serializer.data)
    except Usuario.DoesNotExist:
        return Response({"mensagem": f"Usuário de telefone {pk} não encontrado"}, status=404)


def exibir_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        usuario_serializer = Usuario_Serializer(usuario, many=False)
        return Response(usuario_serializer.data)
    except Usuario.DoesNotExist:
        return Response({"mensagem": f"Usuário de id {pk} não encontrado"}, status=404)


def criar_usuarioCompleto(request):
    try:
        enderecos_serializers = []
        if not 'usuario' in request.data:
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": ["Campo 'usuario' ausente."]}, status=400)
        usuario_serializer = Usuario_Serializer(data=request.data['usuario'])
        serializers = [usuario_serializer]
        if not 'enderecos' in request.data:
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": ["Liste de endereços pendente."]}, status=400)
        if len(request.data.get('enderecos', [])) == 0:
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": ["Nenhum endereço registrado."]}, status=400)
        for endereco in request.data['enderecos']:
            serializers.append(Endereco_Serializer(data=endereco))
            enderecos_serializers.append(Endereco_Serializer(data=endereco))

        if serializersValidos(serializers):
            # ----Criar Table Usuario
            usuarioInstancia = usuario_serializer.save()
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
            return Response({"mensagem": "Usuário Completo criado com sucesso!"}, status=200)
        else:
            error_messages = listarErros(serializers)
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": error_messages}, status=400)
    except ValidationError as e:
        error_messages = e.messages
        return Response({"mensagem": "Não foi possível criar o usuário.", "errors": error_messages}, status=400)


def criar_usuario(data):
    serializer = Usuario_Serializer(data=data)
    if serializer.is_valid():
        usuario = serializer.save()
        return Response({"mensagem": "Usuário criado com sucesso!", "usuarioId": usuario.__dict__['usuarioId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o usuário, revise os campos e tente novamente!", "errors": error_messages}, status=404)


def inativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 1:
            usuario.statusAtivo = 0
            usuario.save()
            return Response({"mensagem": f"Usuário {pk} inativado com sucesso!"})
        else:
            return Response({"mensagem": f"Usuário {pk} já estava inativado!"})
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Usuário {pk} não encontrado"}, status=404)


def ativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 0:
            usuario.statusAtivo = 1
            usuario.save()
            return Response({"mensagem": f"Usuário {pk} ativado com sucesso!"})
        else:
            return Response({"mensagem": f"Usuário {pk} já estava ativado!"})
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Usuário {pk} não encontrado"}, status=404)


def editar_usuarioCompleto(request, pk):
    try:
        if not 'usuario' in request.data:
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": ["Campo 'usuario' ausente."]}, status=400)
        if not 'enderecos' in request.data:
            return Response({"mensagem": "Não foi possível criar o usuário.", "errors": ["Campo 'enderecos' ausente."]}, status=400)
        usuario_model = Usuario.objects.get(usuarioId=pk)
        usuario_Serializer = Usuario_Serializer(
            instance=usuario_model, data=request.data['usuario'])
        if usuario_Serializer.is_valid():
            usuario_Serializer.save()

        for endereco in request.data['enderecos']:
            endereco_model = Endereco.objects.get(
                enderecoId=endereco['enderecoId'])
            endereco_Serializer = Endereco_Serializer(
                instance=endereco_model, data=endereco)
            if endereco_Serializer.is_valid():
                endereco_Serializer.save()
        return Response({"mensagem": f"Usuário {pk} atualizado com sucesso.", f"reserva{pk}": usuario_Serializer.data})

    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        error_messages = listarErros([usuario_Serializer])
        return Response({"mensagem": f"Usuário {pk} não encontrado", "errors": error_messages}, status=404)


def editar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        serializer = Usuario_Serializer(instance=usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Usuário {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def deletar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response({"mensagem": f"Usuário {pk} deletado com sucesso!"}, status=200)
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Usuário {pk} não encontrado"}, status=404)
