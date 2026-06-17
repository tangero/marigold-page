---
slug: "l2r"
url: "/mobilnisite/slovnik/l2r/"
type: "slovnik"
title: "L2R – COP L2R Character Orientated Protocol"
date: 2025-01-01
abbr: "L2R"
fullName: "COP L2R Character Orientated Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/l2r/"
summary: "Znakově orientovaný protokol linkové vrstvy používaný pro spolehlivou komunikaci typu point-to-point, často pro signalizaci správy nebo řízení. Data rámcuje jako posloupnosti znaků, poskytuje funkce ř"
---

L2R je znakově orientovaný protokol linkové vrstvy používaný pro spolehlivou komunikaci typu point-to-point, který poskytuje řízení chyb a správu spoje pro starší rozhraní 3GPP.

## Popis

COP L2R (Character Orientated Protocol) je protokol linkové vrstvy standardizovaný v rámci 3GPP, navržený pro synchronní, znakově orientovanou komunikaci přes spoje point-to-point. Funguje tak, že zachází s daty jako se streamem znaků (typicky 8bitových bajtů), které zapouzdřuje do rámců pro přenos. Mezi primární funkce protokolu patří rámcování, detekce chyb pomocí kontrolního součtu a procedury správy spoje, jako je navázání, udržování a ukončení spojení. Zajišťuje spolehlivý přenos dat mezi dvěma přímo propojenými síťovými entitami implementací mechanismů kladného potvrzení příjmu s retransmiscemi pro poškozené nebo ztracené rámce.

Architektonicky se L2R nachází přímo nad fyzickou vrstvou a pod protokoly síťové vrstvy. Často se používá ve scénářích vyžadujících jednoduchý, robustní a deterministický spoj, například v backhaulovém připojení mezi základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v GSM nebo pro některá rozhraní správy v UMTS. Protokol definuje specifické řídicí znaky pro ohraničení rámců a řízení spoje, čímž strukturuje bitový stream do rozpoznatelných rámců. Klíčovým aspektem jeho fungování je jeho synchronní povaha, kdy jsou vysílač a přijímač synchronizovány, často prostřednictvím hodin fyzické vrstvy, což umožňuje efektivní využití šířky pásma bez nutnosti start/stop bitů na každý znak.

Podrobně se rámec L2R skládá z počátečního oddělovače, polí adresy a řízení (pro konfigurace s více účastníky), informačního pole obsahujícího užitečná data, sekvence pro kontrolu rámce ([FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb a koncového oddělovače. Protokol spravuje spoj pomocí sady příkazů a odpovědí, řeší inicializaci, testování a obnovu po chybách. Jeho znakově orientovaná povaha znamená, že je vhodný pro přenos textově založených protokolů správy nebo binárních dat zpracovávaných jako oktetové streamy. Přestože byl v mnoha moderních aplikacích z velké části nahrazen bitově orientovanými protokoly, jako jsou [HDLC](/mobilnisite/slovnik/hdlc/) a PPP, jeho specifikace ve standardech 3GPP zdůrazňuje jeho historickou roli při poskytování standardizované, spolehlivé přenosové služby vrstvy 2 pro kritické řídicí a správní funkce v raných nasazeních sítí 2G a 3G, což zajišťovalo interoperabilitu mezi zařízeními různých výrobců.

## K čemu slouží

L2R byl vyvinut, aby splnil potřebu standardizovaného, spolehlivého protokolu linkové vrstvy pro rozhraní telekomunikačních zařízení, zejména v éře GSM a raného UMTS. Před takovou standardizací používali výrobci proprietární protokoly linkové vrstvy, což vytvářelo problémy s interoperabilitou a uzamklo operátory do řešení od jediného dodavatele. Protokol COP L2R poskytl společnou, znakově orientovanou metodu pro propojení síťových prvků, což umožnilo více-dodavatelské sítě a zjednodušilo nasazení a údržbu sítě.

Protokol řešil problém spolehlivého přenosu signalizačních a správních dat přes často zašuměné a náchylné k chybám fyzické okruhy, jako jsou linky E1/T1. Jeho návrh s robustní detekcí chyb a retransmisčními mechanismy zajišťoval integritu dat pro kritické řídicí zprávy. Znakově orientovaný přístup byl přirozeně vhodný pro výpočetní systémy a hardwarovou sériovou komunikaci té doby. Specifikací L2R zajistilo 3GPP, že základní spoje v RAN a mezi systémy správy sítě mohou být navázány předvídatelným a interoperabilním způsobem, čímž vytvořilo spolehlivou 'transportní' vrstvu, na kterou se mohly spolehnout funkce vyšších síťových vrstev.

## Klíčové vlastnosti

- Znakově orientovaný synchronní protokol linkové vrstvy
- Poskytuje spolehlivý přenos dat s potvrzením příjmu a retransmiscemi
- Implementuje rámcování, detekci chyb prostřednictvím sekvence pro kontrolu rámce (FCS)
- Obsahuje procedury správy spoje pro navázání a zrušení
- Navržen pro konfigurace point-to-point a potenciálně s více účastníky
- Používá specifické řídicí znaky pro ohraničení rámců a řízení

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [L2R na 3GPP Explorer](https://3gpp-explorer.com/glossary/l2r/)
