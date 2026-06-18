---
slug: "svg"
url: "/mobilnisite/slovnik/svg/"
type: "slovnik"
title: "SVG – Scalable Vector Graphics"
date: 2025-01-01
abbr: "SVG"
fullName: "Scalable Vector Graphics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/svg/"
summary: "Vektorový obrazový formát založený na XML, standardizovaný 3GPP pro multimediální služby, umožňující tvorbu grafiky nezávislé na rozlišení pro mobilní aplikace. Podporuje interaktivitu a animaci, což"
---

SVG je vektorový obrazový formát založený na XML, standardizovaný 3GPP pro rozlišení nezávislou, interaktivní a animovanou grafiku v mobilních multimediálních službách, jako je MBMS.

## Popis

Scalable Vector Graphics (SVG) je vektorový obrazový formát odvozený od [W3C](/mobilnisite/slovnik/w3c/) a založený na [XML](/mobilnisite/slovnik/xml/), který byl přijat a profilován 3GPP pro použití v mobilních multimediálních službách. Na rozdíl od rastrových obrázků SVG definuje grafiku pomocí matematických popisů tvarů, cest, textu a vizuálních efektů, což umožňuje škálování obrázků na libovolnou velikost bez ztráty kvality. To je zvláště výhodné pro různorodé velikosti a rozlišení obrazovek mobilních zařízení. V rámci specifikací 3GPP je SVG integrováno do architektury služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a dalších multimediálních aplikací a poskytuje standardizovaný způsob doručování bohatého, interaktivního grafického obsahu přes mobilní sítě.

Technická architektura SVG v 3GPP zahrnuje definovanou podmnožinu nebo profil plné specifikace W3C SVG, optimalizovanou pro omezení mobilních zařízení, jako je omezený výpočetní výkon a paměť. Formát podporuje statickou grafiku, animaci prostřednictvím jazyka Synchronized Multimedia Integration Language ([SMIL](/mobilnisite/slovnik/smil/)), skriptování pro interaktivitu a stylování pomocí [CSS](/mobilnisite/slovnik/css/). Mezi klíčové komponenty patří vektorové tvary (např. obdélníky, kružnice, cesty definované Bézierovými křivkami), textové elementy, výplně přechody a vzory a filtrační efekty pro vizuální vylepšení. V síti je obsah SVG typicky přenášen jako součást multimediální prezentace, často zabalený s dalšími typy médií, jako je audio a video, v rámci přenosového rámce specifikovaného v dokumentu 26.234 pro MBMS.

SVG funguje tak, že klient, jako je mediální přehrávač nebo prohlížeč v mobilním zařízení, parsuje soubor SVG založený na XML, interpretuje příkazy pro kreslení a vykreslí grafiku na obrazovku. Vykreslovací engine vypočítává pozice a vzhled všech grafických elementů na základě matematických definic, čímž zajišťuje ostrý výstup při jakémkoli úrovni přiblížení nebo hustotě displeje. Pro animovaný nebo interaktivní obsah engine zpracovává časovací elementy a reaguje na uživatelské události nebo příkazy skriptů. Jeho role v ekosystému 3GPP spočívá v poskytování deklarativního, škálovatelného a efektivního formátu pro grafický obsah, což umožňuje službám jako je mobilní [TV](/mobilnisite/slovnik/tv/), interaktivní reklama a rozšířené zasílání zpráv prezentovat vysoce kvalitní vizuály, které se plynule přizpůsobují různým možnostem zařízení.

## K čemu slouží

SVG bylo zavedeno, aby vyřešilo potřebu standardizovaného, vysoce kvalitního grafického formátu vhodného pro omezené a heterogenní prostředí mobilních sítí. Před jeho přijetím mobilní služby často spoléhaly na bitmapovou grafiku (jako [PNG](/mobilnisite/slovnik/png/) nebo [JPEG](/mobilnisite/slovnik/jpeg/)), která je závislá na rozlišení a při škálování může působit pixelovaně, což vedlo ke špatnému uživatelskému zážitku napříč zařízeními s různými velikostmi a rozlišeními obrazovek. Vytvoření standardů pro vektorovou grafiku bylo motivováno růstem bohatých multimediálních služeb, jako je MBMS, které vyžadovaly způsob doručování vizuálně atraktivního obsahu, který by se mohl efektivně přizpůsobit různým charakteristikám displeje bez nutnosti více verzí assetů.

Historický kontext zahrnuje rozšíření pokročilých mobilních datových služeb v 3GPP Release 8 a novějších, kde operátoři usilovali o nabídku vylepšených vizuálních zážitků. SVG řeší problém škálovatelnosti grafiky a efektivity šířky pásma; jeden soubor SVG může obsloužit mnoho typů zařízení, což snižuje režii úložiště a přenosu ve srovnání s více soubory rastrových obrázků. Také umožňuje dynamický a interaktivní obsah, který se stával stále důležitějším pro poutavá uživatelská rozhraní a aplikace. Standardizací profilu SVG zajistilo 3GPP interoperabilitu napříč zařízeními a sítěmi, čímž podpořilo konzistentní ekosystém pro vývoj multimediálních služeb.

## Klíčové vlastnosti

- Vektorová grafika nezávislá na rozlišení založená na syntaxi XML
- Podpora animace a interaktivního obsahu prostřednictvím SMIL a skriptování
- Stylování a prezentační atributy ovladatelné pomocí CSS
- Integrace s multimediálními architekturami 3GPP, jako je MBMS, pro vysílací doručování
- Optimalizovaný mobilní profil pro omezené prostředky zařízení
- Schopnost vkládat rastrové obrázky a další typy médií do grafiky

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [SMIL – Synchronized Multimedia Integration Language](/mobilnisite/slovnik/smil/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study

---

📖 **Anglický originál a plná specifikace:** [SVG na 3GPP Explorer](https://3gpp-explorer.com/glossary/svg/)
