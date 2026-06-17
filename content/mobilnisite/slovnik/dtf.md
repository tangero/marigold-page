---
slug: "dtf"
url: "/mobilnisite/slovnik/dtf/"
type: "slovnik"
title: "DTF – Domain Transfer Function"
date: 2007-01-01
abbr: "DTF"
fullName: "Domain Transfer Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dtf/"
summary: "Domain Transfer Function (DTF) je funkční entita definovaná v 3GPP pro kontinuitu hlasového hovoru (VCC). Působí jako kotvicí bod v jádru IMS, směruje hovory a usnadňuje plynulý přenos hlasových relac"
---

DTF je funkční entita v jádru IMS, která kotví a směruje hovory, aby umožnila plynulý přenos hlasových relací mezi okruhově spínanou (CS) doménou a doménou IMS pro kontinuitu hlasového hovoru (VCC).

## Popis

Domain Transfer Function (DTF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS) definovaná speciálně pro funkci kontinuity hlasového hovoru (VCC), zavedenou ve 3GPP Release 7. DTF sídlí v domovské IMS síti uživatele. Jejím hlavním operačním úkolem je sloužit jako kotvicí bod pro hlasový hovor s podporou VCC. Když účastník zahájí nebo přijme hovor s VCC, relace je vždy směrována přes DTF v domovské síti, bez ohledu na to, zda je uživatel původně připojen přes [CS](/mobilnisite/slovnik/cs/) doménu (jako tradiční hlas GSM/UMTS) nebo přes IMS/PS doménu (jako VoIP přes LTE).

Princip její činnosti je nedílnou součástí procedury přenosu mezi doménami. DTF udržuje probíhající větévku hovoru směrem ke vzdálené straně (např. k jinému mobilnímu uživateli nebo číslu v PSTN). Současně spravuje větévku hovoru směrem k uživatelskému zařízení (UE) přes aktuální přístupovou doménu. Když je vyžadován přenos mezi doménami – například při přechodu z IMS VoIP hovoru přes WLAN na CS hovor přes [GERAN](/mobilnisite/slovnik/geran/) kvůli zhoršujícímu se pokrytí WLAN – UE nebo síť spustí proceduru přenosu. DTF je instruována, aby přepnula větévku hovoru směrem k UE ze staré domény na novou. Koordinuje přitom s dalšími entitami VCC, jako je CS Adaptation Function ([CSAF](/mobilnisite/slovnik/csaf/)) pro CS větévky a potenciálně Service Centralization and Continuity Application Server (SCC [AS](/mobilnisite/slovnik/as/)) v pozdějších architekturách. DTF přepnutí provede a zajistí překotvení mediální cesty s minimálním přerušením pro uživatele.

Mezi klíčové komponenty, které s DTF interagují, patří VCC aplikace (která může být s ní umístěna společně), CSAF pro rozhraní s [MSC](/mobilnisite/slovnik/msc/) a Serving-Call Session Control Function (S-CSCF), která k ní směruje počáteční SIP zprávy. Role DTF je klíčová pro transparentnost; vzdálená strana si přenosu mezi doménami není vědoma, protože DTF na její straně udržuje relaci. Tato architektura centralizuje řízení a správu stavu pro službu VCC, což umožňuje robustní logiku kontinuity a provádění služeb účastníka z domovské sítě.

## K čemu slouží

DTF byla vytvořena, aby vyřešila problém plynulé kontinuity hlasového hovoru mezi různými technologickými doménami, konkrétně mezi starší okruhově spínanou ([CS](/mobilnisite/slovnik/cs/)) doménou a nově vznikající paketově spínanou doménou IP Multimedia Subsystem (IMS). Před zavedením VCC a DTF by musel být hlasový hovor ustavený v jedné doméně (např. CS) ukončen, pokud se uživatel přesunul do oblasti podporované pouze druhou doménou (např. IMS přes WLAN), což vedlo ke špatnému uživatelskému zážitku. Motivací bylo umožnit operátorům nasadit hlasové služby založené na IMS (jako VoIP přes WLAN) a zároveň využít všudypřítomné pokrytí stávající CS sítě pro spolehlivost, čímž vznikla kombinovaná nabídka služeb.

Historický kontext je Release 7, kde bylo IMS prosazováno pro multimediální služby, ale rádiové pokrytí pro čistý IP přístup (jako rané LTE nebo WLAN) bylo nerovnoměrné. VCC bylo klíčovým prvkem umožňujícím konvergenci pevných a mobilních sítí a raných předchůdců VoLTE. DTF odstranila omezení předchozích přístupů, kde byly tyto dvě domény zcela oddělené a neměly koordinovaný mechanismus přenosu. Zavedením centralizované kotvící funkce v domovském IMS poskytla DTF standardizovanou, sítí řízenou metodu pro přenos aktivní relace, která zachovává hovor a zajišťuje kontinuitu služby, což byl základní požadavek pro přijetí nových VoIP služeb uživateli.

## Klíčové vlastnosti

- Působí jako kotvicí bod relace v domovském IMS pro všechny hovory s VCC.
- Spravuje dvě větévky hovoru: jednu směrem ke vzdálené straně a jednu směrem k UE přes jeho aktuální doménu.
- Provede přenos mezi doménami přepnutím větévky hovoru směrem k UE z CS na IMS nebo naopak.
- Spolupracuje s CS Adaptation Function (CSAF) pro zpracování signalizace a médií v CS doméně.
- Zajišťuje, že kontinuita služby je transparentní pro vzdálenou volající/přijímající stranu.
- Centralizuje logiku služby VCC a stav účastníka v domovské síti.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSAF – CS Adaptation Function](/mobilnisite/slovnik/csaf/)

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS

---

📖 **Anglický originál a plná specifikace:** [DTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtf/)
