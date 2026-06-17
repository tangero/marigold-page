---
slug: "edge"
url: "/mobilnisite/slovnik/edge/"
type: "slovnik"
title: "EDGE – Enhanced Data rates for Global Evolution"
date: 2025-01-01
abbr: "EDGE"
fullName: "Enhanced Data rates for Global Evolution"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/edge/"
summary: "Mobilní síťová technologie 2,5. generace, která vylepšuje GSM/GPRS použitím účinnější modulace (8-PSK) vedle GMSK. Výrazně zvyšuje přenosové rychlosti a umožňuje rané mobilní internetové služby, jako"
---

EDGE je mobilní síťová technologie 2,5. generace, která vylepšuje GSM/GPRS účinnější modulací, aby výrazně zvýšila přenosové rychlosti pro rané mobilní internetové služby, a představuje evoluční krok směrem k 3G.

## Popis

Enhanced Data rates for Global Evolution (EDGE), standardizovaná jako Enhanced [GPRS](/mobilnisite/slovnik/gprs/) ([EGPRS](/mobilnisite/slovnik/egprs/)), je digitální mobilní technologie, která funguje jako dodatečné vylepšení sítí GSM a GPRS 2. generace. Funguje v rámci stávající šířky pásma nosné 200 kHz a struktury časových slotů GSM, ale zavádí klíčovou inovaci: modulaci 8-Phase Shift Keying ([8-PSK](/mobilnisite/slovnik/8-psk/)) vedle standardní Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)). Zatímco GMSK přenáší 1 bit na symbol, 8-PSK přenáší 3 bity na symbol, čímž teoreticky ztrojnásobuje hrubou přenosovou rychlost na časový slot. V praxi může EDGE dosáhnout špičkové přenosové rychlosti 384 kbps za ideálních podmínek při použití více časových slotů, ve srovnání s 115 kbps u GPRS.

Z architektonického hlediska EDGE primárně upravuje fyzickou vrstvu a vrstvu řízení rádiového spoje v zásobníku protokolů GSM/GPRS. Základnová přenosová stanice ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanice musí podporovat nové modulační a kódovací schémata ([MCS](/mobilnisite/slovnik/mcs/)). Jádrová síť zůstává oproti GPRS z velké části nezměněna a využívá stejný Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN). Klíčovým technickým rysem je zavedení devíti modulačních a kódovacích schémat (MCS-1 až MCS-9), která se dynamicky přizpůsobují rádiovým podmínkám. Schémata MCS-1 až MCS-4 používají GMSK, zatímco MCS-5 až MCS-9 používají 8-PSK, s různou mírou korekčního kódování. To umožňuje systému přepnout zpět na robustnější modulaci GMSK při špatných signálových podmínkách, a tím udržet spojení tam, kde by 8-PSK selhalo.

EDGE také vylepšuje řízení rádiového spoje technikami jako je přírůstková redundance (Incremental Redundancy, [IR](/mobilnisite/slovnik/ir/)) neboli Hybrid [ARQ](/mobilnisite/slovnik/arq/) Type II. Při použití IR, pokud je datový blok přijat s chybami, přijímač jej uloží a v následných přenosech požádá o další paritní bity (redundanci). Přijímač pak všechny přijaté verze bloku zkombinuje, čímž zvýší pravděpodobnost správného dekódování. Díky tomu je přenos dat efektivnější, protože se snižuje počet potřebných úplných retransmisí. Úlohou EDGE bylo poskytnout GSM operátorům nákladově efektivní cestu k vysokorychlostnímu datovému upgradu, která oddálila potřebu okamžitého nasazení sítí 3G UMTS, a zároveň uspokojila rostoucí poptávku zákazníků po mobilních datových službách.

## K čemu slouží

EDGE byla vyvinuta, aby řešila kritické omezení sítí GSM a GPRS: jejich relativně nízké přenosové rychlosti, které byly nedostatečné pro přesvědčivý mobilní internetový zážitek. Jak na přelomu tisíciletí rostla poptávka po službách, jako je prohlížení webu, e-mail a multimediální zprávy, potřebovali operátoři způsob, jak poskytovat vyšší rychlosti bez masivních kapitálových výdajů na výstavbu zcela nových sítí 3G. EDGE toto řešení poskytla tím, že maximalizovala spektrální účinnost stávajícího kmitočtového pásma a infrastruktury GSM.

Hlavním problémem, který řešila, bylo omezení přenosové rychlosti. GPRS, ačkoli zavádělo paketové přepínání, stále používalo pouze modulaci GMSK. Zavedení modulace 8-PSK v rámci stejné šířky pásma u EDGE efektivně ztrojnásobilo spektrální účinnost. To umožnilo operátorům nabízet (pro tehdejší dobu) 'broadbandový' zážitek a konkurovat raným nabídkám 3G. Byla k tomu motivována zejména konkurenčním prostředím v Severní Americe, kde operátoři GSM potřebovali odpověď na vyšší rychlosti technologie CDMA2000 1xEV-DO.

EDGE navíc prodloužila komerční životnost sítí GSM. Umožnila hladkou evoluční cestu, protože vyžadovala především softwarové upgrady stávajícího hardwaru BTS a nový software terminálů, přičemž některé stanice potřebovaly hardwarový upgrade pro výkonový zesilovač 8-PSK. Díky tomu se stala vysoce nákladově efektivní investicí. Sloužila jako klíčová přechodová technologie, která udržela sítě GSM relevantní a generující příjmy během pomalého a nákladného zavádění sítí 3G UMTS po celém světě.

## Klíčové vlastnosti

- Modulace 8-PSK vedle GMSK, což zvyšuje spektrální účinnost
- Devět modulačních a kódovacích schémat (MCS-1 až MCS-9) pro adaptaci spoje
- Přírůstková redundance (Hybrid ARQ Type II) pro vyšší efektivitu retransmisí
- Zpětná kompatibilita se sítěmi a terminály GSM/GPRS
- Využívá stávající 200 kHz nosnou a strukturu časových slotů GSM
- Teoretické špičkové přenosové rychlosti až 384 kbps (s více časovými sloty)

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.943** (Rel-19) — SES Codec Selection Report
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [EDGE na 3GPP Explorer](https://3gpp-explorer.com/glossary/edge/)
