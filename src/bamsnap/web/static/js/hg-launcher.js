/* Copyright HiGlass Team: HiGlass Launcher */
!(function(e,t){
	"object"==typeof exports&&"undefined"!=typeof module?t(require("hglib")):"function"==typeof define&&define.amd?define(["hglib"],t):t(e.hglib)})(this,(function(e){"use strict";
function t(e){
	var t=e.split("+").join(" "),n={},i=void 0,r=/[?&]?([^=]+)=([^&]*)/g;
for(i=r.exec(t);i;) n[decodeURIComponent(i[1])]=decodeURIComponent(i[2]),i=r.exec(t);
return n}function n(e,t){var n=Et(e);
document.addEventListener("dragenter",(function(e){return n.addClass("is-dragging-over"),e.stopPropagation(),e.preventDefault(),!1})),document.addEventListener("dragover",(function(e){return e.stopPropagation(),e.preventDefault(),!1})),e.addEventListener("dragleave",(function(e){return"drop-layer"===e.target.id&&n.removeClass("is-dragging-over"),e.stopPropagation(),e.preventDefault(),!1})),document.addEventListener("drop",(function(i){i.preventDefault(),wt(i.target,e)&&t(i),n.removeClass("is-dragging-over")}),!1)}var i=new Function("return this")(),r=function(e){for(var t=e.length,n=new Array(t),i=0;
i<t;
i++)n[i]=e[i];
return n},o=function(e,t,n){var i=e.length;
if(void 0!==i&&void 0===e.nodeType)for(var r=0;
r<i;
r++)t.call(n,e[r],r,e);
else t.call(n,e,0,e);
return e},s=function(e){for(var t=arguments.length,n=Array(t>1?t-1:0),i=1;
i<t;
i++)n[i-1]=arguments[i];
return n.forEach((function(t){for(var n in t)e[n]=t[n]})),e},u=function(e){return e.filter((function(t,n){return e.indexOf(t)===n}))},a=!1,c=/^\s*<(\w+|!)[^>]*>/,f=/^<(\w+)\s*\/?>(?:<\/\1>|)$/,l=/^[\.#]?[\w-]*$/,d=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:document,n=void 0;
if(e){if(e instanceof y)return e;
"string"!=typeof e?n=e.nodeType||e===window?[e]:e:c.test(e)?n=g(e):(t="string"==typeof t?document.querySelector(t):t.length?t[0]:t,n=v(e,t))}else n=document.querySelectorAll(null);
return m(n)},p=function(e){var t=[];
return o(this,(function(n){return o(v(e,n),(function(e){t.indexOf(e)===-1&&t.push(e)}))})),d(t)},h=(function(){var e="undefined"!=typeof Element?Element.prototype:i,t=e.matches||e.matchesSelector||e.mozMatchesSelector||e.msMatchesSelector||e.oMatchesSelector||e.webkitMatchesSelector;
return function(e,n){return t.call(e,n)}})(),v=function(e,t){var n=l.test(e);
if(n){if("#"===e[0]){var i=(t.getElementById?t:document).getElementById(e.slice(1));
return i?[i]:[]}return"."===e[0]?t.getElementsByClassName(e.slice(1)):t.getElementsByTagName(e)}return t.querySelectorAll(e)},g=function(e){if(f.test(e))return[document.createElement(RegExp.$1)];
var t=[],n=document.createElement("div"),i=n.childNodes;
n.innerHTML=e;
for(var r=0,o=i.length;
r<o;
r++)t.push(i[r]);
return t},m=function(e){return a||(y.prototype=d.fn,y.prototype.constructor=y,a=!0),new y(e)},y=function(e){for(var t=0,n=e.length;
t<n;
)this[t]=e[t++];
this.length=n},b=Object.freeze({$:d,find:p,matches:h,Wrapper:y}),E=Array.prototype,w=E.every,N=function(e,t){var n="function"==typeof e?e:function(t){return h(t,e)};
return d(E.filter.call(this,n,t))},C=function(e,t){return o(this,e,t)},O=C,_=E.indexOf,L=E.map,T=E.pop,S=E.push,j=E.reduce,A=E.reduceRight,D=function(){return d(r(this).reverse())},z=E.shift,x=E.some,M=E.unshift,P=Object.freeze({every:w,filter:N,forEach:C,each:O,indexOf:_,map:L,pop:T,push:S,reduce:j,reduceRight:A,reverse:D,shift:z,some:x,unshift:M}),H="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},I=function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")},B=function(e){var t=function e(){I(this,e),y.call(this,d.apply(void 0,arguments))};
return s(t.prototype,e),t},$=function(e){return!isNaN(parseFloat(e))&&isFinite(e)},k=function(e){return e.replace(/-([\da-z])/gi,(function(e,t){return t.toUpperCase()}))},q=function(e){return e.replace(/([a-z\d])([A-Z])/g,"$1-$2").toLowerCase()},R=function(e,t){var n=void 0,i=void 0,r=void 0;
if("string"==typeof e){if(e=k(e),"undefined"==typeof t){var s=this.nodeType?this:this[0];
if(s)return r=s.style[e],$(r)?parseFloat(r):r;
return}n={},n[e]=t}else{n=e;
for(i in n)r=n[i],delete n[i],n[k(i)]=r}return o(this,(function(e){for(i in n)n[i]||0===n[i]?e.style[i]=n[i]:e.style.removeProperty(q(i))})),this},F=Object.freeze({css:R}),U=Array.prototype.forEach,J=function e(t){if(this instanceof Node)if("string"==typeof t)this.insertAdjacentHTML("beforeend",t);
else if(t instanceof Node)this.appendChild(t);
else{var n=t instanceof NodeList?r(t):t;
U.call(n,this.appendChild.bind(this))}else Q(this,e,t);
return this},W=function e(t){if(this instanceof Node)if("string"==typeof t)this.insertAdjacentHTML("afterbegin",t);
else if(t instanceof Node)this.insertBefore(t,this.firstChild);
else{var n=t instanceof NodeList?r(t):t;
U.call(n.reverse(),e.bind(this))}else Q(this,e,t);
return this},K=function e(t){if(this instanceof Node)if("string"==typeof t)this.insertAdjacentHTML("beforebegin",t);
else if(t instanceof Node)this.parentNode.insertBefore(t,this);
else{var n=t instanceof NodeList?r(t):t;
U.call(n,e.bind(this))}else Q(this,e,t);
return this},V=function e(t){if(this instanceof Node)if("string"==typeof t)this.insertAdjacentHTML("afterend",t);
else if(t instanceof Node)this.parentNode.insertBefore(t,this.nextSibling);
else{var n=t instanceof NodeList?r(t):t;
U.call(n.reverse(),e.bind(this))}else Q(this,e,t);
return this},Z=function(){return d(G(this))},G=function(e){return"string"==typeof e?e:e instanceof Node?e.cloneNode(!0):"length"in e?[].map.call(e,(function(e){return e.cloneNode(!0)})):e},Q=function(e,t,n){for(var i=e.length;
i--;
){var r=0===i?n:G(n);
t.call(e[i],r)}},X=Object.freeze({append:J,prepend:W,before:K,after:V,clone:Z,_clone:G,_each:Q}),Y=function(e,t){if("string"==typeof e&&"undefined"==typeof t){var n=this.nodeType?this:this[0];
return n?n.getAttribute(e):void 0}return o(this,(function(n){if("object"===("undefined"==typeof e?"undefined":H(e)))for(var i in e)n.setAttribute(i,e[i]);
else n.setAttribute(e,t)}))},ee=function(e){return o(this,(function(t){return t.removeAttribute(e)}))},te=Object.freeze({attr:Y,removeAttr:ee}),ne=function(e){return e&&e.length&&o(e.split(" "),se.bind(this,"add")),this},ie=function(e){return e&&e.length&&o(e.split(" "),se.bind(this,"remove")),this},re=function(e){return e&&e.length&&o(e.split(" "),se.bind(this,"toggle")),this},oe=function(e){return(this.nodeType?[this]:this).some((function(t){return t.classList.contains(e)}))},se=function(e,t){return o(this,(function(n){return n.classList[e](t)}))},ue=Object.freeze({addClass:ne,removeClass:ie,toggleClass:re,hasClass:oe}),ae=function(e,t){return!(!e||!t||e===t)&&(e.contains?e.contains(t):!!e.compareDocumentPosition&&!(e.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_DISCONNECTED))},ce=Object.freeze({contains:ae}),fe="__DOMTASTIC_DATA__",le=function(e,t){if("string"==typeof e&&"undefined"==typeof t){var n=this.nodeType?this:this[0];
return n&&n[fe]?n[fe][e]:void 0}return o(this,(function(n){n[fe]=n[fe]||{},n[fe][e]=t}))},de=function(e,t){if("string"==typeof e&&"undefined"==typeof t){var n=this.nodeType?this:this[0];
return n&&n?n[e]:void 0}return o(this,(function(n){return n[e]=t}))},pe=Object.freeze({data:le,prop:de}),he=function(e){var t="string"==typeof e?d(e):e;
return J.call(t,this),this},ve=function(){return o(this,(function(e){return e.innerHTML=""}))},ge=function(){return o(this,(function(e){e.parentNode&&e.parentNode.removeChild(e)}))},me=function(){return K.apply(this,arguments).remove()},ye=function(e){return void 0===e?this[0].textContent:o(this,(function(t){return t.textContent=""+e}))},be=function(e){return void 0===e?this[0].value:o(this,(function(t){return t.value=e}))},Ee=Object.freeze({appendTo:he,empty:ve,remove:ge,replaceWith:me,text:ye,val:be}),we=function(e){if("string"!=typeof e){var t=this.nodeType?this:this[0];
return t?t.innerHTML:void 0}return o(this,(function(t){return t.innerHTML=e}))},Ne=Object.freeze({html:we}),Ce=(function(){var e=function(e,t){var n=[];
return o(this,(function(i){for(;
i&&i!==t;
){if(h(i,e)){n.push(i);
break}i=i.parentElement}})),d(u(n))};
return"undefined"!=typeof Element&&Element.prototype.closest?function(t,n){if(n)return e.call(this,t,n);
var i=[];
return o(this,(function(e){var n=e.closest(t);
n&&i.push(n)})),d(u(i))}:e})(),Oe=Object.freeze({closest:Ce}),_e=void 0,Le=function(e,t,n,i,r){var s=this;
"function"==typeof t&&(n=t,t=null);
var u=void 0,a=void 0,c=void 0;
return e.split(" ").forEach((function(f){u=f.split("."),f=u[0]||null,a=u[1]||null,c=Pe(n),o(s,(function(o){if(t&&(c=ke.bind(o,t,c)),r){var s=c;
c=function(r){Te.call(o,e,t,n,i),s.call(o,r)}}o.addEventListener(f,c,i||!1),xe(o).push({eventName:f,handler:n,eventListener:c,selector:t,namespace:a})}))}),this),this},Te=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments[1],n=this,i=arguments[2],r=arguments[3];
"function"==typeof t&&(i=t,t=null);
var s=void 0,u=void 0,a=void 0;
return e.split(" ").forEach((function(e){return s=e.split("."),e=s[0]||null,u=s[1]||null,o(n,(function(n){a=xe(n),o(a.filter((function(n){return!(e&&n.eventName!==e||u&&n.namespace!==u||i&&n.handler!==i||t&&n.selector!==t)})),(function(e){n.removeEventListener(e.eventName,e.eventListener,r||!1),a.splice(a.indexOf(e),1)})),e||u||t||i?0===a.length&&Me(n):Me(n)}))}),this),this},Se=function(e,t,n,i){return Le.call(this,e,t,n,i,1)},je="__domtastic_event__",Ae=1,De={},ze=[],xe=function(e){e[je]||(e[je]=0===ze.length?++Ae:ze.pop());
var t=e[je];
return De[t]||(De[t]=[])},Me=function(e){var t=e[je];
De[t]&&(De[t]=null,e[je]=null,ze.push(t))},Pe=function(e){return function(t){return e.call(this,$e(t))}},He={preventDefault:"isDefaultPrevented",stopImmediatePropagation:"isImmediatePropagationStopped",stopPropagation:"isPropagationStopped"},Ie=function(){return!0},Be=function(){return!1},$e=function(e){if(!e.isDefaultPrevented||e.stopImmediatePropagation||e.stopPropagation){for(var t in He)!(function(t,n,i){e[t]=function(){return this[n]=Ie,i&&i.apply(this,arguments)},e[n]=Be})(t,He[t],e[t]);
e._preventDefault&&e.preventDefault()}return e},ke=function(e,t,n){var i=n._target||n.target,r=Ce.call([i],e,_e)[0];
r&&r!==_e&&(r!==i&&n.isPropagationStopped&&n.isPropagationStopped()||t.call(r,n))},qe=Le,Re=Te,Fe=Object.freeze({on:Le,off:Te,one:Se,getHandlers:xe,clearHandlers:Me,proxyHandler:Pe,delegateHandler:ke,bind:qe,unbind:Re}),Ue=/^(?:mouse|pointer|contextmenu)|click/,Je=/^key/,We=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},i=n.bubbles,r=void 0===i||i,s=n.cancelable,u=void 0===s||s,a=n.preventDefault,c=void 0!==a&&a,f=Ke(e),l=new f(e,{bubbles:r,cancelable:u,preventDefault:c,detail:t});
return l._preventDefault=c,o(this,(function(n){!r||Ye||Ze(n)?Xe(n,l):Ge(n,e,{bubbles:r,cancelable:u,preventDefault:c,detail:t})}))},Ke=function(e){return et?Ue.test(e)?MouseEvent:Je.test(e)?KeyboardEvent:CustomEvent:CustomEvent},Ve=function(e,t){this[0]&&We.call(this[0],e,t,{bubbles:!1,preventDefault:!0})},Ze=function(e){return e===window||e===document||ae(e.ownerDocument.documentElement,e)},Ge=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};
n.bubbles=!1;
var i=new CustomEvent(t,n);
i._target=e;
do Xe(e,i);
while(e=e.parentNode)},Qe=["blur","focus","select","submit"],Xe=function(e,t){Qe.indexOf(t.type)===-1||"function"!=typeof e[t.type]||t._preventDefault||t.cancelable?e.dispatchEvent(t):e[t.type]()};
!(function(){var e=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{bubbles:!1,cancelable:!1,detail:void 0},n=document.createEvent("CustomEvent");
return n.initCustomEvent(e,t.bubbles,t.cancelable,t.detail),n};
e.prototype=i.CustomEvent&&i.CustomEvent.prototype,i.CustomEvent=e})();
var Ye=(function(){var e=!1,t=i.document;
if(t){var n=t.createElement("div"),r=n.cloneNode();
n.appendChild(r),n.addEventListener("e",(function(){e=!0})),r.dispatchEvent(new CustomEvent("e",{bubbles:!0}))}return e})(),et=(function(){try{new window.MouseEvent("click")}catch(e){return!1}return!0})(),tt=Object.freeze({trigger:We,triggerHandler:Ve}),nt=function(e){return/complete|loaded|interactive/.test(document.readyState)&&document.body?e():document.addEventListener("DOMContentLoaded",e,!1),this},it=Object.freeze({ready:nt}),rt=i.$,ot=function(){return i.$=rt,this},st=Object.freeze({noConflict:ot}),ut=function(e){var t=[];
return o(this,(function(n){n.children&&o(n.children,(function(n){(!e||e&&h(n,e))&&t.push(n)}))})),d(t)},at=function(){var e=[];
return o(this,(function(t){return e.push.apply(e,r(t.childNodes))})),d(e)},ct=function(e){return pt.call(this,e,e+1)},ft=function(e){return this[e]},lt=function(e){var t=[];
return o(this,(function(n){(!e||e&&h(n.parentNode,e))&&t.push(n.parentNode)})),d(t)},dt=function(e){var t=[];
return o(this,(function(n){return o(n.parentNode.children,(function(i){i!==n&&(!e||e&&h(i,e))&&t.push(i)}))})),d(t)},pt=function(e,t){return d([].slice.apply(this,arguments))},ht=Object.freeze({children:ut,contents:at,eq:ct,get:ft,parent:lt,siblings:dt,slice:pt}),vt=function(e){return"function"==typeof e},gt=Array.isArray,mt=Object.freeze({isFunction:vt,isArray:gt}),yt={},bt={};
"undefined"!=typeof b&&(bt=d,bt.matches=h,yt.find=p),s(bt,ce,st,mt),s(yt,P,F,te,X,ue,pe,Ee,Ne,Fe,tt,it,Oe,ht),bt.fn=yt,bt.version="__VERSION__",bt.extend=s,"undefined"!=typeof B&&(bt.BaseClass=B(bt.fn));
var Et=bt,wt=function(e,t){
	for(var n=e;n!==t&&"HTML"!==n.tagname;)n=n.parentNode;
	return n===t},Nt=t(document.location.search),Ct=function(t,n,i){document.querySelector(t)&&e.createHgComponent(document.querySelector(t),n,{bounded:i},(function(e){window.higlassApi=e}))};
