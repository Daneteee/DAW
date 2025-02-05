import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CotxesComponent } from "./cotxes/cotxes.component";
import { CountryComponent } from "./country/country.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CotxesComponent, CountryComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'DanMaldonado_MP07UF4_Angular4';
}
