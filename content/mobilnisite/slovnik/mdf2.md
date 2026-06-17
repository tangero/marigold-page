---
slug: "mdf2"
url: "/mobilnisite/slovnik/mdf2/"
type: "slovnik"
title: "MDF2 – Mediation and Delivery Function 2"
date: 2025-01-01
abbr: "MDF2"
fullName: "Mediation and Delivery Function 2"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mdf2/"
summary: "Bezpečnostní funkce pro zákonný odposlech a uchovávání dat. Zprostředkovává a doručuje odposlechnutý komunikační obsah a přidružená data ze síťových funkcí orgánům činným v trestním řízení, čímž zajiš"
---

MDF2 je bezpečnostní funkce, která zprostředkovává a doručuje odposlechnutý komunikační obsah a přidružená data ze síťových funkcí orgánům činným v trestním řízení pro účely zákonného odposlechu.

## Popis

Funkce zprostředkování a doručení 2 (MDF2) je klíčovou komponentou v bezpečnostní architektuře 3GPP, specificky definovanou pro zákonný odposlech ([LI](/mobilnisite/slovnik/li/)) a uchovávání dat ([DR](/mobilnisite/slovnik/dr/)). Funguje jako zprostředkující entita, která přijímá odposlechnutý komunikační obsah ([CC](/mobilnisite/slovnik/cc/)) a informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) z různých síťových funkcí, jako je funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v síti 5G Core. MDF2 je zodpovědná za standardizaci, formátování a zabezpečené doručení těchto odposlechnutých dat do jedné či více monitorovacích zařízení orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)), jak nařizují příslušné právní autority. Její architektura je navržena tak, aby byla nezávislá na typu přístupu, podporujíc odposlech napříč více generacemi sítí a technologiemi, včetně 5G, 4G a přístupu mimo 3GPP.

Z funkčního hlediska MDF2 přijímá zprávy rozhraní HI2 a HI3 (pro doručení IRI a CC) z interních odposlechových funkcí sítě. Reaguje na aktivační požadavky přijaté přes rozhraní HI1 od administrační funkce (ADMF). MDF2 provádí zprostředkovatelské úkoly, jako je ukládání dat do vyrovnávací paměti, korelace IRI a CC pro stejný cíl, převod do standardizovaných formátů (např. formáty standardizované ETSI, jako je ETSI TS 102 232) a přizpůsobení specifickým požadavkům různých LEMF. Následně zpracovaná data doručuje do LEMF přes předávací rozhraní HI2 (pro IRI) a HI3 (pro CC). Funkce zajišťuje zabezpečené, spolehlivé a auditovatelné doručení a zachovává integritu a důvěrnost odposlechnutých dat v celém procesu.

Mezi klíčové komponenty role MDF2 patří její rozhraní: HI1 pro aktivaci/deaktivaci odposlechu, HI2 pro doručení IRI a HI3 pro doručení CC. Musí zvládat vysoké objemy dat s nízkou latencí, zejména u odposlechu obsahu v reálném čase, jako jsou hlasové hovory. MDF2 také hraje zásadní roli v zajištění, aby byl proces odposlechu cílený a minimalizovalo se shromažďování dat pouze na subjekty právně autorizované, čímž se hájí principy soukromí. Její implementace je klíčová pro síťové operátory, aby splnili regulatorní povinnosti, aniž by byla ohrožena celková bezpečnost a výkon komerční sítě. V samostatné architektuře 5G je MDF2 logickou funkcí, která může být implementována jako dedikovaný síťový prvek nebo integrována do jiných síťových funkcí, což operátorům poskytuje flexibilitu.

## K čemu slouží

MDF2 byla vytvořena, aby řešila vyvíjející se požadavky na zákonný odposlech v moderních telekomunikačních sítích, zejména se zavedením 5G. Jak se sítě stávaly více virtualizovanými, cloud-nativními a službami založenými, tradiční metody odposlechu navržené pro monolitické síťové uzly se staly nedostatečnými. Účelem MDF2 je poskytnout standardizovanou, škálovatelnou a bezpečnou zprostředkovatelskou funkci, která může komunikovat s novými síťovými funkcemi (NF) 5G Core, které jsou často nasazovány jako softwarové instance v cloudovém prostředí. Řeší problém efektivního shromažďování a doručování odposlechnutých dat z disaggregační síťové architektury orgánům činným v trestním řízení.

Historicky byly funkce zákonného odposlechu často těsně integrovány do specifických síťových prvků, jako jsou MSC nebo SGSN. Přechod na architekturu založenou na službách (SBA) v 5G, kde řídicí rovinné funkce komunikují přes služební rozhraní založená na HTTP/2 (např. Nausf, Namf), si vyžádal přearchitekturovaný odposlechový systém. MDF2 poskytuje tuto novou zprostředkovatelskou vrstvu a zajišťuje, že odposlechové mandáty mohou být splněny bez ohledu na podkladovou implementaci síťového softwaru nebo cloudovou infrastrukturu. Řeší omezení předchozích přístupů tím, že je navržena pro agilitu, podporuje síťové slicing (kde odposlech musí být vědomý každého slicu) a zvládá zvýšené datové toky a služby s nízkou latencí v 5G.

Dále je MDF2 spolu s MDF3 specifikována tak, aby zajistila jasné oddělení odpovědností. Zatímco MDF2 zajišťuje doručení odposlechnutého komunikačního obsahu a přidružených dat, jiné funkce zajišťují aktivaci a provisioning. Tento modulární design zjednodušuje implementaci, testování a certifikaci shody pro výrobce síťového vybavení a operátory. Její vytvoření bylo motivováno potřebou rámce pro odposlech připraveného na budoucnost, který zachovává regulatorní soulad a zároveň podporuje technické inovace a architektonickou komplexitu 5G a dalších generací.

## Klíčové vlastnosti

- Zprostředkovává doručení informací souvisejících s odposlechem (IRI) přes rozhraní HI2
- Zprostředkovává doručení komunikačního obsahu (CC) přes rozhraní HI3
- Přijímá příkazy k aktivaci odposlechu přes rozhraní HI1 od ADMF
- Formátuje a převádí odposlechnutá data do standardizovaných formátů pro LEMF
- Podporuje odposlech pro technologie přístupu 5G, 4G a mimo 3GPP
- Navržena pro provoz ve virtualizovaném, cloud-nativním prostředí sítě 5G Core

## Související pojmy

- [MDF3 – Mediation and Delivery Function 3](/mobilnisite/slovnik/mdf3/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [MDF2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdf2/)
