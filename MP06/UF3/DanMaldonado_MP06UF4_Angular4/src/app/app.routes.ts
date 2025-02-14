import { Routes } from '@angular/router';
import { CountryComponent } from './country/country.component';
import { CotxesComponent } from './cotxes/cotxes.component';
import { NotFoundComponent } from './notfound/notfound.component';

export const routes: Routes = [
  { path: '', redirectTo: 'country', pathMatch: 'full' },
  { path: 'country', component: CountryComponent },
  { path: 'cotxes', component: CotxesComponent },
  { path: '**', component: NotFoundComponent }, 
];
