package py.una.pol.sd.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import py.una.pol.sd.model.Persona;
import py.una.pol.sd.repository.PersonaRepository;
import javax.persistence.EntityNotFoundException;


@Service
public class PersonaService {


   @Autowired
    private PersonaRepository personaRepository;
  
    public List<Persona> findAll() {
        return personaRepository.findAll();
    }

    public Persona findByCedula(Integer cedula) {
        return personaRepository.findByCedula(cedula);
    }

    public Persona save(Persona persona) {
        return personaRepository.save(persona);
    }

    public void deleteByCedula(Integer cedula) {
        if (!personaRepository.existsById(cedula)) {
            throw new EntityNotFoundException("Persona no encontrada con cédula: " + cedula);
        }
        personaRepository.deleteById(cedula);
    }

    public Persona updateByCedula(Integer cedula, Persona persona) {
        if (!personaRepository.existsById(cedula)) {
            throw new EntityNotFoundException("Persona no encontrada con cédula: " + cedula);
        }
        persona.setCedula(cedula); 
        return personaRepository.save(persona);
    }
}