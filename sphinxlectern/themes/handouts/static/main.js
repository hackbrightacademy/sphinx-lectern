(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
(()=>{"use strict";const t={getLocation:function(){return window.fillinLocationHash?new Promise((t,e)=>{t(window.fillinLocationHash)}):crypto.subtle.digest("SHA-1",(new TextEncoder).encode(window.location)).then(t=>Array.from(new Uint8Array(t)).map(t=>t.toString(16).padStart(2,"0")).join("")).then(t=>(window.fillinLocationHash=t,window.fillinLocationHash))},getItem:function(t,e){return this.getLocation().then(e=>localStorage.getItem([e,t].join("-")))},setItem:function(t,e){return this.getLocation().then(n=>localStorage.setItem([n,t].join("-"),e))}};for(const e of document.querySelectorAll(".fillin"))t.getItem(e.getAttribute("id").split("-").slice(-1)).then(t=>e.value=t),e.addEventListener("blur",e=>{const n=e.target;n.value&&t.setItem(n.getAttribute("id").split("-").slice(-1),n.value)})})();

},{}],2:[function(require,module,exports){
require("./printutils.js"),require("./fillin.js");

},{"./fillin.js":1,"./printutils.js":3}],3:[function(require,module,exports){
(()=>{"use strict";window.addEventListener("beforeprint",e=>{for(const e of document.querySelectorAll("details"))e.setAttribute("open",!0)}),window.addEventListener("afterprint",e=>{for(const e of document.querySelectorAll("details"))e.setAttribute("open",!1)})})();

},{}]},{},[2]);
