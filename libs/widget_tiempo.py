from libs.widget import widget


class widget_tiempo(widget):
    
    def __init__(self, nombre):
        """Constructor de clase Supervisor"""
        # Invoca al constructor de clase widget
        widget.__init__(self,  nombre)
    def view():
        return '<h3>tiempo molon</h3>'