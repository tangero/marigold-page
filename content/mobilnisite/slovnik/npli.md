---
slug: "npli"
url: "/mobilnisite/slovnik/npli/"
type: "slovnik"
title: "NPLI – Network Provided Location Information"
date: 2025-01-01
abbr: "NPLI"
fullName: "Network Provided Location Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/npli/"
summary: "Polohové údaje (např. zeměpisné souřadnice) uživatelského zařízení (UE), které určuje síť sama, nikoli zařízení UE. Jde o základní schopnost pro služby založené na poloze, tísňová volání (E911/E112) a"
---

NPLI jsou polohové údaje uživatelského zařízení (UE), například zeměpisné souřadnice, které určuje mobilní síť sama pro služby jako tísňová volání a služby založené na poloze.

## Popis

Network Provided Location Information (NPLI, informace o poloze poskytované sítí) označuje architektonický princip a soubor funkcí, kde infrastruktura mobilní sítě odpovídá za odhad geografické polohy uživatelského zařízení (UE). Na rozdíl od metod založených na UE nebo s asistencí UE, kde mobilní zařízení hraje aktivní roli při výpočtu polohy (např. pomocí vestavěného [GPS](/mobilnisite/slovnik/gps/)), je u NPLI primární výpočetní entitou síť. Hlavní síťovou entitou, která tuto službu řídí, je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), které komunikuje s obsluhujícími uzly jádra sítě pro dané UE (jako [MSC](/mobilnisite/slovnik/msc/) nebo [MME](/mobilnisite/slovnik/mme/)) a s polohovacími systémy v rádiové přístupové síti (RAN).

Technický proces začíná, když klient služby polohy ([LCS](/mobilnisite/slovnik/lcs/)) – což může být externí aplikace, síť tísňových služeb nebo vlastní služba operátora – odešle požadavek na určení polohy do GMLC. GMLC ověří klienta a určí obsluhující uzel pro cílové UE. Poté předá požadavek příslušnému uzlu (např. MSC pro přepojování okruhů, MME pro přepojování paketů). Tento uzel ve spolupráci s RAN (např. Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo evolved NodeB ([eNB](/mobilnisite/slovnik/enb/))) zahájí polohovací proceduru. Síť shromažďuje potřebná měření bez spoléhání na výpočetní schopnosti UE pro konečné určení polohy.

Klíčové polohovací metody spadající pod NPLI zahrnují Cell-ID (nejjednodušší forma, poskytující polohu obsluhující buňky), Timing Advance (TA), Uplink Time Difference of Arrival (U-TDOA) a Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)), který kombinuje identifikaci buňky s měřením času, úhlu a výkonu. Pro U-TDOA specializované Location Measurement Units (LMU) v síti měří čas příchodu signálů z UE na více místech. Všechna naměřená data jsou odeslána do centrálního uzlu, často Serving Mobile Location Centre (SMLC) nebo Evolved SMLC (E-SMLC) v RAN, který vypočítá odhad polohy pomocí algoritmů, jako je multilaterace. Vypočítaná poloha (zeměpisná šířka, délka a nejistota) je pak směrována zpět přes jádro sítě k autorizovanému LCS klientovi. Tato architektura zajišťuje fungování polohových služeb i pro UE bez GPS a poskytuje síťově řízený mechanismus klíčový pro regulatorní služby, jako je lokalizace tísňového volajícího.

## K čemu slouží

NPLI byla vyvinuta pro splnění kritických požadavků na určení polohy mobilního účastníka nezávisle na schopnostech nebo spolupráci koncového zařízení. Hlavními hnacími silami byly regulatorní povinnosti pro tísňové služby (jako E911 v USA a E112 v Evropě) a komerční potřeba služeb založených na poloze (LBS), jako je sledování vozového parku, navigace a reklamy využívající polohu. Před standardizovaným síťovým určováním polohy bylo možné polohu pouze hrubě odhadnout podle obsluhující základnové stanice, což bylo nedostatečné pro zásah tísňových služeb, kdy volající nemusí být schopen svou polohu sdělit slovně.

Zavedení NPLI řešilo omezení spočívající pouze v závislosti na GPS v zařízení, která nebyla všeobecně dostupná, mohla být uživatelem vypnuta a často špatně fungovala v interiérech nebo městských kaňonech. Síťově orientované řešení zajišťuje, že operátor může splnit svou regulatorní povinnost poskytnout polohu volajícího pro tísňové služby pro *všechna* zařízení ve své síti bez ohledu na jejich výrobce, model nebo funkce. Poskytuje také spolehlivou záložní nebo doplňkovou metodu k metodám založeným na UE.

Dále NPLI umožňuje síťovým operátorům udržovat kontrolu a vlastnictví polohových dat a vytvářet služební platformu pro třetí strany (LCS klienty). Řeší problém poskytování polohy pro služby, kde explicitní souhlas nebo interakce koncového uživatele nemusí být možná nebo žádoucí, jako je sledování majetku v logistice nebo některé scénáře zákonného odposlechu. Standardizace v 3GPP, zejména od Release 11 s vylepšeným určováním polohy v LTE, poskytla jednotný, interoperabilní rámec pro NPLI napříč globálními sítěmi, což překonalo implementace závislé na konkrétním dodavateli.

## Klíčové vlastnosti

- Výpočet geografické polohy UE prováděný centrálně sítí
- Podpora více polohovacích metod: Cell-ID, TA, U-TDOA a E-CID
- Řízeno prvky jádra sítě (GMLC) s využitím polohovacích uzlů v RAN (SMLC/E-SMLC)
- Funguje nezávisle na schopnostech UE (nevyžaduje GPS v UE)
- Nezbytné pro splnění regulatorních požadavků na lokalizaci pro tísňové služby (E911/E112)
- Poskytuje platformu pro služby založené na poloze (LBS) operátora i třetích stran

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.842** (Rel-11) — NPLI Architecture Study for IMS
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [NPLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/npli/)
