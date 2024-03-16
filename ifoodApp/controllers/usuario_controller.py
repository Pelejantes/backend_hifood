from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Usuario, EnderecoEntrega, Endereco
from ..serializers import Usuario_Serializer, Endereco_Serializer, EnderecoEntrega_Serializer, CodVerif
from utils.func_gerais import gerar_code


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
            "usuario":usuario_serializer,
            "endereco":endereco_serializer
        }
        return Response(response)
    except Usuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)


def criar_usuarioCompleto(request):
    request.data ['usuario']['codVerif'] = gerar_code(6)
    usuarioSerializer = Usuario_Serializer(data=request.data['usuario'])
    enderecoSerializer = Endereco_Serializer(data=request.data['endereco'])

    # print(request.data['usuario'])
    # print(request.data['endereco'])
    print(request.data)
    dados_validos = True
    for serializer in [usuarioSerializer, enderecoSerializer]:
        if not serializer.is_valid():
            dados_validos = False
            break
    # print("dados_validos == True ",dados_validos)
    if dados_validos == True:
        # Criar tabelas individuais
        # ----Criar Table Usuario
        usuarioInstancia = usuarioSerializer.save()
        usuarioId = usuarioInstancia.__dict__['usuarioId']
        # Retornar ID (individual - instancia)

        # ----Criar Table Endereco
        enderecoInstancia = enderecoSerializer.save()
        enderecoId = enderecoInstancia.__dict__['enderecoId']
        # Retornar ID (individual - instancia)

        # print("Chegou aqui!!!") 
        # ----Criar Table Endereco Entrega
        enderecoEntregaData = {
            "usuarioId": usuarioId,
            "enderecoId": enderecoId
        }
        enderecoEntregaSerializer = EnderecoEntrega_Serializer(
            data=enderecoEntregaData)

        print(f"request: {request.data}")
        if enderecoEntregaSerializer.is_valid():
            enderecoEntregaSerializer.save()

        return Response({"message": "Usuário Completo criado com sucesso!"}, status=200)
    else:
        return Response({"message": "Não foi possível criar o usuário Completo, revise os campos e tente novamente!"}, status=404)


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
