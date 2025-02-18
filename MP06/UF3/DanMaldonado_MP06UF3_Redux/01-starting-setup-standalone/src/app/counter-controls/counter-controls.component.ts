import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { increment, decrement } from '../store/counter.actions';

import { CounterService } from '../counter.service';

@Component({
  selector: 'app-counter-controls',
  templateUrl: './counter-controls.component.html',
  styleUrls: ['./counter-controls.component.css'],
  standalone: true,
})
export class CounterControlsComponent {

  constructor(private store: Store) {}

  increment() {
	this.store.dispatch(increment({ value:3 }));
  }

  decrement(){
	this.store.dispatch(decrement({ value:3 }));
  }
}
