!function(e){var n={};function t(o){if(n[o])return n[o].exports;var r=n[o]={i:o,l:!1,exports:{}};return e[o].call(r.exports,r,r.exports,t),r.l=!0,r.exports}t.m=e,t.c=n,t.d=function(e,n,o){t.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:o})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,n){if(1&n&&(e=t(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(t.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)t.d(o,r,function(n){return e[n]}.bind(null,r));return o},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},t.p="",t(t.s=0)}([function(e,n,t){var o=t(1);o.init();var r=o.get();try{!function(){var e={scripts:[{name:"qchoice",loadModule:function(){t(4)}},{name:"adconsent",skipLoadOnExists:!0,loadModule:function(){t(5)},onLoad:{emitEvent:"adnginLoaderReady",scripts:[{name:"pbjs",obj:{que:[]},queue:"que",path:"?v="+escape(r.version)},{name:"apstag",obj:{init:function(){this._Q.push(["i",arguments])},fetchBids:function(){this._Q.push(["f",arguments])},setDisplayBids:function(){},targetingKeys:function(){return[]},_Q:[]}},{name:"gpt",obj:{cmd:[]},queue:"cmd"},{name:"adsbygoogle",obj:[]},{name:"adngin",obj:{queue:[],metrics:{timing:{}}},queue:"queue",path:"/"+escape(r.site)+"/"+escape(r.version)+"/adngin.js"},{name:"scripts",argus:{obj:{cmd:[]},queue:"cmd"}}]}}]},n=window.performance,o=n&&n.now?function(){return Math.floor(n.now())}:function(){return-1};function i(e,t){var r=function(e){if(n&&n.getEntriesByType)for(var t=0;t<n.getEntriesByType("resource").length;t++){var o=n.getEntriesByType("resource")[t];if(e(o.name))return o}return{startTime:-1,responseEnd:-1}}(t);d[e]=d[e]||{},d[e].requested=[Math.floor(r.startTime)],d[e].loaded=[Math.floor(r.responseEnd)],d[e].ready=[o()]}function a(e,n,t){var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.onload=function(){i(e,(function(e){return-1!==e.indexOf(n.toLowerCase())})),r.resources[e].loaded=!0,t&&t()},d[e]=d[e]||{},d[e].queued=[o()],r.resources=r.resources||{},r.resources[e]={scriptElement:a,loaded:!1},a.src=n,document.head.appendChild(a)}function s(e,n,t){e.scripts.forEach((function(e){var o=r.settings[e.name]||{};!Array.isArray(o)&&o.load&&n(o.objName,e),e.onLoad&&e.onLoad.scripts&&t(e.onLoad)}))}function c(e,n){var t=n.obj;if(t)if(window[e]){var o=window[e];for(var r in t)o[r]=o[r]||t[r]}else window[e]=t}function u(e,n){n.queue&&window[e][n.queue].push((function(){d[n.name]=d[n.name]||{},d[n.name].apiReady=[o()]}))}(window.adsbygoogle=window.adsbygoogle||[]).pauseAdRequests=1,window.snigelPubConf=window.snigelPubConf||{},function e(n){s(n,c,e)}(e);var l=window[r.settings.adngin.objName],d=l.metrics.timing;i("loader",(function(e){return/.*snigel.*loader.js$/i.test(e)})),function e(n){s(n,u,e)}(e),function e(n){if(!n)return!1;n.emitEvent&&(window.dispatchEvent(new CustomEvent(n.emitEvent)),l[n.emitEvent]=!0,d.loader[n.emitEvent]=[o()]),n.scripts&&n.scripts.forEach((function(n){var t=r.settings[n.name]||{};if(Array.isArray(t))t.forEach((function(e){if(!e.freq||Math.floor(100*Math.random())<e.freq){var t=e.name,o=n[t]||{};c(t,o),u(t,o),a(e.name||e.url,e.url)}}));else{t.load&&n.loadModule&&n.loadModule();var o=!!window[t.objName];t.load&&t.url&&(!o||o&&!n.skipLoadOnExists)?function(e,n){var t=r.settings[e.name].queryParameters,o=r.settings[e.name].url+(e.path||"")+(t?"?"+t:"");a(e.name,o,n)}(n,(function(){e(n.onLoad)})):e(n.onLoad)}}))}(e)}()}catch(e){if(!0===r.passThroughException)throw e;console.error(e)}},function(e,n,t){function o(e,n){return function(e){if(Array.isArray(e))return e}(e)||function(e,n){var t=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==t)return;var o,r,i=[],a=!0,s=!1;try{for(t=t.call(e);!(a=(o=t.next()).done)&&(i.push(o.value),!n||i.length!==n);a=!0);}catch(e){s=!0,r=e}finally{try{a||null==t.return||t.return()}finally{if(s)throw r}}return i}(e,n)||function(e,n){if(!e)return;if("string"==typeof e)return r(e,n);var t=Object.prototype.toString.call(e).slice(8,-1);"Object"===t&&e.constructor&&(t=e.constructor.name);if("Map"===t||"Set"===t)return Array.from(e);if("Arguments"===t||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))return r(e,n)}(e,n)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function r(e,n){(null==n||n>e.length)&&(n=e.length);for(var t=0,o=new Array(n);t<n;t++)o[t]=e[t];return o}var i=t(2),a=t(3);function s(e,n,t){var o=function(){var o=e.getElementById("sn-session-override-warnings");o||((o=e.createElement("div")).id="sn-session-override-warnings",o.setAttribute("style","background: darkred; position: fixed; bottom: 0; left: 0; right: 0; z-index: 1000000; padding: 0.25em; color: white; font-family: monospace; font-size: small;"),o.innerHTML="(!) Session overrides:",o.addEventListener("mouseover",(function(){this.style.opacity="0.20"})),o.addEventListener("mouseout",(function(){this.style.opacity="1"})),e.body.appendChild(o)),o.innerHTML+=" ("+n+":"+t+")"},r=e.readyState;if("interactive"===r||"complete"===r)o();else{e.addEventListener("DOMContentLoaded",(function n(){e.removeEventListener("DOMContentLoaded",n,!1),o()}),!1)}}n.init=function(){try{for(var e in window._snigelConfig=window._snigelConfig||{},a)"exp"!=e&&(window._snigelConfig[e]=a[e]);var n=window.localStorage;if(a.exp){var t,r,c=o((n.getItem("_sn_exp")||"").split(";"),2);t=c[0],r=c[1],t!=a.cfgVer&&(t=a.cfgVer,r=i.undefined),a.exp.some((function(e){if(r==e.id||r==i.undefined&&Math.random()<e.freq){var n="exp="+(r=e.id),t=e.settings.adngin.queryParameters;return e.settings.adngin.queryParameters=t?t+"&"+n:n,window._snigelConfig.settings=e.settings,!0}return!1}))||(r=0),n.setItem("_sn_exp",t+";"+r)}else n.removeItem("_sn_exp");var u=JSON.parse(window.sessionStorage.getItem("snSessionOverrides"));if(null!==u)for(var l in u){var d=u[l];a.settings[l].url=d.url,a.settings[l].overrideBranch=d.branch,console.warn("Override detected. Loading '"+l+"' branch '"+d.branch+"'."),s(document,l,d.branch)}}catch(e){}},n.get=function(){return window._snigelConfig||{}}},function(e,n){n.undefined=void 0},function(e){e.exports=JSON.parse('{"site":"w3schools.com","version":"5482-1669131563816","cfgVer":"6225","settings":{"adconsent":{"load":true,"objName":"adconsent","url":"//cdn.snigelweb.com/adconsent/adconsent.js"},"pbjs":{"load":true,"objName":"pbjs","url":"//cdn.snigelweb.com/prebid/7.17.0/prebid.js"},"gpt":{"load":true,"objName":"googletag","url":"//securepubads.g.doubleclick.net/tag/js/gpt.js"},"adngin":{"load":true,"objName":"adngin","url":"//adengine.snigelweb.com"},"apstag":{"load":true,"objName":"apstag","url":"//c.amazon-adsystem.com/aax2/apstag.js"},"scripts":[{"url":"//cdn.snigelweb.com/argus/argus.js","freq":100,"name":"argus"},{"url":"//boot.pbstck.com/v1/tag/6b8021b6-6874-4ef7-a983-9bb3141ccb5c","freq":5,"name":"pubstack"}]}}')},function(e,n){},function(e,n,t){"use strict";function o(e){return(o="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function r(e){return(r="function"==typeof Symbol&&"symbol"==o(Symbol.iterator)?function(e){return o(e)}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":o(e)})(e)}!function(e,n,t,o,i,a){var s=e._snigelConfig;if(s)try{t=s.settings.adconsent.objName}catch(e){}var c=void 0,u="__"+t;try{a=localStorage}catch(e){}var l,d=e.performance,f=d&&d.now?function(){return Math.floor(d.now())}:function(){return 0};function p(e){if(window.argus){var n=1===e.length&&e[0]instanceof Error?{stack:e[0].stack}:{log:e,stack:(new Error).stack};window.argus.cmd.push((function(){window.argus.queueError("adconsent",n)}))}}!function(){if("function"===r(e.CustomEvent))return!1;function t(e,t){t=t||{bubbles:!1,cancelable:!1,detail:c};var o=n.createEvent("CustomEvent");return o.initCustomEvent(e,t.bubbles,t.cancelable,t.detail),o}t.prototype=e.Event.prototype,e.CustomEvent=t}();try{var g=function(n,t,o,r){e.console[n]&&L.level>=t&&console[n].apply(console,function(e,n,t){return e=[].slice.call(e),n&&e.unshift(n),e.unshift("display: inline-block; color: #fff; background: "+t+"; padding: 1px 4px; border-radius: 3px;"),e.unshift("%cAdConsent"),e}(o,n.toUpperCase()+":",r))},v=function(e,n){return{region:e,loaded:!1,applies:c,version:n,status:"stub"}},m=function(n){return function(t,o,r){e[n](t,c,r,o)}},b=function(e,n,t){return!n||n===e.version||(C(t,null,!1),x("Wrong framework version detected: "+n),!1)},y=function(e,n,t){var o=M.applies?c:M.applies,r={tcString:c,tcfPolicyVersion:2,cmpId:229,cmpVersion:71,gdprApplies:o,eventStatus:!1===o?"tcloaded":c,cmpStatus:M.status,listenerId:n,isServiceSpecific:!0,useNonStandardStacks:!1,publisherCC:j.publisherCC,purposeOneTreatment:!1};x("Sending TCData structure:",r,t),C(t,r,!0)},h=function(e,n,t,o,r){e.queue.push({command:n,version:t,parameter:o,callback:r})},w=function(t,o,i){if(i){var a=t+"Locator";!function t(){if(!e.frames[a]){var o=n.body;if(o){var r=n.createElement("iframe");r.style.display="none",r.name=a,o.appendChild(r)}else setTimeout(t,5)}}();var s=function(n){var o=n.data,r="string"==typeof o;try{var i=(r?JSON.parse(o):o)[t+"Call"];i&&e[t](i.command,i.version,(function(e,o){try{if(n&&n.source&&n.source.postMessage){var a={};a[t+"Return"]={returnValue:e,success:o===c||o,callId:i.callId},n.source.postMessage(r?JSON.stringify(a):a,"*")}}catch(e){}}),i.parameter)}catch(e){}}}"function"!==r(e[t])&&(e[t]=function(n,r,i,a){var s=e[t];if(s.queue){for(var c in o)if(n===c){var u=!0;(0,o[c])(s,n,r,i,a);break}u||h(s,n,r,a,i)}else s(n,r,i,a)},e[t].queue=[],i&&(e.addEventListener?e.addEventListener("message",s,!1):e.attachEvent("onmessage",s)))},C=function(e,n,t){e&&"function"==typeof e&&setTimeout((function(){e(n,t)}),0)},E=function(n,t,o,r,a){if(A.region===c)if(O[a]){for(var s in T){var u=T[s];u.applies=u.region==a,u.applies?G=s:(u.loaded=!0,u.status="loaded")}A.region=a,q("Configured consent region "+O[a]),function(){if(1!==A.region&&S.processListeners(y),2!==A.region){var n=e[i],t=n.queue;if(t){n.queue=[];for(var o=0;o<t.length;o++){var r=t[o];n(r.command,r.version,r.callback,r.parameter)}}}}()}else k("Incorrect consent region "+a)},_=m(u);_.gdpr=m("__tcfapi");var S=_.gdpr;S.listenerId=1,S.tcfListeners=[],S.addEventListener=function(e,n,t){if(b(M,e,n)){x("Adding event listener "+S.listenerId,n);var o={id:S.listenerId++,callback:n||function(){}};S.tcfListeners.push(o),t(null,o.id,o.callback)}},S.removeEventListener=function(e,n,t,o,r){if(b(M,t,o)){x("Removing event listener "+r);for(var i=0;i<S.tcfListeners.length;i++)if(S.tcfListeners[i].id==r)return S.tcfListeners.splice(i,1),void C(o,!0);I("Couldn't find listener id "+r+"."),C(o,!1)}},S.getTCData=function(e,n,t,o){b(M,t,o)&&y(0,0,o)},S.processListeners=function(e){for(var n=S.tcfListeners.slice(),t=0;t<n.length;t++)e(null,n[t].id,n[t].callback)},_.ccpa=m(i),_.version=71,_.cmpId=229,_.cfg={apiBaseUrl:"https://cdn.snigelweb.com/adconsent/71",publisherCC:"US"};var j=_.cfg;_.log={levels:{off:0,error:1,warning:2,info:3,debug:4},level:2,error:function(){p(arguments),g("error",1,arguments,"#ff0000")},warn:function(){g("warn",2,arguments,"#ffe600")},info:function(){g("info",3,arguments,"#3b88a3")},debug:function(){g("debug",4,arguments,"#808080")}};var L=_.log,x=L.debug,q=L.info,I=L.warn,k=L.error;_.consent={regions:{0:"NONE",1:"GDPR",2:"CCPA"},region:c,api:{__tcfapi:v(1,2),__uspapi:v(2,1)}};var A=_.consent,O=A.regions,T=A.api,M=T.__tcfapi,N=T[i];_.analytics={enabled:!1,callback:c,send:function(e){P.sendEvent(O[A.region],e,f())},sendEvent:function(n,t,o){q("Sending analytics event action"+(P.enabled?"":" disabled")+": "+n+", label: "+t+", value: "+o),P.enabled&&(P.callback||function(n){e.gtag?gtag("event",n.action,{event_category:n.category,event_label:n.label,event_value:n.value}):e.ga?ga("send",{hitType:"event",eventCategory:n.category,eventAction:n.action,eventLabel:n.label,eventValue:n.value,nonInteraction:n.nonInteraction}):I("Unable to find Google Analytics module (gtag or ga).")})({category:"AdConsent",action:n,label:t||n,value:o||0,nonInteraction:!0})}};var P=_.analytics,D=P.send;_.event={fired:{},dispatchCustomEvent:function(e,t,o){o&&B[e]||(B[e]=!0,x("Emitting custom event "+e+" with details: ",t),n.dispatchEvent(new CustomEvent(e,t)))},dispatchCustomEventConsent:function(e,n){var t={0:"N/A",1:"NoConsent",2:"PartialConsent",3:"FullConsent"};D(t[n]),1==A.region&&0!=e&&D("Publisher"+t[e]),V.dispatchCustomEvent("cmpConsentAvailable",{detail:{consentSummary:{mapping:{0:"not available",1:"no consent",2:"partial consent",3:"full consent"},publisherConsent:e,vendorsConsent:n,gdprApplies:M.applies,uspApplies:N.applies}}})}};var V=_.event,B=V.fired,R=(l=e.location.search)?l.replace(/^\?/,"").split("&").reduce((function(e,n){var t=n.split("="),o=t[0],r=t.length>1?t[1]:c;return/\[\]$/.test(o)?(e[o=o.replace("[]","")]=e[o]||[],e[o].push(r)):e[o]=r||"",e}),{}):{},U=("true"==R.sn_debug?"debug":null)||("true"==R.adconsent_debug?"debug":null)||R.adconsent_log;if(L.level=L.levels[U]||L.level,e[t])return void k("Stub is tried to load again!");if(e.__tcfapi||e[i])return void I("A cmp is already registered in the system. AdConsent is stopping.");e[t]=_;var G=c,J=!1;w("__tcfapi",{ping:function(e,n,t,o){var r={gdprApplies:M.applies,cmpLoaded:M.loaded,cmpStatus:M.status,displayStatus:"disabled",apiVersion:"2.0",cmpVersion:71,cmpId:229,gvlVersion:c,tcfPolicyVersion:2};C(o,r,!0)},getTCData:S.getTCData,addEventListener:function(e,n,t,o,r){S.addEventListener(t,o,y)},removeEventListener:S.removeEventListener},!0),w(i,{getUSPData:function(e,n,t,o,r){!1===N.applies?b(N,t,o)&&C(o,{version:1,uspString:"1---"},!0):h(e,n,t,r,o)}},!0),w(u,{start:function t(o,r,i,s,u){if(A.region!==c){if(!J)if(J=!0,0==A.region)V.dispatchCustomEventConsent(3,3);else if(G){var l=n.createElement("script");l.type="text/javascript",l.async=!0,l.charset="utf-8",l.src=_.cfg.apiBaseUrl+"/adconsent"+G+".js",n.head.appendChild(l)}}else!function(n){var t=null;if(a){var o=a.getItem("snconsent_geo");if(o){var r=a.getItem("snconsent_geo_exp");if(r)try{parseInt(r)>=(new Date).getTime()&&(t=JSON.parse(e.atob(o)))}catch(e){}}}if(t)n(t);else{var i=new XMLHttpRequest;i.open("GET","https://pro.ip-api.com/json/?fields=57354&key=33arzTfj1gigDqW"),i.timeout=5e3,i.onload=function(){var t=i.responseText.toLowerCase();a&&(a.setItem("snconsent_geo",e.btoa(t)),a.setItem("snconsent_geo_exp",(new Date).getTime()+36e5)),n(JSON.parse(t))},i.onerror=i.ontimeout=function(){n(null)},i.send()}}((function(e){var n=e?e.countrycode:null;"us"===n&&"california"===e.regionname?E(0,0,0,0,2):-1!=="at be bg hr cy cz dk ee fi fr de gr hu is ie it lv li lt lu mt nl no pl pt ro sk si es se gb".indexOf(n)?E(0,0,0,0,1):(n||(D("ErrorGeotargeting"),k("Geotargeting failed")),E(0,0,0,0,0)),t()}))},setPublisherCC:function(e,n,t,o,r){"string"!=typeof r||2!=r.length?C(o,{message:"Invalid publisher country code detected. Ignoring call."},!1):(j.publisherCC=r.toUpperCase(),C(o,null,!0))},setConsentRegion:E,enableGoogleAnalytics:function(e,n,t,o,r){P.enabled=r===c||!!r,P.callback=o}})}catch(e){if(p(e),s&&s.passThroughException)throw e;console.error(e)}}(window,document,"adconsent",0,"__uspapi")}]);/*
  Common dependencies
  Version: 1.0.0
*/

