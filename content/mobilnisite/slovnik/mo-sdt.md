---
slug: "mo-sdt"
url: "/mobilnisite/slovnik/mo-sdt/"
type: "slovnik"
title: "MO-SDT – Mobile Originated Small Data Transmission"
date: 2025-01-01
abbr: "MO-SDT"
fullName: "Mobile Originated Small Data Transmission"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mo-sdt/"
summary: "MO-SDT je mechanismus 3GPP umožňující IoT zařízením přenášet malé datové pakety s minimální signalizační režií, a to i v neaktivních nebo nečinných stavech. Optimalizuje síťovou efektivitu a výdrž bat"
---

MO-SDT je mechanismus 3GPP pro IoT zařízení umožňující přenos malých datových paketů s minimální signalizační režií v neaktivních nebo nečinných stavech, čímž optimalizuje síťovou efektivitu a výdrž baterie.

## Popis

Mobile Originated Small Data Transmission (MO-SDT) je funkce standardizovaná v 3GPP Release 18, navržená pro efektivní zpracování sporadických přenosů malých objemů dat od IoT a dalších zařízení. Funguje tak, že umožňuje uživatelskému zařízení (UE) odeslat omezené množství dat ve směru uplink, aniž by opustilo stav [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE nebo RRC_IDLE, čímž se vyhne signalizační režii a latenci spojené s přechodem do stavu RRC_CONNECTED. Toho je dosaženo zapouzdřením dat do specifických signalizačních zpráv, jako je modifikovaný RRC Resume Request nebo nová zpráva pro přenos malých dat, které síť zpracuje bez plné reaktivace všech přenosových kanálů (bearerů) uživatelské roviny.

Architektura zahrnuje koordinaci mezi rádiovou přístupovou sítí (RAN) a jádrem sítě (CN). Když má UE ve stavu RRC_INACTIVE data k odeslání, může iniciovat MO-SDT, pokud je splněna velikost dat a další podmínky (jako nakonfigurované prahové hodnoty). UE zahrne datovou část (payload) do počáteční přístupové zprávy odeslané gNB. gNB po jejím přijetí může data přeposlat do [UPF](/mobilnisite/slovnik/upf/) přes kontext poslední obsluhující NG-RAN uzlu nebo novou cestu, v závislosti na implementaci. Jádro sítě, konkrétně [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/), tento proces podporuje tím, že umožní krátkodobé vytvoření uživatelské roviny nebo využití předkonfigurovaného prostředku pro přenos malých dat.

Klíčové komponenty zahrnují UE, které musí podporovat procedury MO-SDT dle specifikací 3GPP; gNB, které zajišťuje příjem malých dat a jejich přeposlání; a funkce jádra sítě (AMF, SMF, UPF), které spravují kontext a směrování dat. Procedura využívá uložený kontext UE v RAN (pro stav INACTIVE) k minimalizaci signalizace. Úlohou MO-SDT je snížit latenci, signalizační zátěž a spotřebu energie u zařízení, která primárně vysílají malé, nepravidelné dávky dat, což z něj činí základní kámen efektivní hromadné komunikace typu stroj-stroj (mMTC) v 5G a dalších generacích.

## K čemu slouží

MO-SDT byl vytvořen k řešení neefektivit tradičního navazování spojení pro IoT a M2M zařízení generující malé, sporadické datové pakety. Před jeho zavedením muselo UE potřebující odeslat data provést kompletní nastavení [RRC](/mobilnisite/slovnik/rrc/) spojení, zahrnující mnoho signalizačních výměn, a to i pro pár bajtů dat. Tento proces spotřebovával značnou energii baterie a síťové prostředky, což je neudržitelné pro hromadná IoT nasazení s miliardami zařízení. Omezení předchozích přístupů, jako je trvalé udržování zařízení ve stavu připojení nebo použití neefektivní signalizace, vedla k vysoké režii a snížené kapacitě sítě.

Motivace vychází z růstu IoT aplikací, jako jsou senzory, chytré měřiče a nositelná zařízení, které vyžadují energeticky efektivní a síťově šetrnou komunikaci. 3GPP Release 18 zavedlo MO-SDT jako součást širších vylepšení pro zařízení se sníženou schopností (RedCap) a optimalizaci IoT. Řeší problém signalizačních bouří a vybíjení baterie tím, že umožňuje přenos dat bez přechodů mezi stavy, což je v souladu s cíli 5G podporovat různé služby s různými požadavky. Historicky raná IoT řešení v LTE využívala techniky jako Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) nebo rozšířené Discontinuous Reception (eDRX), ale ty stále nesla režii během přenosu dat; MO-SDT poskytuje integrovanější a efektivnější řešení v rámci architektury 5G NR.

## Klíčové vlastnosti

- Umožňuje přenos dat ve směru uplink ze stavů RRC_INACTIVE nebo RRC_IDLE
- Snižuje signalizační režii vyhýbáním se plnému navázání RRC spojení
- Podporuje malé datové pakety s velikostními limity definovanými síťovou konfigurací
- Využívá uložený kontext UE v RAN pro rychlé zpracování
- Integruje se s 5G Core Network pro efektivní směrování dat
- Prodlužuje výdrž baterie IoT zařízení minimalizací rádiové aktivity

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MO-SDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mo-sdt/)
