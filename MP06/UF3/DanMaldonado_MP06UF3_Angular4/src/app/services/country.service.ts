import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Country } from '../models/country';

@Injectable()
export class CountryService {
  private apiUrl = 'https://restcountries.com/v3.1/name/';

  constructor(private http: HttpClient) {}

  getCountryData(country: string): Observable<Country[]> {
    // Fem la petició a l'API i retornem un array de `Country`
    return this.http.get<Country[]>(`${this.apiUrl}${country}`);
  }
}