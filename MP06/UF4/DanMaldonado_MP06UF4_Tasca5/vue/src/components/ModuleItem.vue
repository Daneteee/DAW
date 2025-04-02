<template>
    <div :class="{'completed': isCompleted, 'pending': !isCompleted}" class="module-item">
      <!-- Vista Resum -->
      <div class="summary">
        <span>{{ modul.shortName }}</span>
        <button @click="toggleDetails">
          {{ showDetails ? 'Amagar detall' : 'Veure detall' }}
        </button>
      </div>
      <!-- Vista Detallada -->
      <div v-if="showDetails" class="details">
        <p><strong>Nom:</strong> {{ modul.nom }}</p>
        <p><strong>Durada:</strong> {{ modul.durada }}</p>
        <p><strong>Hores de lliure disposició:</strong> {{ modul.horesLliure }}</p>
        <p><strong>Equivalència en crèdits ECTS:</strong> {{ modul.ects }}</p>
        <p><strong>Unitats formatives:</strong> {{ modul.unitatsFormatives }}</p>
        <p><strong>Completades:</strong> {{ modul.completades }}</p>
        <button 
          @click="incrementCompleted"  
          :disabled="modul.completades >= modul.unitatsFormatives"
        >
          Incrementar UF completada
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ModuleItem',
    props: {
      modul: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        showDetails: false
      }
    },
    computed: {
      isCompleted() {
        return this.modul.completades === this.modul.unitatsFormatives;
      }
    },
    methods: {
      toggleDetails() {
        this.showDetails = !this.showDetails;
      },
      incrementCompleted() {
        // Emetem un esdeveniment perquè el component pare pugui actualitzar el valor.
        this.$emit('increment-uf', this.modul);
      }
    }
  }
  </script>
  
  <style scoped>
  .module-item {
    border: none;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 12px;
    transition: all 0.3s;
    box-shadow: 0 4px 10px rgba(90, 43, 126, 0.1);
  }

  .module-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(90, 43, 126, 0.15);
  }

  .completed {
    background-color: #e3f8e1;
    border-left: 5px solid #A125F0;
  }

  .pending {
    background-color: #f8eaff;
    border-left: 5px solid #5A2B7E;
  }

  .summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .summary span {
    font-weight: 600;
    color: #2A0944;
    font-size: 18px;
  }

  .module-item button {
    padding: 8px 16px;
    border: none;
    background-color: #5A2B7E;
    color: white;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.3s;
  }

  .module-item button:hover:not(:disabled) {
    background-color: #A125F0;
    transform: translateY(-2px);
  }

  .module-item button:disabled {
    background-color: #c9b7e0;
    cursor: not-allowed;
  }

  .details {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #e4d4f5;
  }

  .details p {
    margin: 8px 0;
    color: #444;
  }

  .details p strong {
    color: #3B185F;
  }

  /* ModuleList.vue */
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .container h1 {
    color: #2A0944;
    text-align: center;
    margin-bottom: 30px;
    font-size: 28px;
  }
  </style>
  