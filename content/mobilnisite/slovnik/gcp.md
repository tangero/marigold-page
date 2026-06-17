---
slug: "gcp"
url: "/mobilnisite/slovnik/gcp/"
type: "slovnik"
title: "GCP – Gateway Control Protocol"
date: 2025-01-01
abbr: "GCP"
fullName: "Gateway Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gcp/"
summary: "Gateway Control Protocol (GCP) je 3GPP adaptace protokolu ITU-T H.248/Megaco. Definuje signalizační rozhraní mezi řadičem mediální brány (Media Gateway Controller, MGC) a mediální bránou (Media Gatewa"
---

GCP je 3GPP adaptace protokolu ITU-T H.248/Megaco, která definuje signalizační rozhraní mezi řadičem mediální brány (Media Gateway Controller) a mediální bránou (Media Gateway) pro řízení přenosových (bearer) prostředků.

## Popis

Gateway Control Protocol (GCP) je protokol typu master-slave standardizovaný 3GPP, založený na standardu [ITU-T](/mobilnisite/slovnik/itu-t/) H.248 (známém také jako Megaco). Funguje přes rozhraní Mc, které spojuje řadič mediální brány (Media Gateway Controller, [MGC](/mobilnisite/slovnik/mgc/)), entitu řízení stavu hovoru, s mediální bránou (Media Gateway, [MGW](/mobilnisite/slovnik/mgw/)), entitou zpracování médií. MGC, který vystupuje jako kontroler, používá příkazy GCP k instruování MGW, řízené entity, jak navazovat, upravovat a ukončovat mediální toky. To zahrnuje vytváření a mazání logických entit zvaných terminace (které reprezentují mediální toky nebo koncové body) a jejich umisťování do kontextů (které reprezentují asociace mezi terminacemi, například část hovoru).

GCP používá transakční model, kde kontroler posílá příkazy uvnitř transakcí a brána odpovídá replikami. Příkazy zahrnují Add, Modify, Subtract, Move a AuditValue. Protokol je nezávislý na transportu, běžně běží přes UDP, TCP nebo SCTP, a pro zprávy používá textový nebo binární formát kódování (ASN.1 PER). Podporuje balíčky (packages), což jsou rozšíření definující vlastnosti, události, signály a statistiky pro specifické typy terminací, jako jsou analogové linky, TDM okruhy nebo RTP toky. Tato modularita umožňuje GCP řídit širokou škálu typů mediálních bran.

V architektuře 3GPP je GCP základním kamenem dekomponovaného modelu brány zavedeného s 3GPP Release 4. Umožňuje oddělení roviny řízení hovorů (zajišťované MGC/[MSC](/mobilnisite/slovnik/msc/) Serverem) od uživatelské roviny/roviny přenosu médií (zajišťované MGW). Toto oddělení je klíčové pro škálovatelnost sítě, flexibilitu a efektivní nasazování nových služeb. MGC používá GCP k instruování MGW, aby alokovala prostředky, aplikovala kodeky, řešila potlačení ozvěn, generovala tóny a hlášení a propojovala mediální toky pro hovory procházející různými typy sítí (např. z TDM do IP).

## K čemu slouží

GCP byl vytvořen, aby řešil omezení monolitických přepínacích systémů, kde bylo řízení hovorů a přepínání médií těsně integrováno v rámci jediného síťového uzlu, jako je tradiční okruhově přepínaná [MSC](/mobilnisite/slovnik/msc/). Tato integrace činila sítě nepružnými, nákladnými na škálování a obtížnými na upgrade s novými schopnostmi zpracování médií. Primární motivací bylo umožnit dekomponovanou architekturu sítě příští generace ([NGN](/mobilnisite/slovnik/ngn/)).

Standardizací řídicího rozhraní mezi inteligencí řízení hovorů a přepínací strukturou médií umožnilo 3GPP (přijetím práce [ITU-T](/mobilnisite/slovnik/itu-t/) H.248) vyvíjet, nasazovat a škálovat tyto dvě funkce nezávisle. Toto oddělení řeší několik klíčových problémů: umožňuje centralizované řízení distribuovaných mediálních prostředků, umožňuje efektivnější využití přenosových prostředků (např. pomocí TrFO a provozu bez transkódéru) a usnadňuje zavedení paketového (IP) přenosu médií vedle nebo namísto staršího TDM. Vytvoření GCP/H.248 bylo konkurenčním a kolaborativním úsilím v průmyslu s cílem definovat robustní, na dodavateli nezávislý protokol pro řízení mediálních bran, který se nakonec stal nástupcem dřívějších proprietárních nebo méně schopných protokolů, jako je [MGCP](/mobilnisite/slovnik/mgcp/).

## Klíčové vlastnosti

- Řídicí model master-slave (MGC řídí MGW)
- Transakční struktura příkaz/odpověď
- Modulární systém balíčků pro rozšiřování funkcionality
- Nezávislost na transportu (UDP, TCP, SCTP)
- Podpora textového a binárního kódování zpráv
- Řízení kontextů a terminací pro asociaci mediálních toků

## Související pojmy

- [MEGACO – MEdia GAteway COntrol](/mobilnisite/slovnik/megaco/)

## Definující specifikace

- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TR 43.903** (Rel-19) — Feasibility Study for A-interface over IP

---

📖 **Anglický originál a plná specifikace:** [GCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gcp/)
