from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido 

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.RepositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):

        candidatoActual=Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula=infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion "]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)
    #Borra por cedula
    def delete(self,id):
        return self.repositorioCandidato.delete(id)

        """
    Relación candidato y partido
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)