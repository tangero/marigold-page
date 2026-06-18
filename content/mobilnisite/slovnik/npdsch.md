---
slug: "npdsch"
url: "/mobilnisite/slovnik/npdsch/"
type: "slovnik"
title: "NPDSCH – Narrow Band Physical Downlink Shared Channel"
date: 2025-01-01
abbr: "NPDSCH"
fullName: "Narrow Band Physical Downlink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/npdsch/"
summary: "Primární fyzický kanál pro přenos dat ve směru dolní linky pro LTE-M a NB-IoT. Přenáší uživatelská data, vysílané systémové informace (SIBs) a stránkovací zprávy k IoT zařízením. Pracuje v šířce pásma"
---

NPDSCH je úzkopásmový fyzický sdílený kanál pro přenos ve směru dolní linky pro LTE-M a NB-IoT, který přenáší uživatelská data, systémové informace a stránkovací zprávy v šířce pásma 180 kHz, aby umožnil efektivní komunikaci IoT s nízkou spotřebou.

## Popis

Úzkopásmový fyzický sdílený kanál pro přenos ve směru dolní linky (NPDSCH) je klíčový transportní kanál pro data uživatelské a řídicí roviny v sítích LTE-M (eMTC) a NB-IoT. Zavedený ve specifikaci 3GPP Release 13, je úzkopásmovou obdobou kanálu LTE [PDSCH](/mobilnisite/slovnik/pdsch/), specificky optimalizovanou pro omezení IoT zařízení. Kanál zabírá šířku pásma 180 kHz, což odpovídá jednomu zdrojovému bloku v klasickém LTE, což drasticky snižuje složitost [RF](/mobilnisite/slovnik/rf/) a základního pásma přijímače UE. NPDSCH se používá k přenosu různých druhů dat, včetně uživatelských dat ze sdíleného kanálu dolní linky ([DL-SCH](/mobilnisite/slovnik/dl-sch/)), vysílaných bloků systémových informací (SIBs-NB pro NB-IoT) a stránkovacích zpráv.

Z provozní perspektivy je NPDSCH vždy plánován Úzkopásmovým fyzickým řídicím kanálem dolní linky ([NPDCCH](/mobilnisite/slovnik/npdcch/)). UE nejprve dekóduje zprávu [DCI](/mobilnisite/slovnik/dci/) na NPDCCH, která obsahuje plánovací přiřazení specifikující přesné zdroje (podsnímky) alokované pro následný přenos NPDSCH, schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a klíčově počet opakování. Přenos NPDSCH může zabírat více podsnímků a pro zařízení s rozšířeným pokrytím jsou tyto podsnímky mnohokrát opakovány (od několika až po stovky), aby bylo zajištěno spolehlivé dekódování při velmi nízkých úrovních signálu. UE kombinuje opakované podsnímky ke zlepšení efektivního poměru signálu k šumu.

Zpracování na fyzické vrstvě zahrnuje kanálové kódování (Turbo kódování pro LTE-M, konvoluční kódování s vracením na začátek pro NB-IoT), skramblování, modulaci (typicky [QPSK](/mobilnisite/slovnik/qpsk/), s modulacemi vyššího řádu možnými v pozdějších verzích pro LTE-M) a mapování vrstev. Modulované symboly jsou následně mapovány na zdrojové elementy v rámci alokovaného úzkého pásma. Klíčovou architektonickou vlastností je podpora různých velikostí transportních bloků ([TBS](/mobilnisite/slovnik/tbs/)) pro efektivní přenos malých, sporadických datových paketů typických pro IoT provoz. NPDSCH spolupracuje s kanálem NPUSCH (pro směr nahoru) a NPDCCH (řídicí) a vytváří tak kompletní, optimalizované rozhraní pro mobilní IoT, které vyvažuje propustnost dat, pokrytí a spotřebu zařízení.

## K čemu slouží

NPDSCH byl vytvořen, aby poskytoval životaschopnou datovou cestu ve směru dolní linky pro novou třídu zařízení pro nízkopříkonové širokopásmové sítě (LPWA) definovanou ve specifikaci 3GPP Release 13. Standardní kanál LTE PDSCH se pro tento účel nehodil, protože vyžadoval zařízení schopná přijímat šířky pásma 1,4 MHz a více, což zvyšovalo náklady a spotřebu. Dále mu chyběla nativní podpora masivního opakování potřebného k dosažení zařízení v extrémních lokalitách, jako jsou podzemní měřiče nebo venkovní zemědělské senzory. Stávající kanál nemohl dosáhnout cílové maximální ztráty spojení (MCL) 164 dB pro NB-IoT.

Konstrukce NPDSCH přímo řeší tato omezení. Jeho šířka pásma 180 kHz umožňuje velmi levné implementace UE s jednou anténou a polovičním duplexem. Vestavěný mechanismus opakování je primární funkcí, nikoli dodatečným řešením, což umožňuje spolehlivou komunikaci v nejnáročnějším rádiovém prostředí. Díky těsnému propojení s plánovacím mechanismem NPDCCH mohou zařízení spát po delší dobu a probouzet se pouze k naslouchání řídicí zprávě před přijetím dat, což je zásadní pro dosažení cíle desetileté životnosti baterií na trhu IoT. NPDSCH tedy řeší kritický problém doručování dat ve směru dolní linky k ultra levným zařízením s omezeným pokrytím a omezenou spotřebou energie, čímž činí standardy 3GPP konkurenceschopnými v širším ekosystému LPWA oproti neceliulárním technologiím.

## Klíčové vlastnosti

- Pracuje v rámci úzkopásmového nosiče o šířce 180 kHz
- Přenáší uživatelská data, systémové informace (SIBs) a stránkovací zprávy
- Podporuje rozsáhlé opakování podsnímků pro hluboké rozšíření pokrytí
- Je dynamicky plánován kanálem NPDCCH prostřednictvím DCI
- Používá optimalizovaná schémata modulace (základně QPSK) a kódování pro IoT
- Umožňuje efektivní provoz s polovičním duplexem a dlouhou životnost baterie zařízení

## Související pojmy

- [NPDCCH – Narrow Band Physical Downlink Control Channel](/mobilnisite/slovnik/npdcch/)
- [NPUSCH – Narrowband Physical Uplink Shared Channel](/mobilnisite/slovnik/npusch/)
- [DL-SCH – Downlink Shared Channel](/mobilnisite/slovnik/dl-sch/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NPDSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/npdsch/)