/* js-cookie v3.0.0-rc.1 | MIT */
!function (e, t) { "object" == typeof exports && "undefined" != typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define(t) : (e = e || self, function () { var n = e.Cookies, r = e.Cookies = t(); r.noConflict = function () { return e.Cookies = n, r } }()) }(this, function () { "use strict"; function e(e) { for (var t = 1; t < arguments.length; t++) { var n = arguments[t]; for (var r in n) e[r] = n[r] } return e } var t = { read: function (e) { return e.replace(/(%[\dA-F]{2})+/gi, decodeURIComponent) }, write: function (e) { return encodeURIComponent(e).replace(/%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g, decodeURIComponent) } }; return function n(r, o) { function i(t, n, i) { if ("undefined" != typeof document) { "number" == typeof (i = e({}, o, i)).expires && (i.expires = new Date(Date.now() + 864e5 * i.expires)), i.expires && (i.expires = i.expires.toUTCString()), t = encodeURIComponent(t).replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent).replace(/[()]/g, escape), n = r.write(n, t); var c = ""; for (var u in i) i[u] && (c += "; " + u, !0 !== i[u] && (c += "=" + i[u].split(";")[0])); return document.cookie = t + "=" + n + c } } return Object.create({ set: i, get: function (e) { if ("undefined" != typeof document && (!arguments.length || e)) { for (var n = document.cookie ? document.cookie.split("; ") : [], o = {}, i = 0; i < n.length; i++) { var c = n[i].split("="), u = c.slice(1).join("="); '"' === u[0] && (u = u.slice(1, -1)); try { var f = t.read(c[0]); if (o[f] = r.read(u, f), e === f) break } catch (e) { } } return e ? o[e] : o } }, remove: function (t, n) { i(t, "", e({}, n, { expires: -1 })) }, withAttributes: function (t) { return n(this.converter, e({}, this.attributes, t)) }, withConverter: function (t) { return n(e({}, this.converter, t), this.attributes) } }, { attributes: { value: Object.freeze(o) }, converter: { value: Object.freeze(r) } }) }(t, { path: "/" }) });

