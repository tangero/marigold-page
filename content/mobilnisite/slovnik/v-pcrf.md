---
slug: "v-pcrf"
url: "/mobilnisite/slovnik/v-pcrf/"
type: "slovnik"
title: "V-PCRF – Visited Policy and Charging Rules Function"
date: 2025-01-01
abbr: "V-PCRF"
fullName: "Visited Policy and Charging Rules Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-pcrf/"
summary: "Funkce pravidel pro zásady a účtování (PCRF) umístěná v navštívené veřejné pozemní mobilní síti (VPLMN). Působí jako proxy nebo spolupracující rozhodovací bod, komunikuje s domácí PCRF (H-PCRF) a posk"
---

V-PCRF je funkce pravidel pro zásady a účtování (Policy and Charging Rules Function) umístěná ve navštívené síti, která komunikuje s domácí PCRF (H-PCRF) za účelem poskytnutí pravidel pro zásady a účtování k vynucení na provozu roamujícího účastníka.

## Popis

Navštívená funkce pravidel pro zásady a účtování (V-PCRF) je klíčový síťový prvek v architektuře 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) pro EPS (Evolved Packet System) a starší systémy, který se specificky zabývá roamingem. Nachází se v navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)). Jejím hlavním účelem je usnadnit řízení zásad a účtování pro účastníka, který roamuje. V-PCRF obvykle sama nečiní konečná rozhodnutí o zásadách; místo toho působí jako zprostředkovatel mezi vynucovacím bodem v navštívené síti ([V-PCEF](/mobilnisite/slovnik/v-pcef/), umístěným na [PGW](/mobilnisite/slovnik/pgw/)) a rozhodovacím bodem v domácí síti ([H-PCRF](/mobilnisite/slovnik/h-pcrf/)). Komunikace mezi V-PCRF a H-PCRF probíhá přes referenční bod S9, který je založen na protokolu Diameter. Když roamující účastník naváže připojení [PDN](/mobilnisite/slovnik/pdn/), V-PCEF signalizuje V-PCRF (přes rozhraní Gx). V-PCRF následně iniciuje relaci s H-PCRF přes S9 a předává informace jako identitu účastníka a požadovanou službu. H-PCRF, která má přístup k profilu účastníka a servisním datům, učiní rozhodnutí o zásadách a vygeneruje PCC pravidla. Tato pravidla jsou odeslána zpět V-PCRF. V-PCRF může provádět lokální funkce, jako je přidání zásad specifických pro navštívenou síť (např. souvisejících s lokálním breakoutem nebo dohodami o účtování v navštívené síti), nebo může jednoduše předat pravidla od H-PCRF. Nakonec V-PCRF zřídí tato PCC pravidla pro V-PCEF přes rozhraní Gx. V-PCRF tedy slouží jako kotva lokální funkce pravidel pro zásady a účtování v navštívené síti, zajišťuje, že zásady domácího operátora jsou správně interpretovány a aplikovány v kontextu navštívené sítě, a zároveň umožňuje navštívenému operátorovi vložit vlastní logiku zásad tam, kde to roamingové dohody povolují.

## K čemu slouží

V-PCRF byla zavedena za účelem rozšíření rámce [PCC](/mobilnisite/slovnik/pcc/), původně definovaného pro domácí síť, do robustních roamingových scénářů. Před standardizovaným PCC roamingem bylo obtížné aplikovat dynamické, služebně-aware zásady pro roamery, což často vedlo k 'nejnižšímu společnému jmenovateli' v uživatelském zážitku. V-PCRF to řeší vytvořením jasného architektonického rozdělení: domácí síť ([H-PCRF](/mobilnisite/slovnik/h-pcrf/)) vlastní účastníka a činí primární rozhodnutí o zásadách, zatímco navštívená síť poskytuje lokální funkci zásad (V-PCRF) pro komunikaci s vlastním vynucovacím bodem (V-PCEF). Tento model řeší několik problémů. Umožňuje domácímu operátorovi udržovat kontrolu nad služebním zážitkem a účtováním účastníka. Umožňuje navštívenému operátorovi spravovat vlastní síťové zdroje a aplikovat jakékoli lokální zásady nebo doplňky účtování. Poskytuje také škálovatelné a bezpečné rozhraní (S9) mezi operátory, které skrývá interní detaily sítí. V-PCRF je nezbytná pro umožnění pokročilých služeb jako IMS roaming, kde je vyžadována konzistentní QoS pro hlasové a videohovory bez ohledu na polohu, a pro implementaci složitých modelů účtování, jako je sponzorované datové připojení, v roamingovém kontextu.

## Klíčové vlastnosti

- Proxy/funkce pro rozhodování o zásadách v navštívené PLMN pro roamující účastníky
- Komunikuje s domácí PCRF (H-PCRF) přes roamingové rozhraní S9 založené na Diameter
- Komunikuje s V-PCEF (na PGW) přes rozhraní Gx
- Může rozšiřovat rozhodnutí H-PCRF o lokální zásady navštívené sítě
- Usnadňuje řízení účtování a správu kreditu pro roamingové relace
- Centrální uzel pro aplikaci roamingových dohod v řídicí rovině zásad (policy control plane)

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [V-PCEF – Visited Policy and Charging Enforcement Function](/mobilnisite/slovnik/v-pcef/)
- [H-PCRF – Home Policy and Charging Rules Function](/mobilnisite/slovnik/h-pcrf/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming

---

📖 **Anglický originál a plná specifikace:** [V-PCRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-pcrf/)
