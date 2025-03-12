import { Component } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})

// Afegim les propietats del component About
export class AboutComponent {
  titulo: string = 'Projecte Angular V8';
  subtitulo: string = 'UF3 MP06 - Desenvolupament Web en Entorn Client';
  email: string = 'dan.maldonado.2132@lacetania.cat';
}
