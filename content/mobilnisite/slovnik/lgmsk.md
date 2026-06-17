---
slug: "lgmsk"
url: "/mobilnisite/slovnik/lgmsk/"
type: "slovnik"
title: "LGMSK – Linearised Gaussian Minimum Shift Keying"
date: 2025-01-01
abbr: "LGMSK"
fullName: "Linearised Gaussian Minimum Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lgmsk/"
summary: "Modulační technika používaná v GSM EDGE Evolution (EDGE+) pro zvýšení spektrální účinnosti a přenosových rychlostí. Linearizuje signál GMSK, aby umožnila vyšší modulační schémata jako 8-PSK a 16-QAM,"
---

LGMSK je modulační technika používaná v GSM EDGE Evolution, která linearizuje signál GMSK, aby umožnila vyšší modulační schémata pro zvýšení přenosových rychlostí v rámci stávajícího kmitočtového pásma GSM.

## Popis

Linearizované Gaussovské klíčování s minimálním posuvem (LGMSK) je klíčová modulační a signálová technika zavedená jako součást standardu GSM [EDGE](/mobilnisite/slovnik/edge/) Evolution (známého také jako EDGE+). Zásadně upravuje klasickou modulaci [GMSK](/mobilnisite/slovnik/gmsk/) používanou v GSM. Standardní GMSK je modulace s konstantní obálkou a nelineární charakteristikou, která je energeticky účinná, ale omezuje dosažitelné přenosové rychlosti, protože s ní nelze přímo kombinovat vyšší a spektrálně účinnější modulační schémata (jako [8-PSK](/mobilnisite/slovnik/8-psk/) nebo QAM). LGMSK tento problém řeší aplikací linearizačního procesu na signál GMSK.

Technický proces zahrnuje filtrování modulovaného signálu GMSK specifickým linearizačním filtrem. Tento filtr je navržen tak, aby kompenzoval inherentní nelinearitu modulace GMSK a efektivně 'linearizoval' fázovou trajektorii signálu. Výsledný signál se přibližuje lineárně modulovanému signálu, jako je například offsetové kvadraturní fázové klíčování (OQPSK). Tato linearizovaná konstelace signálu je klíčová, protože umožňuje následnou aplikaci pokročilejších, vyšších modulačních technik ve stejném rádiovém kanálu.

Jakmile je signál linearizován, může systém EDGE+ použít modulační schémata jako 8-PSK, 16-QAM nebo dokonce 32-QAM v downlinku. Tato schémata přenášejí více bitů na symbol, což dramaticky zvyšuje špičkové přenosové rychlosti a spektrální účinnost ve srovnání se standardním GMSK nebo dokonce s původním 8-PSK v EDGE. Příjemce používá inverzní linearizační filtr jako součást demodulačního procesu pro správnou interpretaci signálu. LGMSK je klíčovým prvkem pro dosažení downlinkových rychlostí přesahujících 1 Mbps v rámci 200 kHz nosné GSM, což operátorům umožňuje vylepšit své sítě GSM/EDGE pro služby mobilního širokopásmového přístupu bez nutnosti nového kmitočtového spektra nebo kompletního přechodu na infrastrukturu 3G/4G.

## K čemu slouží

LGMSK byl vyvinut za účelem rozšíření schopností a prodloužení životnosti sítí GSM v reakci na rostoucí poptávku po mobilních datech, a to před masovým nasazením 3G [HSPA](/mobilnisite/slovnik/hspa/) a 4G LTE. Hlavní problém, který řešil, byl základní strop přenosových rychlostí tradiční technologie GSM/[EDGE](/mobilnisite/slovnik/edge/). Zatímco EDGE zavedlo modulaci [8-PSK](/mobilnisite/slovnik/8-psk/), nelineární povaha [GMSK](/mobilnisite/slovnik/gmsk/) ji činila nekompatibilní s ještě vyššími a účinnějšími modulacemi, jako je QAM, které jsou z definice lineární.

Vytvoření LGMSK bylo motivováno potřebou nákladově efektivní evoluční cesty pro operátory GSM. Umožnilo jim výrazně zvýšit datovou propustnost jejich stávajícího kmitočtového spektra GSM (850, 900, 1800, 1900 MHz) a infrastruktury pomocí cílených upgradů, namísto nákladné a časově náročné kompletní obnovy sítě. To poskytlo konkurenceschopnou nabídku mobilního širokopásmového přístupu a pomohlo překlenout mezeru mezi 2.5G EDGE a nasazením sítí 3G/4G, zejména na trzích, kde bylo spektrum pro 3G nedostupné nebo jeho nasazení bylo opožděné.

## Klíčové vlastnosti

- Linearizuje klasický nelineární modulační signál GMSK
- Umožňuje použití vyšších modulací (např. 16-QAM, 32-QAM) na nosných GSM
- Zvyšuje špičkové downlinkové přenosové rychlosti nad 1 Mbps v 200 kHz kanálu
- Zlepšuje spektrální účinnost rozhraní GSM/EDGE
- Umožňuje vývoj využívající stávající kmitočtové spektrum GSM a infrastrukturu stanovišť
- Používá specifické vysílací a přijímací filtry pro linearizaci a de-linearizaci

## Související pojmy

- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)

## Definující specifikace

- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B

---

📖 **Anglický originál a plná specifikace:** [LGMSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/lgmsk/)
