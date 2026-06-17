---
slug: "icscf"
url: "/mobilnisite/slovnik/icscf/"
type: "slovnik"
title: "I-CSCF – Interrogating Call Session Control Function"
date: 2025-01-01
abbr: "I-CSCF"
fullName: "Interrogating Call Session Control Function"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/icscf/"
summary: "I-CSCF je klíčový funkční prvek v jádru sítě IMS (IP Multimedia Subsystem). Slouží jako výchozí kontaktní bod pro požadavky SIP vstupující do domovské sítě z jiných sítí, provádí skrytí topologie sítě"
---

I-CSCF je prvek IMS, který představuje výchozí kontaktní bod pro příchozí požadavky SIP, provádí skrytí topologie sítě a vybírá pro uživatele příslušný S-CSCF.

## Popis

Interrogating Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) je proxy server SIP (Session Initiation Protocol) definovaný v architektuře IMS podle 3GPP. Jeho hlavní operační doménou je hranice sítě operátora IMS. Když požadavek SIP, například INVITE pro hlasové nebo video volání, dorazí z externí sítě (jako jiná síť IMS nebo sít s komutací okruhů přes Media Gateway Control Function), je nejprve přijat právě I-CSCF. Prvním hlavním úkolem I-CSCF je dotazovat se na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pomocí rozhraní Diameter Cx. Předá HSS veřejnou identitu uživatele (např. SIP URI) a HSS odpoví požadovanými schopnostmi pro uživatelův Serving-CSCF (S-CSCF), nebo, pokud je uživatel již registrován, může přímo poskytnout adresu přiřazeného S-CSCF.

Na základě informací od HSS I-CSCF vybere pro uživatele vhodný S-CSCF, pokud již není přiřazen. Tento výběr je založen na schopnostech S-CSCF vyžadovaných servisním profilem uživatele. I-CSCF následně přepošle požadavek SIP na zvolený S-CSCF. Zásadní bezpečnostní a topologickou funkcí I-CSCF je skrytí topologie sítě (network hiding). Může fungovat jako Topology Hiding Inter-network Gateway (THIG), odstraňující informace o vnitřní topologii sítě (jako adresy konkrétních S-CSCF) ze zpráv SIP před jejich opuštěním domovské sítě, čímž zvyšuje zabezpečení.

V opačném směru, pro relace iniciované v jeho domovské síti a směřující do externí sítě, může být I-CSCF také výstupním bodem. Směruje odchozí požadavek SIP směrem k cílové síti na základě dotazů [DNS](/mobilnisite/slovnik/dns/) (Domain Name System) pro cílovou doménu. I-CSCF je bezstavový v tom smyslu, že neudržuje stav relace po dobu trvání hovoru, ale podílí se na počátečním rozhodnutí o směrování. Jeho přítomnost je povinná v prostředí více operátorů a je nezbytná pro umožnění roamingu, propojení mezi operátory a pro udržení bezpečné a škálovatelné architektury jádra sítě IMS.

## K čemu slouží

[I-CSCF](/mobilnisite/slovnik/i-cscf/) byl zaveden k řešení klíčových výzev ve směrování, škálovatelnosti a zabezpečení při přechodu na poskytování služeb přes IMS v prostředí plně IP. V čisté SIP síti bez takového funkčního prvku by externí entity potřebovaly znát přímou adresu uživatelova obslužného proxy serveru (S-CSCF), což by odhalovalo vnitřní architekturu sítě a vytvářelo jediný bod selhání a úzké hrdlo pro škálování. I-CSCF tuto vnitřní informaci abstrahuje.

Jeho vytvoření bylo motivováno potřebou standardizované a bezpečné metody pro zpracování příchozích relací z jiných sítí, zejména pro scénáře roamingu. Funguje jako určená hraniční řídicí funkce pro signalizaci SIP. Centralizací logiky dotazů na [HSS](/mobilnisite/slovnik/hss/) a výběru S-CSCF umožňuje vyrovnávání zatížení napříč fondy více S-CSCF a umožňuje síťovým operátorům skrýt svou vnitřní topologii před potenciálními hrozbami nebo konkurenční analýzou, což je koncept známý jako skrytí topologie (topology hiding).

Dále I-CSCF poskytuje jasné oddělení odpovědností uvnitř jádra IMS. Zatímco S-CSCF zpracovává řízení relací a servisní logiku pro registrované uživatele a [P-CSCF](/mobilnisite/slovnik/p-cscf/) je prvním kontaktním bodem uživatele, I-CSCF se specializuje na směrování mezi sítěmi a počáteční dotazování. Tato modulární architektura umožňuje operátorům škálovat, zabezpečovat a spravovat tyto funkce nezávisle, což bylo zásadní pro komerční nasazení rozsáhlých, operátorsky robustních služeb VoIP a multimédií.

## Klíčové vlastnosti

- Slouží jako první kontaktní bod pro příchozí relace SIP z externích sítí
- Dotazuje se na HSS přes rozhraní Diameter Cx, aby získal servisní profil uživatele a informace o přiřazení S-CSCF
- Vybere vhodný S-CSCF na základě požadovaných schopností pro neregistrované uživatele
- Přepošle požadavky SIP na přiřazený S-CSCF pro další zpracování relace
- Poskytuje skrytí topologie tím, že maskuje adresy interních S-CSCF před externími sítěmi
- Umožňuje vyrovnávání zatížení napříč fondem serverů S-CSCF

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [I-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/icscf/)
