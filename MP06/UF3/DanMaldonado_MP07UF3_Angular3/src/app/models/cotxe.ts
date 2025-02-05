export type Combustible = 'gasolina' | 'gas' | 'diesel' | 'electric' | 'hybrid';

export class Cotxe {
    constructor (

        public model: string,
        public marca: string,
        public color: string,
        public velocitat: number,
        public combustible: Combustible, 
        public correComUnLlamp: boolean = false 

    ){
        if (this.velocitat > 150) {
            this.correComUnLlamp = true;
        }
    }
}