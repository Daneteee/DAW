import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Modul6Component } from './modul6/modul6.component';
import { WarningComponentComponent } from './warning-component/warning-component.component';
import { SuccesfulComponentComponent } from './succesful-component/succesful-component.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Modul6Component, WarningComponentComponent, SuccesfulComponentComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'DanMaldonado_MP06UF3_Angular1';
}
