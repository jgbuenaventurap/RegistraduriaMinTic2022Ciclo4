from Modelos.Resultado import Resultado 
from Modelos.Mesa import Mesa 
from Modelos.Candidato import Candidato 
from Repositorios.RepositorioResultado import RepositorioResultado 
from Repositorios.RepositorioMesa import RepositorioMesa 
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorInscripcion(): 

    def __init__(self): 
        self.repositorioResultado = RepositorioResultado() 
        self.repositorioMesa = RepositorioMesa() 
        self.repositorioCandiato = RepositorioCandidato() 

    def index(self): 
        return self.repositorioResultado.findAll() 

#Asignacion Mesa y Candidato a Resultado

    def create(self,infoResultado,id_candidato,id_mesa): 
        nuevoResultado=Resultado(infoResultado) 
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato)) 
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa)) 
        nuevoResultado.Candidato=elCandidato
        nuevoResultado.mesa=laMesa
        return self.repositorioResultado.save(nuevoResultado) 

    def show(self,id): 
        elResultado=Resultado(self.repositorioResultado.findById(id)) 
        return elResultado.__dict__

 #Modificación de Resultado (Candidato y mesa)

    def update(self,id,infoResultado,id_candidato,id_mesa,id_partido): 
        elResultado=Resultado(self.repositorioResultado.findById(id)) 
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato)) 
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa)) 
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioInscripcion.save(elResultado) 

    def delete(self, id): 
        return self.repositorioInscripcion.delete(id) 