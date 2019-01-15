# Vue-TypeScript-Template

> 脚手架可选装vuex、router、logan、rem(默认100px)、unit test等

## 使用Cli安装

1. 升级MDTPL脚手架到最新版

```bash
npm install -g @dp/mdtpl-cli@latest
```

2. 初始化项目

```bash
mdtpl init vue-ts-template my-project
```

## 为什么使用TypeScript

- Js的超集，兼容所有js语法

- 静态类型检查

- 运行时检查，有什么问题在写代码时就直接提示给你，省去大量调试时间

- IDE 智能提示，配合Vscode非常好用

- 代码重构

- 可读性高

目前zaku项目就是使用的vue+ts的方式开发，非常好用

## 变量声明

官方文档：https://www.tslang.cn/docs/handbook/basic-types.html

使用ts，其实你只需要知道怎么给变量加上类型就可以

ts的变量声明相比于js只多了一个类型，如

```javascript
var str: string = 'msg' // 声明string类型的变量

str = 2 // error, 因为2是number类型
```

当然也不是所有的变量都需要声明类型，如果不声明类型，ts会自动判断并加上类型，如：

```javascript
var num = 2 // ts自动判断num是number类型

num = 'test' // error
```

如果有类型变更需求，或类型不确定，则可以使用any类型

```javascript
var test: any = 2 // any类型

test = 'msg' // 可以正常运行
```

## 在Vue里使用TypeScript

在vue中写ts是基于类的，这个和vue官方写法有较大区别，先上一段代码：

```javascript
import { Vue, Component } from "vue-property-decorator";
import { State, Action } from "vuex-class";

@Component
export default class HelloWorld extends Vue {
  // vuex state，访问方式为this.test, 等同于this.$store.state.test
  @State test: string;
  // vuex action, 调用方式为this.toggle(true | false), 等同于this.$store.dispatch('toggle', true | false)
  @Action toggle: (flag: boolean) => void;
  // data， 直接声明即可
  msg: string = "Msg";

  // computed
  get testComputed(): string {
    return "test computed";
  }

  // method, 默认是public
  testFunc() {
    this.msg = "func msg" + Date.now();

    // error: Type '2' is not assignable to type 'string'
    // this.msg = 2
  }
}
```

上面的代码等同于

```javascript
import Vue from "vue";

export default {
  data() {
    return {
      msg: "test msg"
    };
  },
  computed: {
    testComputed() {
    	return "test computed";
    },
    test() {
    	return this.$store.state.test;
    }
  },
  methods: {
    testFunc() {
      this.mag = "func msg" + Date.now();
    }
  }
};
```

## 引入组件

引入组件组要在@Components里操作，如

```javascript
import { Vue, Component } from "vue-property-decorator";
import HelloWorld from './HelloWorld.vue'

@Component({
	components: { HelloWorld }
})
export default class HelloWorld extends Vue {

}
```

## 详细文档

基本写法：基本文档：https://github.com/vuejs/vue-class-component

vuex使用：https://github.com/ktsn/vuex-class

Watch，Inject等高级用法：https://github.com/kaorun343/vue-property-decorator

## 交流

有问题或建议欢迎大象我 zhangren