/* Base64Decode@base64.js | https://gist.github.com/chrisveness/e121cffb51481bd1c142 | MIT */
function Base64Decode(r) { if (!/^[a-z0-9+/]+={0,2}$/i.test(r) || r.length % 4 != 0) throw Error("Not base64 string"); for (var t, e, n, o, h, a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", i = [], f = 0; f < r.length; f += 4)t = (h = a.indexOf(r.charAt(f)) << 18 | a.indexOf(r.charAt(f + 1)) << 12 | (n = a.indexOf(r.charAt(f + 2))) << 6 | (o = a.indexOf(r.charAt(f + 3)))) >>> 16 & 255, e = h >>> 8 & 255, h = 255 & h, i[f / 4] = String.fromCharCode(t, e, h), 64 == o && (i[f / 4] = String.fromCharCode(t, e)), 64 == n && (i[f / 4] = String.fromCharCode(t)); return r = i.join("") }

if (typeof window.atob === 'undefined') {
  window.atob = Base64Decode;
}/*
  MyLearning script
  Version: 1.0.11
*/

window.MyLearning = {
  pages_read_count: 0,
  total_pages_count: 0,
  user_progress_collected: false,
  _debug: null,
  _version: null,
  _user_is_logged_in: null,
};

MyLearning._isDebugMode = function () {
  if (this._debug !== null) {
    return this._debug;
  }

  this._debug = Cookies.get('my_learning.debug')

  if (typeof this._debug === 'undefined' || this._debug === null) {
    this._debug = false;
  }

  return this._debug === true || this._debug === 'true';
}

MyLearning.getCurrentUts = function () {
  return Math.round((new Date()).getTime() / 1000);
};

MyLearning.getCurrentUtus = function () {
  return (new Date()).getTime();
};

MyLearning.log = function (message, data) {
  if (this._isDebugMode()) {
    if (typeof data === 'undefined') {
      console.log(getCurrentUtus().toString() + ' MyLearning -> ' + message);
    } else {
      console.log(getCurrentUtus().toString() + ' MyLearning -> ' + message, data);
    }
  }
}

MyLearning._cacheVersion = function () {
  // return cached result
  if (this._version !== null) {
    this.log('version: ', this._version);
    return this._version;
  }

  this._version = Cookies.get('my_learning.version')

  // fallback to v2.1
  if (typeof this._version === 'undefined' || !this._version) {
    this._version = '2.1';
  }

  this.log('version: ', this._version);
  return this._version;
}

MyLearning._version_to_base_url_map = {
  '1': 'https://mypage.w3schools.com',
  '1.5': 'https://my-learning.w3schools.com',
  '1.5L': 'https://my-learning-legacy.w3schools.com',
  '2': 'https://myl-api.w3schools.com',
  '2.1': 'https://myl-api.w3schools.com'
}

MyLearning._version_and_name_to_rel_url_map = {
  '1': {
    'api.meta': '/mypage/beta.php',
    'api.meta_for_default': '/mypage/beta_for_default.php',
    'api.exercise.get': '/mypage/get_exercise_obj2.php',
    'api.exercise.set': '/mypage/set_exercise_obj.php',
    'api.quiz.set_score': '/mypage/set_quiz_score2.php'
  },
  '1.5': {
    'api.meta': '/api/meta/',
    'api.meta_for_default': '/api/meta-for-default/',
    'api.exercise.get': '/api/exercise/get/',
    'api.exercise.set': '/api/exercise/set/',
    'api.quiz.set_score': '/api/quiz/set-score/'
  },
  '1.5L': {
    'api.meta': '/api/meta/',
    'api.meta_for_default': '/api/meta-for-default/',
    'api.exercise.get': '/api/exercise/get/',
    'api.exercise.set': '/api/exercise/set/',
    'api.quiz.set_score': '/api/quiz/set-score/'
  },
  '2': {
    'api.meta': '/api/classic/get-set-topic-progress',
    // 'api.meta_for_default': '/api/meta-for-default/', // deprecated
    'api.exercise.get': '/api/classic/get-exercises-progress',
    'api.exercise.set': '/api/classic/set-exercises-progress',
    'api.quiz.set_score': '/api/classic/set-quiz-progress'
  },
  '2.1': {
    'api.meta': '/api/classic/get-set-topic-progress',
    'api.exercise.get': '/api/classic/get-exercises-progress',
    'api.exercise.set': '/api/classic/set-exercises-progress',
    'api.quiz.set_score': '/api/classic/set-quiz-progress'
  }
}

// usage:
// MyLearning.getUrl('api.quiz.set_score') -> https://mypage.w3schools.com/mypage/set_quiz_score2.php
MyLearning.getUrl = function (api_name, version) {
  this.log('getUrl: ', api_name);

  if (typeof version === 'undefined') {
    this._cacheVersion();

    version = this._version;
  }

  if (this._isDebugMode()) {
    if (typeof this._version_to_base_url_map[version] === 'undefined') {
      console.warn('MyLearning -> Version is not valid. version: ', version);

      return '/';
    }

    if (typeof this._version_and_name_to_rel_url_map[version][api_name] === 'undefined') {
      console.warn('MyLearning -> Api name is not valid. version, api_name: ', version, api_name);

      return '/';
    }
  }

  return this._version_to_base_url_map[version] + this._version_and_name_to_rel_url_map[version][api_name];
}

MyLearning.userSessionIsPresent = function () {
  var cognitoCfg = getCognitoConfig();

  var userSessionVerificationRes = verifyUserSession(
    cognitoCfg,
    Cookies.get('userSession'),
    Cookies.get('accessToken'),
  );
  this.log('userSessionIsPresent -> userSessionVerificationRes: ', userSessionVerificationRes);

  if (
    userSessionVerificationRes.error.code !== '0'
    && userSessionVerificationRes.error.code !== 'USNF'
  ) { // session is present but not valid -> refresh
    refreshUserSessionViaRedirect(window.location.href); // redirect to profile then refresh and bring the user back to current location
  }

  return userSessionVerificationRes.error.code === '0' && !userSessionVerificationRes.data.expired;
}

MyLearning.userIsLoggedIn = function () {
  if (this._user_is_logged_in === null) { // cache the bool value
    this._user_is_logged_in = this.userSessionIsPresent();
  }

  this.log('userIsLoggedIn: ', this._user_is_logged_in);

  return this._user_is_logged_in;
}

// << classic

// < common

MyLearning.makePostRequest = function (url, data, callback) {
  var xhr = new XMLHttpRequest();

  var reqRes = {
    error: {
      code: '0'
    },
    status: 0,
    dataStr: '',
  };

  var reqTimeout = setTimeout(function () {
    reqRes.error = {
      code: 'RWTE',
      description: 'Request wait time exceeded'
    };

    MyLearning.log('MyLearning.makePostRequest -> reqRes: ', reqRes);

    callback(reqRes);
  }, 15000);

  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      clearTimeout(reqTimeout);

      reqRes.status = this.status;
      reqRes.dataStr = this.responseText;

      if (
        typeof reqRes.status !== 'undefined'
        && reqRes.status
      ) {
        if (reqRes.status == 401) {
          reqRes.error = {
            code: 'UNAUTHORIZED',
            description: 'Request unauthorized'
          };
        } else if (!(reqRes.status >= 200 && reqRes.status < 300)) {
          reqRes.error = {
            code: 'RSC_' + reqRes.status,
            description: (typeof this.statusText !== 'undefined' && this.statusText) ? this.statusText : 'Request failed'
          };
        }
      } else {
        reqRes.error = {
          code: 'RTWNSC', // Request terminated with no status code
          description: 'Request failed'
        };
      }

      callback(reqRes);

      if (reqRes.error.code === 'UNAUTHORIZED') {
        refreshUserSessionViaRedirect(window.location.href); // redirect to profile then refresh and bring the user back to current location
      }
    }
  };

  xhr.open('POST', url, true);
  xhr.withCredentials = true;
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhr.send(data);
}

