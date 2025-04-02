<template>
    <nav class="navbar">
      <button 
        @click="$emit('change-view', 'list')"
        :class="{ 'active': activeView === 'list' }"
      >
        📚 Mòduls
      </button>
      <button 
        @click="$emit('change-view', 'form')"
        :class="{ 'active': activeView === 'form' }"
      >
        ➕ Afegir mòdul
      </button>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'AppNavbar',
    props: {
      activeView: {
        type: String,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .navbar {
    background: #2A0944;
    padding: 1.2rem;
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(42, 9, 68, 0.15);
    margin-bottom: 30px;
  }
  
  button {
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s;
    background-color: #3B185F;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  button:hover {
    background-color: #5A2B7E;
    transform: translateY(-2px);
  }
  
  button.active {
    background-color: #A125F0 !important;
    box-shadow: 0 4px 6px rgba(161, 37, 240, 0.3);
  }
  </style>