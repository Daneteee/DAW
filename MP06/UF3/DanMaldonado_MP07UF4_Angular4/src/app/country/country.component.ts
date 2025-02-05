import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CountryService } from '../services/country.service';

@Component({
  selector: 'app-country',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  providers: [CountryService],
  templateUrl: './country.component.html',
  styleUrls: ['./country.component.css']
})
export class CountryComponent {
  selectedCountry: string = '';
  countryData: any = null;
  error: boolean = false;

  constructor(private countryService: CountryService) {}

  fetchCountryData() {
    if (!this.selectedCountry.trim()) return;

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

  getLanguages(languages: any): string {
    return languages ? Object.values(languages).join(', ') : 'N/A';
  }
}
