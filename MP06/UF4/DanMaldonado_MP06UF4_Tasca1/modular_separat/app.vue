import { createApp, ref } from 'https://unpkg.com/vue@3.2.41/dist/vue.esm-browser.js';

createApp({
  setup() {
    const name = ref('Dan Maldonado');
    const age = ref(19);
    const randomNumber = ref(Math.floor(Math.random() * 10));
    const imageUrl = ref('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZUJFO5miYPVea0e6NeD8wIhdanrsk8o7DGw&s');
    const inputValue = ref('Bondia! Això és un valor per defecte.');

    return {
      name,
      age,
      randomNumber,
      imageUrl,
      inputValue
    };
  }
}).mount('#app');