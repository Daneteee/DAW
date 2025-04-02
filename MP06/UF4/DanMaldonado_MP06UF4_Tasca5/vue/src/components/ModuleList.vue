<template>
  <div class="container">
    <div v-if="activeView === 'list'">
      <h1>Llista de Mòduls Professionals</h1>
      <ModuleItem
        v-for="(modul, index) in moduls"
        :key="index"
        :modul="modul"
        @increment-uf="handleIncrement"
      />
    </div>

    <div v-else>
      <h1>Afegir nou mòdul</h1>
      <ModuleForm 
        :existingModules="moduls" 
        @module-added="addModule" 
      />
    </div>
  </div>
</template>

<script>
import ModuleForm from './ModuleForm.vue';
import ModuleItem from './ModuleItem.vue';

export default {
  name: 'ModuleList',
  components: { ModuleItem, ModuleForm },
  props: {
    activeView: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      moduls: [
        {
          shortName: 'M5: entorns de desenvolupament',
          nom: 'Mòdul professional 5: entorns de desenvolupament',
          durada: '66 hores',
          horesLliure: 'no se n’assignen',
          ects: 6,
          unitatsFormatives: 3,
          completades: 2
        },
        {
          shortName: 'M6: desenvolupament web en entorn client',
          nom: 'Mòdul professional 6: desenvolupament web en entorn client',
          durada: '165 hores',
          horesLliure: '33 hores',
          ects: 9,
          unitatsFormatives: 4,
          completades: 4
        },
        {
          shortName: 'M7: desenvolupament web en entorn servidor',
          nom: 'Mòdul professional 7: desenvolupament web en entorn servidor',
          durada: '165 hores',
          horesLliure: '33 hores',
          ects: 12,
          unitatsFormatives: 4,
          completades: 3
        }
      ]
    }
  },
  methods: {
    handleIncrement(modul) {
      if (modul.completades < modul.unitatsFormatives) {
        modul.completades++;
      }
    },
    addModule(newModule) {
      const exists = this.moduls.some(modul => modul.shortName === newModule.shortName);
      if (!exists) {
        this.moduls.push(newModule);
      } else {
        alert('Ja existeix un mòdul amb el mateix identificador.');
      }
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 20px;
}

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
