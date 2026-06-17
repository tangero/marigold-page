---
slug: "b-alg"
url: "/mobilnisite/slovnik/b-alg/"
type: "slovnik"
title: "B-ALG – Bearer Level Application-Level Gateway"
date: 2025-01-01
abbr: "B-ALG"
fullName: "Bearer Level Application-Level Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/b-alg/"
summary: "Síťová funkce, která provádí hloubkovou inspekci paketů a vynucování politik s ohledem na aplikaci na úrovni přenosového kanálu (bearer). Umožňuje poskytovatelům služeb implementovat sofistikované str"
---

B-ALG je síťová funkce, která provádí hloubkovou inspekci paketů a vynucování politik s ohledem na aplikaci na úrovni přenosového kanálu (bearer) v rámci IMS, aby umožnila účtování, optimalizaci provozu a politiky kvality služeb (QoS).

## Popis

Bearer Level Application-Level Gateway (B-ALG) je specializovaný síťový prvek v architektuře IP Multimedia Subsystem (IMS), který funguje na rozhraní řídicí a uživatelské roviny. Působí jako zprostředkující prvek s povědomím o aplikaci, který zkoumá signalizační zprávy protokolu Session Initiation Protocol (SIP) a související mediální toky, aby identifikoval konkrétní aplikace, služby nebo typy obsahu. Na rozdíl od tradičních ALG, které fungují primárně na transportní vrstvě, B-ALG provádí hloubkovou inspekci paketů na aplikační vrstvě, což umožňuje detailní identifikaci služeb i v případě, že používají nestandardní porty nebo šifrovací techniky.

Z architektonického hlediska je B-ALG umístěn mezi Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-Call Session Control Function (S-CSCF) v signalizační cestě IMS. Zachycuje SIP zprávy během procedur navazování, změny a ukončování relace, analyzuje nabídky a odpovědi SDP (Session Description Protocol) k identifikaci charakteristik médií a otisků aplikací. B-ALG udržuje informace o stavu relace a koreluje signalizační zprávy s odpovídajícími mediálními toky, což mu umožňuje uplatňovat konzistentní politiky po celou dobu životnosti relace. Rozhraní s funkcemi pro řízení politik, jako je Policy and Charging Rules Function (PCRF), zajišťuje přes rozhraní Rx, aby získal dynamická pravidla politik založená na detekci aplikace.

Fungování B-ALG zahrnuje několik klíčových komponent: analyzátor SIP a stavový automat pro zpracování signalizačních zpráv, enginy pro hloubkovou inspekci paketů pro analýzu mediálních toků, body pro vynucování politik pro aplikaci pravidel QoS a účtování a rozhraní k externím politickým serverům. Při zřízení relace B-ALG prozkoumá zprávu SIP INVITE a přidružené SDP, aby identifikoval typ aplikace (např. video streamování, hlasový hovor, hraní her). Následně komunikuje s PCRF, aby získal příslušná pravidla politik, která mohou zahrnovat specifické parametry QoS, sazby účtování nebo pokyny pro optimalizaci provozu. Tato pravidla jsou vynucována označováním paketů příslušnými hodnotami [DSCP](/mobilnisite/slovnik/dscp/), tvarováním toků provozu nebo spouštěním specializovaných událostí účtování.

V síťovém ekosystému hraje B-ALG klíčovou roli při umožnění sítí s povědomím o aplikaci v rámci IMS. Umožňuje operátorům implementovat sofistikované strategie diferenciace služeb, kdy různé aplikace dostávají různý přístup na základě svých požadavků a obchodních modelů. Například služba video streamování může dostat vyšší prioritu a jiné účtování než služba přenosu souborů. B-ALG také podporuje požadavky na zákonné odposlechy tím, že poskytuje podrobnou identifikaci aplikací a možnosti sledování relací. Jeho integrace s architekturou Policy and Charging Control (PCC) zajišťuje, že politiky na úrovni aplikace jsou konzistentně uplatňovány napříč prvky řídicí i uživatelské roviny.

## K čemu slouží

B-ALG byl vyvinut, aby řešil rostoucí potřebu vynucování politik s ohledem na aplikaci v IP multimediálních sítích. Jak se mobilní sítě vyvíjely od přepojování okruhů pro hlasové služby k paketovým multimediálním službám, potřebovali operátoři mechanismy k identifikaci a rozlišení různých aplikací běžících přes IP. Tradiční síťové prvky mohly klasifikovat provoz pouze na základě IP adres, portů nebo typů protokolů, což se stalo nedostatečným, když aplikace začaly používat dynamické porty, šifrování a tunelovací techniky k obcházení jednoduchých klasifikačních metod.

Před implementací B-ALG čelili operátoři významným výzvám při zavádění podrobného účtování a politik QoS pro služby IMS. Základní funkce ALG existovaly, ale fungovaly primárně na transportní vrstvě a postrádaly sofistikovanost potřebnou pro moderní multimediální aplikace. Mezi omezení předchozích přístupů patřila neschopnost identifikovat konkrétní aplikace v rámci šifrovaných toků, špatné zacházení s dynamicky přidělovanými porty a omezená integrace se systémy pro řízení politik. Tyto nedostatky ztěžovaly operátorům efektivní nabízení diferencovaných služeb nebo zavádění politik spravedlivého využívání.

Vytvoření B-ALG bylo motivováno komerční potřebou vhodně monetizovat různé typy provozu a zajistit kvalitu uživatelského zážitku pro prémiové služby. Díky umožnění hloubkové inspekce paketů na aplikační vrstvě v rámci IMS získali operátoři schopnost implementovat sofistikované obchodní modely, kde různé aplikace mohly dostávat různý síťový přístup a být účtovány rozdílně. Tato schopnost se stala obzvláště důležitou s rozšířením over-the-top ([OTT](/mobilnisite/slovnik/ott/)) aplikací a potřebou operátorů efektivně konkurovat při zachování síťové účinnosti a standardů kvality.

## Klíčové vlastnosti

- Hloubková inspekce paketů na aplikační vrstvě pro přesnou identifikaci služeb
- Integrace s architekturou Policy and Charging Control (PCC) přes rozhraní Rx
- Stavová inspekce SIP signalizace a korelace s mediálními toky
- Podpora dynamického vynucování politik na základě detekce aplikace
- Schopnosti zákonného odposlechu pro soulad s regulacemi
- Optimalizace provozu a označování QoS na základě požadavků aplikace

## Související pojmy

- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [B-ALG na 3GPP Explorer](https://3gpp-explorer.com/glossary/b-alg/)
