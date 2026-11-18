from views import janela_view
from controllers import cliente_controller, fila_controller, servico_controller

cliente_controller.iniciar()
fila_controller.iniciar()
servico_controller.iniciar()

janela_view.janela.mainloop()
