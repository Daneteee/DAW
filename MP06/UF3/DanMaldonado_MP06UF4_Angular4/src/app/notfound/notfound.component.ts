import { Component } from '@angular/core';

@Component({
  selector: 'app-not-found',
  template: `<h2>Pàgina no trobada</h2><p>Torna a la <a routerLink="/">pàgina principal</a></p>`,
  styles: [`h2 { color: red; }`]
})
export class NotFoundComponent {}
