console.log("HEX_SPECTER loaded");

document.addEventListener("mousemove", (e) => {
  document.body.style.filter = `hue-rotate(${e.clientX / 10}deg)`;
});
