<template>
  <div class="hello">
    <h1>欢迎来到 [ 靖欣婚介 ] </h1>
    <p>请选择一种角色注册</p>
    
    <form action="" method="post">
    	
    	<input type="button" value="注册红娘" class="btn" /> <br/>
    	<input type="button" value="注册单身" class="btn" />
    	
    </form>
    
    
    <br />
    <br />
    
    <p class="p1">此处放宣传广告语，由客户提供文案</p >
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.btn{
	margin:20px;
	border: 1px solid #ff77bf;
	color: #ff77bf;
	width: 200px;
	height: 45px;
	border-radius: 25px;
	background-color: #FFFFFF;
	font-size: 16px;
}
.p1{
	text-align:left;
	font-size: 12px;
	margin-left: 30px;
}
</style>
