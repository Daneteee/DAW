import { Component } from '@angular/core';
import { Cotxe } from '../models/cotxe';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-cotxes',
  imports: [FormsModule, CommonModule],
  templateUrl: './cotxes.component.html',
  styleUrl: './cotxes.component.css'
})
export class CotxesComponent {

  public titol: string = "Array de cotxes";
  public cotxes: Array<Cotxe>;

  constructor() {
    this.cotxes = [
      new Cotxe("is220d", "Lexus", "Negre", 200, "diesel"),
      new Cotxe("S14", "Nissan", "Vermell", 140, "electric"),
      new Cotxe("NSX", "Honda", "Blanc", 240, "gas"),
      new Cotxe("Miata", "Mazda", "Blau", 110, "gasolina"),
      new Cotxe("Trueno", "Toyota", "Blanc", 120, "hybrid")
    ]
  }

  // Nuevo objeto para los datos del formulario
  public nouCotxe: Cotxe = new Cotxe('', '', '', 0, 'gasolina');

  // Función para agregar un nuevo coche
  afegirCotxe() {
    this.cotxes.push(new Cotxe(
      this.nouCotxe.model,
      this.nouCotxe.marca,
      this.nouCotxe.color,
      this.nouCotxe.velocitat,
      this.nouCotxe.combustible
    ));

    // Limpiar el formulario después de añadir el coche
    this.nouCotxe = new Cotxe('', '', '', 0, 'gasolina');
  }

  eliminarCotxe(cotxe: Cotxe) {
    const index = this.cotxes.indexOf(cotxe);
    if (index !== -1) {
      this.cotxes.splice(index, 1);
    }
  }

}
