import messages from "/app/js/db.json";
const app = new Vue({
  el: "#app",
  data: messages.messages,
  template: `
    <div>
      <p v-for="message in messages"><b>Name: </b>{{message.name}} </br><b>Message: </b>{{message.message}}</br></p>
    </div>
  `
})