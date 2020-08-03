// alert('Funciona JS')
// var mydata = JSON.parse(db);
// import { db } from "../db.js";

// alert(db['v'])
let teclas = []

function mostrarPropiedades(objeto, nombreObjeto) {
  var resultado = ``;
  for (var i in objeto) {
    //objeto.hasOwnProperty se usa para filtrar las propiedades del objeto
    if (objeto.hasOwnProperty(i)) {
        //resultado = `${i}`;
        teclas.push(i)
    }
  }
  return true;
}

let data = []

function getData(objeto){
  for (let index = 0; index < teclas.length; index++) {
    data.push(db[teclas[index]])
  }
  return true
}

// Ejecución de mstrarPropiedades
console.log(mostrarPropiedades(db,"miDB"))
console.log('El array de teclas es : ')
console.log(teclas)

// Ejecución de getData
console.log(getData(data))
console.log(data)

var ctx = document.getElementById("myLineChart").getContext('2d');
var myLineChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels:teclas,
    datasets:[{
      label:'Num datos',
      data:data,
      backgroundColor:
        'rgb(2, 10, 150)'

    }]
  },
  options:{
    scales:{
      yAxes:[{
        ticks:{
          beginAtZero:true
        }
      }]
    }
  }
});

function actualizar(){location.reload(true);}
//Función para actualizar cada 4 segundos(4000 milisegundos)
setInterval("actualizar()",5000);