MyLearning.elmIsInViewport = function (x) {
  var rect = x.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /* or $(window).height() */
    rect.right <= (window.innerWidth || document.documentElement.clientWidth) /* or $(window).width() */
  );
}

MyLearning.elmIsAboveViewport = function (x) {
  var rect = x.getBoundingClientRect();
  if (rect.top < 0) return true;
  return false;
}

MyLearning.getCircleMeta = function (xx, yy, r, aD) {
  var aR = (aD - 90) * Math.PI / 180.0;
  return {
    x: xx + (r * Math.cos(aR)),
    y: yy + (r * Math.sin(aR))
  };
}

MyLearning.getProfileIconCirclesRendered = function (x, y, r, sa, ea) {
  var s = this.getCircleMeta(x, y, r, ea);
  var e = this.getCircleMeta(x, y, r, sa);
  var f = ea - sa <= 180 ? "0" : "1";
  return ["M", s.x, s.y, "A", r, r, 0, f, 0, e.x, e.y].join(" ");
}

MyLearning.loadUser = function (context) {
  this.log('loadUser -> args: ', [context]);

  if (context === 'default') {
    this._loadUser();
  } else if (context === 'footer') {
    this._footerLoadUser();
  }
}

MyLearning.renderAnonymousUser = function () {
  this.log('renderAnonymousUser');

  var a = document.getElementById("mypagediv");
  var b = document.getElementById("w3loginbtn");
  if (a) a.style.display = "none";
  if (b) b.style.display = "inline";
}

