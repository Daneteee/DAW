import { Actions, createEffect, ofType } from '@ngrx/effects';
import { increment, decrement, init, set } from './counter.actions';
import { selectCount } from './counter.selectors';
import { tap, withLatestFrom, switchMap, of } from 'rxjs';
import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';

@Injectable()
export class CounterEffects{
 
    saveCount=createEffect(() => this.actions$.pipe(
    ofType(increment, decrement),
    withLatestFrom(this.store.select(selectCount)),
    tap(([action, counter]) => {
        console.log(counter);
        localStorage.setItem('count',counter.toString());
    })),
    { dispatch: false });

    loadCount=createEffect(() => this.actions$.pipe(
    ofType(init),
    switchMap(() => {
        const storedCounter=localStorage.getItem('count');
        if(storedCounter){ // No es null
        // Convertim a number afegint + al davant…
            return of(set({value: +storedCounter}));
        }
        return of(set({value: 0}));
        })
    )
    );

 constructor(private actions$: Actions, private store: Store<{counter: number}>){}
}
