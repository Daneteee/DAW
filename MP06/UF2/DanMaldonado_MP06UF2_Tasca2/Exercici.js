/**
 * Classe Cotxe
 * Un cotxe amb una marca i una velocitat.
 */
class Cotxe {
  /**
   * Constructor de la classe Cotxe.
   * @param {string} marca - La marca del cotxe.
   * @param {number} velocitat - La velocitat inicial del cotxe.
   */
  constructor(marca, velocitat) {
    this.marca = marca;
    this.velocitat = velocitat; 
  }

  /**
   * Mètode per accelerar el cotxe.
   * Incrementem la velocitat en 10 km/h fins a un màxim de 250 km/h.
   */
  accelerar() {
    if (this.velocitat < 250) {

      // Incrementem la velocitat en 10 sense passar de 250 km/h
      this.velocitat = Math.min(this.velocitat + 10, 250);
      console.log(`${this.marca} ha accelerat. Velocitat actual: ${this.velocitat} km/h`);
    } else {
      console.log(`${this.marca} ja està a la velocitat màxima de 250 km/h.`);
    }
  }

  /**
   * Mètode per frenar el cotxe.
   * Reduim la velocitat en 5 km/h fins a un mínim de 0 km/h.
   */
  fre() {
    if (this.velocitat > 0) {

      // Reduim la velocitat en 5 i ens assegurem de no baixar de 0 km/h
      this.velocitat = Math.max(this.velocitat - 5, 0);
      console.log(`${this.marca} ha frenat. Velocitat actual: ${this.velocitat} km/h`);
    } else {
      console.log(`${this.marca} ja està aturat.`);
    }
  }
}

// Array de cotxes amb marques i velocitats diferents.
const cotxes = [
  new Cotxe('Lexus', 240),
  new Cotxe('Toyota', 180),
  new Cotxe('Nissan', 200),
  new Cotxe('Mazda', 150),
  new Cotxe('Honda', 90)
];

/**
 * Classe Ev
 * Representa un cotxe elèctric, hereda de Cotxe, amb una propietat de càrrega de bateria.
 */
class Ev extends Cotxe {
  /**
   * Constructor de la classe Ev.
   * @param {string} marca - La marca del cotxe elèctric.
   * @param {number} velocitat - La velocitat inicial del cotxe.
   * @param {number} carrega - La càrrega inicial de la bateria.
   */
  constructor(marca, velocitat, carrega) {
    super(marca, velocitat); // Cridem al constructor de la classe superior
    this.carrega = carrega; 
  }

  /**
   * Mètode per carregar la bateria.
   * Fiquem el nivell de càrrega dins del rang vàlid (0% a 100%).
   * @param {number} chargeTo - El percentatge al qual carregar la bateria.
   */
  chargeBattery(chargeTo) {

    // Ens assegurem que la càrrega estigui entre 0 i 100
    this.carrega = Math.min(Math.max(chargeTo, 0), 100);
    console.log(`${this.marca} ha carregat la bateria al ${this.carrega}%.`);
  }

  /**
   * Mètode per accelerar el cotxe elèctric.
   * Incrementem la velocitat en 20 km/h i reduim la càrrega en 1%.
   * Si la bateria està esgotada, no es pot accelerar.
   */
  accelerar() {
    if (this.carrega > 0) {
      // Incrementa la velocitat i redueix la càrrega de la bateria
      this.velocitat = Math.min(this.velocitat + 20, 250);
      this.carrega = Math.max(this.carrega - 1, 0);
      console.log(
        `${this.marca} anirà a ${this.velocitat} km/h, amb una càrrega del ${this.carrega}%.`
      );
    } else {
      console.log(`${this.marca} no pot accelerar perquè no té bateria.`);
    }
  }
}

// Creem un objecte Ev
const tesla = new Ev('Tesla', 100, 50);

tesla.accelerar(); 
tesla.fre();
tesla.chargeBattery(90); 
tesla.accelerar(); 
tesla.accelerar(); 

// Treiem la càrrega i tractem d'accelerar
tesla.chargeBattery(0); 
tesla.accelerar(); 
