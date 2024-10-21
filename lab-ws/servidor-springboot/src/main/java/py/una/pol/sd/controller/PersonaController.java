package py.una.pol.sd.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import py.una.pol.sd.model.Persona;
import py.una.pol.sd.service.PersonaService;

import java.util.List;
import org.springframework.http.MediaType;

@RestController
@RequestMapping("/personas")
public class PersonaController {

    @Autowired
    PersonaService personaService;

    @GetMapping("/saludo")
    public String index() {
        return "Hola mundo caluroso de Springboot";
    }

    @GetMapping(value = "/listar", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE})
    public ResponseEntity<List<Persona>> getPersonas() {
        List<Persona> r = personaService.findAll(); 
        return new ResponseEntity<>(r, HttpStatus.OK);
    }

    @PostMapping(value = "/crear", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> create(@RequestBody Persona per) {
        if (per != null && per.getCedula() != null) {
            System.out.println("Persona recepcionada " + per.getNombre());
            personaService.save(per);
            return new ResponseEntity<>("Se recepcionó correctamente la persona: " + per.toString(), HttpStatus.OK);
        } else {
            System.out.println("Datos mal enviados por el cliente");
            return new ResponseEntity<>("Debe enviar el campo cédula.", HttpStatus.BAD_REQUEST);
        }
    }

    @PutMapping(value = "/actualizar/{cedula}", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Persona> updatePersona(@PathVariable Integer cedula, @RequestBody Persona persona) {
        Persona updatedPersona = personaService.updateByCedula(cedula, persona);
        System.out.println("Persona actualizada: " + updatedPersona.getNombre());
        return new ResponseEntity<>(updatedPersona, HttpStatus.OK);
    }

    @DeleteMapping(value = "/borrar/{cedula}", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> deletePersona(@PathVariable Integer cedula) {
        personaService.deleteByCedula(cedula);
        System.out.println("Persona eliminada con cédula: " + cedula);
        return new ResponseEntity<>("Persona eliminada correctamente.", HttpStatus.OK);
    }
}
