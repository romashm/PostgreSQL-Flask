# PostgreSQL-Flask
<p align="center">
  <img src="https://media.giphy.com/media/l1J9RvTMj524KBkac/giphy.gif">
</p>
<h2> 📦 Installation </h2>
<p> Before the installation this project, you should be sure that you install PostgreSQL. In addition to this files, install a requirements.txt. First of all, inside config.py input <b> YOUR DATABASE POSTGRESQL PASSWORD & HOST & etc.  </b>. Second, inside <code>command prompt</code> print <b> python main.py </b> ( make sure you inside project folder </b>. Unarchive the file __pycache__.zip to deploy it.</p>
<h2> 💡 Main target </h2>
<p> <b>Postgresql</b> is a database, we should render this & return it. However, it's not at all, we should add feature which can sort objects in the result. Inside derivation we put JSON format file. </p>
<h2> 📩 Developing </h2>
<p> Firstly, lets create a basic <b>Flask</b> file. Likewise, I created 2 types of files: <code>Main.py</code> & <code>Database.ini</code>.   <b>Main.py</b> is for rendering, sorting our objects. Last file for transfer a database datas. I started write first function <b>config</b>, this function read file database.ini. It is need for <b> starting section postgresql </b>, likewise after rendering this file with received datas we recreate dictionary with datas for entry my <i> PostgreSQL</i>.</p>
<p align="center">
  <img src="https://sun9-61.userapi.com/impg/9gcrTyl9eIp0LWyZNv4f9QhHAy1d89uef0Ms6w/eLsfeCpiD7w.jpg?size=1280x784&quality=96&sign=847254a2f836b56de4d85e2ce5cc9727&type=album">
</p>
<p><b> Function main( ) </b>- which below func. config responsible for main content on the web-server. Inside function we create a place for saving information ( it 'll be dict & arrays. ), thereafter I call a function config( ) to read & open <b> PostgreSQL </b>. I find amount of colums to create a condition ( how many users will be ) & receive header table information. Work done, I returned & execute all information from table to put in dict. . </p>
<p align="center">
  <img src="https://sun9-35.userapi.com/impg/0XPUiIBUqwE6gakydfqn1gGDJAvrn-yHt6xHgw/PZoCOCH_eZE.jpg?size=1280x720&quality=96&sign=0cfab295d3a20a0ef8ab79cd660ceabf&type=album">
</p>
<p> Likewise, I create a function <b> SortedEnd ( ) </b>. It is main function for sorting list of data viseversa.You can behold it if put /SortedEnd. Therefore, I create another function for helping sorting -><b>FindaHotel</b>. This function will return special statistics about hotel you wanna find. For instance, you input <code> localhost/2 </code> it will render all information about user 2.</p>
<p align="center">
  <img src="https://sun9-23.userapi.com/impg/FnYaip2FHxoVwaXwbMQnOArJqJRoSlFzOAig9A/DBtZ3N4SCtw.jpg?size=676x410&quality=96&sign=6cc9c470b53f6ed392812ed3b657d83f&type=album">
</p>
<h2> 🌍 Result </h2>
<h1> Function main, rendering entire database </h1>
<p align="center">
  <img src="https://sun9-55.userapi.com/impg/bpzLDqYut3F51yTnrTw6QGSERDZRiSQYdL0qpw/-NO1IV0MqI0.jpg?size=1280x276&quality=95&sign=aa6ec916bd4f7f7e030b02e8cb785095&type=album">
</p>
<h1> Sorting reverse </h1>
<p align="center">
  <img src="https://sun9-28.userapi.com/impg/qBCsxVdjC9QOrHjXCz-Ph2KO7ehP73B7WDoreg/6qd0CYrAdwE.jpg?size=952x58&quality=96&sign=0ad84c8ed1ecf02303747e053a05ef1f&type=album">
</p>
<h1> Find a special user-id </h1>
<p align="center">
  <img src="https://sun9-46.userapi.com/impg/hIKL4k8wdvUzXO0DUAsJ3Ze0yjq9PHuPdwJwZw/S2x7YmmjHDM.jpg?size=1280x83&quality=95&sign=4630673b09fe60486fc5bc4428f0a7ea&type=album">
</p>