MyLearning.getStrWithPrefixRemoved = function (str, subStr) {
  const extractedChunk = str.slice(0, subStr.length);

  if (extractedChunk === subStr) {
    return str.slice(subStr.length);
  }

  return str;
}
// > common

// < default
MyLearning._loadUser = function () {
  if (this.userIsLoggedIn()) {
    this.renderActiveUserLite("B", {});
  } else {
    this.renderAnonymousUser();
  }
}

MyLearning.renderActiveUserLite = function (cc, obj) {
  this.log('renderActiveUserLite -> args: ', [cc, obj]);

  var x, degrees = 0, txt = "", txt2 = "", color1 = "rgba(76, 175, 80, 0.1)", color2 = "rgba(76, 175, 80, 1)";
  var a = document.getElementById("w3loginbtn");
  var b = document.getElementById("mypagediv");
  if (a) a.style.display = "none";
  if (b) {
    //document.getElementById("loginactioncontainer").style.marginLeft =  "0";
    if (cc == "Q") {
      color1 = "rgba(44, 156, 202, 0.1)";
      color2 = "rgba(44, 156, 202, 1)";
    }
    b.style.display = "block";
    txt += "<a href='https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F'>";
    //txt += "<a href='https://mypage.w3schools.com/mypage/default.php'>";
    txt += "<img src='/images/mypagelogo32x32.png' alt='MyLearning' style='position:absolute;top:18px;right:28px'>";
    txt += '<svg style="position:absolute;top:0;right:0;height:70px;width:70px">';
    txt += '<path id="mypage_circle1" fill="none" stroke="' + color1 + '" stroke-width="4"/>';
    txt += '<path id="mypage_circle2" fill="none" stroke="' + color2 + '" stroke-width="4"/>';
    txt += '</svg>';
    txt += '</a>';
    b.innerHTML = "&nbsp;" + txt;
    document.getElementById("mypage_circle1").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, 359.99));
    document.getElementById("mypage_circle2").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, degrees));
  }
}
// > default

