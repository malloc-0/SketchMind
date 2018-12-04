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
            <div id="jsmind_container" style='height: 400px; width: 800px;' class="jsmind_container" editable="true"></div>
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
import jsMind from 'jsmind'
import "../node_modules/jsmind/style/jsmind.css"
import '../node_modules/jsmind/js/jsmind.draggable'

import './main'




export default Vue.extend({
  data: function() {
    return {
      didUpload: true,
      mind: {
        /* 元数据，定义思维导图的名称、作者、版本等信息 */
        "meta": {
          "name": "Example",
          "author": "malloc(0)",
          "version": "0.1.0"
        },
        /* 数据格式声明 */
        "format": "node_array",
        /* 数据内容 */
        "data": [
          { "id": "1", "isroot": true, "topic": "Microsoft" },
          { "id": "2", "parentid": "1", "topic": "Windows", "direction": "left" },
          { "id": "3", "parentid": "1", "topic": "Office" },
          { "id": "4", "parentid": "1", "topic": "Visual Studio" },
          { "id": "5", "parentid": "1", "topic": "Visual Studio Code" },
          { "id": "6", "parentid": "1", "topic": "Xbox" },
          { "id": "7", "isroot": true, "topic": "Apple", "expanded": false, "direction": "right" },
          { "id": "8", "parentid": "7", "topic": "macOS" },
          { "id": "9", "parentid": "7", "topic": "iOS" },
          { "id": "10", "parentid": "7", "topic": "tvOS", "direction": "right" },
          { "id": "11", "parentid": "7", "topic": "watchOS" },
        ]
      },
      options: {
        container: 'jsmind_container',
        editable: true,
        theme: 'orange'
      }
    }
  },
  methods: {
    init_Mind() {
      let jm = new jsMind(this.$data.options);
      jm.show(this.$data.mind);
      alert("Tried init mind")
    },
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
