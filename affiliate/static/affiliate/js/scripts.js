const root = document.querySelector(".root");
const bg = document.querySelector(".background");

bg.style.top = -480 + "px";

const positions = [];

root.addEventListener("mousemove", e => {
  var y = -(e.pageY + bg.offsetTop)/10;
  positions.push({y});
  if (positions.length > 2)
    positions.splice(0, 1);
    
  const current = positions.reduce((acc, e) => { acc.y += e.y; return acc }, { y: 0 });
  current.y /= positions.length;
  
  bg.style.transform = `translateY(${current.y}px)`;
});