<template>
    <div class="module-form">
      <h2>Afegeix un nou mòdul</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="shortName">Nom curt:</label>
          <input v-model="newModule.shortName" type="text" id="shortName" required />
        </div>
        <div>
          <label for="nom">Nom complet:</label>
          <input v-model="newModule.nom" type="text" id="nom" required />
        </div>
        <div>
          <label for="durada">Durada:</label>
          <input v-model="newModule.durada" type="text" id="durada" required />
        </div>
        <div>
          <label for="horesLliure">Hores de lliure disposició:</label>
          <input v-model="newModule.horesLliure" type="text" id="horesLliure"/>
        </div>
        <div>
          <label for="ects">Equivalència en crèdits ECTS:</label>
          <input v-model="newModule.ects" type="number" id="ects" required />
        </div>
        <div>
          <label for="unitatsFormatives">Unitats formatives:</label>
          <input v-model="newModule.unitatsFormatives" type="number" id="unitatsFormatives" required />
        </div>
        <button type="submit">Afegeix mòdul</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ModuleForm',
    props: {
      existingModules: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        newModule: {
          shortName: '',
          nom: '',
          durada: '',
          horesLliure: '',
          ects: '',
          unitatsFormatives: '',
          completades: 0
        }
      }
    },
    methods: {
      submitForm() {
        // Enviar el nou mòdul al component pare
        this.$emit('module-added', { ...this.newModule });
  
        // Reset form
        this.newModule = {
          shortName: '',
          nom: '',
          durada: '',
          horesLliure: '',
          ects: '',
          unitatsFormatives: ''
        };
      }
    }
  }
  </script>
  
  <style scoped>
  .module-form {
    max-width: 500px;
    margin: 0 auto;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  