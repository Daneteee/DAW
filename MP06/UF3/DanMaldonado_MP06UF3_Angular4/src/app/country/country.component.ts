import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CountryService } from '../services/country.service';
import { Country } from '../models/country';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-country',
  imports: [CommonModule, FormsModule, RouterModule],
  providers: [CountryService],
  templateUrl: './country.component.html',
  styleUrls: ['./country.component.css']
})
export class CountryComponent {
  selectedCountry: string = '';
  countryData: Country | null = null;
  error: boolean = false;

  // Injectem CountryService
  constructor(private countryService: CountryService) {}

  fetchCountryData() {
    // Si no hi ha país seleccionat, no fem res
    if (!this.selectedCountry.trim()) {
      return; 
    } else {
      // Fem la petició per obtenir dades del país
      this.countryService.getCountryData(this.selectedCountry).subscribe({
        next: (data) => {
          this.countryData = data[0];
          this.error = false;
        },
        error: () => {
          this.countryData = null;
          this.error = true;
        }
      });
    }
  }
  

  // Mètode per obtenir els idiomes d'un país
  getLanguages(languages: { [key: string]: string } | undefined): string {
    return languages ? Object.values(languages).join(', ') : 'N/A';
  }
}
