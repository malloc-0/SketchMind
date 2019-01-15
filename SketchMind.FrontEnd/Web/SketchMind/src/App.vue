<template>
  <div id="app">
    <img width="150" height="150" src="./assets/logo.png">
    <h1>SketchMind</h1>
    <h3>手绘思维导图转换</h3>
    <md-layout md-align="center">
      <md-stepper>
        <md-step :md-editable="true" md-label="上传" :md-error="!didUpload" :md-continue="didUpload" md-message="UPLOAD"  md-button-back="返回" md-button-continue="继续">
          <p>请上传一张图片。</p>
          <md-button class="md-raised md-primary">浏览…</md-button>
        </md-step>
        <md-step :md-disabled="!didUpload" md-label="调整"  md-message="ADJUST" md-button-back="返回" md-button-continue="继续">
          <p>可以在这里对思维导图稍作调整。</p>
          <md-button class="md-raised md-primary" v-on:click="init_Mind()">浏览…</md-button>
          <md-layout md-align="center">
            <div id="app">
              <mindmap
                :nodes="nodes"
                :connections="connections"
                :editable="true"
              ></mindmap>
            </div>
          </md-layout>
        </md-step>
        <md-step :md-disabled="!didUpload" md-label="导出"  md-message="EXPORT" md-button-back="返回" md-button-continue="完成">
          <p>导出为图片／FreeMind 格式。</p>
        </md-step>
      </md-stepper>
    </md-layout>
    <md-bottom-bar :md-shift="true">
      <md-bottom-bar-item onclick='window.open("https://github.com/malloc-0/SketchMind")' md-icon="code">GitHub 页面</md-bottom-bar-item>
    </md-bottom-bar>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import './main'
// You need a specific loader for CSS files like https://github.com/webpack/css-loader

import map from "./sprite/map";


export default Vue.extend({
  data: function() {
    return {
      didUpload: true,
      map
    }
  }
})


</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
<style src="../node_modules/vue-material/dist/vue-material.css"></style>
