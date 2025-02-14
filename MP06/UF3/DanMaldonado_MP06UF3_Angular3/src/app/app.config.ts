import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { Routes, provideRouter } from '@angular/router';

import { CotxesComponent } from './cotxes/cotxes.component';
import { HomeComponent } from './home/home.component';
import { Modul6Component  } from './modul6/modul6.component';
import { UnitatsFormativesComponentComponent } from './unitats-formatives-component/unitats-formatives-component.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'home' },
  { path: 'cotxes', component: CotxesComponent },
  { path: 'modul6', component: Modul6Component },
  { path: 'home', component: HomeComponent },
  { path: 'unitats-formatives', component: UnitatsFormativesComponentComponent },
  { path: 'cotxes/:model/:marca/:color/:velocitat/:combustible', component: CotxesComponent },

];

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes)]
};
