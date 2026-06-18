---
slug: "rqi"
url: "/mobilnisite/slovnik/rqi/"
type: "slovnik"
title: "RQI – Reflective QoS Indication"
date: 2026-01-01
abbr: "RQI"
fullName: "Reflective QoS Indication"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rqi/"
summary: "Příznak nastavený v hlavičce paketu v uživatelské rovině pro spuštění Reflective QoS v UE. Když UE, která má autorizovaný QoS Flow (RQA), přijme downlinkový paket s nastaveným RQI, odvodí z něj pravid"
---

RQI je příznak nastavený v hlavičce paketu v uživatelské rovině, který spouští v UE odvození pravidla QoS pro uplink po přijetí paketu v downlinku, což umožňuje dynamický a signalizačně efektivní Reflective QoS.

## Popis

Reflective QoS Indication (RQI) je příznak v uživatelské rovině klíčový pro fungování mechanismu Reflective QoS v 5G sítích. Na rozdíl od své protějškové řídicí roviny, [RQA](/mobilnisite/slovnik/rqa/), je RQI jednobitový indikátor vložený do zapouzdřovacích hlaviček paketů uživatelských dat putujících ve směru downlink. Typicky je přenášen v rozšiřující hlavičce [GTP-U](/mobilnisite/slovnik/gtp-u/) pro rozhraní N3/N9 nebo v rámci rámcové struktury na rádiovém rozhraní Uu, a je asociován s QoS Flow ID ([QFI](/mobilnisite/slovnik/qfi/)). Entitou nastavující RQI může být [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) nebo v některých nasazeních gNB, a to na základě politik přijatých od [SMF](/mobilnisite/slovnik/smf/)/[PCF](/mobilnisite/slovnik/pcf/).

Z architektonického hlediska RQI funguje na průsečíku uživatelské roviny a funkce vynucování QoS politiky v UE. Síť, poté co určí, že konkrétní downlinkový paket patří do QoS Flow nakonfigurovaného pro reflexivní zpracování, nastaví bit RQI v hlavičce paketu. Tento paket pak prochází přes rozhraní N3 a Uu k UE. Protokolový zásobník UE, konkrétně jeho vrstva [SDAP](/mobilnisite/slovnik/sdap/) (Service Data Adaptation Protocol) v 5G NR nebo její ekvivalent, kontroluje příchozí downlinkové pakety. Detekce bitu RQI je klíčovou spouštěcí událostí.

Mechanismus funguje prostřednictvím koordinované sekvence. Za prvé, UE musí mít předtím přijato pravidlo QoS v řídicí rovině pro daný QoS Flow obsahující atribut RQA, což poskytuje autorizaci. Když UE přijme downlinkový paket s nastaveným bitem RQI pro tento autorizovaný tok, spustí reflexivní akci QoS. Tato akce zahrnuje vytvoření nového pravidla QoS pro uplink nebo aktualizaci stávajícího pravidla UE. UE odvozuje parametry pro toto uplinkové pravidlo – jako je [5QI](/mobilnisite/slovnik/5qi/), Allocation and Retention Priority (ARP) a potenciálně i filtry specifické pro tok – z charakteristik pozorovaného downlinkového toku paketů. Odvozené pravidlo je pak nainstalováno v klasifikátoru a značkovači uplinku v UE, čímž je zajištěno, že následné uplinkové pakety pro daný aplikační tok získají odpovídající QoS zacházení bez potřeby nového požadavku na SMF.

Jeho úlohou je poskytovat mechanismus signalizace v reálném čase, v pásmu, který vyzve UE k vlastní konfiguraci své QoS pro uplink. Tím se odděluje dynamická aktivace symetrické QoS od pomalejších procedur řídicí roviny. Je klíčový pro dosažení nízké latence při nastavování služeb, snížení signalizační zátěže v jádru sítě a umožnění efektivní podpory aplikací, kde jsou vzorce provozu a požadované zdroje zrcadleny mezi uplinkem a downlinkem. RQI mění samotný downlinkový datový proud na řídicí kanál pro poskytování QoS.

## K čemu slouží

RQI byl vyvinut k řešení problému latence a signalizační režie spojené se zřizováním symetrických QoS toků prostřednictvím tradičních metod centralizovaných v jádru sítě. V systémech před 5G, pokud aplikace začala generovat downlinkový provoz vyžadující odpovídající uplinkový QoS tok, musela síť toto detekovat, formulovat politiku (přes PCF), instruovat SMF/PGW a následně signalizovat nové pravidlo QoS k UE – proces trvající stovky milisekund. Pro interaktivní služby v reálném čase je toto zpoždění nepřijatelné.

Vytvoření RQI bylo motivováno potřebou 'zero-touch' nebo okamžité aktivace QoS. Označením downlinkového paketu může síť okamžitě instruovat řádně autorizovanou UE, aby zřídila potřebné uplinkové zdroje. To je analogické 'popostrčení' ze strany sítě, které využívá existující datovou cestu pro řízení. Řeší to omezení čistě reaktivních, signalizačních přístupů, které jsou pro případy užití URLLC a kritické komunikace plánované pro 5G příliš pomalé.

V historickém kontextu poskytovaly QoS značky jako DSCP v IP hlavičkách náznaky, ale reakce UE nebyla standardizována ani svázána se zabezpečenými, sítí autorizovanými politikami. RQI od 3GPP, zavedený ve verzi 15, formalizuje tento mechanismus náznaku v rámci protokolového zásobníku 3GPP a bezpečně jej spojuje s autorizací v řídicí rovině (RQA). Tím se řeší dvojí problém rychlosti a zabezpečení, což umožňuje rychlou adaptaci při zachování síťové kontroly nad tím, které toky mohou používat reflexivní QoS a jaké zdroje si mohou nárokovat.

## Klíčové vlastnosti

- Jednobitový indikátor v hlavičce downlinkového paketu v uživatelské rovině.
- Nastavován UPF nebo gNB na základě politiky SMF/PCF.
- Při detekci spouští na straně UE odvození pravidel QoS pro uplink.
- Vyžaduje předchozí autorizaci UE prostřednictvím atributu RQA v řídicí rovině.
- Umožňuje signalizaci aktivace QoS v pásmu s nízkou latencí.
- Snižuje signalizační zátěž řídicí roviny pro dynamickou správu toků.

## Související pojmy

- [RQA – Reflective QoS Attribute](/mobilnisite/slovnik/rqa/)
- [QFI – QoS Flow Identifier](/mobilnisite/slovnik/qfi/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [SDAP – Service Data Adaptation Protocol](/mobilnisite/slovnik/sdap/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 37.324** (Rel-19) — Service Data Adaptation Protocol (SDAP)
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [RQI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rqi/)
