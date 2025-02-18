import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormulariPostComponent } from "./formulari-post/formulari-post.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormulariPostComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'DanMaldonado_MP06UF3_Angular5';
}
