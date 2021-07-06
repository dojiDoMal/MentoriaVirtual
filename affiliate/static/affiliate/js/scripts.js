const root = document.querySelector(".root");
const bg = document.querySelector(".background");
const descriptionTab = document.querySelector("#description-tab");
const profileTab = document.querySelector("#profile-tab");
const contactTab = document.querySelector("#contact-tab");
const positions = [];

if(bg){
  bg.style.top = -480 + "px";
}

if(root){
  root.addEventListener("mousemove", e => {
    var y = -(e.pageY + bg.offsetTop)/40;
    positions.push({y});
    if (positions.length > 2)
      positions.splice(0, 1);
      
    const current = positions.reduce((acc, e) => { acc.y += e.y; return acc }, { y: 0 });
    current.y /= positions.length;
    
    bg.style.transform = `translateY(${current.y}px)`;
  });
}


descriptionTab.addEventListener("click", e => {
  e.preventDefault();
  activate(descriptionTab, profileTab, contactTab);
  activateAndShow(
    document.querySelector('#description'),
    document.querySelector("#profile"),
    document.querySelector("#contact"),
  )
})

profileTab.addEventListener("click", e => {
  e.preventDefault();
  activate(profileTab, descriptionTab, contactTab);
  activateAndShow(
    document.querySelector("#profile"),
    document.querySelector('#description'),
    document.querySelector("#contact"),
  )
})

contactTab.addEventListener("click", e=> {
  e.preventDefault();
  activate(contactTab, descriptionTab, profileTab);
  activateAndShow(
    document.querySelector("#contact"),
    document.querySelector("#profile"),
    document.querySelector('#description'),
  )
})

/** Insere a classe 'active' no elemento passado como primeiro argumento e remove a mesma classe dos outros elementos restantes*/
function activate(...args) {
  args.forEach((arg, index) => {
    if(index == 0){
      arg.classList.add('active');
    } else{
      arg.classList.remove('active');
    }
  });
}

function activateAndShow(...args) {
  args.forEach((arg, index) => {
    if(index == 0){
      arg.classList.add('show');
      arg.classList.add('active');
    } else{
      arg.classList.remove('show');
      arg.classList.remove('active');
    }
  });
}
