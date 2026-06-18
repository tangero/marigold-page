---
slug: "lapb"
url: "/mobilnisite/slovnik/lapb/"
type: "slovnik"
title: "LAPB – Link Access Procedure Balanced"
date: 2025-01-01
abbr: "LAPB"
fullName: "Link Access Procedure Balanced"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lapb/"
summary: "LAPB je protokol linkové vrstvy používaný v systémech 3GPP pro spolehlivá, na chyby odolná bod-bod spojení, často pro přenos signalizace. Jedná se o vyváženou (balanced) adaptaci HDLC, která zajišťuje"
---

LAPB je vyvážený (balanced) HDLC protokol linkové vrstvy používaný v systémech 3GPP k zajištění spolehlivých, řízených a na chyby odolných bod-bod spojení pro přenos signalizace mezi síťovými prvky.

## Popis

Link Access Procedure Balanced (LAPB) je protokol linkové vrstvy (vrstva 2) standardizovaný v rámci 3GPP, odvozený z rámce High-Level Data Link Control ([HDLC](/mobilnisite/slovnik/hdlc/)). Funguje ve vyváženém režimu (balanced mode), což znamená, že obě komunikující stanice (např. mobilní stanice a síťový uzel) mohou nezávisle iniciovat a řídit spojení, fungujíce jako kombinované primární a sekundární stanice. Tento symetrický design eliminuje hierarchii typu pán-otrok (master-slave) a umožňuje efektivní plně duplexní komunikaci. LAPB se primárně používá nad spolehlivými fyzickými vrstvami k poskytování sekvenovaného, bezchybného přenosu dat pro protokoly vyšších vrstev, zejména v legacy okruhově přepínaných doménách GSM a UMTS pro signalizaci a přenos některých uživatelských dat.

Architektura protokolu je rámcová a využívá tři typy rámců: Informační (I-rámce) pro přenos uživatelských dat, Řídicí (S-rámce) pro potvrzení řízení toku a chyb (jako [RR](/mobilnisite/slovnik/rr/), [RNR](/mobilnisite/slovnik/rnr/), [REJ](/mobilnisite/slovnik/rej/)) a Nečíslované (U-rámce) pro navázání a ukončení spojení ([SABM](/mobilnisite/slovnik/sabm/), [DISC](/mobilnisite/slovnik/disc/), [UA](/mobilnisite/slovnik/ua/)). Každý rámec obsahuje pole adresy, řízení, informací a kontrolního součtu rámce ([FCS](/mobilnisite/slovnik/fcs/)). Řídicí pole spravuje sekvenční čísla (N(S) pro odesílání, N(R) pro příjem) pro klouzavé okénko řízení toku, typicky s modulem 8 nebo 128. Detekce chyb se provádí pomocí FCS (pomocí CRC) s mechanismy automatického opakovaného dotazu (ARQ) pro retransmisi poškozených nebo ztracených rámců, což zajišťuje vysokou spolehlivost.

V kontextu sítě 3GPP je LAPB specifikován pro rozhraní jako je rozhraní Gb mezi BSS a SGSN v GPRS/EDGE, kde může být použit nad frame relay pro řízení spojení signalizačních dat. Jeho úlohou je vytvořit logické spojení (LLC) pro spolehlivý přenos paketů BSSGP (Base Station System GPRS Protocol). Ačkoli byl v pozdějších verzích z velké části nahrazen IP transportem, robustní mechanismy LAPB pro kontrolu chyb a toku poskytly kritický základ pro rané mobilní datové služby, zajišťující integritu signalizace a efektivní využití šířky pásma i nad někdy nespolehlivými fyzickými okruhy.

## K čemu slouží

LAPB byl zaveden, aby poskytl standardizovaný, spolehlivý protokol linkové vrstvy pro bod-bod spojení v mobilních sítích 3GPP, řešíc potřebu řízeného a na chyby odolného přenosu signalizace a dat. Před jeho přijetím mohla proprietární nebo méně robustní řešení linkové vrstvy vést k problémům s interoperabilitou a poškození dat. LAPB, jako protokol odvozený od ITU-T X.25, nabídl dobře známou, na dodavateli nezávislou metodu pro zajištění integrity dat mezi síťovými prvky, jako jsou základnové stanice a uzly jádra sítě.

Historický kontext spočívá ve vývoji GSM a raných paketových datových služeb (GPRS), kde byl spolehlivý transport pro signalizační zprávy (např. pro správu mobility, řízení hovorů) a paketové datové jednotky nezbytný nad pozemními spoji. Rozhraní fyzické vrstvy (jako linky E1/T1) mohla zavádět chyby; ARQ a sekvenční mechanismy LAPB zaručovaly, že zprávy byly doručeny správně a v pořadí. Řešil problém vybudování spolehlivé komunikační podvrstvy nad potenciálně šumivými okruhy, což bylo klíčové pro udržení stability sítě a kvality služeb.

Navíc byl vyvážený režim (balanced mode) LAPB zvolen specificky pro zlepšení efektivity oproti dřívějším nevyváženým (unbalanced) režimům HDLC používaným v některých telekomunikačních systémech. Tím, že umožňoval kterémukoli konci iniciovat přenos a řízení, snižoval latenci a zjednodušoval správu spojení pro komunikaci typu peer-to-peer mezi síťovými uzly. Tento design byl vhodný pro vyvíjející se architekturu, kde síťové uzly potřebovaly v dialogu vystupovat jako rovné, podporujíc rostoucí inteligenci a autonomii distribuovanou napříč rádiovým přístupem a jádrem sítě.

## Klíčové vlastnosti

- Provoz ve vyváženém režimu (kombinovaná stanice) umožňující symetrické, peer-to-peer řízení
- Komplexní detekce chyb pomocí kontrolního součtu rámce (FCS) s CRC
- Mechanismy automatického opakovaného dotazu (ARQ) pro spolehlivou retransmisi rámců
- Řízení toku pomocí klouzavého okénka s mod-8 nebo mod-128 sekvenčním číslováním
- Podpora informačních (I), řídicích (S) a nečíslovaných (U) typů rámců
- Procedury pro navázání, údržbu a ukončení spojení (např. SABM, DISC)

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.044** (Rel-4) — GSM Teletex Service Support

---

📖 **Anglický originál a plná specifikace:** [LAPB na 3GPP Explorer](https://3gpp-explorer.com/glossary/lapb/)
