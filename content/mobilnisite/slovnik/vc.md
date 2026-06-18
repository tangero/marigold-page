---
slug: "vc"
url: "/mobilnisite/slovnik/vc/"
type: "slovnik"
title: "VC – Virtual Connection"
date: 2025-01-01
abbr: "VC"
fullName: "Virtual Connection"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vc/"
summary: "Virtuální spojení (VC) je logická komunikační cesta zřízená mezi koncovými body v přenosové síti, jako je síť ATM nebo IP, pro přenos uživatelských dat a signalizace. Poskytuje spolehlivou, spojově or"
---

VC (Virtual Connection) je logická, spojově orientovaná komunikační cesta v přenosové síti, která spolehlivě přenáší uživatelská data a signalizaci mezi koncovými body, aby zajistila integritu a správné pořadí datových jednotek protokolů 3GPP.

## Popis

Virtuální spojení (VC) je základním konceptem v přenosovém síťování, který poskytuje logický komunikační kanál typu bod–bod nebo bod–více bodů přes sdílenou fyzickou infrastrukturu. V kontextu 3GPP se VC primárně používají v rozhraních Iu, Iub a Iur pro přenos dat uživatelské roviny, signalizace řídicí roviny a provozu pro provoz a údržbu ([OAM](/mobilnisite/slovnik/oam/)) mezi síťovými uzly, jako jsou [RNC](/mobilnisite/slovnik/rnc/), Node B a prvky jádra sítě. VC je identifikováno sadou parametrů, jako je identifikátor virtuální cesty (VPI) a identifikátor virtuálního kanálu (VCI) v sítích [ATM](/mobilnisite/slovnik/atm/), nebo analogickými štítky v přenosu založeném na [MPLS](/mobilnisite/slovnik/mpls/) nebo Ethernetu. Funguje na vrstvě spojů dat (vrstva 2) a poskytuje spojově orientovanou službu, což znamená, že cesta je zřízena před zahájením přenosu dat, a nabízí garantovanou šířku pásma, nízkou latenci a doručování paketů ve správném pořadí, což je klíčové pro služby v reálném čase, jako je hlas a video.

Architektura VC zahrnuje fáze zřízení, údržby a zrušení spojení řízené signalizačními protokoly. Pro přenos založený na ATM, který převládal v raných vydáních 3GPP (od [R99](/mobilnisite/slovnik/r99/)), se VC zřizují pomocí adaptační vrstvy ATM ([AAL](/mobilnisite/slovnik/aal/)), konkrétně [AAL2](/mobilnisite/slovnik/aal2/) pro komprimovaný hlas a [AAL5](/mobilnisite/slovnik/aal5/) pro data a signalizaci. Koncové body VC, jako jsou RNC a Node B, při zřizování spojení vyjednávají parametry, jako je špičkový přenosový výkon, udržitelný přenosový výkon a třídy kvality služby (QoS), aby vyhověly požadavkům různých typů provozu. VC funguje jako „potrubí“, které multiplexuje více logických kanálů, z nichž každý přenáší různé typy provozu (např. vyhrazené kanály pro přenos, signalizační kanály), přes jeden fyzický spoj, čímž optimalizuje využití zdrojů.

Při provozu jsou data z protokolů vyšších vrstev segmentována do buněk nebo rámců vhodných pro přenosové médium. Například v ATM VC segmentuje IP pakety nebo data z okruhového přepojování do 53bajtových buněk, které jsou pak směrovány sítí na základě štítků VPI/VCI. VC zajišťuje, že všechny buňky patřící ke stejnému spojení sledují stejnou cestu, čímž minimalizuje chvění a ztrátu paketů. S vývojem 3GPP došlo k přechodu přenosu z ATM na řešení založená na IP (např. GTP přes UDP/IP), ale koncept VC přetrval ve formě logických tunelů, jako jsou tunely GTP, které poskytují podobnou spojově orientovanou sémantiku přes nespojové IP sítě. Úlohou VC v síti je abstrahovat podrobnosti podkladového přenosu a nabízet konzistentní rozhraní pro protokoly vyšších vrstev pro spolehlivý přenos dat, což je nezbytné pro udržení kvality služeb napříč segmenty rádiového přístupu a jádra sítě.

## K čemu slouží

Virtuální spojení (VC) bylo zavedeno, aby řešilo potřebu spolehlivého a efektivního přenosu různých typů provozu – hlasu, dat a signalizace – v raných sítích 3GPP (počínaje R99). Před 3GPP se telekomunikační sítě silně spoléhaly na okruhově přepínaná spojení (např. linky T1/E1), která byla rigidní a neefektivní pro přerušovaný datový provoz. Technologie VC, zejména s využitím ATM, poskytla flexibilní, spojově orientovaný mechanismus, který mohl statisticky multiplexovat více logických kanálů přes jeden fyzický spoj, optimalizovat využití šířky pásma a snižovat náklady. Vyřešila problém přenosu služeb v reálném čase s přísnými požadavky na QoS (jako je nízká latence a chvění) přes sdílenou infrastrukturu, což bylo klíčové pro podporu služeb UMTS.

Motivováno konvergencí hlasových a datových sítí, VC umožnilo integraci okruhově přepínaného a paketově přepínaného provozu na společné přenosové platformě. V implementacích založených na ATM umožňovala VC jemně odstupňovanou kontrolu QoS prostřednictvím přenosových kontraktů a kategorií služeb (např. CBR pro hlas, VBR pro video, UBR pro data), což zajišťovalo, že citlivé aplikace dostávaly přednostní zacházení. To byl významný pokrok oproti dřívějším IP sítím, kterým chyběly nativní záruky QoS. Vytvoření standardů pro VC ve specifikacích 3GPP (např. 25.410 pro rozhraní Iu, 25.414 pro přenos) zajistilo interoperabilitu mezi zařízeními různých výrobců a usnadnilo globální nasazení 3G sítí.

S vývojem sítí vedly omezení ATM – jako je složitost a režie – k přechodu na přenos IP/MPLS a Ethernet. Koncept VC však zůstal relevantní díky přizpůsobení se novým technologiím; například štítky MPLS nebo tunely GTP plní podobné účely v pozdějších vydáních. Trvalým účelem VC je poskytnout logickou, spravovanou cestu, která zajišťuje předvídatelný výkon, podporuje škálovatelnost sítě a abstrahuje přenosovou vrstvu od servisních vrstev, což umožňuje systémům 3GPP využívat různé podkladové technologie při zachování kontinuity a kvality služeb.

## Klíčové vlastnosti

- Spojově orientovaná služba zajišťující spolehlivé doručování dat ve správném pořadí
- Podpora multiplexování více logických kanálů přes jeden fyzický spoj
- Poskytování QoS prostřednictvím přenosových parametrů a kategorií služeb
- Identifikace pomocí štítků, jako je VPI/VCI v ATM, nebo analogických identifikátorů v IP/MPLS
- Segmentace a zpětné složení datových jednotek protokolů vyšších vrstev
- Interoperabilita napříč různými přenosovými technologiemi (ATM, IP, MPLS)

## Související pojmy

- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)
- [AAL5 – ATM Adaptation Layer type 5](/mobilnisite/slovnik/aal5/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [VC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vc/)
