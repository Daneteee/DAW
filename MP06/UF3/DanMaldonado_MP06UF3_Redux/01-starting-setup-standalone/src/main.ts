import { bootstrapApplication } from '@angular/platform-browser';

import { AppComponent } from './app/app.component';
import { provideStore } from '@ngrx/store';

import { counterReducer } from './app/store/counter.reducer';
import { provideStoreDevtools } from '@ngrx/store-devtools';
import { provideEffects } from '@ngrx/effects';
import { isDevMode } from '@angular/core';
import { CounterEffects } from './app/store/counter.effects';

bootstrapApplication(AppComponent, {
  providers: [provideStore({ counter: counterReducer }),  
  provideEffects([CounterEffects])],
});
