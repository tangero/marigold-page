---
slug: "harq-ack"
url: "/mobilnisite/slovnik/harq-ack/"
type: "slovnik"
title: "HARQ-ACK – Hybrid Automatic Repeat Request Acknowledgement"
date: 2025-01-01
abbr: "HARQ-ACK"
fullName: "Hybrid Automatic Repeat Request Acknowledgement"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/harq-ack/"
summary: "Zpětnovazební signál vysílaný přijímačem (UE nebo gNB) pro indikaci úspěchu (ACK) nebo selhání (NACK) HARQ dekódovaného transportního bloku. Jde o klíčový řídicí prvek, který spouští retransmise a pří"
---

HARQ-ACK je zpětnovazební signál vysílaný přijímačem, který indikuje úspěch nebo selhání dekódovaného transportního bloku, a spouští retransmise, čímž ovlivňuje spolehlivost spoje, latenci a propustnost.

## Popis

HARQ-ACK (Hybrid Automatic Repeat Request Acknowledgement) je řídicí informace generovaná fyzickou vrstvou přijímače (uživatelského zařízení v uplinku, gNodeB v downlinku) jako odpověď na pokus o [HARQ](/mobilnisite/slovnik/harq/) přenos. Jejím hlavním účelem je informovat vysílač, zda byl konkrétní transportní blok úspěšně dekódován ([ACK](/mobilnisite/slovnik/ack/) - Acknowledgement) či nikoliv ([NACK](/mobilnisite/slovnik/nack/) - Negative Acknowledgement). Tato jednobitová nebo vícenásobná zpětná vazba je zásadním spouštěčem retransmisního mechanismu protokolu HARQ. Generování HARQ-ACK nastává poté, co přijímač provede kontrolu cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)) na dekódovaném transportním bloku. Úspěšná kontrola CRC vede k ACK, zatímco neúspěšná kontrola vede k NACK.

Přenos zpětné vazby HARQ-ACK je detailně definovaný postup fyzické vrstvy. V 5G NR jsou bity HARQ-ACK multiplexovány s dalšími řídicími informacemi uplinku (UCI), jako je Scheduling Request (SR) a Channel State Information ([CSI](/mobilnisite/slovnik/csi/)). Tento multiplexovaný řídicí přenos je následně kanálově kódován (např. pomocí Reed-Muller nebo Polar kódů pro malé přenosy), modulován a namapován na konkrétní fyzické zdroje na PUCCH (Physical Uplink Control Channel), nebo v případě souběžných uplink dat přenášen spolu s daty na PUSCH (Physical Uplink Shared Channel). Časový vztah mezi příjmem downlink dat (na [PDSCH](/mobilnisite/slovnik/pdsch/)) a odpovídajícím uplink přenosem HARQ-ACK je definován parametrem K1, který poskytuje flexibilitu pro přizpůsobení různým zpracovatelským schopnostem a požadavkům na latenci.

Pro scénáře s agregací nosných nebo více TRP (Transmission Reception Point) se zpětná vazba HARQ-ACK stává vícenásobným kódovým slovem. UE toto kódové slovo vytváří na základě přijatých rozhodnutí o plánování (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)), což zajišťuje, že gNB může jednoznačně přiřadit každý bit ACK/NACK konkrétnímu vysílanému transportnímu bloku. Spolehlivost přenosu HARQ-ACK je prvořadá, neboť ztracený ACK může způsobit zbytečnou retransmisi (plýtvání zdroji), zatímco ztracený NACK může vést ke ztrátě paketu. Proto jsou fyzické zdroje pro PUCCH navrženy pro vysokou spolehlivost, často s využitím modulace nízkého řádu a frekvenční diverzity.

## K čemu slouží

HARQ-ACK existuje k uzavření smyčky protokolu [HARQ](/mobilnisite/slovnik/harq/). Bez explicitní a včasné zpětné vazby by vysílač nevěděl, zda má vysílat nová data nebo retransmitovat stará, což by činilo mechanismus HARQ nefunkčním. Jeho účelem je poskytovat nízkolatenční a spolehlivý indikátor stavu dekódování, který umožňuje efektivní a adaptivní správu retransmisí na MAC vrstvě. Tím se řeší problém vysílání naslepo, které by vedlo buď k nadměrné redundanci (pokud by vysílač vždy retransmitoval), nebo k vysokým ztrátám paketů (pokud by nikdy neretransmitoval).

Návrh mechanismů HARQ-ACK, zejména od LTE k 5G NR, byl motivován potřebou podporovat složitější nasazení a přísné požadavky služeb. V LTE bylo časování HARQ-ACK převážně synchronní. Přechod k plně asynchronnímu HARQ v NR vyžadoval sofistikovanější signalizaci zpětné vazby, protože časování retransmisí není předem dané. Dále, pro podporu ultra-spolehlivé komunikace s nízkou latencí (URLLC), musí být latence zpětné vazby (K1) extrémně krátká a spolehlivost samotného signálu HARQ-ACK musí být velmi vysoká. Návrh vícenásobného kódového slova pro agregaci nosných řeší problém efektivního poskytování zpětné vazby pro více komponentních nosných bez proporcionálního nárůstu signalizační režie, což je klíčové pro využití širokých šířek pásma.

## Klíčové vlastnosti

- Přenáší ACK (úspěch) nebo NACK (selhání) pro HARQ proces
- Vysílá se na PUCCH nebo je multiplexován na PUSCH v uplinku
- Časování vůči příjmu dat je konfigurovatelné (parametr K1 v NR)
- Může být jeden bit nebo součást vícenásobného kódového slova pro agregaci nosných
- Vysoká spolehlivost přenosu je zásadní pro výkon systému
- Integrální součást rámce řídicích informací uplinku (UCI)

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures

---

📖 **Anglický originál a plná specifikace:** [HARQ-ACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/harq-ack/)