// < footer
MyLearning._footerLoadUser = function () { // on lessons this is the first request, on quiz the only one
  this.log('_footerLoadUser');

  if (!this.userIsLoggedIn()) {
    this.renderAnonymousUser();
    return;
  }

  var urlPath = window.location.pathname,
    urlPathWlo = this.getStrWithPrefixRemoved(urlPath, '/'), // wlo - without leading slash
    isQuizPage = false;

  if (urlPathWlo.indexOf('quiztest/quiztest') === 0) {
    isQuizPage = true;

    var pathMetaStr = sessionStorage.getItem(urlPath);

    if (pathMetaStr !== null) {
      var pathMeta = JSON.parse(pathMetaStr);

      if (pathMeta.isQuizPage) {
        this.renderActiveUserWithProgress(pathMeta.reqRes.type, pathMeta.reqRes.raw);
        return;
      }
    }
  }

  // show the user active session first and update the progress when we have it on hands
  this.renderActiveUserWithProgress('T', 'T{"a":0,"b":0}'); // T - unused state, stands for "Temporary/Transitory"

  var x, y, pos, foldername, filename, typ, cc, pathname = window.location.pathname;
  if (pathname.substr(0, 1) == "/") { pathname = pathname.substr(1); }
  pos = pathname.indexOf("/");
  foldername = pathname.substr(0, pos);
  if (pathname.indexOf("pandas") > -1) { foldername = "python/pandas"; }
  if (pathname.indexOf("numpy") > -1) { foldername = "python/numpy"; }
  if (pathname.indexOf("scipy") > -1) { foldername = "python/scipy"; }
  filename = pathname.substr(pos + 1);
  typ = foldername;
  if (foldername == "quiztest") {
    cc = window.location.href;
    pos = cc.indexOf("qtest=");
    typ = cc.substr(pos + 6);
  }

  var reqDataStr = "a=" + foldername + "&b=" + filename + "&c=" + typ + "&d=0&p=" + encodeURIComponent(window.location.pathname);

  MyLearning.makePostRequest(
    MyLearning.getUrl('api.meta'),
    reqDataStr,
    function (reqRes) {
      if (
        reqRes.error.code === '0'
        && reqRes.status === 200
      ) {
        var y = reqRes.dataStr;
        var x = y.substr(0, 1);

        MyLearning.log('_footerLoadUser -> req_res -> x: ', x);

        if (x == "F" || x == "G" || x == "H" || x == "I" || x == "J" || x == "K" || x == "L" || x == "M" || x == "Q") {
          MyLearning.user_progress_collected = true;
          MyLearning.renderActiveUserWithProgress(x, y); // this one sets the scroll event

          if (isQuizPage) {
            sessionStorage.setItem(urlPath, JSON.stringify({
              'isQuizPage': true,
              'reqRes': {
                'type': x,
                'raw': y
              }
            }));
          }
        }
      }
    }
  );
}

MyLearning.checkIfGotToTheBottomOfThePage = function () {
  var a = document.getElementById("mypagediv2");
  var elm_in_or_above_viewport = MyLearning.elmIsInViewport(a) || MyLearning.elmIsAboveViewport(a);
  // this.log('checkIfGotToTheBottomOfThePage: ', elm_in_or_above_viewport);

  if (elm_in_or_above_viewport) {
    MyLearning.log('checkIfGotToTheBottomOfThePage: ', true);

    window.removeEventListener("scroll", MyLearning.checkIfGotToTheBottomOfThePage);
    MyLearning.finishedPage();
  }
}

MyLearning.renderActiveUserWithProgress = function (cc, obj) {
  this.log('renderActiveUserWithProgress -> args: ', [cc, obj]);

  var x, degrees = 0, txt = "", txt2 = "", color1 = "rgba(76, 175, 80, 0.1)", color2 = "rgba(76, 175, 80, 1)", jsonobj;
  var a = document.getElementById("w3loginbtn");
  var b = document.getElementById("mypagediv");
  var c = document.getElementById("mypagediv2");
  if (a) a.style.display = "none";
  if (b) {
    if (cc == "I" || cc == "J" || cc == "H" || cc == "G" || cc == "O" || cc == "Q") {
      jsonobj = JSON.parse(obj.substr(1));
      this.pages_read_count = jsonobj.b;
      this.total_pages_count = jsonobj.a;
      x = Math.round((this.pages_read_count / this.total_pages_count) * 100);
      degrees = x * 3.6;
      if (degrees > 359) degrees = 359.99;
    }
    if (cc == "Q") {
      color1 = "rgba(44, 156, 202, 0.1)";
      color2 = "rgba(44, 156, 202, 1)";
    }
    b.style.display = "block";
    txt += "<a href='https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F'>";
    //  txt += "<a href='https://mypage.w3schools.com/mypage/default.php'>";
    txt2 = txt;
    txt += "<img src='/images/mypagelogo32x32.png' alt='MYPAGE' style='position:absolute;top:18px;right:28px'>";
    txt2 += "<img src='/images/mypagelogo32x32.png' alt='MYPAGE' style='position:absolute;top:18px;margin-left:10px;xright:28px'>";
    if (cc != "F") {
      txt += '<svg style="position:absolute;top:0;right:0;height:70px;width:70px">';
      txt += '<path id="mypage_circle1" fill="none" stroke="' + color1 + '" stroke-width="4"/>';
      txt += '<path id="mypage_circle2" fill="none" stroke="' + color2 + '" stroke-width="4"/>';
      txt += '</svg>';
      txt2 += '<svg style="position:absolute;xtop:0;xright:0;height:70px;width:70px">';
      txt2 += '<path id="mypage2_circle1" fill="none" stroke="' + color1 + '" stroke-width="4"/>';
      txt2 += '<path id="mypage2_circle2" fill="none" stroke="' + color2 + '" stroke-width="4"/>';
      txt2 += '</svg>';
    }
    if (cc == "J" || cc == "H" || cc == "G") {
      window.addEventListener("scroll", this.checkIfGotToTheBottomOfThePage);
      this.checkIfGotToTheBottomOfThePage();
    }
    if (cc == "Q") {
      if (degrees == 359.99) {
        txt += "<span id='usergetsstar'>&#x2605;</span>";
      }
    }
    txt += '</a>';
    txt2 += '</a>';
    b.innerHTML = "&nbsp;" + txt;
    c.innerHTML = "&nbsp;" + txt2;
    if (cc != "L" && cc != "F") {
      document.getElementById("mypage_circle1").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, 359.99));
      document.getElementById("mypage_circle2").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, degrees));
      document.getElementById("mypage2_circle1").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, 359.99));
      document.getElementById("mypage2_circle2").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, degrees));
    }
  }

  // ga('send', 'event', 'user', 'login');
}

