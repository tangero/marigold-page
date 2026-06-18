---
slug: "procedurecode"
url: "/mobilnisite/slovnik/procedurecode/"
type: "slovnik"
title: "ProcedureCode – Procedure Code"
date: 2025-01-01
abbr: "ProcedureCode"
fullName: "Procedure Code"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/procedurecode/"
summary: "Jednobajtová (1-octet) neznaménková výčtová hodnota používaná v aplikačním protokolu Xn (XnAP) k jednoznačné identifikaci konkrétního postupu nebo typu zprávy. Umožňuje efektivní dekódování a zpracová"
---

ProcedureCode je jednobajtová (1-octet) výčtová hodnota použitá v protokolu XnAP k jednoznačné identifikaci konkrétního postupu nebo typu zprávy za účelem korektní signalizace mezi 5G gNB.

## Popis

ProcedureCode je základním polem v aplikačním protokolu Xn (XnAP) definovaném ve specifikaci 3GPP TS 37.466 pro architekturu 5G New Radio (NR). Jedná se o kompaktní jednobajtovou (8bitovou) neznaménkovou celočíselnou hodnotu sloužící jako výčtový identifikátor. Každému odlišnému postupu XnAP – jako je Příprava přechodu (Handover Preparation), Uvolnění kontextu UE (UE Context Release) nebo Aktualizace konfigurace RAN (RAN Configuration Update) – je v tomto poli přiřazena unikátní číselná hodnota. Když gNB odešle zprávu XnAP protějškovému gNB přes rozhraní Xn, je ProcedureCode zahrnuto v hlavičce protokolu nebo v iniciálním elementu zprávy. To umožňuje přijímajícímu gNB a jeho entitě protokolu XnAP okamžitě identifikovat typ příchozí zprávy a vyvolat odpovídající procedurální logiku pro parsování, validaci a provedení.

Technicky ProcedureCode funguje ve spojení s dalšími informacemi pro diskriminaci protokolu. Protokol XnAP používá ASN.1 pro definici dat a je kódován pomocí Pravidel baleného kódování (Packed Encoding Rules – [PER](/mobilnisite/slovnik/per/)). Struktura zprávy typicky začíná diskriminátorem protokolu a ID transakce, po kterém následuje ProcedureCode, jež určuje strukturu zbytku zprávy – kritičnost (Criticality), typ zprávy (Message Type) a procedurálně specifické informační elementy (Information Elements – IEs). Například hodnota ProcedureCode odpovídající 'Přípravě přechodu' (Handover Preparation) sděluje přijímači, že následující IEs budou zahrnovat ID cílové buňky (Target Cell ID), bezpečnostní schopnosti UE a [RRC](/mobilnisite/slovnik/rrc/) kontext. To umožňuje efektivní zpracování; přijímač nepotřebuje parsovat celou zprávu, aby pochopil její účel.

Z architektonického hlediska je ProcedureCode klíčovou součástí signalizace řídicí roviny mezi gNB (rozhraní Xn-C). Je zásadní pro mobilitu mezi gNB, duální konektivitu a pokročilé funkce koordinace rádiového rozhraní v 5G. Velikost jednoho bajtu představuje kompromis návrhu, poskytující dostatek prostoru (256 možných hodnot) pro všechny definované i budoucí postupy a zároveň minimalizující režii protokolu. Výčet je spravován 3GPP, přičemž nové kódy jsou přiřazovány pro nové postupy zaváděné v následujících vydáních specifikací. Spolehlivá interpretace tohoto kódu je kritická pro interoperabilitu sítě, protože neshoda nebo neznámý kód může vést k selhání postupu a přerušení spojení.

## K čemu slouží

ProcedureCode existuje za účelem umožnění efektivní a jednoznačné identifikace signalizačních postupů v protokolu rozhraní mezi základnovými stanicemi. V komplexních sítích s rádiovým přístupem od více dodavatelů musí gNB od různých výrobců komunikovat bezproblémově. Standardizovaný číselný kód poskytuje jednoduchý a rychlý způsob, jak příchozí zprávu předat správnému softwarovému modulu obsluhy (handler). Bez takového kódu by musel přijímač typ postupu odvozovat z obsahu zprávy, což je neefektivní, náchylné k chybám a mohlo by vést k selhání interoperability. Jeho zavedení bylo motivováno potřebou štíhlého a robustního signalizačního protokolu pro rozhraní Xn v 5G, vycházejícího z podobných mechanismů u starších rozhraní jako [S1AP](/mobilnisite/slovnik/s1ap/) a X2AP.

Historicky podobné koncepty existovaly v protokolech 3GPP (např. Procedure IDs v [RANAP](/mobilnisite/slovnik/ranap/), Message Types v X2AP), ale formální definice jako 'ProcedureCode' v TS 37.466 pro 5G NR představuje čistý a konzistentní přístup. Řeší omezení plynoucí z implicitní definice identity postupu pouze typem zprávy ASN.1, což může být méně efektivní pro runtime dekódování. Velikost jednoho bajtu je zvolena záměrně, aby se minimalizovalo využití přenosové kapacity na rozhraní Xn, které může pokrývat velké geografické vzdálenosti, a zároveň aby byla zachována rozšiřitelnost. To je zvláště důležité pro případy užití 5G vyžadující ultra-nízké latence, kde efektivita signalizace přímo ovlivňuje zpoždění při přechodu.

ProcedureCode řeší problém rozšiřitelnosti protokolu a zpětné kompatibility. Nové postupy lze v budoucích vydáních 3GPP přidat přiřazením nových, nepoužitých kódů. Starší gNB přijímající zprávu s neznámým ProcedureCode mohou následovat standardizovaná pravidla pro zpracování chyb (např. odeslání zprávy o selhání postupu), což umožňuje elegantní degradaci. Jeho účel je fundamentální pro principy architektury založené na službách (service-based architecture) v 5G, umožňující diskrétní, dobře definované postupy mezi síťovými funkcemi. Podporuje dynamické a husté scénáře nasazení 5G, kde postupy jako podmíněný přechod (conditional handover) nebo koordinace síťového řezu (network slicing coordination) vyžadují rychlou a spolehlivou výměnu signalizace.

## Klíčové vlastnosti

- Jednobajtová (1-octet) neznaménková celočíselná hodnota poskytující 256 možných výčtových hodnot
- Jednoznačně identifikuje každý typ postupu XnAP (např. Příprava přechodu, Uvolnění kontextu UE)
- Umožňuje rychlé předání (dispatch) a zpracování příchozích signalizačních zpráv na přijímajícím gNB
- Definováno v ASN.1 jako součást struktury PDU XnAP pro jednoznačné kódování/dekódování
- Zásadní pro interoperabilitu mezi gNB od více dodavatelů přes rozhraní Xn
- Podporuje rozšiřitelnost pro nové postupy v budoucích vydáních 3GPP

## Definující specifikace

- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [ProcedureCode na 3GPP Explorer](https://3gpp-explorer.com/glossary/procedurecode/)
