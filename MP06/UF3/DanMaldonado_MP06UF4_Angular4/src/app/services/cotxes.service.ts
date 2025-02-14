import { Injectable } from '@angular/core';
import { Cotxe } from '../models/cotxe';

@Injectable()
export class CotxesService {

  public cotxes: Array<Cotxe>;

  constructor() { 
    this.cotxes = [
      new Cotxe("is220d", "Lexus", "Negre", 200, "diesel"),
      new Cotxe("S14", "Nissan", "Vermell", 140, "electric"),
      new Cotxe("NSX", "Honda", "Blanc", 240, "gas"),
      new Cotxe("Miata", "Mazda", "Blau", 110, "gasolina"),
      new Cotxe("Trueno", "Toyota", "Blanc", 120, "hybrid")
    ];
  }

  getText():String{
    return "Hola des del servei de cotxes";
  }

  getCotxes(): Array<Cotxe> {
    return this.cotxes;
  }
}