MyLearning.finishedPage = function () {
  this.log('finishedPage');

  if (!this.userIsLoggedIn() || !this.user_progress_collected) {
    this.log('finishedPage -> jumping out');
    return;
  }

  var x, y, pos, foldername, filename, typ, pathname = window.location.pathname;
  if (pathname.substr(0, 1) == "/") { pathname = pathname.substr(1); }
  pos = pathname.indexOf("/");
  foldername = pathname.substr(0, pos);
  if (pathname.indexOf("pandas") > -1) { foldername = "python/pandas"; }
  if (pathname.indexOf("numpy") > -1) { foldername = "python/numpy"; }
  if (pathname.indexOf("scipy") > -1) { foldername = "python/scipy"; }
  filename = pathname.substr(pos + 1);
  typ = foldername;

  var reqDataStr = "a=" + foldername + "&b=" + filename + "&c=" + typ + "&d=1&p=" + encodeURIComponent(window.location.pathname);

  MyLearning.makePostRequest(
    MyLearning.getUrl('api.meta'),
    reqDataStr,
    function (reqRes) {
      if (
        reqRes.error.code === '0'
        && reqRes.status === 200
      ) {
        var y = reqRes.dataStr;
        var x = y.substr(0, 1);

        if (x == "O") {
          MyLearning.registerPointForFinishedPage(x);
        }
      }
    }
  );
}

MyLearning.registerPointForFinishedPage = function (cc) {
  MyLearning.log('registerPointForFinishedPage -> args: ', [cc]);

  var x, degrees = 0, txt = "", txt2 = "", completed = 0, color1 = "rgba(76, 175, 80, 0.1)", color2 = "rgba(76, 175, 80, 1)";
  var a = document.getElementById("w3loginbtn");
  var b = document.getElementById("mypagediv");
  var c = document.getElementById("mypagediv2");
  if (c) {
    this.pages_read_count++;
    x = Math.round((this.pages_read_count / this.total_pages_count) * 100);
    degrees = x * 3.6;
    if (degrees > 359) degrees = 359.99;
    txt += "<span class='usergetspoint' id='usergetstutpoint'>+1</span>";
    if (degrees == 359.99) { completed = 1; }
    if (completed == 1) {
      txt += "<span id='usergetsstar'>&#x2605;</span>";
    }
    c.innerHTML += txt;
    document.getElementById("mypage_circle1").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, 359.99));
    document.getElementById("mypage_circle2").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, degrees));
    document.getElementById("mypage2_circle1").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, 359.99));
    document.getElementById("mypage2_circle2").setAttribute("d", this.getProfileIconCirclesRendered(26, 35, 24, 0, degrees));
  }
}
// > footer
// >> classic/*
  User session script
  Version: 1.0.2
*/

function getCognitoConfig() {
  return {
    region: 'us-east-1',
    userPoolId: 'us-east-1_uG9SGX7Wd',
  };
};

function getCognitoIssuerUrl(cognitoCfg) {
  return 'https://cognito-idp.' + cognitoCfg.region + '.amazonaws.com/' + cognitoCfg.userPoolId;
};

function verifyUserSession(
  cognitoCfg,
  userSession, // cookie
  accessToken, // cookie
) {
  var output = {
    error: {
      code: '0',
    },
    data: {},
  };

  if (
    typeof accessToken === 'undefined'
    || !accessToken
  ) {
    // cookie access token will vanish after expiration .. the presence of "userSession" is an indicator that there was a session before
    if (
      typeof userSession !== 'undefined'
      && userSession
    ) {
      if (userSession === '-1') {
        output.error = {
          code: 'USSBR',
          description: 'User session should be refreshed'
        };

        return output;
      }

      output.error = {
        code: 'USHE',
        description: 'User session has expired'
      };

      return output;
    }

    output.error = {
      code: 'USNF', // previously called ATINS
      description: 'User session not found'
    };

    return output;
  } else if (accessToken === '-1') { // legacy fallback
    output.error = {
      code: 'LUSSBR',
      description: 'User session should be refreshed'
    };

    return output;
  }

  var accessTokenMeta = parseAccessToken(accessToken);

  if (accessTokenMeta.error.code !== '0') {
    output.error = accessTokenMeta.error;

    return output;
  }

  output.data = accessTokenMeta.data;

  var claim = accessTokenMeta.data.payload;

  var issuer = getCognitoIssuerUrl(cognitoCfg);

  if (claim.iss !== issuer) {
    output.error = {
      code: 'ATINVCIDNM',
      description: 'Access token is not valid. Claim issuer does not match',
      meta: {
        accessToken: accessToken,
        issuer: issuer,
        claim: claim,
      }
    };

    return output;
  }

  if (claim.token_use !== 'access') {
    output.error = {
      code: 'ATINVCUINA',
      description: 'Access token is not valid. Claim use is not access',
      meta: {
        accessToken: accessToken,
        claim: claim,
      }
    };

    return output;
  }

  return output;
};

