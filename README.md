# PostgreSQL-Flask
<p align="center">
  <img src="https://media.giphy.com/media/l1J9RvTMj524KBkac/giphy.gif">
</p>
<h2> 📦 Installation </h2>
<p>  </p>
<h2> 💡 Main target </h2>
<p> <b>Postgresql</b> is a database, we should render this & return it. However, it's not at all, we should add feature which can sort objects in the result. Inside derivation we put JSON format file. </p>
<h2> 📩 Developing </h2>
<p> Firstly, lets create a basic <b>Flask</b> file. Likewise, I created 2 types of files: <code>Main.py</code> & <code>Database.ini</code>.   <b>Main.py</b> is for rendering, sorting our objects. Last file for transfer a database datas. I started write first function <b>config</b>, this function read file database.ini. It is need for <b> starting section postgresql </b>, likewise after rendering this file with received datas we recreate dictionary with datas for entry my <i> PostgreSQL</i>.</p>
<p align="center">
  <img src="https://sun9-61.userapi.com/impg/9gcrTyl9eIp0LWyZNv4f9QhHAy1d89uef0Ms6w/eLsfeCpiD7w.jpg?size=1280x784&quality=96&sign=847254a2f836b56de4d85e2ce5cc9727&type=album">
</p>
<p><b> Function main( ) </b>- which below func. config responsible for main content on the web-server. Inside function we create a place for saving information ( it 'll be dict & arrays. ), thereafter I call a function config( ) to read & open <b> PostgreSQL </b>. I find amount of colums to create a condition ( how many users will be ) & receive header table information. Work done, I returned & execute all information from table to put in dict. .  </p>
<p align="center">
  <img src="https://sun9-87.userapi.com/impg/usU0GJq2GXK8jPBJ87yDLdwAx2qAQcfr1CI0-Q/CWdSAVbzZbU.jpg?size=1280x882&quality=96&sign=10e3fcbd4d5dc5b92b9a6e1bf23f0fc9&type=album">
</p>