n(document.body,(function(e){var t=e.dataTransfer.files[0],n=new FileReader;
n.addEventListener("load",(function(e){var t=void 0;
try{t=JSON.parse(e.target.result)}catch(e){console.error("Only drop valid JSON",e)}t&&Ct("#higlass",t,!0)})),n.readAsText(t)}));
var Ot=Nt.config?Nt.config:"default";
Ct("#higlass","/api/v1/viewconfs/?d="+Ot,!0),
Ct("#higlass1","http://higlass.io/api/v1/viewconfs/?d=default",!0),
Ct("#higlass2","http://higlass.io/api/v1/viewconfs/?d=twoviews",!0),
Ct("#higlass3","http://higlass.io/api/v1/viewconfs/?d=browserlike",!1),
Ct("#higlass4","/static/js/test.json",!1),
//Ct("#higlass4","http://higlass.io/api/v1/viewconfs/?d=browserwithdetails",!1),
Ct("#higlass_test1","http://test.higlass.io/api/v1/viewconfs/?d=test_default",!0),
Ct("#higlass_test2","http://test.higlass.io/api/v1/viewconfs/?d=test_twoviews",!0),
Ct("#higlass_test3","http://test.higlass.io/api/v1/viewconfs/?d=test_browserlike",!1),
Ct("#higlass_test4","http://test.higlass.io/api/v1/viewconfs/?d=test_browserwithdetails",!1)
}));

//# sourceMappingURL=hg-launcher.js.map
