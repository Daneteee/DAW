import { Component } from '@angular/core';
import { Cotxe } from '../models/cotxe';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cotxes',
  imports: [FormsModule, CommonModule],
  templateUrl: './cotxes.component.html',
  styleUrls: ['./cotxes.component.css']
})
export class CotxesComponent {

  // Inicialitzem variables
  public titol: string = "Array de cotxes";
  public cotxes: Array<Cotxe>;

  public nouCotxe: Cotxe = new Cotxe('', '', '', 0, 'gasolina');

  constructor(private route: ActivatedRoute, private router: Router) {
    this.cotxes = [
      new Cotxe("is220d", "Lexus", "Negre", 200, "diesel"),
      new Cotxe("S14", "Nissan", "Vermell", 140, "electric"),
      new Cotxe("NSX", "Honda", "Blanc", 240, "gas"),
      new Cotxe("Miata", "Mazda", "Blau", 110, "gasolina"),
      new Cotxe("Trueno", "Toyota", "Blanc", 120, "hybrid")
    ];
  }

  // Ens subscrivim als paràmetres quan carreguem el component
  ngOnInit() {
    this.route.params.subscribe(params => {
      if (params['model'] && params['marca'] && params['color'] && params['velocitat'] && params['combustible']) {
        this.afegirCotxeDesDeURL(params);
      }
    });
  }

  // Afegim un cotxe
  afegirCotxe() {
    this.cotxes.push(new Cotxe(
      this.nouCotxe.model,
      this.nouCotxe.marca,
      this.nouCotxe.color,
      this.nouCotxe.velocitat,
      this.nouCotxe.combustible
    ));
    this.nouCotxe = new Cotxe('', '', '', 0, 'gasolina');
  }

  // Elminem el cotxe
  eliminarCotxe(cotxe: Cotxe) {
    const index = this.cotxes.indexOf(cotxe);
    if (index !== -1) {
      this.cotxes.splice(index, 1);
    }
  }

  // Mitjançant paràmetres de la URL afegim un cotxe
  afegirCotxeDesDeURL(params: any) {
    this.cotxes.push(new Cotxe(
      params['model'],
      params['marca'],
      params['color'],
      +params['velocitat'],  
      params['combustible']
    ));
  }

  // Retornem l'index de l'element actual
  trackByIndex(index: number, item: Cotxe): number {
    return index;  
  }
}
