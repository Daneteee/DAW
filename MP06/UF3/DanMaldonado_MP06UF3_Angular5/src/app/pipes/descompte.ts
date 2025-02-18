import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'descompte',
  standalone: true
})
export class DescomptePipe implements PipeTransform {
  transform(preuOriginal: number, percentatgeDescompte: number): string {
    if (!preuOriginal || !percentatgeDescompte) {
      return 'Dades incorrectes';
    }

    const preuRebaixat = preuOriginal - (preuOriginal * (percentatgeDescompte / 100));
    return `Preu Original ${preuOriginal}€ - Preu Rebaixat ${percentatgeDescompte}% : ${preuRebaixat.toFixed(2)}€`;
  }
}