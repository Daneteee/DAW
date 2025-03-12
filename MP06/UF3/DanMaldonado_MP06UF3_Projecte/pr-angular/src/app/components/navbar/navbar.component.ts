import { Component } from '@angular/core';
import { RouterModule, RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  standalone: true,
  imports: [RouterModule, RouterLink, RouterLinkActive, CommonModule]
})
export class NavbarComponent {
  menuActive = false;

  // Afegim el mètode toggleMenu
  toggleMenu(): void {
    // Canvia l'estat de la propietat menuActive
    this.menuActive = !this.menuActive;
  }
}