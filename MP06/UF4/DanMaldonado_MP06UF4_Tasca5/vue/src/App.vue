<template>
  <div id="app">
    <Navbar :activeView="activeView" @change-view="activeView = $event" />
    <ModuleList :activeView="activeView" />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import ModuleList from './components/ModuleList.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    ModuleList
  },
  data() {
    return {
      activeView: 'list' 
    }
  }
}
</script>

<style>
#app {
  font-family: 'Poppins', Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  color: #333;
  background-color: #f8f5ff;
  min-height: 100vh;
}

/* Resetear algunos estilos del navegador */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

/* ModuleForm.vue */
.module-form {
  max-width: 600px;
  margin: 20px auto;
  padding: 25px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(90, 43, 126, 0.1);
}

.module-form h2 {
  color: #2A0944;
  margin-bottom: 20px;
  text-align: center;
}

.module-form input {
  width: 100%;
  padding: 12px;
  margin: 8px 0 16px;
  border: 1px solid #d4c4eb;
  border-radius: 8px;
  font-size: 16px;
  transition: border 0.3s;
}

.module-form input:focus {
  border-color: #A125F0;
  outline: none;
  box-shadow: 0 0 0 2px rgba(161, 37, 240, 0.2);
}

.module-form label {
  color: #5A2B7E;
  font-weight: 500;
}

.module-form button {
  width: 100%;
  padding: 12px;
  background-color: #A125F0;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 10px;
}

.module-form button:hover {
  background-color: #8A14D5;
  transform: translateY(-2px);
}
</style>
