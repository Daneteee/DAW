import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class CountryService {
  private apiUrl = 'https://restcountries.com/v3.1/name/';

  constructor(private http: HttpClient) {}

  getCountryData(country: string): Observable<any> {
    return this.http.get<any[]>(`${this.apiUrl}${country}`);
  }
}
