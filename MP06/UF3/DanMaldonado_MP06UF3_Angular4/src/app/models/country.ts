export interface Country {
    name: { common: string }; 
    capital: string[]; 
    area: number; 
    population: number; 
    flags: { svg: string };
    languages: { [key: string]: string };
  }
  