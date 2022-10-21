from Modelos.Resultado import Resultado 
from Modelos.Mesa import Mesa 
from Modelos.Candidato import Candidato 
from Modelos.Partido import Partido
from Repositorios.RepositorioResultado import RepositorioResultado 
from Repositorios.RepositorioMesa import RepositorioMesa 
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorResultado(): 

    def __init__(self): 
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato() 
        self.repositorioMesa = RepositorioMesa() 
        self.repositorioPartido = RepositorioPartido() 

    def index(self): 
        return self.repositorioResultado.findAll() 

#Asignacion candidato, mesa y partido a Resultado

    def create(self,infoResultado,id_candidato,id_mesa,id_partido): 
        nuevoResultado=Resultado(infoResultado) 
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        elPartido=Partido(self.repositorioPartido.findById(id_mesa)) 
        laMesa=Mesa(self.repositorioMesa.findById(id_partido)) 
        nuevoResultado.Candidato=elCandidato
        nuevoResultado.mesa=laMesa
        nuevoResultado.Partido=elPartido
        return self.repositorioResultado.save(nuevoResultado) 

    def show(self,id): 
        elResultado=Resultado(self.repositorioResultado.findById(id)) 
        return elResultado.__dict__

 #Modificación de Resultado (Candidato y mesa)

    def update(self,id,infoResultado,id_candidato,id_mesa,id_partido): 
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa=infoResultado["numero_mesa"] 
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato)) 
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa)) 
        elPartido=Partido(self.repositorioPartido.findById(id_partido)) 
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        elResultado.Partido = elPartido
        return self.repositorioInscripcion.save(elResultado) 

    def delete(self, id): 
        return self.repositorioInscripcion.delete(id) 