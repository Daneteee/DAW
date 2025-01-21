import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ServersComponent } from './servers/servers.component';
import { CotxesComponent } from './cotxes/cotxes.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ServersComponent, CotxesComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'DanMaldonado_MP06UF3_Angular2';
}
