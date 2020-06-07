// NOTE: ECMAScript 6
// Libs
window.$ = window.jQuery = require('jquery');
window.M = require('materialize-css');
window.axios = require('axios');
window.Vue = require('vue');

// Components
import mapsection from './_map.vue';

// App
var app = new Vue({
  // Element
  el: '#app',

  // Components
  components: {
    mapsection
  }
});
