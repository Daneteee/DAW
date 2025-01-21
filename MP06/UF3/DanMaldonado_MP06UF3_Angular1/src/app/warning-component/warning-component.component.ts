import { Component } from '@angular/core';

@Component({
  selector: 'app-warning-component',
  imports: [],
  templateUrl: './warning-component.component.html',
  styleUrl: './warning-component.component.css'
})
export class WarningComponentComponent {
  missatge: string = 'This is a warning, you are in danger!';
}
