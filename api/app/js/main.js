
if(sysInfo != ''){
  sysInfo = sysInfo.replace('%','<br>')
  sysInfo = sysInfo.replace('%','<br>')
  sysInfo = sysInfo.replace('%','<br>')
  sysInfo = sysInfo.replace('%','<br>')

}

sectionInfo = document.getElementById("sysInfo").innerHTML = sysInfo

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

// Ejecución de mostrarPropiedades
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

