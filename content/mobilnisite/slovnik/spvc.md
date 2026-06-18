---
slug: "spvc"
url: "/mobilnisite/slovnik/spvc/"
type: "slovnik"
title: "SPVC – Switched PVC"
date: 2025-01-01
abbr: "SPVC"
fullName: "Switched PVC"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spvc/"
summary: "SPVC (Switched PVC) je technologie jádrové sítě v rámci 3GPP, která umožňuje dynamické spínání trvalých virtuálních okruhů (Permanent Virtual Circuits) v paketově přepínaných sítích, jako jsou GPRS a"
---

SPVC je technologie jádrové sítě, která umožňuje dynamické, na požádání spínané přepínání trvalých virtuálních okruhů (Permanent Virtual Circuits) pro optimalizaci využití zdrojů v paketově přepínaných sítích, jako jsou GPRS a EPS.

## Popis

Switched [PVC](/mobilnisite/slovnik/pvc/) (SPVC) je koncept jádrové sítě definovaný v 3GPP, zejména ve specifikacích jako 29.414, pro správu virtuálních okruhů v paketově přepínaných doménách, jako jsou sítě založené na protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)). SPVC funguje v rámci trvalých virtuálních okruhů (PVC), což jsou předkonfigurovaná logická spojení mezi síťovými uzly, ale přidává spínací schopnosti pro jejich dynamické vytváření nebo úpravy na základě požadavků na provoz. V podstatě SPVC umožňuje zřizování a rušení PVC na požádání, čímž transformuje statická spojení na flexibilní, spínané cesty, které se přizpůsobují síťovým podmínkám. Tato technologie je nedílnou součástí Evolved Packet Core (EPC) a starších jádrových sítí GPRS a usnadňuje efektivní směrování dat mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a dalšími síťovými elementy.

Z architektonického hlediska SPVC funguje v řídicí rovině jádrové sítě a využívá signalizační protokoly ke správě stavů virtuálních okruhů. Mezi klíčové komponenty patří spínací uzly (např. SGW, PGW), které implementují logiku SPVC, systémy správy, které konfigurují parametry PVC, a GTP tunely přenášející uživatelská data. SPVC funguje tak, že zachycuje požadavky na spojení, vyhodnocuje dostupnost zdrojů a dynamicky přiděluje prostředky PVC namísto spoléhání se pouze na staticky zřízené okruhy. Například když uživatel zahájí datovou relaci, SPVC může spustit vytvoření spínaného PVC mezi SGW a PGW, čímž optimalizuje využití šířky pásma a snižuje latenci ve srovnání s pevnými PVC, která mohou zůstat nevyužita.

Při provozu SPVC zahrnuje několik kroků: zahájení prostřednictvím signalizace řídicí roviny (např. zprávy [GTP-C](/mobilnisite/slovnik/gtp-c/)), rezervaci zdrojů na základě profilů kvality služeb (QoS) a aktivaci spínané cesty. Podporuje funkce jako vyvažování zátěže, kdy je provoz distribuován přes více PVC, aby se zabránilo přetížení, a mechanismy převzetí služeb při selhání, kdy lze SPVC v případě výpadku uzlu přeměrovat. Úlohou SPVC v síti je zvýšit škálovatelnost a efektivitu, zejména ve velkých nasazeních, jako je mobilní širokopásmový přístup a IoT, minimalizací režie ruční konfigurace spojené s tradičními PVC a umožněním flexibilnější správy zdrojů.

## K čemu slouží

SPVC byl vyvinut k řešení omezení statických trvalých virtuálních okruhů ([PVC](/mobilnisite/slovnik/pvc/)) v raných paketově přepínaných sítích, jako jsou [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Před zavedením SPVC vyžadovaly PVC ruční konfiguraci a trvalé přidělení zdrojů, což vedlo k neefektivnímu využití, zejména v sítích s proměnlivými vzory provozu. Tento statický přístup zvyšoval provozní náklady, omezoval škálovatelnost a bránil schopnosti podporovat dynamické služby, jako je mobilní internet a aplikace v reálném čase. SPVC tyto problémy řeší zavedením spínacích schopností, které umožňují zřizovat PVC na požádání, čímž optimalizuje využití zdrojů a snižuje složitost konfigurace.

Historicky se SPVC objevil ve 3GPP Rel-8 jako součást vylepšení Evolved Packet System (EPS), motivovaný potřebou flexibilnějších architektur jádrové sítě pro podporu rostoucího datového provozu. Navázal na starší koncepty ATM a frame relay, ale přizpůsobil se pro IP sítě, jako je EPC. Díky umožnění dynamické správy PVC usnadnil SPVC přechod na plně IP sítě, zlepšil podporu pro diferenciaci QoS a položil základy pro pozdější inovace, jako je virtualizace síťových funkcí (NFV) a softwarově definované sítě (SDN) v jádrových sítích 5G.

## Klíčové vlastnosti

- Dynamické zřizování a rušení PVC na požádání
- Integrace s jádrovými sítěmi založenými na GTP pro směrování dat
- Podpora přidělování zdrojů s ohledem na QoS a vyvažování zátěže
- Snížení režie ruční konfigurace prostřednictvím automatizace
- Mechanismy převzetí služeb při selhání a redundance pro zvýšení spolehlivosti
- Vylepšení škálovatelnosti pro rozsáhlé mobilní datové služby

## Související pojmy

- [PVC – Permanent Virtual Circuit](/mobilnisite/slovnik/pvc/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [SPVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/spvc/)