function decodeBase64UrlEncodedJwtSection(encodedStr) {
  // https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript-without-using-a-library
  var output = {
    error: {
      code: '0'
    },
    data: '',
  };

  try {
    encodedStr = encodedStr
      .replace(/-/g, '+')
      .replace(/_/g, '/');

    output.data = decodeURIComponent(atob(encodedStr)
      .split('')
      .map(function (char) {
        return '%' + ('00' + char.charCodeAt(0).toString(16)).slice(-2);
      })
      .join(''));
  } catch (exc) {
    output.error = getMetaPreparedFromException(exc);
  }

  return output;
};

function parseAccessToken(
  accessToken,
  parseHeader,
) {
  var output = {
    error: {
      code: '0'
    },
    data: {},
  };

  if (
    typeof accessToken === 'undefined'
    || !accessToken
  ) {
    output.error = {
      code: 'USNF', // previously called ATINS
      description: 'User session not found'
    };

    return output;
  } else if (accessToken === '-1') { // legacy fallback
    output.error = {
      code: 'USSBR',
      description: 'User session should be refreshed'
    };

    return output;
  }

  try {
    var accessTokenSections = accessToken.split('.');

    if (accessTokenSections.length < 3) { // maybe in future we may have more than 3 chunks
      output.error = {
        code: 'ATINVWNOTS',
        description: 'Access token is not valid. Wrong number of token sections',
        meta: {
          accessToken: accessToken,
          accessTokenSections: accessTokenSections,
        }
      };

      return output;
    }

    var accessTokenHeader = undefined;

    if (typeof parseHeader !== 'undefined' && parseHeader) {
      var accessTokenHeaderEncodedStr = accessTokenSections[0];

      var accessTokenHeaderDecodedStrRes = decodeBase64UrlEncodedJwtSection(accessTokenHeaderEncodedStr);

      if (accessTokenHeaderDecodedStrRes.error.code !== '0') {
        output.error = {
          code: 'ATINVFDTTH',
          description: 'Access token is not valid. Failed decoding the token header',
          meta: {
            accessToken: accessToken,
            accessTokenHeaderEncodedStr: accessTokenHeaderEncodedStr,
            decodingError: accessTokenHeaderDecodedStrRes.error
          }
        };

        return output;
      }

      var accessTokenHeaderParseRes = parseJson(
        accessTokenHeaderDecodedStrRes.data, // jsonStr
        ['kid', 'alg'], // requiredFields
      );

      if (accessTokenHeaderParseRes.error.code !== '0') {
        output.error = {
          code: 'ATINVFPTH',
          description: 'Access token is not valid. Failed parsing token header',
          meta: {
            accessToken: accessToken,
            accessTokenHeaderEncodedStr: accessTokenHeaderEncodedStr,
            accessTokenHeaderDecodedStr: accessTokenHeaderDecodedStrRes.data,
            parseError: accessTokenHeaderParseRes.error
          }
        };

        return output;
      }

      accessTokenHeader = accessTokenHeaderParseRes.data;
    }

    var accessTokenPayloadEncodedStr = accessTokenSections[1];

    var accessTokenPayloadDecodedStrRes = decodeBase64UrlEncodedJwtSection(accessTokenPayloadEncodedStr);

    if (accessTokenPayloadDecodedStrRes.error.code !== '0') {
      output.error = {
        code: 'ATINVFDTTP',
        description: 'Access token is not valid. Failed decoding the token payload',
        meta: {
          accessToken: accessToken,
          accessTokenPayloadEncodedStr: accessTokenPayloadEncodedStr,
          decodingError: accessTokenPayloadDecodedStrRes.error
        }
      };

      return output;
    }

    var accessTokenPayloadParseRes = parseJson(
      accessTokenPayloadDecodedStrRes.data, // jsonStr
      [
        'sub',
        'event_id',
        'token_use',
        'scope',
        'auth_time',
        'iss',
        'exp',
        'iat',
        'jti',
        'client_id',
        'username',
      ], // requiredFields
    );

    if (accessTokenPayloadParseRes.error.code !== '0') {
      output.error = {
        code: 'ATINVFPTP',
        description: 'Access token is not valid. Failed parsing token payload',
        meta: {
          accessToken: accessToken,
          accessTokenPayloadEncodedStr: accessTokenPayloadEncodedStr,
          accessTokenPayloadDecodedStr: accessTokenPayloadDecodedStrRes.data,
          parseError: accessTokenPayloadParseRes.error
        }
      };

      return output;
    }

    var accessTokenPayload = accessTokenPayloadParseRes.data;

    var accessTokenExpiryUts = parseInt(accessTokenPayload.exp);

    var accessTokenExpiryDto = new Date(accessTokenExpiryUts * 1000);

    output.data = {
      rawStr: accessToken,
      header: accessTokenHeader,
      payload: accessTokenPayload,
      expiryDto: accessTokenExpiryDto,
      expiryUts: accessTokenExpiryUts,
      // expired: getCurrentUts() >= accessTokenExpiryUts,
    };
  } catch (exc) {
    output.error = getMetaPreparedFromException(exc);
  }

  return output;
};

function refreshUserSessionViaRedirect(redirectUrl) {
  // console.log(getCurrentUtus().toString() + ' refreshUserSessionViaRedirect -> initialized -> redirectUrl: ', redirectUrl);
  Cookies.remove('accessToken'); // extra/safety removal
  Cookies.remove('userSession'); // extra/safety removal

  Cookies.set('userSession', '-1', {
    domain: '.w3schools.com',
    path: '/',
    secure: true,
    sameSite: 'strict',
  });

  // return;

  window.location.href = 'https://profile.w3schools.com/refresh-session?redirect_url=' + encodeURIComponent(redirectUrl);
};

// < utils
function getMetaPreparedFromException(exc) {
  var output = {
    code: '1',
    description: 'Internal server error',
  };

  if (exc instanceof Error) {
    output.description = exc.message;
  } else if (typeof exc === 'string') {
    output.description = exc;
  }

  return output;
};

function parseJson(
  jsonStr,
  requiredFields,
) {
  var output = {
    error: {
      code: '0'
    },
    data: {},
  };

  try {
    output.data = JSON.parse(jsonStr);

    if (typeof requiredFields !== 'undefined') {
      for (var i = 0; i < requiredFields.length; i++) {
        var key = requiredFields[i];

        if (
          typeof output.data[key] === 'undefined'
        ) {
          output.error = {
            code: 'FINPID',
            description: 'Field is not present in data',
            meta: {
              key: key,
            }
          };

          return output;
        }
      }
    }
  } catch (exc) {
    output.error = getMetaPreparedFromException(exc);
  }

  return output;
};
// > utils