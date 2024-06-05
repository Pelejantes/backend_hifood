from rest_framework.response import Response
from ..models import Pedido, EtapaPedido
from ..serializers import Pedido_Serializer
from utils.func_gerais import listarErros, serializersValidos
from twilio.rest import Client
import os
from dotenv import load_dotenv
dotenv_path = "../../dotenv_files/.env"
load_dotenv(dotenv_path)


def exibir_pedidos(request):
    pedidos = Pedido.objects.all()
    serializer = Pedido_Serializer(pedidos, many=True)
    return Response(serializer.data)


def exibir_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        serializer = Pedido_Serializer(pedido, many=False)
        return Response(serializer.data)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Pedido {pk} não encontrado"}, status=404)


def criar_pedido(request):
    serializer = Pedido_Serializer(data=request.data)
    if serializer.is_valid():
        pedido = serializer.save()
        return Response({"mensagem": "Pedido criado com sucesso!", "pedidoId": pedido.__dict__['pedidoId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o pedido, revise os campos e tente novamente!", "erros": error_messages}, status=404)


def editar_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        serializer = Pedido_Serializer(instance=pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": f"Pedido {pk} atualizado com sucesso."})
        else:
            return Response({"mensagem": f"Não foi possível editar o pedido {pk}."})
    except Pedido.DoesNotExist:
        error_messages = listarErros([serializer])
        return Response({"mensagem": f"Pedido {pk} não encontrado", "errors": error_messages}, status=404)


def deletar_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        pedido.delete()
        return Response({"mensagem": f"Pedido {pk} deletado com sucesso!"}, status=200)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Pedido {pk} não encontrado"}, status=404)


# Por ID do Usuario
def exibir_pedidosUsuario(request):
    data = request.data
    data['usuarioId'] = request.usuario.usuarioId
    pedidosUsuario = Pedido.objects.filter(usuarioId=data['usuarioId'])
    serializer = Pedido_Serializer(pedidosUsuario, many=True)
    return Response(serializer.data)


def exibir_ultimoPedido(request):
    try:
        data = request.data
        data['usuarioId'] = request.usuario.usuarioId
        pedidoUsuario = Pedido.objects.filter(
            usuarioId=data['usuarioId']).last()
        serializer = Pedido_Serializer(pedidoUsuario, many=False)
        return Response(serializer.data)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Nenhum pedido encontrado"}, status=404)


def editar_ultimoPedido(request):
    try:
        economizar_recursos = bool(int(os.getenv('ECONOMIZAR_RECURSOS', True)))
        # Puxa telefone do request
        if request.usuario:
            telefoneUsu = request.usuario.telefoneUsu
        else:
            return Response({"mensagem": "Campo de telefone é obrigatório"}, status=404)
        data = request.data
        data['usuarioId'] = request.usuario.usuarioId
        pedido = Pedido.objects.filter(usuarioId=data['usuarioId']).last()
        ultimaEtapaRegistrada = pedido.etapaPedidoId.etapaPedidoId
        serializer = Pedido_Serializer(instance=pedido, data=data)
        if serializer.is_valid():
            serializer.save()
            # serializer.data.etapaPedidoId
            etapaPedido = EtapaPedido.objects.get(
                etapaPedidoId=serializer.data['etapaPedidoId'])
            # Fazer req para a API de Msg via Whatsapp
            nomeEtapaPedido = etapaPedido.etapaPedido
            if(ultimaEtapaRegistrada != serializer.data['etapaPedidoId']):
                try:
                    if (economizar_recursos == False):
                        account_sid = os.getenv('ACCOUNT_SID')
                        auth_token = os.getenv('AUTH_TOKEN')
                        client = Client(account_sid, auth_token)
                        client.messages.create(
                            from_=f"whatsapp:+{os.getenv('TEL_FROM')}",
                            body=f"Status do pedido H!Food:  *{nomeEtapaPedido}*",
                            to=f"whatsapp:+{telefoneUsu}")
                except AssertionError:
                    return Response({"mensagem": f"Não foi possível enviar mensagem ao usuario {data['usuarioId']}."}, status=404)
            return Response({"mensagem": f"Ultimo pedido do usuario {data['usuarioId']} atualizado com sucesso."})
        else:
            error_messages = listarErros([serializer])
            return Response({"mensagem": f"Não foi possível editar o ultimo pedido do usuario {data['usuarioId']}.", "errors": error_messages}, status=404)

    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Nenhum pedido encontrado"}, status=404)


def deletar_ultimoPedido(request):
    try:
        data = request.data
        data['usuarioId'] = request.usuario.usuarioId
        pedido = Pedido.objects.get(pedidoId=data['usuarioId'])
        pedido.delete()
        return Response({"mensagem": f"Ultimo pedido do usuario {data['usuarioId']} deletado com sucesso!"}, status=200)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Ultimo pedido do usuario {data['usuarioId']} não encontrado"}, status=404)
