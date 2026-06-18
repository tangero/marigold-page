---
slug: "arq"
url: "/mobilnisite/slovnik/arq/"
type: "slovnik"
title: "ARQ – Automatic Repeat Request"
date: 2025-01-01
abbr: "ARQ"
fullName: "Automatic Repeat Request"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/arq/"
summary: "ARQ je protokol pro řízení chyb používaný na vazební a transportní vrstvě k zajištění spolehlivého přenosu dat přes nespolehlivé kanály. Funguje na principu detekce chyb v přijatých paketech a automat"
---

ARQ je protokol pro řízení chyb, který zajišťuje spolehlivý přenos dat detekcí chyb v přijatých paketech a automatickým vyžádáním jejich opětovného odeslání od vysílače.

## Popis

Automatic Repeat Request (ARQ) je základní mechanismus pro řízení chyb implementovaný na vazební vrstvě (vrstva 2) a transportní vrstvě (vrstva 4) v systémech 3GPP. Funguje na principu detekce chyb následované žádostí o opakovaný přenos, pokud jsou chyby zjištěny. Protokol používá sekvenční čísla, kladná potvrzení ([ACK](/mobilnisite/slovnik/ack/)), záporná potvrzení ([NACK](/mobilnisite/slovnik/nack/)) a časovače ke správě spolehlivého doručování datových paketů mezi partnerskými entitami. V architekturách 3GPP je ARQ typicky implementován v protokolu Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) pro řídicí rovinu a data uživatelské roviny, stejně jako ve vyšších protokolech, jako je TCP, pro koncově-koncovou spolehlivost.

Protokol ARQ funguje prostřednictvím několika klíčových mechanismů. Nejprve vysílač segmentuje data do přenosových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) a každé přiřadí jedinečné sekvenční číslo. Tyto PDU jsou přeneseny k přijímači, který provádí detekci chyb pomocí cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) nebo podobných metod. Když přijímač úspěšně dekóduje PDU, odešle zpět k vysílači kladné potvrzení (ACK). Pokud přijímač detekuje chybu nebo zaznamená chybějící sekvenční čísla, odešle záporné potvrzení (NACK) nebo prostě neodešle ACK, čímž spustí časovač pro opakovaný přenos na straně vysílače. Vysílač udržuje vyrovnávací paměť pro opakovaný přenos obsahující nepotvrzené PDU a znovu je vysílá, když jsou přijaty NACK nebo vyprší časovače.

Systémy 3GPP implementují několik variant ARQ s různými provozními charakteristikami. Stop-and-Wait ARQ vyžaduje, aby vysílač před odesláním další PDU čekal na potvrzení, což poskytuje jednoduchost, ale špatné využití. Go-Back-N ARQ umožňuje vysílači odeslat více PDU bez čekání na potvrzení, ale vyžaduje opětovný přenos všech PDU od první chybné, když dojde k chybě. Selective Repeat ARQ, nejefektivnější varianta používaná v moderních systémech 3GPP, umožňuje selektivní opětovný přenos pouze chybných nebo chybějících PDU při pokračujícím přenosu nových PDU. Tento přístup maximalizuje propustnost při zachování spolehlivosti.

Protokol ARQ úzce spolupracuje s dalšími mechanismy řízení chyb v systémech 3GPP. Na fyzické vrstvě poskytuje dopředná korekce chyb ([FEC](/mobilnisite/slovnik/fec/)) první obrannou linii proti přenosovým chybám. Když FEC nedokáže chyby opravit, ARQ poskytuje sekundární mechanismus obnovy prostřednictvím opakovaného přenosu. Hybridní ARQ ([HARQ](/mobilnisite/slovnik/harq/)) kombinuje oba přístupy, využívaje FEC pro korekci chyb a ARQ pro opakovaný přenos, když FEC selže. Ve vrstvě RLC funguje ARQ v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)) pro spolehlivý přenos dat, zatímco nepotvrzovaný režim (UM) a transparentní režim (TM) poskytují odlehčené alternativy pro aplikace citlivé na zpoždění.

Parametry ARQ jsou pečlivě konfigurovány na základě požadavků služby a podmínek na kanálu. Mezi klíčové parametry patří maximální počet opakovaných přenosů, hodnoty časovačů pro opakovaný přenos, velikosti oken pro řízení toku a velikosti PDU. Tyto parametry jsou optimalizovány odlišně pro signalizaci v řídicí rovině (která vyžaduje vysokou spolehlivost) oproti datům uživatelské roviny (která mohou tolerovat určitou ztrátu paketů pro služby citlivé na zpoždění). Protokol také zahrnuje mechanismy pro přeřazení PDU na straně přijímače, zahození zastaralých PDU a zpracování chyb protokolu, aby bylo zajištěno robustní fungování za proměnných síťových podmínek.

## K čemu slouží

ARQ byl vyvinut k řešení základní výzvy spolehlivého přenosu dat přes ze své podstaty nespolehlivé bezdrátové kanály. Systémy bezdrátové komunikace trpí časově proměnnými podmínkami na kanálu, interferencí, útlumem a šumem, které způsobují chyby a ztráty paketů. Bez mechanismů řízení chyb by tyto poruchy činily digitální komunikační systémy nepoužitelnými pro většinu aplikací. ARQ poskytuje systematický přístup k detekci a obnově z přenosových chyb, což umožňuje spolehlivou komunikaci přes nedokonalé kanály.

Před rozšířeným přijetím ARQ v digitálních bezdrátových systémech spoléhaly analogové komunikační systémy na zlepšení poměru signálu k šumu a jednoduché techniky opakování, které byly neefektivní a poskytovaly omezenou spolehlivost. Rané digitální systémy používaly základní detekci chyb bez automatické obnovy, což vyžadovalo manuální zásah nebo opakované přenosy na aplikační vrstvě. ARQ automatizoval proces obnovy z chyb, což významně zlepšilo efektivitu a spolehlivost systému a současně snížilo latenci ve srovnání s manuálními přístupy. Automatická povaha protokolu mu umožňuje přizpůsobit se měnícím se podmínkám na kanálu bez lidského zásahu.

ARQ řeší několik kritických problémů v systémech bezdrátové komunikace. Za prvé zajišťuje integritu dat detekcí a opravou přenosových chyb, které by jinak poškodily přijímané informace. Za druhé poskytuje záruky spolehlivosti pro aplikace, které nesnesou ztrátu dat, jako jsou přenosy souborů, signalizační zprávy a kritické řídicí informace. Za třetí umožňuje efektivní využití bezdrátového spektra tím, že se vyhýbá zbytečným opakovaným přenosům prostřednictvím mechanismů selektivního potvrzování. Nakonec ARQ spolupracuje s dalšími technikami řízení chyb, aby poskytl vrstvenou obranu proti poruchám na kanálu, což umožňuje konstruktérům systémů vyvážit spolehlivost, latenci a propustnost podle požadavků aplikace.

## Klíčové vlastnosti

- Detekce chyb prostřednictvím CRC nebo podobných mechanismů
- Automatický opakovaný přenos chybných nebo chybějících paketů
- Schopnost selektivního opakování pro efektivní opakovaný přenos
- Sekvenční číslování pro řazení a identifikaci paketů
- Časovačem řízený opakovaný přenos pro ztracená potvrzení
- Řízení toku prostřednictvím mechanismů posuvného okna

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TR 26.914** (Rel-19) — Multimedia Telephony over IP Optimization
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [ARQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/arq/)
