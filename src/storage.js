const KEY='tiny-systems-v1';
export const dateKey=(date=new Date())=>`${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`;
export function read(){try {const s=JSON.parse(localStorage.getItem(KEY));if(s&&s.version===1&&Array.isArray(s.courses)&&s.progress&&Array.isArray(s.activity))return s;}catch{}return {version:1,courses:[],progress:{},activity:[],xp:0,draft:null};}
export function save(state){try{localStorage.setItem(KEY,JSON.stringify(state));return true;}catch{return false;}}
export function streak(activity){let d=new Date(),n=0;if(!activity.includes(dateKey(d)))d.setDate(d.getDate()-1);while(activity.includes(dateKey(d))){n++;d.setDate(d.getDate()-1);}return n;}
export function download(data,name){const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
