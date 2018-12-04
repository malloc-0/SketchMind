// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false;


let VueMaterial = require('vue-material');
Vue.use(VueMaterial);

new Vue({
  el: '#app',
  template: '<App/>',
  components: {
    App
  }
});







